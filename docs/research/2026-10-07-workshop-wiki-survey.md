# Workshop wiki survey for the Workshop and OverPy skills

Research date: 2026-10-07. Source snapshot: 2026-09-29T03:33:06Z.

This survey informs the skill design; it is not the final skill content or an approved implementation specification.

## Coverage and method

Three reviewers read all **630 archived Markdown article bodies**, divided into non-overlapping assignments balanced by source size. Each article has a source-linked record of useful information, topics, editorial disposition, and uncertainty. Ordinary API entries and site-only material are accounted for explicitly.

| Archive category | Articles reviewed |
| --- | ---: |
| Actions | 227 |
| Values | 264 |
| Constants | 51 |
| Events | 14 |
| Tutorials | 37 |
| References | 32 |
| Workshop.codes | 5 |
| **Total** | **630** |

The coverage check compares every reviewed ID, title, path, and source URL with the archive index, checks required fields, and rejects duplicates or missing records. It verifies the bookkeeping, not the truth of the underlying game behavior.

Research records use portable paths: article `path` fields are relative to the local `archive/` cache, manifest `repository_path` fields are relative to the repository, and assignment/progress report filenames are relative to their containing research directory. Source URLs and hashes identify the evidence when the raw cache is not present.

Large HTML tables were read in compact representations. Linked external images, videos, share codes, and other offsite resources were not fetched or executed. Some articles therefore contain additional visual evidence that remains unexamined. No website scraping, compiler execution, or in-game testing was performed for this survey.

The ledgers contain **721 extracted information notes**; these are not 721 distinct verified quirks. **145 article records** include uncertainty or quality flags. Those flags cover patch sensitivity, missing evidence, inconsistencies, malformed examples, and other limitations; they do not mean all flagged material is wrong.

- [Article-by-article ledger](workshop-wiki-survey-2026-10-07/article-ledger.json)
- [Coverage validation](workshop-wiki-survey-2026-10-07/coverage-summary.json)
- [Actions, events, and supplemental material](workshop-wiki-survey-2026-10-07/group-1-findings.md)
- [Values, constants, and supplemental material](workshop-wiki-survey-2026-10-07/group-2-findings.md)
- [Long-form guides and data catalogs](workshop-wiki-survey-2026-10-07/group-3-findings.md)

## Findings that change the content design

All behavior below is evidence from the archived sources, not a claim of independent verification against the current game.

### 1. Event identity, triggering, and concurrency need a shared explanation

The skill must teach which entity executes a rule, what Event Player means for each event, how ongoing conditions rearm, and which contextual values are available. Subroutine calls and concurrent rule starts inherit context but have different control-flow behavior. These concepts connect many otherwise isolated API descriptions.

