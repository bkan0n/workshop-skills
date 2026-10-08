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
| `npm run release:update-wiki` | Download the wiki through its JSON API, compare hashes, and automatically update the bundled references |
| `npm run release:check-wiki` | Optional check-only comparison; report differences without applying them |

ZIP entries use fixed ordering, dates, modes, platform attributes, and stored compression, avoiding compression-library differences. Workshop content matches across both archives. `RELEASE.json` records source locks, commit, dirty status, and member hashes; the external checksum includes that manifest. Local previews can identify dirty checkouts; public release builds require a clean selected tag.

## Wiki rewriting and updates

`sources/wiki-content.json` holds rewritten claims and metadata. `sources/wiki-tables/` preserves normalized factual data and its limitations. `sources/wiki-articles.json` holds every original API article record, including the full content, slug and any supplied attribution. `scripts/generate-wiki.py` creates selective references, all full article references under `skills/overwatch-workshop/references/wiki/archive/`, and `coverage/wiki-coverage.json` without a raw page cache or network access.

The generator verifies the full snapshot's ID set and each original content SHA-256 against `sources/wiki-index.json`. `sources/lock.json` pins both the index and full source snapshot. The original Markdown is quoted verbatim apart from CRLF display normalization. A fence longer than any source fence keeps HTML/media and remote URLs inert; local article navigation and curated-reference links sit above the quoted text. Do not remove article bodies merely because their curated disposition is excluded or deferred. Linked media are outside the archive's scope.

Workshop.codes wiki articles are trusted as the source of truth. Do not add blanket “unverified” or “not game tested” disclaimers to wiki references. Preserve qualifications actually stated by the source, including historical fixes, dates, units and conditions. The API did not supply per-article authors; preserve available attribution without inventing it.

```sh
# Update the wiki references when preparing a release:
npm run release:update-wiki
# The same automatic update outside release preparation:
npm run refresh:wiki
# Apply an already completed local API snapshot without fetching:
python3 scripts/refresh-wiki.py --compare-existing
# Optional check-only comparison, without applying changes:
npm run release:check-wiki
```

The downloader uses only the paginated JSON API with three-second pacing. It validates all pages and a terminal empty page before replacing `.cache/wiki-candidate/`, then verifies raw-page and article hashes. Failed or incomplete fetches preserve the prior candidate and installed files. No HTML scraping occurs. Ordinary skill use, `npm run check`, and packaging remain offline.

Maintenance writes `.cache/wiki-update-report.json` and `.cache/wiki-articles.candidate.json`. The report records added, changed and removed articles, previous/current hashes, metadata changes, affected references and whether the update was applied. The API assigns new numeric IDs to revisions; stable `group_id` values identify the same article across revisions.

The default command automatically replaces changed sources, updates their hashes and regenerates references. Changed article notes use the latest wiki text directly, replacing older summaries. Their table references use the full current article, preserving all conditions and footnotes; older map/hero table parts become short local routes to it. This avoids carrying forward copied values from an older revision. Local paths and existing claim anchors remain valid; old numeric archive paths lead to the current revision. New articles appear in the local archive and the new-article topic. Removed articles get a notice at their existing paths instead of continuing to display obsolete source text.

Handwritten guides provide patterns and navigation; the current linked wiki article takes precedence. Maintenance regenerates article and table references and inserts current-source routes in affected guides. Readers must open the relevant updated source before using facts or values copied in those guides. It does not attempt to rewrite arbitrary instructional prose. Keep guides focused on reusable patterns and link to the current source for changing lists and values.

Updates are generated in a temporary copy and checked for valid metadata, content hashes, complete source coverage and working local links before replacing installed directories. A generation or validation failure leaves the installed source and skills unchanged. These are integrity checks, not a factual approval gate. The initial research ledger stays as a historical record; stable local article and note IDs remain accounted for while current source revisions and hashes advance automatically.

Successful automatic maintenance exits **0**, including when updates were applied; failures exit **2**. Optional `--check` mode exits **0** for no changes, **1** for differences and **2** for failure, and never applies changes. There is no pending-review queue. Commit the refreshed sources, generated references and coverage with the release preparation changes. Raw page caches and linked media stay out of distribution; full article references are distributed.

