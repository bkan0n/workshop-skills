# Workshop and OverPy skills: design specification

Date: 2026-10-07

Status: Approved by the user on 2026-10-07; implementation authorized.

Approved follow-up, 2026-10-07: release orchestration uses GitHub Actions and Release Please with Conventional Commits, replacing the original manual release uploader. Release PRs synchronize the pair, create a draft/tag on merge, and explicitly invoke package validation/upload. Publication remains manual. Installation documentation includes both `npx skills` and manual installation. The current process is documented in [maintenance](../maintaining.md) and [installation](../../INSTALL.md); this supersedes the original release-flow details below.

## Purpose and agreed outcome

Create a public, portable pair of skills that help an agent write, understand, and debug Overwatch Workshop programs without overlooking the engine's unusual behavior. The user's primary authoring language is OverPy, but native Workshop must be fully supported independently.

The skills must teach the distinctions that change a solution: when execution yields, what a rule's event context means, which inputs are captured or reevaluated, what mutates state, and what needs cleanup. `Wait()` is an important motivating example, not the boundary of the content.

The agreed approach combines rewritten explanations with compact references generated from pinned structured sources. Normal use requires readable Markdown files, not Python search, a compiler, network access, or a particular agent platform. A small required foundation directs the agent to deeper references only when the task needs them. Workshop knowledge is shared with OverPy rather than repeated in both skills.

The initial release includes the two skills, their references and examples, maintainable source accounting, local build tools, GitHub validation and packaging, and evaluation cases. It does not promise current in-game verification of all documented behavior. Uncertainty is explicit so the project can improve incrementally.

## Scope and ownership

| Component | Owns | Uses |
| --- | --- | --- |
| `overwatch-workshop` | Engine behavior, native Workshop syntax and workflow, ordinary authoring and debugging, lifecycle, limits, API semantics, native examples | Rewritten wiki evidence; exact structured API data where available |
| `overpy` | OverPy syntax, types and helpers, compiler behavior, project organization, compile/decompile workflow, diagnostics, generated Workshop inspection, language-specific quirks | Required Workshop foundation and selected Workshop references; pinned OverPy sources |
| Maintainer tooling | Source refresh, catalog generation, coverage validation, example checks, packaging | Workshop.codes JSON API and pinned upstream data |
| Future companions | Complex-system design and Workshop.codes web-editor authoring | The same Workshop foundation; OverPy when applicable |

An engine claim has one canonical explanation under Workshop. OverPy explains only the language mapping, compiler transformation, mitigation, or additional quirk and links to that explanation. A source article can contribute to several references or both skills; an article's original category does not decide ownership.

Workshop.codes web-editor mixins, directives, and editor workflows are excluded from the initial skills. They are a separate future skill. OSTW syntax is not taught as native Workshop or OverPy. The foundations retain small techniques and underlying engine facts used by complex modes, while full boss systems, substantial mode architecture, pathfinding systems, and similar applications remain future companion work.

## Skill loading and dependency contract

Both skill directories contain standard `SKILL.md` entry points with `name` and `description` frontmatter. Descriptions give concrete activation cues and distinguish the native language from OverPy. This project also requires a string `metadata.workshop-skills-version` on both skills and `metadata.workshop-skills-requires-workshop` on OverPy; the latter names the exact compatible Workshop release initially. These are project conventions inside the standard's optional metadata map, not a standard dependency resolver. Compatibility and license fields explain human-readable constraints; the release manifest records source versions.

For a native Workshop task, the agent reads the Workshop entry point and `references/foundation.md`, then follows the relevant task or symptom routes. For an OverPy task, it reads the OverPy entry point, resolves Workshop, reads that same Workshop foundation, and reads OverPy's `references/foundation.md`. Already loaded, applicable content is reused. The agent does not reopen shared material just because both skills are active. Native syntax tutorials are selected only when native output or debugging requires them.

The shared foundation includes a concise topic router, with both task cues and common symptoms. Examples include a rule firing once, stale HUD text, incorrect array mutation, an effect that survives its owner, unexpected raycast results, or code that compiles but behaves incorrectly. The router gives a specific file to read and the question it answers. Exact API lookup uses small indexes and individual entries or narrow families; agents never need to read the entire API catalog.

All skill links are relative. In the supported bundle, the two directories are siblings:

