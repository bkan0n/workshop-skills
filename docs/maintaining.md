# Maintaining the skills

Use Node 24.14.0, npm 11.9.0 and Python 3.14.3. Install the locked development dependency with `npm ci --ignore-scripts`. Skill readers need only Markdown/file access.

Workflow regression tests also use Bash, `jq`, `cmp`, and `sha256sum` (or `shasum` on macOS). These are available on the selected GitHub Ubuntu runner; install them locally when running that test suite on another system.

## Commands

| Command | Purpose |
| --- | --- |
| `npm run validate` | Metadata, companion versions, portable links/anchors, source locks, corpus coverage, context report |
| `npm run catalog:check` | Generated references match normalized data and installed initialized OverPy exports |
| `npm run examples` | Compile/decompile fixtures, check expected visible/hidden diagnostics and packaged copies |
| `npm test` | Pipeline failure tests and archive tests |
| `npm run check` | All checks above |
| `npm run catalog` | Regenerate references from reviewed normalized inputs |
| `npm run build` | Reject stale generated content, validate, and build both archives without fetching sources |

ZIP entries use fixed ordering, dates, modes, platform attributes, and stored compression, avoiding compression-library differences. Workshop content matches across both archives. `RELEASE.json` records source locks, commit, dirty status, and member hashes; the external checksum includes that manifest. Local previews can identify dirty checkouts; public release builds require a clean selected tag.

## Wiki rewriting and updates

`sources/wiki-content.json` holds rewritten claims and metadata. `sources/wiki-tables/` preserves normalized factual data and its limitations. `scripts/generate-wiki.py` creates selective references and `coverage/wiki-coverage.json` without the raw cache.

Keep the research ledger as the initial 630-article/721-note baseline. Every note needs a retained destination or explicit consolidation, historical, deferred, or exclusion decision. A signature does not cover a prose exception. Keep source edit dates, documented tests, compiler checks, and game observations distinct. The API did not supply per-article authors; do not invent them. Preserve attribution available within source material and the general notices.

```sh
npm run refresh:wiki
# Offline comparison of an already completed API snapshot:
python3 scripts/refresh-wiki.py --compare-existing
```

The downloader uses only the paginated JSON API with three-second pacing. It validates all pages and a terminal empty page before replacing the archive. Failed/incomplete fetches preserve the prior snapshot. The comparison writes `.cache/wiki-review-queue.json`, never curated prose. Missing items in a completed snapshot are review candidates, not automatic knowledge deletions.

Inspect each affected claim/reference, reconcile evidence, edit the normalized rewrite, and regenerate. Review added articles explicitly. Expanding the corpus requires updating the baseline accounting and tests in that reviewed change; new sources must not silently count as covered. Update source locks/hashes only after review. Raw responses and linked media stay out of distribution. Never scrape the website.

## OverPy updates

`package-lock.json` pins 9.7.17 and integrity. `sources/lock.json` separately records the annotated tag object, peeled source commit, inspected paths, and normalized snapshot hash. Use the standalone package including `quickjs-ng.wasm`; the repository root is a VS Code extension.

Inspect a target release's source/docs/tests and verify its commit before changing dependencies. With that reviewed version installed, explicitly run `node scripts/generate-api.mjs --snapshot`. Review the export diff, update the source lock, regenerate, and rerun examples. The adapter awaits `readyPromise`; it must not initialize settings twice. Changing the target version also requires updating the explicit extractor pin and source URLs.

Review hidden/internal identifiers, receiver arguments, module exports, aliases, defaults, annotations, and settings. Runtime exports take precedence over declarations for unavailable functions. Keep unknown wiki aliases as discrepancies rather than guessed mappings. Preserve upstream notices when distributing derived data.

## Examples and evaluations

Add complete examples to `examples/manifest.json`, reference applicable claims, record expected visible and hidden diagnostics, and synchronize installable copies. The harness does not bless unexpected warnings or snapshots. Fragments must be labeled; a compilation result never implies a live-game test.

`npm run validate` reports characters, words and `ceil(characters/4)` estimates. Targets are 2,500 estimated tokens for Workshop and 4,500 for the unique combined path. These estimates are not tokenizer measurements. Large selective references are listed for editorial review, not loaded by default.