Function usage groups are curated in `sources/api-usage.json`. Every native action/value and public OverPy callable/member must be assigned once; generation rejects missing, duplicate and stale assignments. Add new functions to the appropriate task group when updating compiler data. Keep task routers short and link to individual entries instead of repeating signatures or loading every group.

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

The public repository is [bkan0n/workshop-skills](https://github.com/bkan0n/workshop-skills), with `main` as the release branch. Preserve its full history, including the bootstrap commit below. Actions must be enabled and **Settings → Actions → General** must allow GitHub Actions to create pull requests. The workflow declares its required contents, pull-request, and issue permissions.

The default token is the repository's `GITHUB_TOKEN`. Under GitHub's current behavior, checks on a PR created or updated with that token need a writer to select **Approve workflows to run**. For unattended bot-PR checks, optionally provide `RELEASE_PLEASE_TOKEN` with the required repository permissions, using a suitably scoped personal access token. GitHub App authentication can also be configured later. Never place tokens in source files. See [GitHub's event/token rules](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).

### Normal release flow

1. Merge changes using [Conventional Commits](../CONTRIBUTING.md). Prefer squash merges with a conventional PR title. `fix:` and visible `docs:` changes produce patches; `feat:` produces a minor release. Breaking changes produce a minor bump before 1.0 and a major bump after it. CI-only changes wait for a releasable change.
2. **Prepare release PR** runs on pushes to `main` and can be dispatched manually on `main`. It maintains one root release PR with the changelog and synchronized version updates. During release preparation, run `npm run release:update-wiki` and include the automatically refreshed sources and references in the release changes. This maintenance download is separate from the offline build. Approve the PR's checks if GitHub requests it, then review and merge the PR.
3. Release Please creates the tag and a draft release. The workflow explicitly calls **Package draft release** with that tag and commit SHA. This avoids relying on a bot-created tag to start another workflow.
4. The packaging workflow verifies the tag, clean checkout, package/source-lock versions, and existing draft's target commit. It runs the complete checks, builds both ZIPs, uploads them with `SHA256SUMS` and the context report, downloads the assets again, and compares their bytes. It never publishes a release.
5. Review the successful run and release notes, then publish the draft. Releases currently default to prereleases; choose release status deliberately when the project reaches its intended stable milestone.

The node release strategy updates `package.json` and both root entries in `package-lock.json`. Configured updaters also synchronize both skills' metadata, OverPy's companion requirement and version-check prose, `sources/lock.json.release`, and marked README/INSTALL version examples. Compiler versions, wiki source locks, and historical research/evaluations remain unchanged. Keep exactly one SemVer occurrence per line inside generic updater blocks: the pinned updater replaces the first matching version on each marked line. Tests exercise the actual Release Please library's updater behavior.

### Initial version and retries

The manifest starts at **0.1.0**, with bootstrap commit `aed867aa85a8b17a8797af301e973c4372c31bf8` as the exclusive history boundary. This is a development baseline, not a claim that a public 0.1.0 release exists. The first subsequent documentation/fix change proposes 0.1.1; a feature proposes 0.2.0. Preserve that commit in the repository history. After the first release, Release Please uses its release history; do not keep resetting the bootstrap boundary.

If asset upload fails after draft creation, run **Package draft release** manually for the same existing draft tag. Supply its full commit SHA when available. The workflow rechecks the draft and tag, replaces only the four expected asset names, and verifies the downloaded result. It refuses a published release, a mismatched target commit, or a moved tag. Keep the release in draft until the packaging run succeeds. If creation failed before a draft/tag exists, rerun **Prepare release PR** first; the packaging workflow does not invent a release.

Workflow artifacts expire; public distribution uses release assets. Action versions are pinned to verified commit SHAs. Release Please Action 5.0.0 bundles the same 17.6.0 library used by the offline updater tests; update both together. Local tests validate updater behavior and workflow failure paths with fake GitHub responses. They do not claim a remote Actions run or public release occurred. Workflow syntax follows [official GitHub documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
