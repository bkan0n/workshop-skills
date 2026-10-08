import assert from 'node:assert/strict';
import {spawnSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join, resolve} from 'node:path';
import {test} from 'node:test';
import {parse as parseYaml} from 'yaml';

const root = resolve(import.meta.dirname, '..');
const readWorkflow = name => parseYaml(readFileSync(join(root, '.github/workflows', name), 'utf8'));
const release = readWorkflow('release.yml');
const prepare = readWorkflow('release-please.yml');
const check = readWorkflow('check.yml');
const scripts = Object.fromEntries(release.jobs.package.steps.filter(step => step.id && step.run).map(step => [step.id, step.run]));
const commit = '1234567890123456789012345678901234567890';
const otherCommit = 'abcdefabcdefabcdefabcdefabcdefabcdefabcd';
const tagObject = '2222222222222222222222222222222222222222';
const tag = 'v0.1.1';
const assets = ['workshop-skills-0.1.1.zip', 'workshop-overpy-skills-0.1.1.zip', 'SHA256SUMS', 'context-report.json'];
const quote = value => `'${value.replaceAll("'", "'\\''")}'`;

// Only these deterministic local implementations stand in for Git and gh.
// The workflow's jq, cmp and checksum commands run normally.
const stub = String.raw`
import {appendFileSync, copyFileSync, mkdirSync, readFileSync, writeFileSync} from 'node:fs';
import {basename, join} from 'node:path';
const [tool, ...args] = process.argv.slice(2);
const statePath = process.env.STUB_STATE;
const state = JSON.parse(readFileSync(statePath, 'utf8'));
appendFileSync(process.env.STUB_LOG, JSON.stringify({tool, args}) + '\n');
function save() { writeFileSync(statePath, JSON.stringify(state)); }
function fail(message) { console.error(message); process.exit(1); }
if (tool === 'git') {
  if (args[0] === 'status') process.stdout.write(state.dirty);
  else if (args[0] === 'rev-parse' && args[1] === 'HEAD') console.log(state.commit);
  else if (args[0] === 'rev-parse' && args[1] === '--verify' && args[2] === 'refs/tags/' + state.tag + '^{commit}') console.log(state.tagCommit);
  else if (args[0] === 'rev-parse' && args[1] === 'refs/tags/' + state.tag) console.log(state.tagObject);
  else fail('Unexpected Git operation: ' + JSON.stringify(args));
} else if (tool === 'gh') {
  if (args[0] === 'api' && args[1] === 'repos/test-owner/test-repository/git/ref/tags/' + state.tag) {
    console.log(state.remoteTagObject);
  } else if (args[0] === 'release' && args[1] === 'view' && args[2] === state.tag) {
    const draft = state.views > 0 && state.laterDraft ? state.laterDraft : state.draft;
    state.views++;
    save();
    console.log(JSON.stringify(draft));
  } else if (args[0] === 'release' && args[1] === 'upload' && args[2] === state.tag && args[4] === '--clobber') {
    const filename = basename(args[3]);
    if (!state.assets.includes(filename)) fail('Unexpected upload: ' + filename);
    copyFileSync(args[3], join(process.env.STUB_REMOTE, filename));
    state.uploads.push(filename);
    save();
  } else if (args[0] === 'release' && args[1] === 'download' && args[2] === state.tag) {
    const destination = args[args.indexOf('--dir') + 1];
    if (!destination) fail('Missing download directory');
    mkdirSync(destination, {recursive: true});
    for (const filename of state.assets) copyFileSync(join(process.env.STUB_REMOTE, filename), join(destination, filename));
    if (state.corruptDownload) appendFileSync(join(destination, state.corruptDownload), 'CORRUPTED');
  } else fail('Unexpected GitHub operation: ' + JSON.stringify(args));
} else fail('Unexpected tool');
`;