```text
overwatch-workshop/
  SKILL.md
  references/
  examples/
overpy/
  SKILL.md
  references/
  examples/
```

OverPy locates Workshop using the host's available-skill listing when provided, with the verified sibling path `../overwatch-workshop/` as the packaged default. It verifies the companion's identity and compatible release metadata before following its references. Version `0.1.0` starts with exact matched skill versions; compatibility can be broadened later after testing. Shared reference paths are part of this contract.

There is no portable mechanism that forces every SKILL.md host to install dependencies or expose sibling files. The published requirement is a host capable of reading a skill's bundled references and its required companion. Installation documentation explains the sibling layout and how to expose both roots when a host isolates skills. No host-specific global path appears in skill content. If the dependency cannot be read or is incompatible, the agent explains how to install the matched pair and clearly identifies the resulting knowledge limitation.

Initial context targets are at most 2,500 estimated tokens for Workshop's required entry and foundation, and 4,500 for the unique required files in the combined OverPy path. The build reports both character and word counts and uses `ceil(character_count / 4)` as a transparent, model-independent estimate, not an actual tokenizer measurement. These are quality targets: accuracy must not be sacrificed to meet them. A release documents any exception and its reason. Deep references aim for one decision or tightly related topic per file; larger catalogs have selective indexes. No required reading chain loads a whole book before useful work can begin.

## Workshop content design

The required foundation teaches a compact mental model and tells the agent when to look deeper:

- Rules execute in an event context; ongoing conditions, discrete events, loops, and subroutines have different triggering and concurrency behavior.
- Wait is a scheduling and state-observation decision. Choose its mode and placement deliberately. Do not add a Wait to every rule as a universal repair, and do not remove one merely to reduce code size.
- Global and player storage, lifecycle, captured inputs, reevaluation, and contextual values must be chosen explicitly.
- Returned values, mutations, handles, and ongoing controls have different ownership and lifetime rules.
- Workshop does not inherit ordinary Python or JavaScript type, collection, coordinate, or concurrency assumptions.
- Compiler acceptance, archived documentation, and observed game behavior are different kinds of evidence.

Detailed references are organized by use rather than the archive's Actions/Values split:

| Topic | Required depth and examples of selective content |
| --- | --- |
| Execution and event context | Condition rearming; Wait variants and cancellation; loops; event subjects; context availability; subroutine calls and concurrent starts; retrigger limitations |
| State and lifecycle | Initialization; global/player scope; joining versus loading/spawning; death, hero/team changes, leaving; ownership when departed-player data is unavailable |
| Values and collections | Type coercion and comparisons; null/failure values; array copies versus variable mutation; flattening; indexed writes; array evaluation context |
| Reevaluation and observation | Snapshot versus live inputs; action-specific reevaluation; chase initialization; change notification; server versus viewer evaluation |
| Resources and cleanup | IDs and Last Created/Started scope; capacity and creation failure; cleanup of visuals, projectiles, health pools, modifiers, assists, ongoing controls |
| Geometry and movement | Coordinates and signs; points versus directions; local/world transforms; raycast misses; player-to-position behavior; motion, camera, collision, attachment |
| Combat and heroes | Damage/heal/health/kill differences; attribution and statistics; barriers and turrets; projectiles; dated hero and ability exceptions |
| Players and bots | Player sets, spectators, dummy bots versus AI, spawn and hero restrictions |
| Match and configuration | Base-mode constraints, scoring and completion, time versus game progression, respawns, custom settings, native import/export and share codes |
| Visuals, audio, and strings | HUD/effects, Local Player, viewer-dependent values, localization, fonts and string limitations, rendering and layout |
| Limits, performance, debugging | Static element count versus execution/server/render/resource cost; event loss from throttling; instrumentation; minimal reproduction and symptom routes |
| Compatibility and data | Dated bugs and workarounds; historical techniques; exact APIs/enums/settings; selectively loaded maps, assets, measurements, and their limitations |

Numeric limits and hero lists are dated source data, not timeless facts. Cross-cutting topics link to the canonical owner. For example, a HUD reference points to the resource-lifetime explanation rather than repeating it.

Native authoring guidance covers complete rule structure, event/condition/action syntax, variables and subroutines, settings boundaries, and importing or exporting text in the game. Debugging distinguishes parse/import problems, incorrect event or data context, timing/reevaluation errors, lifecycle failures, and resource/performance issues. Small diagnostic examples demonstrate the distinction being taught; complete mode design is not required to understand them.