The performance tutorial reports that an active damage-event rule can lose retriggers while waiting, with attacker-scoped versus victim-scoped execution affecting multi-target behavior. The short damage-event API pages establish the event subject but omit this concurrency claim. That omission is neither a contradiction nor independent corroboration. [Ongoing Each Player](https://workshop.codes/wiki/articles/4824), [Subroutine](https://workshop.codes/wiki/articles/1292), [server stability](https://workshop.codes/wiki/articles/6064).

### 2. Lifecycle determines what data and operations are available

Joining, loading, spawning, dying, changing hero, changing team, and leaving are different states. The Player Left Match article says the departed player's variables and other information are already unavailable. Cleanup designs therefore need an explicit ownership and storage strategy. The performance tutorial also reports that hero/slot filters can abort active rules when a player changes away from the filter. [Player Left Match](https://workshop.codes/wiki/articles/4821), [server stability](https://workshop.codes/wiki/articles/6064).

### 3. Reevaluation, snapshots, and change notification are distinct

Reevaluation is specific to an action and its inputs. Some inputs remain live, some are captured, and selecting reevaluation does not necessarily change the selected player. Chase requires compatible initialized storage. The bug registry reports that chased values may change without notifying conditions or Wait Until until arrival; the performance guide reports that changing one array member can invalidate all conditions using that variable. These claims need clear applicability and verification labels. [Chase Global Variable At Rate](https://workshop.codes/wiki/articles/6027), [OW2 Changes/Bugs](https://workshop.codes/wiki/articles/9463), [server stability](https://workshop.codes/wiki/articles/6064).

### 4. Type coercion and collection behavior deserve their own references

The comparison tables document surprising boolean coercion, asymmetric comparisons, and results that make ordinary cross-type algebra unsafe. Their behavioral test date is April 22, 2024, despite a January 2026 article edit date. The required foundation should flag the risk; the full tables and exact caveats belong in selective references.

Other concrete distinctions include Append To Array returning a copy while a similarly named variable modification mutates state, appending an array flattening its elements, indexed writes extending arrays with zeros, and Current Array Element being meaningful only in an array-evaluation context. [Comparisons and truth](https://workshop.codes/wiki/articles/7978), [Append To Array](https://workshop.codes/wiki/articles/4565), [Current Array Element](https://workshop.codes/wiki/articles/6956).

### 5. Resource ownership, cleanup, and capacity failures form a major topic

Effects, HUD text, icons, projectiles, health pools, modifiers, assists, and ongoing controls have different lifetimes and identifiers. Their Last Created/Last Started values need the right ownership assumptions. Creation can fail at capacity, and visual disappearance is not necessarily proof of resource release. The bug registry reports projectile ownership-related leaks when an owner leaves or changes. [Create HUD Text](https://workshop.codes/wiki/articles/4343), [OW2 Changes/Bugs](https://workshop.codes/wiki/articles/9463).

### 6. Server context and viewer context must be distinguished

Local Player is documented as a client-specific visual/HUD value, with spectator/replay caveats. A shared visual can display different data to different viewers, but this is not a general replacement for server-side Event Player. The bug registry also reports values whose behavior differs during client-side visual evaluation. [Local Player](https://workshop.codes/wiki/articles/4807), [OW2 Changes/Bugs](https://workshop.codes/wiki/articles/9463).

### 7. Geometry and movement contain action-specific conventions

The corpus documents positive X as left, different world/local transformations, player-to-position coercions, and different raycast miss results. Ray Cast Hit Player returns Null on a miss, whereas Ray Cast Hit Position returns the supplied endpoint. Passing a player as a position has a documented offset that must not be casually equated with an explicit position expression. Impulse, acceleration, throttle, attachment, camera, collision, and forced position also have distinct semantics. [Vector](https://workshop.codes/wiki/articles/4758), [Ray Cast Hit Player](https://workshop.codes/wiki/articles/4729), [Ray Cast Hit Position](https://workshop.codes/wiki/articles/4730), [vectors guide](https://workshop.codes/wiki/articles/1903).

### 8. Combat operations, attribution, and hero support differ

Set Player Health, Heal, Damage, Kill, Respawn, and Resurrect are not interchangeable. Attribution, statistics, barriers/turrets, death state, and modifiers affect their behavior. The hero exception registry separately distinguishes reading ammo from setting it, reading maximum ammo from changing it, charges from cooldowns, alternate forms, and control schemes. These are dated compatibility records, not universal rules for all current or future heroes. [Set Player Health](https://workshop.codes/wiki/articles/4518), [OW2 Changes/Bugs](https://workshop.codes/wiki/articles/9463).

### 9. Match state and base-mode behavior need explicit treatment

Pausing match time is not described as freezing players, objectives, or game-mode advancement. Scoring, completion, spawning, restart rules, and hero availability interact with the selected base mode. Several API calls can silently do nothing in an unsupported context. Empty allowed-hero input, for example, is documented as a no-op and undermines a tutorial workaround if only one hero was allowed. [Pause Match Time](https://workshop.codes/wiki/articles/4399), [Set Player Allowed Heroes](https://workshop.codes/wiki/articles/4426), [hero-selection workaround](https://workshop.codes/wiki/articles/4856).

### 10. Static size limits and runtime performance need separate guidance

Element count, execution workload, resource capacity, startup spikes, and client rendering are different concerns. Disabling content is documented to affect execution cost differently from element count. Polling, batching, and throttling can change gameplay behavior or lose events; they are not automatically equivalent optimizations. Numeric examples in performance articles must remain examples. [Element Count Calculation](https://workshop.codes/wiki/articles/4857), [server stability](https://workshop.codes/wiki/articles/6064).

### 11. Text and UI have correctness issues beyond layout

String limits, language-dependent censorship, whole-string font fallback, sort order, reevaluation, FOV, spectators, and world-space anchoring can affect correctness. The long text guide mixes Workshop runtime behavior with OverPy helpers, so it requires claim-level separation between the two skills. Large effect, texture, map, and measurement catalogs should load only when relevant. [Text formatting](https://workshop.codes/wiki/articles/5734), [camera-relative text](https://workshop.codes/wiki/articles/9496).

### 12. The archive contains multiple authoring dialects and source-quality defects

Workshop.codes editor mixins and control directives are a third dialect. **The user has placed web-editor support in a separate future skill. Its features and authoring workflows are excluded from both foundation skills.** Its source articles remain in this survey for coverage and future reuse. OSTW-specific material also needs explicit identification. API labels, constants, and user-facing function syntax should come from appropriate authoritative sources rather than a naive conversion of page titles.

The reviewers found assignment/comparison mistakes, incomplete examples, malformed JSON, mismatched tables, ambiguous aliases, and unsupported generalizations. These require editorial decisions and example checks. Geometry examples also contain a cross-product sign contradiction and conflicting-looking vertical-angle conventions. Old material alone is not classified as fixed or obsolete. Two entire articles are clearly historical: the health-pool exploit and Stadium workaround. Other articles can mix patched methods with unverified workarounds and need finer-grained labels. [Editor directives](https://workshop.codes/wiki/articles/2082), [Mixins](https://workshop.codes/wiki/articles/1876), [dot/cross guide](https://workshop.codes/wiki/articles/1963), [patched health-pool technique](https://workshop.codes/wiki/articles/6790), [broken Stadium workaround](https://workshop.codes/wiki/articles/7385).

## Revised candidate topic map

This is a proposal informed by the survey, pending design review.

| Topic | Selectively loaded material |
| --- | --- |
| Execution and event context | Conditions, rearming, waits, cancellation, concurrency, subroutines |
| State and lifecycle | Globals/player state, initialization, join/spawn/death/hero/leave transitions |
| Values and collections | Coercion, null/failure values, arrays, mutation versus copies, contextual values |
| Reevaluation and observation | Captured/live inputs, chase, change notification, server/client evaluation |
| Resource ownership | Handles, capacity, lifetime, cleanup, modifiers and ongoing actions |
| Geometry and movement | Coordinates, raycasts, movement controls, physics, camera, collision |
| Combat and hero interactions | Damage/healing, health pools, attribution, projectiles, ability exceptions |
| Players and bots | Player groups, spectators, dummy bots versus AI, spawning and hero restrictions |
| Match and configuration | Base-mode integration, custom settings, in-game presets, native import/export and share codes |
| Visuals, audio, and strings | HUD/effects, viewer context, localization, layout, assets |
| Budgets, performance, and debugging | Element counts, workload, instrumentation, symptom-driven diagnosis |
| Compatibility and dated exceptions | Patch-specific bugs, supported environments, historical techniques |
| Optional data catalogs | Exact APIs/enums/settings, maps, measurements, assets and source limitations |

The short required foundation should teach the concepts that tell an agent **when to open these references**. It should not try to absorb every exception, table, API entry, or workaround. A single topic may have several small files where that improves selective reading.

OverPy should own its syntax, compiler behavior, language helpers, generated-code interpretation, and complete project workflow. Shared engine facts stay in Workshop. The wiki alone is not a complete authoritative OverPy language reference; OverPy documentation, structured compiler exports, and upstream tests remain additional inputs.

## Deferred companion-skill roadmap stubs

### Workshop.codes web editor

- **Purpose:** Author and debug code using the Workshop.codes web editor and its own preprocessing features.
- **Future scope:** Editor workflow, mixins, parameters/defaults, `@include`, `@contents`, and editor-specific `@if`, `@for`, and `@each`; explain how preprocessing produces native Workshop output.
- **Source starting points:** [Mixins](https://workshop.codes/wiki/articles/1876) and [Editor control directives](https://workshop.codes/wiki/articles/2082), with the survey's unfinished-documentation and inconsistent-example flags preserved.
- **Proposed dependency:** Reuse Workshop's runtime foundation. This is a distinct authoring dialect; OverPy is not its language reference.
- **Release boundary:** Deferred. No editor-feature guidance or editor workflow is included in the initial Workshop or OverPy skills. This stub records future work rather than defining an installable skill.

### Complex-system companions

- **Purpose:** Design and maintain substantial modes and interconnected systems using the foundation skills.
- **Candidate areas:** State machines and mode architecture; complex combat/boss systems; deeper optimization; pathfinding and compression where supported by appropriate sources.
- **Dependency:** Workshop knowledge, plus OverPy when that is the project's authoring language.
- **Release boundary:** Deferred. First-release foundations still retain the underlying engine facts and small examples needed for ordinary authoring and debugging.

Workshop.codes API documentation belongs to repository maintenance and source-refresh tooling. It is separate from both web-editor support and normal runtime skill loading.

## Consequences for the rewrite and build

1. Preserve a coverage map from each source article to its rewritten destination, consolidation, historical note, or justified exclusion.
2. Separate source edit date, documented test patch/date, compilation status, in-game verification, and editorial uncertainty.
3. Generate exact catalogs from pinned structured sources where available; curate the interactions and exceptions described above.
4. Verify complete examples appropriately. Compiler acceptance is a syntax/toolchain result, not in-game proof. Keep fragments and unverified recipes labeled.
5. Track disagreements at the claim level. Do not resolve them by silently choosing the newest article timestamp.
6. Keep source refresh separate from rewriting. Workshop.codes access uses its JSON API, with conservative pacing. Changed article IDs/hashes should identify references for review.
7. Use the survey to design focused evaluation prompts around event context, lifecycle cleanup, reevaluation, collections, resource limits, raycast results, language boundaries, and uncertainty handling, as well as Wait.
8. Preserve complex-system applications as future companion-skill stubs. The foundation still owns the underlying engine facts needed by small and large programs alike.

## Remaining evidence gaps

- Current in-game behavior has not been tested. The user has chosen explicit uncertainty for the initial release.
- External media and shared-mode reproduction harnesses were not inspected or executed.
- Several source examples and catalogs need correction or resolution before becoming canonical skill material.
- The required core's size and routing effectiveness still need to be measured against representative tasks after drafting.
- This survey accounts for the complete local snapshot; it is not a claim that the snapshot covers every current Workshop or OverPy feature.
