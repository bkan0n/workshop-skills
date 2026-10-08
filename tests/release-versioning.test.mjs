import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
import {test} from 'node:test';
import {parse as parseYaml} from 'yaml';

const require = createRequire(import.meta.url);
const {Manifest} = require('release-please/build/src/manifest.js');
const {setLogger} = require('release-please/build/src/util/logger.js');

const root = fileURLToPath(new URL('../', import.meta.url));
const silent = {error() {}, warn() {}, info() {}, debug() {}, trace() {}};
setLogger(silent);
const paths = [
  'release-please-config.json', '.release-please-manifest.json',
  'package.json', 'package-lock.json', 'CHANGELOG.md',
  'skills/overwatch-workshop/SKILL.md', 'skills/overpy/SKILL.md',
  'README.md', 'INSTALL.md', 'sources/lock.json',
  'evals/results/2026-10-07/results.json',
  'evals/results/2026-10-07/raw/pair-health.json',
];

function files() {
  return new Map(paths.map(path => [path, readFileSync(root + path, 'utf8')]));
}

// Exercise the complete first-run manifest path with no GitHub releases or
// tags. The library must synthesize its baseline from the version manifest.
// This stub has no API client; unexpected remote operations fail.
async function prepare(message) {
  const before = files();
  const bootstrap = JSON.parse(before.get('release-please-config.json'))['bootstrap-sha'];
  const github = new Proxy({
    repository: {owner: 'test-owner', repo: 'test-repository', defaultBranch: 'main'},
    async *releaseIterator() {},
    async *tagIterator() {},
    async *mergeCommitIterator(branch) {
      assert.equal(branch, 'main');
      if (message) {
        yield {
          sha: '1234567890123456789012345678901234567890', message,
          files: ['skills/overwatch-workshop/references/execution.md'],
        };
      }
      // If the exclusive baseline were included, this would incorrectly bump
      // a docs-only patch release and appear in its changelog.
      yield {sha: bootstrap, message: 'feat!: excluded baseline content', files: ['README.md']};
      throw new Error('Manifest read commits older than its bootstrap boundary');
    },
    async getFileJson(path) {
      assert.ok(before.has(path), `unexpected file read: ${path}`);
      return JSON.parse(before.get(path));
    },
    async getFileContentsOnBranch(path) {
      assert.ok(before.has(path), `unexpected file read: ${path}`);
      return {parsedContent: before.get(path), content: before.get(path), sha: 'fixture'};
    },
  }, {
    get(target, property) {
      assert.ok(property in target, `unexpected GitHub operation: ${String(property)}`);
      return target[property];
    },
  });
  const manifest = await Manifest.fromManifest(github, 'main');
  const current = manifest.releasedVersions['.'];
  const candidates = await manifest.buildPullRequests();
  assert.ok(candidates.length <= 1, 'the matched pair has one release PR');
  const candidate = candidates[0];
  const version = candidate?.body.releaseData[0].version;
  return {before, manifest, current, candidate, version};
}

function applyCandidate(before, candidate) {
  const after = new Map(before);
  const changed = new Set();
  for (const update of candidate.updates) {
    if (!after.has(update.path) && !update.createIfMissing) continue;
    const previous = after.get(update.path);
    const next = update.updater.updateContent(previous, silent);
    after.set(update.path, next);
    if (next !== previous) changed.add(update.path);
  }
  return {after, changed};
}

function frontmatter(text) {
  return parseYaml(text.split('\n---\n', 1)[0].slice(4));
}

function outsideVersionBlocks(text) {
  return text.replace(/^[^\n]*x-release-please-start-version[^\n]*\n[\s\S]*?^[^\n]*x-release-please-end[^\n]*$/gm, '');
}

test('release config has one matched root component and the pinned updater library', async () => {
  const {before, manifest} = await prepare('docs: clarify rule reactivation');
  assert.equal(require('release-please/package.json').version, '17.6.0');
  assert.deepEqual(Object.keys(manifest.repositoryConfig), ['.']);
  const config = manifest.repositoryConfig['.'];
  assert.equal(config.releaseType, 'node');
  assert.equal(config.includeComponentInTag, false);
  assert.equal(config.includeVInTag, true);
  assert.equal(config.draft, true);
  assert.equal(config.forceTag, true);
  assert.equal(JSON.parse(before.get('.release-please-manifest.json'))['.'], JSON.parse(before.get('package.json')).version);
});

