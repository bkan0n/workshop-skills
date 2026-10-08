# Workshop and OverPy skills

Two portable Agent Skills for writing and debugging Overwatch Workshop programs, with particular attention to engine quirks that ordinary programming assumptions miss.

- [overwatch-workshop](skills/overwatch-workshop/SKILL.md) supports native Workshop independently and owns shared engine knowledge.
- [overpy](skills/overpy/SKILL.md) adds the language, compiler, project workflow, and diagnostics. It requires the matched Workshop skill.

Each starts with a small required foundation, then routes to functions grouped by task, focused guides, exact APIs, and rewritten evidence. The Workshop skill also includes all 630 full archived article bodies as optional local references. Shared runtime explanations live in Workshop. Normal use requires readable Markdown, without a search script or network lookup; installing the archive does not load it all into context.

## Install

Use [the Skills CLI](https://github.com/vercel-labs/skills) to discover the skills and install the matched pair for Codex from [bkan0n/workshop-skills](https://github.com/bkan0n/workshop-skills):

```sh
npx skills add bkan0n/workshop-skills --list
npx skills add bkan0n/workshop-skills --skill overwatch-workshop --skill overpy --agent codex
```

For native Workshop only, omit `--skill overpy`. Select **Project** if prompted, or add `--global` for use across projects. Replace `codex` with your agent's identifier. OverPy needs both skills explicitly selected; dependency metadata does not install its companion.

Alternatively, copy the complete skill folders or extract a matched release archive, keeping them as siblings with all references and examples. See [installation instructions](INSTALL.md) for manual setup, local checkouts, other agents, and updates. Versioned archives will appear on the [releases page](https://github.com/bkan0n/workshop-skills/releases) as maintainers publish them.

<!-- x-release-please-start-version -->
Skill release **0.1.0** requires matching versions of both skills for OverPy.
<!-- x-release-please-end -->

The references use **OverPy 9.7.17** and the bundled Workshop.codes wiki snapshot. The host must expose reference and companion files.

## Evidence and scope

The rewrite accounts for all 630 archived articles and 721 extracted notes, including explicit exclusions, historical material, and deferred work. Source dates, conflicts, and practical exceptions accompany the generated signatures.

The installed wiki is the trusted source of truth for runtime behavior and takes precedence over derivative guides. Examples are checked with the pinned compiler and expected diagnostics. See [the survey](docs/research/2026-10-07-workshop-wiki-survey.md), [coverage](coverage/wiki-coverage.json), and [agent evaluations](evals/README.md).

Workshop.codes web-editor authoring and complex-system companions remain in the [roadmap](docs/roadmap.md). Their underlying engine facts still belong in the foundations.

## Build and maintain

Maintainers use Node **24.14.0**, npm **11.9.0**, and Python **3.14.3** (standard library only). Normal skill use needs none of these tools.

Local workflow tests also require the shell utilities listed in [maintenance](docs/maintaining.md); GitHub's selected Ubuntu runner supplies them.

```sh
npm ci --ignore-scripts --no-audit --no-fund
npm run check
npm run build
```

`dist/` receives Workshop-only and matched-pair ZIP archives, SHA-256 checksums, and a context report. Packaging never fetches the wiki. Generated Markdown and source data are checked in.

[Maintenance instructions](docs/maintaining.md) explain source updates and GitHub releases. Release Please uses [Conventional Commits](CONTRIBUTING.md) to prepare a version PR and changelog. Merging that PR creates a **draft** release; GitHub Actions validates its tag, builds both packages, and verifies the uploaded assets. Publishing remains a maintainer action. No remote repository or release is created by a local build.

When preparing a release, run `npm run release:update-wiki` (also available as `npm run refresh:wiki`). It downloads the complete Workshop.codes JSON API snapshot with conservative pacing, compares article hashes, validates structure and completeness, then automatically updates the tracked sources and bundled references. No factual approval gate is required. `npm run release:check-wiki` is an optional check-only command that reports upstream changes without applying them. Ordinary checks and builds remain offline.

The original `archive/` and downloaded `.cache/wiki-candidate/` contain raw API page caches and are excluded from tracking and packages. The tracked full article snapshot is `sources/wiki-articles.json`; its generated per-article references are included in the installed Workshop skill. Retrieval uses the API, never website scraping.

## License

Original material is GPL-3.0-only. Generated data derives from OverPy; the wiki rewrite uses written permission confirmed by the maintainer. See [LICENSE](LICENSE) and [source notices](THIRD_PARTY_NOTICES.md). Linked media and game assets are not distributed.
