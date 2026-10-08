#!/usr/bin/env node
/** Compile complete fixtures in isolated processes; never update expectations. */
import { readFileSync } from 'node:fs';
import { dirname, resolve, relative, isAbsolute, basename, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';

const self = fileURLToPath(import.meta.url);
const root = resolve(dirname(self), '..');
const PIN = '9.7.17';
const SOURCE_COMMIT = '5a7d0e294b8cad73b9701987bb584d0551d7fa4d';
const sha256 = text => createHash('sha256').update(text).digest('hex');
const fail = message => { throw new Error(message); };

function repoPath(name) {
  if (typeof name !== 'string' || !name || isAbsolute(name)) fail('Expected a nonempty repository-relative path');
  const file = resolve(root, name);
  const rel = relative(root, file);
  if (rel === '..' || rel.startsWith(`..${sep}`)) fail(`Path leaves repository: ${name}`);
  return file;
}

function warningCode(warning) {
  const message = warning.message ?? String(warning);
  const match = message.match(/\((w_[a-z0-9_]+)\)/i);
  return { code: match?.[1] ?? null, message: message.split(root).join('<repo>') };
}

async function worker() {
  // Upstream can print diagnostics itself. Keep stdout a single JSON result.
  for (const method of ['log', 'warn', 'error']) {
    console[method] = (...args) => process.stderr.write(`${args.map(String).join(' ')}\n`);
  }
  const fixture = JSON.parse(readFileSync(0, 'utf8'));
  const require = createRequire(import.meta.url);
  const pkg = require('overpy/package.json');
  if (pkg.version !== PIN) fail(`Expected OverPy ${PIN}, got ${pkg.version}`);
  const overpy = require('overpy');
  await overpy.readyPromise;
  const file = repoPath(fixture.path);
  const original = readFileSync(file, 'utf8');
  const inputSha256 = Object.fromEntries([...new Set([fixture.path, ...(fixture.inputs ?? [])])].map(name => [name, sha256(readFileSync(repoPath(name)))]));
  let source = original;
  let result;
  let stage = fixture.dialect === 'workshop' ? 'decompile' : 'compile';
  try {
    if (fixture.dialect === 'workshop') source = overpy.decompileAllRules(original, fixture.language);
    stage = 'compile';
    result = await overpy.compile(source, fixture.language, dirname(file), basename(file, '.workshop') + (fixture.dialect === 'workshop' ? '.opy' : ''));
  } catch (error) {
    return { outcome: 'rejected', stage, error: String(error).split(root).join('<repo>'), sourceSha256: sha256(original), inputSha256 };
  }
  return {
    outcome: 'accepted', sourceSha256: sha256(original), inputSha256,
    output: result.result, outputSha256: sha256(result.result),
    elements: result.nbElements, warnings: result.encounteredWarnings.map(warningCode),
    hiddenWarnings: (result.hiddenWarnings ?? []).map(warningCode),
  };
}

function verifyFixture(fixture, knownClaims) {
  if (!fixture.id || typeof fixture.id !== 'string') fail('Example is missing an ID');
  if (fixture.complete !== true) fail(`${fixture.id}: only complete fixtures belong in this harness`);
  if (!['overpy', 'workshop'].includes(fixture.dialect)) fail(`${fixture.id}: unknown dialect`);
  if (!['accept', 'reject'].includes(fixture.expected.outcome)) fail(`${fixture.id}: unknown expected outcome`);
  if (!Array.isArray(fixture.expected.warningCodes)) fail(`${fixture.id}: warningCodes must be explicit`);
  if (!fixture.game?.status) fail(`${fixture.id}: separate game-test status is required`);
  if (!Array.isArray(fixture.claims) || !fixture.claims.length) fail(`${fixture.id}: claim references are required`);
  for (const claim of fixture.claims) if (!knownClaims.has(claim)) fail(`${fixture.id}: unknown claim ${claim}`);
  repoPath(fixture.path);
  for (const copy of fixture.copies ?? []) {
    const source = readFileSync(repoPath(copy.source ?? fixture.path));
    const target = readFileSync(repoPath(copy.destination));
    if (!source.equals(target)) fail(`${fixture.id}: packaged copy differs: ${copy.destination}`);
  }
  const child = spawnSync(process.execPath, [self, '--worker'], {
    cwd: root, input: JSON.stringify(fixture), encoding: 'utf8',
    timeout: 20000, maxBuffer: 4 * 1024 * 1024,
  });
  if (child.error) fail(`${fixture.id}: worker failed: ${child.error.message}`);
  if (child.status !== 0) fail(`${fixture.id}: worker exited ${child.status}: ${child.stderr.trim()}`);
  let observed;
  try { observed = JSON.parse(child.stdout); }
  catch { fail(`${fixture.id}: compiler worker did not return JSON: ${child.stderr.trim()}`); }
  const errors = [];
  if (fixture.expected.outcome === 'reject') {
    if (observed.outcome !== 'rejected') errors.push('Expected rejection, but source compiled');
    else if (!fixture.expected.errorIncludes || !observed.error.includes(fixture.expected.errorIncludes)) {
      errors.push(`Unexpected rejection: ${observed.error}`);
    }
  } else if (observed.outcome !== 'accepted') {
    errors.push(`Unexpected ${observed.stage} failure: ${observed.error}`);
  } else {
    if (!observed.output.trim()) errors.push('Compiler returned empty output');
    const actualWarnings = observed.warnings.map(w => w.code ?? w.message).sort();
    if (JSON.stringify(actualWarnings) !== JSON.stringify([...fixture.expected.warningCodes].sort())) {
      errors.push(`Expected warnings ${JSON.stringify(fixture.expected.warningCodes)}, got ${JSON.stringify(actualWarnings)}`);
    }
    const expectedHidden = fixture.expected.hiddenWarnings ?? [];
    if (observed.hiddenWarnings.length !== expectedHidden.length || expectedHidden.some((expected, i) => {
      const actual = observed.hiddenWarnings[i];
      return !actual || actual.code !== expected.code || !actual.message.includes(expected.messageIncludes);
    })) {
      errors.push(`Unexpected hidden diagnostics: ${JSON.stringify(observed.hiddenWarnings)}`);
    }
    for (const fragment of fixture.expected.outputIncludes ?? []) {
      if (!observed.output.includes(fragment)) errors.push(`Missing expected generated fragment: ${fragment}`);
    }
    for (const fragment of fixture.expected.outputExcludes ?? []) {
      if (observed.output.includes(fragment)) errors.push(`Unexpected generated fragment: ${fragment}`);
    }
  }
  const { output, ...details } = observed;
  return {
    id: fixture.id, dialect: fixture.dialect, fixture: fixture.path, claims: fixture.claims,
    status: errors.length ? 'failed' : 'passed',
    validation: fixture.expected.outcome === 'reject' ? 'expected-compiler-rejection' : fixture.dialect === 'workshop' ? 'accepted-by-pinned-overpy-roundtrip' : 'accepted-by-pinned-overpy',
    ...details, game: fixture.game, ...(errors.length ? { errors } : {}),
  };
}

function main() {
  const args = process.argv.slice(2);
  let manifestPath = resolve(root, 'examples/manifest.json');
  if (args.length) {
    if (args.length !== 2 || args[0] !== '--manifest') fail('Usage: node scripts/check-examples.mjs [--manifest path]');
    manifestPath = resolve(args[1]);
  }
  const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
  if (manifest.compiler?.version !== PIN || manifest.compiler?.sourceCommit !== SOURCE_COMMIT) fail('Manifest compiler pin mismatch');
  if (!Array.isArray(manifest.examples) || !manifest.examples.length) fail('Manifest has no examples');
  const ownClaims = JSON.parse(readFileSync(resolve(root, 'examples/claims.json'), 'utf8')).claims;
  const coverage = JSON.parse(readFileSync(resolve(root, 'coverage/wiki-coverage.json'), 'utf8'));
  const knownClaims = new Set([...ownClaims.map(claim => claim.id), ...coverage.articles.flatMap(article => article.notes.map(note => note.id))]);
  const ids = new Set();
  const results = manifest.examples.map(fixture => {
    if (ids.has(fixture.id)) return { id: fixture.id, status: 'failed', errors: ['Duplicate example ID'] };
    ids.add(fixture.id);
    try { return verifyFixture(fixture, knownClaims); }
    catch (error) { return { id: fixture.id, status: 'failed', errors: [String(error)] }; }
  });
  const failed = results.filter(result => result.status === 'failed').length;
  process.stdout.write(JSON.stringify({
    compiler: manifest.compiler, gameVerification: 'No game tests are performed by this harness.',
    totals: { examples: results.length, passed: results.length - failed, failed }, results,
  }, null, 2) + '\n');
  if (failed) process.exitCode = 1;
}

if (process.argv[2] === '--worker') {
  worker().then(result => process.stdout.write(JSON.stringify(result))).catch(error => {
    process.stderr.write(`${String(error)}\n`); process.exitCode = 1;
  });
} else {
  try { main(); }
  catch (error) { process.stdout.write(JSON.stringify({ status: 'failed', error: String(error) }, null, 2) + '\n'); process.exitCode = 1; }
}