test('a documentation-only change updates every release destination and preserves source pins and evidence', async () => {
  const {before, current, candidate, version} = await prepare('docs: clarify rule reactivation');
  assert.ok(candidate, 'knowledge-only documentation changes must produce a release');
  const expected = `${current.major}.${current.minor}.${current.patch + 1}`;
  assert.equal(version.toString(), expected);
  assert.match(candidate.body.toString(), /Skill knowledge and guidance/);
  assert.ok(!candidate.body.toString().includes('excluded baseline content'));
  const {after, changed} = applyCandidate(before, candidate);
  assert.deepEqual([...changed].sort(), [
    '.release-please-manifest.json', 'CHANGELOG.md', 'INSTALL.md', 'README.md',
    'package-lock.json', 'package.json', 'skills/overpy/SKILL.md',
    'skills/overwatch-workshop/SKILL.md', 'sources/lock.json',
  ].sort());

  assert.equal(JSON.parse(after.get('.release-please-manifest.json'))['.'], expected);
  assert.equal(JSON.parse(after.get('package.json')).version, expected);
  const oldPackageLock = JSON.parse(before.get('package-lock.json'));
  const newPackageLock = JSON.parse(after.get('package-lock.json'));
  assert.equal(newPackageLock.version, expected);
  assert.equal(newPackageLock.packages[''].version, expected);
  oldPackageLock.version = expected;
  oldPackageLock.packages[''].version = expected;
  assert.deepEqual(newPackageLock, oldPackageLock, 'a release bump must not upgrade dependencies');
  const oldSources = JSON.parse(before.get('sources/lock.json'));
  const newSources = JSON.parse(after.get('sources/lock.json'));
  oldSources.release = expected;
  assert.deepEqual(newSources, oldSources, 'only the source lock release field may change');

  for (const skill of ['overwatch-workshop', 'overpy']) {
    const text = after.get(`skills/${skill}/SKILL.md`);
    assert.equal(frontmatter(text).metadata['workshop-skills-version'], expected);
  }
  const overpy = after.get('skills/overpy/SKILL.md');
  assert.equal(frontmatter(overpy).metadata['workshop-skills-requires-workshop'], expected);
  assert.ok(overpy.includes(`metadata.workshop-skills-version: '${expected}'`));
  assert.ok(after.get('README.md').includes(`Skill release **${expected}**`));
  assert.ok(after.get('INSTALL.md').includes(`skill release **${expected}**`));
  assert.ok(after.get('INSTALL.md').includes(`workshop-skills-${expected}.zip`));
  assert.ok(after.get('INSTALL.md').includes(`workshop-overpy-skills-${expected}.zip`));

  for (const path of ['README.md', 'INSTALL.md', 'skills/overpy/SKILL.md', 'skills/overwatch-workshop/SKILL.md']) {
    assert.equal(outsideVersionBlocks(after.get(path)), outsideVersionBlocks(before.get(path)), `${path}: unmarked guidance must stay unchanged`);
    assert.ok(!after.get(path).includes(current.toString()), `${path}: stale current-version text`);
  }
  for (const path of paths.filter(path => path.startsWith('evals/'))) {
    assert.equal(after.get(path), before.get(path), 'historical evaluation versions are evidence, not release metadata');
  }
  assert.ok(after.get('CHANGELOG.md').includes(before.get('CHANGELOG.md')), 'existing changelog history must be preserved');
});

test('features retain minor bumps and pre-1.0 breaking changes bump minor', async () => {
  for (const message of ['feat: add a companion route', 'fix!: change the companion reference contract']) {
    const {current, candidate, version} = await prepare(message);
    assert.ok(candidate);
    const expected = current.major === 0 || message.startsWith('feat:')
      ? `${current.major}.${current.minor + 1}.0`
      : `${current.major + 1}.0.0`;
    assert.equal(version.toString(), expected);
  }
});

test('maintenance-only commits do not create empty user-facing releases', async () => {
  const {candidate} = await prepare('ci: adjust an internal check');
  assert.equal(candidate, undefined);
});

test('an unreleased baseline alone does not manufacture an initial release', async () => {
  const {candidate} = await prepare(null);
  assert.equal(candidate, undefined);
});