## OverPy content design

The OverPy foundation first establishes that OverPy is its own language. Python-looking syntax is not permission to invent Python libraries, runtime behavior, or unsupported constructs. It states the required Workshop dependency, pinned compiler version, exact-lookup routes, and the distinction between source semantics and generated engine behavior.

Selective references cover:

- Source organization, imports/includes as actually supported, variables, rule declarations, events, conditions, annotations, functions/subroutines, and relevant preprocessing.
- Expressions, types, collections, control flow, language helpers, built-ins, and documented differences from both Python and native Workshop.
- Project and file conventions, compiler installation/use, input and output language settings, reproducible compilation, and diagnostic interpretation.
- Decompiling existing native code, explaining representational limitations, and inspecting generated Workshop when source behavior is surprising.
- Compiler transformations, optimizations, warnings, and language-specific quirks, with references to inherited Workshop behavior.
- Exact functions, members, modules, macros, constants, annotations, directives, and custom settings from pinned structured exports.

This is a complete ordinary authoring/debugging process, not just a grammar sheet. If a compiler is unavailable, the agent still provides useful source and a precise validation procedure while labeling the result uncompiled. It does not claim a compiler run or silently install dependencies in the user's project without considering that project's conventions.

OverPy documentation, upstream implementation, and upstream tests are additional source inputs; the Workshop wiki is not sufficient authority for the language. The initial catalog target is the standalone `overpy` package at version `9.7.17`. Its annotated source tag `v9.7.17` has tag-object SHA `bce4ef757d9c0de0153eaeebc65af472b997f9c6` and points to commit `5a7d0e294b8cad73b9701987bb584d0551d7fa4d`. The source tag, resolved commit, package integrity, inspected files, and retrieval date must be recorded separately; the installed package is checked against these source expectations during implementation. A version appearing in a repository's package file is not proof that the current branch equals the release tag.

The adapter loads the standalone module and awaits `readyPromise` before extracting initialized data. It does not import the repository root, whose entry point belongs to the VS Code extension. The installed compiler must retain its adjacent `quickjs-ng.wasm` runtime file; it is not a single-file JavaScript dependency. Relevant exports include action/value data, OverPy functions/members/modules/macros, constants, heroes/maps, event data, annotations, directives, keywords, and the initialized custom-game-settings schema. The adapter follows upstream autocomplete's public-name and visibility rules, including member receivers and internal identifiers, rather than printing raw map keys as valid syntax. It must not initialize the custom settings schema a second time. Actual runtime exports take precedence over declarations of functions that are not exported.

Workshop catalogs may also use these structured exports, clearly attributed to the pinned OverPy interpretation of the Workshop API. Wiki prose supplies semantic notes and exceptions. A wiki-only entry or source disagreement is retained with an explicit disposition instead of silently discarded because it is absent from the compiler data.

## Source accounting and rewriting

The [full corpus survey](../research/2026-10-07-workshop-wiki-survey.md) accounts for all 630 articles in the local snapshot of 2026-09-29. It contains 721 extracted information notes and 145 article records with uncertainty or quality flags. These are bookkeeping totals, not counts of unique verified quirks. Article bodies were read; external media, shared modes, and current game behavior were not tested.

Every source article receives a maintained disposition: rewritten, consolidated, catalog-covered, historical, deferred, or excluded with a reason. Multi-topic articles can have several destinations. The initial survey's 721 notes are also accounted for through retained claim IDs or a documented duplicate, correction, historical, deferred, or exclusion decision. Mapping an article to a generated signature alone does not cover its prose exceptions.

Curated references rewrite the information into a consistent practical form:

1. The behavior or constraint and its applicability.
2. Why an ordinary programming assumption can fail here.
3. The safe pattern or debugging check.
4. A minimal example only when it adds clarity.
5. Evidence, limitations, and links to related material.

This is an editorial shape, not a requirement to pad every short API note with five headings. Repeated prose, navigation, irrelevant site instructions, and duplicate examples are removed. Useful facts inside advanced tutorials remain available even when the full system recipe is deferred. Large tables become indexed data references when their accuracy supports doing so.

Maintainer records have these interfaces:

| Record | Essential fields |
| --- | --- |
| Source | Stable source ID, canonical URL, source kind, snapshot/version, content hash, source edit date when provided, retrieval date, attribution/notice information |
| Claim | Stable claim ID, concise assertion, applicability, source IDs and locations, evidence status, documented test date/patch if known, conflicts, destination anchors |
| Coverage | Article ID and note locator, disposition, destination/claim IDs or reason, review state |
| Example | Stable ID, dialect, complete or fragment, referenced claims, fixture path, compiler/version and results, expected diagnostics, separate game-test status |
| Release | Skill versions and dependency contract, source locks, generator version, package file manifest and checksums |

Source edit dates, documented test dates, local compilation dates, and actual game-test dates are separate. Unknown values stay explicitly unknown; they are never inferred from a recent edit. Claim labels distinguish archived documentation, upstream implementation evidence, source-reported tests, unresolved conflict, historical/patched behavior, and local game verification when it later exists. Example validation is recorded separately so a successful compile cannot upgrade an engine claim's evidence status.

Inline caution is proportional to the claim. An uncertain exception is qualified where it affects a recommendation and has a focused way to check it. The agent should not burden every ordinary response with a catalog of caveats. Sources remain in the files and are surfaced in replies when attribution, uncertainty, or verification is useful.

Known source conflicts, such as geometry sign examples, are recorded and corrected only with identified supporting evidence. An older alias is not automatically obsolete. The comparison article's 2026 edit does not supersede its stated 2024 test date. Historical health-pool and Stadium workarounds stay labeled historical, not recommended as current techniques.

## Repository and package boundaries

The current workspace becomes the repository; no remote repository name or public publication is implied by this specification. Existing archive tooling is reused where appropriate. The proposed layout separates installable knowledge from maintenance evidence:

```text
skills/
  overwatch-workshop/{SKILL.md,references/,examples/}
  overpy/{SKILL.md,references/,examples/}
sources/                 # locks, source identities, compact normalized data
coverage/                # article/note dispositions and claim destinations
examples/                # canonical compiler fixtures and validation metadata
scripts/                 # existing API archive tooling and maintenance commands
tests/                   # focused checks for the generation/build pipeline
evals/                   # agent prompts, rubrics, and recorded evaluation method
docs/
  specs/
  research/
  roadmap.md
  maintaining.md
.github/workflows/
README.md
LICENSE
THIRD_PARTY_NOTICES.md
```

The skill directories contain all normal-use material. Examples shown in references are checked against canonical fixtures or explicitly marked as fragments; package generation does not leave links pointing outside the installed skill pair. Source paths in public records are repository-relative, never this machine's absolute paths. Existing raw archive files remain a local refresh cache, excluded from release packages and from public tracking by default. Build output and dependency caches are also excluded.

Checked-in rewritten Markdown and generated catalogs make the skills readable directly from a checkout. Compact normalized source records, source locks, and coverage data make generation and review reproducible without redistributing the full raw wiki. If a source snapshot is unavailable, ordinary use and package assembly still work; a source refresh is a separate maintenance operation.

The user-approved license for original project material is GPL-3.0, aligning with the OverPy source used for generated references. This does not imply that all sources have identical terms. The user has confirmed written consent to rewrite the wiki. Source-specific attribution and notices are retained, the permission's public scope is recorded without publishing private correspondence, and any material with incompatible or unclear redistribution rights is omitted or replaced before public release. No remote images, game assets, or compiler binaries are bundled merely because an article links to them.

## Generation, updates, and GitHub builds

Normal packaging is deterministic and never fetches the wiki. It consumes the reviewed skill files and pinned normalized data, validates them, and produces two archives: Workshop alone and a matched Workshop+OverPy pair. The shared Workshop directory is byte-identical in both. There is no separate OverPy-only archive in the initial release. Each archive includes the relevant license/notice material and a release manifest. ZIP ordering, timestamps, file modes, platform attributes, line endings, and compression settings are fixed; generated package metadata does not contain wall-clock build times. Repeated builds from the same inputs in the recorded locked build environment must have identical checksums.

Node.js 24 LTS is the initial maintainer-tool runtime for the standalone OverPy adapter and example checks; its exact tested patch and package-manager version are recorded with the implementation lockfile. The existing standard-library Python downloader can remain the API refresh tool. Neither runtime is a skill-use requirement. Dependency installation in CI uses a frozen lockfile; catalog generation must not silently upgrade OverPy.

The source-update flow is deliberately separate:

1. Fetch Workshop.codes through its documented paginated JSON API, using conservative pacing and the existing cache where valid. Do not scrape the website.
2. Record the completed snapshot, IDs, hashes, edit dates, and API metadata. Compare against the prior successful snapshot.
3. Map added, changed, and missing articles to affected claims and references. A missing item in a failed or incomplete fetch is not a confirmed deletion.
4. Produce a review queue; do not overwrite curated prose. Reconcile contradictions and update source/coverage records with the editorial changes.
5. For OverPy updates, compare pinned structured exports and relevant documentation/tests, review public-name mappings and changed compiler behavior, then regenerate catalogs and rerun examples.

Build commands expose distinct validation, catalog generation/check, source-refresh, example-check, and package operations. A routine build does not require API credentials or refresh sources. A maintainer can reproduce the package from committed content after the locked build dependencies are available.

GitHub pull requests and branch pushes run deterministic checks and upload review artifacts. A manually triggered release workflow resolves a chosen existing version tag to its commit, checks out and builds that commit, and rejects a mismatch between the tag version, either skill version, and the companion requirement. The release manifest identifies that repository commit and its source locks. After checks pass, the workflow creates a draft GitHub Release containing those archives and checksums. Publishing that draft is a maintainer action. Workflow artifacts are useful for review, but durable public downloads are GitHub Release assets because workflow artifacts expire. This work prepares the repository and workflows; remote creation or publication requires the user to supply the destination when ready.

## Validation and evaluation

Automated checks must distinguish structural integrity from behavioral truth:

| Check | What it establishes |
| --- | --- |
| Skill metadata and portability | Valid names/descriptions, documented compatibility, no machine-specific paths or mandatory agent-specific commands |
| Reference and dependency validation | Existing files and anchors, compatible companion versions, installable links within the allowed skill roots |
| Coverage validation | All 630 initial article IDs and 721 survey notes accounted for, explicit exclusions/deferred material, valid claim destinations |
| Catalog reproducibility | Pinned input identity, deterministic output, valid public identifiers, no unreviewed generated diff |
| Example validation | Appropriate compiler acceptance, expected diagnostics, complete-versus-fragment distinction, honest validation metadata |
| Package validation | Required files/notices, excluded caches/raw archive, matching Workshop copies, reproducible checksums, no links to missing repository-only content |
| Context report | Unique required-file cost for each loading path, unusually large references, duplicate shared prose and routing problems |

Complete OverPy examples compile with the pinned standalone API after initialization. The harness checks diagnostics as well as output and records expected warnings rather than treating every successful return as a clean example. Complete native examples are checked through decompilation/recompilation when supported by the pinned compiler. This is labeled "accepted by pinned OverPy," not "verified in Overwatch." Unsupported native constructs are recorded with an explicit review reason; they do not silently disappear from coverage. Roundtrips need not be byte-identical because compilation can transform representation.

The example harness is noninteractive and fails rather than silently blessing new snapshots. It does not run upstream's interactive test runner as a blanket substitute. Fragments are never counted as successful complete-program tests. Actual game verification remains optional and is recorded with a patch/date and observed result when performed.

Agent evaluations contain both native and OverPy prompts and evaluate behavior rather than matching one reference answer. The initial suite includes:

- Correct Wait placement/mode, plus a case where blindly adding a Wait is wrong.
- Event subject and unavailable context, ongoing-rule rearming, and a lifecycle cleanup problem.
- Array-copy versus mutation behavior and a captured-versus-reevaluated value problem.
- Resource ownership/capacity, raycast miss handling, and a dated hero exception.
- A nonexistent API request and Python-looking constructs unsupported by OverPy.
- Missing companion, missing compiler, and conflicting/stale evidence.
- A simple native task and an OverPy task where only the foundation and a small set of relevant references should be read.

Rubrics score semantic reasoning, valid dialect/API use, relevant reference retrieval, uncertainty handling, and validation honesty. Where a model run is available, compare the same prompts without skills, with the existing search-based skill, and with the new pair using the same model and settings. Record files read and unique context size alongside answer quality. The initial repository includes the cases and a manual/repeatable evaluation procedure; it does not require a paid model service for ordinary GitHub checks or claim unrun agent evaluations passed.

Pipeline tests concentrate on meaningful failure modes: missing coverage records, broken companion links, nonpublic API names, incomplete snapshots, unexpected compiler warnings, stale catalogs, and packages that cannot be used after extraction. Trivial prose changes do not require duplicative tests.