function fixture(t, changes = {}, environment = {}) {
  const directory = mkdtempSync(join(tmpdir(), 'skills-workflow-test-'));
  t.after(() => rmSync(directory, {recursive: true, force: true}));
  for (const path of ['bin', 'dist', 'sources', 'runner-temp', 'remote']) mkdirSync(join(directory, path));
  const draft = {tagName: tag, isDraft: true, targetCommitish: commit, url: 'https://example.invalid/draft'};
  const initial = {
    commit, tag, tagCommit: commit, tagObject, remoteTagObject: tagObject,
    dirty: '', draft, views: 0, uploads: [], assets, ...changes,
  };
  const statePath = join(directory, 'state.json');
  writeFileSync(statePath, JSON.stringify(initial));
  writeFileSync(join(directory, 'stub.mjs'), stub);
  for (const tool of ['git', 'gh']) {
    writeFileSync(join(directory, 'bin', tool), `#!/bin/sh\nexec ${quote(process.execPath)} ${quote(join(directory, 'stub.mjs'))} ${quote(tool)} "$@"\n`, {mode: 0o755});
  }
  if (spawnSync('sha256sum', ['--version'], {encoding: 'utf8'}).error?.code === 'ENOENT') {
    writeFileSync(join(directory, 'bin', 'sha256sum'), '#!/bin/sh\nexec shasum -a 256 "$@"\n', {mode: 0o755});
  }
  writeFileSync(join(directory, 'package.json'), JSON.stringify({version: changes.packageVersion ?? '0.1.1'}));
  writeFileSync(join(directory, 'sources/lock.json'), JSON.stringify({release: changes.lockVersion ?? '0.1.1'}));
  writeFileSync(join(directory, 'dist', assets[0]), 'first deterministic archive fixture\n');
  writeFileSync(join(directory, 'dist', assets[1]), 'second deterministic archive fixture\n');
  writeFileSync(join(directory, 'dist', 'context-report.json'), '{"verified":true}\n');
  const sums = [assets[0], assets[1], 'context-report.json'].map(filename => {
    const hash = createHash('sha256').update(readFileSync(join(directory, 'dist', filename))).digest('hex');
    return `${hash}  ${filename}\n`;
  }).join('');
  writeFileSync(join(directory, 'dist', 'SHA256SUMS'), sums);
  const env = {
    ...process.env,
    PATH: join(directory, 'bin') + ':' + process.env.PATH,
    RELEASE_TAG: tag, EXPECTED_SHA: commit, RELEASE_COMMIT: commit,
    RUNNER_TEMP: join(directory, 'runner-temp'),
    GITHUB_OUTPUT: join(directory, 'output'), GITHUB_STEP_SUMMARY: join(directory, 'summary'),
    GH_TOKEN: 'offline-test-token', GH_REPO: 'test-owner/test-repository',
    STUB_STATE: statePath, STUB_LOG: join(directory, 'commands.jsonl'), STUB_REMOTE: join(directory, 'remote'),
    ...environment,
  };
  function run(id) {
    assert.ok(scripts[id], `missing workflow run step: ${id}`);
    const result = spawnSync('bash', ['-eo', 'pipefail', '-c', scripts[id]], {
      cwd: directory, env, encoding: 'utf8', timeout: 10000,
    });
    assert.ifError(result.error);
    return result;
  }
  function state() { return JSON.parse(readFileSync(statePath, 'utf8')); }
  function logs() {
    return existsSync(env.STUB_LOG) ? readFileSync(env.STUB_LOG, 'utf8').trim().split('\n').filter(Boolean).map(JSON.parse) : [];
  }
  return {directory, env, run, state, logs};
}

function pass(result) { assert.equal(result.status, 0, result.stdout + result.stderr); }
function failWithoutUpload(f, result) {
  assert.notEqual(result.status, 0, `unsafe workflow input was accepted: ${JSON.stringify(f.state())}\n${result.stdout}${result.stderr}`);
  assert.deepEqual(f.state().uploads, [], 'failure must precede all uploads');
}

test('release workflows pin actions, separate read-only CI, and invoke the reusable package job directly', () => {
  assert.deepEqual(check.permissions, {contents: 'read'});
  assert.deepEqual(release.permissions, {contents: 'write'});
  assert.deepEqual(prepare.permissions, {contents: 'write', 'pull-requests': 'write', issues: 'write'});
  assert.deepEqual(prepare.on.push.branches, ['main']);
  assert.equal(prepare.jobs.prepare.if, "github.ref == 'refs/heads/main'");
  assert.equal(prepare.jobs.package.needs, 'prepare');
  assert.equal(prepare.jobs.package.if, "needs.prepare.outputs.release_created == 'true'");
  assert.equal(prepare.jobs.package.uses, './.github/workflows/release.yml');
  assert.equal(prepare.jobs.package.with.tag, '${{ needs.prepare.outputs.tag_name }}');
  assert.equal(prepare.jobs.package.with['expected-sha'], '${{ needs.prepare.outputs.sha }}');
  assert.equal(release.on.workflow_call.inputs['expected-sha'].required, true);
  assert.equal(release.on.workflow_dispatch.inputs['expected-sha'].required, false);
  assert.equal(release.defaults.run.shell, 'bash');
  assert.equal(release.jobs.package.steps.find(step => step.uses?.startsWith('actions/checkout@')).with.ref, 'refs/tags/${{ inputs.tag }}');
  assert.equal(release.jobs.package.steps.find(step => step.id === 'upload').env.RELEASE_COMMIT, '${{ steps.identity.outputs.commit }}');
  for (const workflow of [release, prepare, check]) {
    assert.ok(!Object.hasOwn(workflow.on, 'pull_request_target'));
    for (const job of Object.values(workflow.jobs)) {
      for (const step of job.steps ?? []) {
        if (step.uses) assert.match(step.uses, /^[^@]+@[a-f0-9]{40}$/, 'actions must use immutable commit pins');
        if (step.run) assert.ok(!step.run.includes('${{'), 'shell values must enter through environment variables');
      }
    }
  }
});

