# Workshop and OverPy skills

Two portable Agent Skills for writing and debugging Overwatch Workshop programs, with particular attention to engine quirks that ordinary programming assumptions miss.

- [overwatch-workshop](skills/overwatch-workshop/SKILL.md) supports native Workshop independently and owns shared engine knowledge.
- [overpy](skills/overpy/SKILL.md) adds the language, compiler, project workflow, and diagnostics. It requires the matched Workshop skill.

Each starts with a small required foundation, then routes to focused guides, exact APIs, and rewritten evidence. Shared runtime explanations live in Workshop. Normal use requires readable Markdown, without a search script or network lookup.

## Install

Copy the directories under `skills/` into your agent's supported skill location, keeping both as siblings for OverPy. See [installation instructions](INSTALL.md) for package layout and hosts that isolate skill files.

Version **0.1.0** uses **OverPy 9.7.17** and the **September 29, 2026** wiki snapshot. Both skills must be version 0.1.0. The host must expose reference and companion files; SKILL.md metadata does not install dependencies.

## Evidence and scope

The rewrite accounts for all 630 archived articles and 721 extracted notes, including explicit exclusions, historical material, and deferred work. Source dates, conflicts, and practical exceptions accompany the generated signatures.

Archived observations are not current-game guarantees. Examples are checked with the pinned compiler and expected diagnostics; no in-game testing is claimed. See [the survey](docs/research/2026-10-07-workshop-wiki-survey.md), [coverage](coverage/wiki-coverage.json), and [agent evaluations](evals/README.md).

Workshop.codes web-editor authoring and complex-system companions remain in the [roadmap](docs/roadmap.md). Their underlying engine facts still belong in the foundations.

## Build and maintain

Maintainers use Node **24.14.0**, npm **11.9.0**, and Python **3.14.3** (standard library only). Normal skill use needs none of these tools.

```sh
npm ci --ignore-scripts --no-audit --no-fund
npm run check
npm run build
```

`dist/` receives Workshop-only and matched-pair ZIP archives, SHA-256 checksums, and a context report. Packaging never fetches the wiki. Reviewed Markdown and normalized source data are checked in.

[Maintenance instructions](docs/maintaining.md) explain source updates and GitHub releases. GitHub validates changes; the manual release workflow builds an existing tag and creates a **draft** for review. No remote repository or release is created by a local build.

The existing `archive/` is a local raw cache, excluded from tracking and packages. Retrieval uses the Workshop.codes JSON API with conservative pacing, never website scraping.

## License

Original material is GPL-3.0-only. Generated data derives from OverPy; the wiki rewrite uses written permission confirmed by the maintainer. See [LICENSE](LICENSE) and [source notices](THIRD_PARTY_NOTICES.md). Linked media and game assets are not distributed.
