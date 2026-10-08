import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, writeFileSync, mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { resolve, join } from 'node:path';
import { spawnSync } from 'node:child_process';

const root = resolve(import.meta.dirname, '..');
const original = JSON.parse(readFileSync(join(root, 'examples/manifest.json'), 'utf8'));
function assertRejectedFixture(id, mutate, errorPattern) {
  const manifest = structuredClone(original);
  manifest.examples = [manifest.examples.find(example => example.id === id)];
  assert.ok(manifest.examples[0], `Missing fixture ${id}`);
  mutate(manifest.examples[0]);
  const temp = mkdtempSync(join(tmpdir(), 'overpy-harness-test-'));
  try {
    const file = join(temp, 'manifest.json');
    writeFileSync(file, JSON.stringify(manifest));
    const result = spawnSync(process.execPath, ['scripts/check-examples.mjs', '--manifest', file], {
      cwd: root, encoding: 'utf8', timeout: 30000,
    });
    assert.ifError(result.error);
    assert.equal(result.status, 1);
    const report = JSON.parse(result.stdout);
    assert.equal(report.totals.failed, 1);
    assert.match(report.results[0].errors.join('\n'), errorPattern);
  } finally {
    rmSync(temp, { recursive: true, force: true });
  }
}

test('example harness rejects unexpected emitted warnings', () => {
  assertRejectedFixture('opy-expected-warning', fixture => { fixture.expected.warningCodes = []; }, /Expected warnings/);
});
test('example harness rejects unexpected hidden diagnostics', () => {
  assertRejectedFixture('opy-strings', fixture => { fixture.expected.hiddenWarnings = []; }, /Unexpected hidden diagnostics/);
});
test('example harness detects missing generated behavior', () => {
  assertRejectedFixture('opy-collections', fixture => { fixture.expected.outputIncludes = ['NONEXISTENT REQUIRED ACTION']; }, /Missing expected generated fragment/);
});
test('example harness detects a stale packaged copy', () => {
  assertRejectedFixture('opy-collections', fixture => { fixture.copies = [{ destination: 'skills/overpy/examples/strings.opy' }]; }, /packaged copy differs/);
});
test('example harness never blesses an expected failure that compiles', () => {
  assertRejectedFixture('opy-collections', fixture => { fixture.expected.outcome = 'reject'; fixture.expected.errorIncludes = 'Deliberate error'; }, /Expected rejection, but source compiled/);
});
test('example harness rejects untraceable claim references', () => {
  assertRejectedFixture('opy-collections', fixture => { fixture.claims = ['missing-claim-id']; }, /unknown claim/);
});