test('invalid release tags and SHA inputs are rejected before GitHub access', t => {
  for (const badTag of ['0.1.1', 'v0.1.1-beta.1', 'main', 'v0.1.1; echo bad', 'v0.1.1\n']) {
    const f = fixture(t, {}, {RELEASE_TAG: badTag});
    failWithoutUpload(f, f.run('inputs'));
    assert.deepEqual(f.logs(), []);
  }
  const f = fixture(t, {}, {EXPECTED_SHA: 'not-a-commit'});
  failWithoutUpload(f, f.run('inputs'));
  assert.deepEqual(f.logs(), []);
});

test('tag, checkout, version and initial draft mismatches fail before upload', t => {
  const badDrafts = [
    {isDraft: false}, {tagName: 'v0.1.2'}, {targetCommitish: otherCommit}, {targetCommitish: 'main'},
  ];
  const cases = [
    {tagCommit: otherCommit}, {dirty: ' M README.md\n'},
    {packageVersion: '0.1.0'}, {lockVersion: '0.1.0'},
    ...badDrafts.map(draft => ({draft: {tagName: tag, isDraft: true, targetCommitish: commit, ...draft}})),
  ];
  for (const changes of cases) {
    const f = fixture(t, changes);
    pass(f.run('inputs'));
    failWithoutUpload(f, f.run('identity'));
  }
  const f = fixture(t, {}, {EXPECTED_SHA: otherCommit});
  pass(f.run('inputs'));
  failWithoutUpload(f, f.run('identity'));
});

test('upload rechecks moved tags, changed drafts and local checksums', t => {
  const cases = [
    {remoteTagObject: otherCommit},
    {laterDraft: {tagName: tag, isDraft: false, targetCommitish: commit}},
    {laterDraft: {tagName: tag, isDraft: true, targetCommitish: otherCommit}},
    {laterDraft: {tagName: 'v0.1.2', isDraft: true, targetCommitish: commit}},
  ];
  for (const changes of cases) {
    const f = fixture(t, changes);
    pass(f.run('identity'));
    failWithoutUpload(f, f.run('upload'));
  }
  const f = fixture(t);
  pass(f.run('identity'));
  writeFileSync(join(f.directory, 'dist', assets[0]), 'corrupted local archive');
  failWithoutUpload(f, f.run('upload'));
});

test('a matching draft receives exactly four verified assets and supports safe recovery reruns', t => {
  const f = fixture(t, {}, {EXPECTED_SHA: ''});
  pass(f.run('inputs'));
  pass(f.run('identity'));
  assert.equal(readFileSync(f.env.GITHUB_OUTPUT, 'utf8'), `commit=${commit}\n`);
  for (let run = 0; run < 2; run++) {
    pass(f.run('upload'));
    assert.deepEqual(f.state().uploads, Array.from({length: run + 1}, () => assets).flat());
    for (const asset of assets) {
      assert.deepEqual(readFileSync(join(f.directory, 'remote', asset)), readFileSync(join(f.directory, 'dist', asset)));
    }
  }
  const commands = f.logs().filter(entry => entry.tool === 'gh');
  assert.ok(commands.every(entry => entry.args[1] !== 'create'), 'recovery must populate the existing draft');
  assert.equal(commands.filter(entry => entry.args[1] === 'download').length, 2);
  assert.match(readFileSync(f.env.GITHUB_STEP_SUMMARY, 'utf8'), /Draft assets verified for v0\.1\.1/);
});

test('a corrupted downloaded asset fails verification without claiming success', t => {
  const f = fixture(t, {corruptDownload: 'context-report.json'});
  pass(f.run('identity'));
  const result = f.run('upload');
  assert.notEqual(result.status, 0);
  assert.deepEqual(f.state().uploads, assets);
  assert.ok(!existsSync(f.env.GITHUB_STEP_SUMMARY));
});