## Failure behavior in ordinary use

| Situation | Expected agent behavior |
| --- | --- |
| Missing/incompatible Workshop dependency | Identify the missing version/access requirement, give matched-bundle installation guidance, avoid claiming to have read unavailable evidence |
| No compiler available | Continue useful authoring/analysis, label code uncompiled, give the exact check required |
| Source uncertainty or disagreement | Qualify the affected assertion, use a supported conservative pattern where possible, propose a focused check |
| Task needs a dated limit or exception | Read its focused reference and evidence date; do not generalize an old observation to every patch |
| Requested operation unsupported by Workshop | Explain the constraint and feasible alternatives without inventing an API |
| Task uses web-editor or another dialect | Identify the dialect boundary and the deferred companion; do not teach its syntax as Workshop or OverPy |
| Source refresh fails | Preserve last good sources/catalogs and report an incomplete update; do not treat missing data as deletion |

## Deferred work recorded now

`docs/roadmap.md` contains concrete stubs, not empty installable skills:

- **Workshop.codes web editor:** authoring workflow, mixins, defaults, inclusion and editor control directives; requires Workshop; starts from the relevant surveyed articles; must distinguish editor preprocessing from the engine and OverPy.
- **Complex-system companions:** substantial mode/state-machine architecture, boss/combat systems, deeper performance work, and other advanced techniques; requires Workshop and optionally OverPy; scopes are chosen in later design sessions.
- **Growing verification coverage:** focused game reproductions, patch-specific regression records, expanded real-world agent evaluations, and improved source conflict resolution.

Maintainer API access remains repository tooling, not a web-editor feature or an additional required skill. Optional convenience tools can be added later only when they improve a demonstrated lookup or validation need; the first release does not rebuild a mandatory Python search layer.

## Acceptance criteria

The initial implementation is ready for review when:

1. Both discoverable skills exist; Workshop works alone and the matched pair follows the shared loading/dependency contract.
2. The full corpus and its extracted notes have explicit final dispositions. All retained in-scope information has rewritten destinations or exact catalog entries with its semantic exceptions preserved.
3. The required foundations, topic routes, native workflow, and complete OverPy workflow are usable without network access, a search script, or a specific agent host.
4. Exact catalogs come from a verified pinned source/package pair, with language names and internal identifiers handled correctly.
5. Claims and examples distinguish source evidence, compiler results, and game verification. Known conflicts/historical techniques are not silently promoted into current recommendations.
6. Complete examples receive the applicable checks, unresolved limitations are recorded, and deterministic metadata/link/coverage/catalog/package checks pass.
7. Local package builds produce the two self-contained archives with matching shared files, notices, and checksums. GitHub workflows can perform the same checks and prepare a draft release.
8. Evaluation cases and loading/context reports exist; results identify what actually ran. The required reading stays small, with any target exceptions visible for review.
9. Roadmap stubs preserve the web-editor and complex-system ideas without exposing them as finished skills.
10. Public-facing installation, maintenance, attribution, and compatibility documentation explains how to use and improve the release. Actual public publication remains a distinct destination-specific action.

## Design evidence

- [Workshop corpus survey and linked ledgers](../research/2026-10-07-workshop-wiki-survey.md): all archived articles reviewed, proposed topic boundaries, source limitations.
- [OverPy issue 439](https://github.com/Zezombye/overpy/issues/439): motivating language/runtime knowledge, minimized API data, and evaluation ideas.
- [Workshop.codes API documentation](https://workshop.codes/wiki/articles/workshopcodes-api): source-maintenance contract; use the API instead of scraping.
- [Agent Skills specification](https://agentskills.io/specification): portable metadata, bundled references, relative navigation, and progressive disclosure.
- [Pinned OverPy source](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d): standalone exports, compiler/decompiler, autocomplete presentation, publishing and license sources. The [annotated tag object](https://api.github.com/repos/Zezombye/overpy/git/tags/bce4ef757d9c0de0153eaeebc65af472b997f9c6) records the release-to-commit mapping. The implementation verifies the package integrity.
- [Node.js release status](https://nodejs.org/en/about/previous-releases): Node 24 as the selected LTS tooling line at design time.
- [GitHub workflow artifact documentation](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/download-workflow-artifacts): temporary workflow artifact retention, distinct from release distribution.
