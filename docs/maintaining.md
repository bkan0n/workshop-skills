# Maintaining the skills

Use Node 24.14.0, npm 11.9.0 and Python 3.14.3. Install the locked development dependency with `npm ci --ignore-scripts`. Skill readers need only Markdown/file access.

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

Official actions are pinned to verified release commit SHAs. Read-only push/pull-request checks are separate from the manually invoked draft-release workflow.

Update package version, both skill versions, OverPy's companion requirement, source-lock release version, and installation/download examples together. Commit the passing state, create and push its matching `vX.Y.Z` tag to the chosen repository, then manually run **Prepare draft release** with that existing tag.

The workflow checks out the tag, verifies its resolved commit and versions, reruns checks, packages, and creates a draft prerelease. It refuses to overwrite an existing release. If upload fails after draft creation, inspect/remove the incomplete draft before retrying or repair its assets deliberately. Publishing is a separate maintainer action.

Workflow artifacts expire; public distribution uses release assets. Workflow syntax and action inputs were checked against [official GitHub documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax). A local validation does not claim a remote GitHub run occurred.