Follow [the evaluation procedure](../evals/README.md) for controlled behavior/retrieval comparisons. Unrun cases remain unrun. Routine GitHub checks use no paid model API.

## GitHub releases

Release orchestration lives in GitHub Actions. [Release Please](https://github.com/googleapis/release-please-action) owns version PRs, changelogs, tags, and draft creation. GitHub's CLI handles draft asset upload/download inside the workflow. There is no custom Python release uploader. The local packager remains responsible for this project's deterministic archive layout, source manifests, and content validation; it performs no remote release operations.

### Repository setup

Push this repository and its full history to the intended GitHub destination, using `main` as the release branch. Update the clearly labeled `OWNER/REPO` installation examples to that destination. Enable Actions and, in **Settings → Actions → General**, allow GitHub Actions to create pull requests. The workflow declares its required contents, pull-request, and issue permissions.

The default token is the repository's `GITHUB_TOKEN`. Under GitHub's current behavior, checks on a PR created or updated with that token need a writer to select **Approve workflows to run**. For unattended bot-PR checks, optionally provide `RELEASE_PLEASE_TOKEN` with the required repository permissions, using a suitably scoped personal access token. GitHub App authentication can also be configured later. Never place tokens in source files. See [GitHub's event/token rules](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).

### Normal release flow

1. Merge changes using [Conventional Commits](../CONTRIBUTING.md). Prefer squash merges with a conventional PR title. `fix:` and visible `docs:` changes produce patches; `feat:` produces a minor release. Breaking changes produce a minor bump before 1.0 and a major bump after it. CI-only changes wait for a releasable change.
2. **Prepare release PR** runs on pushes to `main` and can be dispatched manually on `main`. It maintains one root release PR with the changelog and synchronized version updates. Approve its checks if GitHub requests it, then review and merge the PR.
3. Release Please creates the tag and a draft release. The workflow explicitly calls **Package draft release** with that tag and commit SHA. This avoids relying on a bot-created tag to start another workflow.
4. The packaging workflow verifies the tag, clean checkout, package/source-lock versions, and existing draft's target commit. It runs the complete checks, builds both ZIPs, uploads them with `SHA256SUMS` and the context report, downloads the assets again, and compares their bytes. It never publishes a release.
5. Review the successful run and release notes, then publish the draft. Releases currently default to prereleases; choose release status deliberately when the project reaches its intended stable milestone.

The node release strategy updates `package.json` and both root entries in `package-lock.json`. Configured updaters also synchronize both skills' metadata, OverPy's companion requirement and version-check prose, `sources/lock.json.release`, and marked README/INSTALL version examples. Compiler versions, wiki source locks, and historical research/evaluations remain unchanged. Keep exactly one SemVer occurrence per line inside generic updater blocks: the pinned updater replaces the first matching version on each marked line. Tests exercise the actual Release Please library's updater behavior.

### Initial version and retries

The manifest starts at **0.1.0**, with bootstrap commit `aed867aa85a8b17a8797af301e973c4372c31bf8` as the exclusive history boundary. This is a development baseline, not a claim that a public 0.1.0 release exists. The first subsequent documentation/fix change proposes 0.1.1; a feature proposes 0.2.0. Preserve that commit in the repository history. After the first release, Release Please uses its release history; do not keep resetting the bootstrap boundary.

If asset upload fails after draft creation, run **Package draft release** manually for the same existing draft tag. Supply its full commit SHA when available. The workflow rechecks the draft and tag, replaces only the four expected asset names, and verifies the downloaded result. It refuses a published release, a mismatched target commit, or a moved tag. Keep the release in draft until the packaging run succeeds. If creation failed before a draft/tag exists, rerun **Prepare release PR** first; the packaging workflow does not invent a release.

Workflow artifacts expire; public distribution uses release assets. Action versions are pinned to verified commit SHAs. Release Please Action 5.0.0 bundles the same 17.6.0 library used by the offline updater tests; update both together. Local tests validate updater behavior and workflow failure paths with fake GitHub responses. They do not claim a remote Actions run or public release occurred. Workflow syntax follows [official GitHub documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
