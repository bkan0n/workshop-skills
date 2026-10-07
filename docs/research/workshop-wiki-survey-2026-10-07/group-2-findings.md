# Group 2 corpus findings

## Coverage and interpretation

Read the complete bodies of all **338 assigned articles** (366,054 source bytes): 51 Constants, 7 References, 14 Tutorials, 264 Values, and 2 Workshop.codes articles. The ledger contains one record per manifest article, with source URL, path, update timestamp, hash, reading status, disposition, semantic findings, uncertainty, and source anchors. Of these, 192 contain extracted important information and 59 have explicit uncertainties; the remainder explain their ordinary API-only/catalog/site content. Editorial dispositions: 256 API references, 58 data catalogs, 21 guides, 3 site-only.

This was textual review, not current-game verification. Embedded media and external import codes were not inspected; no network or compiler tests were performed. **Old/unverified does not mean patched or obsolete.** Ammo Bugs remains diagnostic guidance with uncertainty. TX/FG distinguishes an explicitly reported patch from a separate workaround reported unpatched. No entire article required a historical-only disposition.

## Mandatory foundation candidates

Keep these concepts short and link to the deeper material below:

1. **Execution context and ownership:** distinguish Event Player, event participants, client Local Player, and global/player-scoped resources. Capture created IDs immediately and clean up the resources the feature owns.
2. **Evaluation is not mutation:** array value operations generally return copies. Assign the result or use the appropriate variable-modification action.
3. **Live values versus snapshots:** reevaluation selects changing parameters; Evaluate Once captures a subexpression; Update Every Frame changes frequency. These solve different problems.
4. **Rule lifecycle matters:** waits, restart policies, occupied invocations, and cleanup must be designed together. Bounded loops are different from indefinite repetition.
5. **Missing values often fail quietly:** absent entries, unsupported stats, invalid clips, and event-attribution bugs can return zero, Null, -1, or empty text. Interpret each API's sentinel in context.
6. **A vector's role matters:** position, direction, displacement, and velocity share a representation but need different transforms, units, and normalization.

Hero-specific tables, texture workarounds, full enums, advanced geometry, and numerical limits belong in selective references, not the mandatory foundation.

## Runtime, reevaluation, and performance

[Async Behavior 4843](https://workshop.codes/wiki/articles/4843) explains that already-running policies apply to the same player/global entity: Restart Rule replaces event context, whereas Do Nothing preserves the current invocation. [Wait Behaviour 4854](https://workshop.codes/wiki/articles/4854) distinguishes abort, ignore, and restart semantics. [Loops 4841](https://workshop.codes/wiki/articles/4841) separates bounded immediate loops from repeated loops needing pacing; its minimum-wait/crash wording should retain version uncertainty.

[Evaluate Once 4788](https://workshop.codes/wiki/articles/4788) supplies a useful closure-like example: freeze each loop iteration's effect offset while continuing to follow the player. [Update Every Frame 4789](https://workshop.codes/wiki/articles/4789) distinguishes logical and visual update frequencies and their server/client costs. Preserve the conceptual distinction but label its 12.5/62.5 Hz claims unverified. Reevaluation catalogs describe field-specific choices for acceleration, chase, damage/healing modification, facing, effects, icons, HUD, in-world text, progress bars, and throttle; a compact comparison reference is more useful than repeatedly explaining reevaluation in every skill.

[Effect cleanup 4849](https://workshop.codes/wiki/articles/4849) gives an ownership pattern: save Last Created Entity immediately, collect owned IDs, destroy selectively, then clear storage. Array-accepting Destroy Effect is described as a recent capability and needs verification. Last-created text, effect/entity, health-pool, assist, and modification IDs have distinct APIs and scoped meanings. [Local Player 4807](https://workshop.codes/wiki/articles/4807) enables one global HUD to render different per-viewer data, cannot be stored, and has archived spectator/replay caveats. Entity/Text/Assist Count and the Server Load values support diagnosis; load near 100 indicates increased shutdown risk rather than a guaranteed threshold.

## Collections and defensive retrieval

[Append 4565](https://workshop.codes/wiki/articles/4565), Remove, Filter, Map, Sort, and Shuffle produce copies. Append with an array appends its members. [Combined filters 1994](https://workshop.codes/wiki/articles/1994) demonstrates And/Or composition and parentheses. Sort ranks ascending and does not implicitly remove inappropriate players. Current Array Element/Index refer to the active array-evaluation context.

Slice takes a start and count, not an end index. First/Last/Value In Array report zero for documented missing cases; Index Of reports -1. Count Of a non-array reports zero. [Index Of Array Value 8904](https://workshop.codes/wiki/articles/8904) contains unusual flattened/first-element handling for one-dimensional array targets versus exact vector/nested-array matching: preserve this as a targeted verification case. Archived array/string capacities should be versioned data, not universal assumptions.

## Geometry, visibility, and targeting

[Ray casts 1948](https://workshop.codes/wiki/articles/1948) explains endpoint construction as start + direction × range and the no-hit defaults. [Ray Cast Hit Position 4730](https://workshop.codes/wiki/articles/4730) and related APIs distinguish players, owned objects, exclusions, Phased Out targets, and automatic player-height offsets. Raycasts end at their explicit endpoint, including in air. View-angle tests ignore occlusion and use feet-based geometry; line-of-sight and eye-based aiming require explicit choices.

The archived coordinate convention is X left, Y up, Z forward. Local/world conversion distinguishes rotation-only direction/velocity from rotation-plus-translation position. Direction Towards is normalized; Vector Towards is displacement. [Dot/cross guide 1963](https://workshop.codes/wiki/articles/1963) contains reusable projection, off-axis momentum removal, and camera-plane placement patterns, but also a contradicted cross-product example and missing parallel-vector fallback. [Impulse behavior 8044](https://workshop.codes/wiki/articles/8044) distinguishes legacy XZ/Y cancellation from XYZ cancellation and velocity incorporation.

The FAQ's target-selection examples need repair: one opposite-team query switches to the player's own team, and dummy creation lacks a dummy-exclusion guard. Nearest-walkable position additionally requires spawn reachability. Aim-assist/AI guidance in [2032](https://workshop.codes/wiki/articles/2032) combines target filtering, slower selection, faster aiming, and travel prediction; keep as an advanced pattern with patch-sensitive projectile tables and missing empty/zero guards.

## Player identity, event attribution, and game lifecycle

[Event Ability 9595](https://workshop.codes/wiki/articles/9595) is unusually important diagnostic material: an extensive hero table records Null or wrong-button returns. Null must not be taken as proof that no ability caused an event. [Ammo Bugs 2160](https://workshop.codes/wiki/articles/2160) reports zero clip information for several heroes and special Bastion behavior; these are archived, untested bug reports, not known fixes.

[Status behavior 3226](https://workshop.codes/wiki/articles/3226) and [ability/status matrix 2698](https://workshop.codes/wiki/articles/2698) distinguish native and scripted statuses, visual Burning, external movement while Rooted, Invincible versus Unkillable, and collision/attack effects of Phased Out. Hero examples require version labels. Echo duplication, copied ultimates, alternate forms, and weapon indices are separate concepts.

FFA/team values have special meanings: Team Of and Opposite Team can return All; team and individual scores differ; slots use different scopes. Several statistics are current-match/in-progress only and exclude dummy bots. Match Time differs from total elapsed instance time. Host can change. Hero-order tables are explicitly mutable and already unsynchronized. [Post-game timings 1855](https://workshop.codes/wiki/articles/1855) remain a versioned catalog requiring retesting.

## UI, strings, settings, and visual catalogs

[Custom String 4590](https://workshop.codes/wiki/articles/4590) distinguishes editor input character capacity from runtime byte capacity and explains nested chunks. Input Binding String is viewer-dependent and cannot be stored. String indexing/slicing/replacement have useful sentinel and count semantics. Spectator visibility, clipping, team colors, and perspective-specific effects deserve a shared presentation reference.

[Capture-point guide 4836](https://workshop.codes/wiki/articles/4836) supplies a concrete state-machine example: attacker scaling, contested pause, checkpoint decay, chase control, and tick-time bounds. Its hardcoded geometry and inconsistent checkpoint wording need cleanup before becoming a curated example. Workshop settings return different types (including combo index rather than displayed text), enforce ranges, and sort within categories.

[TX/FG 6560](https://workshop.codes/wiki/articles/6560) is advanced, fragile guidance: preserve its explicit patch chronology and avoid copying its Destroy All Dummy Bots setup into an existing mode. Effect/sound galleries are largely data references; perspective, team, start/loop/exit phases, and visual persistence carry semantics beyond names. Their linked media was not visually verified.

## Contradictions, boundaries, and maintenance

- **Geometry contradiction:** 1963 says Forward × Right = Up; its formula and archived axes imply Down. Correct or verify the example.
- **Angle-sign discrepancy:** [Direction From Angles 7747](https://workshop.codes/wiki/articles/7747) says positive vertical points up, while Vertical Facing Angle/Vertical Angle Towards use down-positive descriptions. Do not assume these are inverse conversions.
- **Schema/editor defects:** Evaluate Once/Update Every Frame list suspicious Void inputs; Objective Position lists Integer; several examples omit arguments or guards. Use compiler data for signatures, preserve wiki prose for semantics, and record conflicts.
- **Language boundary:** [High-level languages 8308](https://workshop.codes/wiki/articles/8308) supports external-source/compile/paste workflows, but overstates roundtrip guarantees. [Mixins 1876](https://workshop.codes/wiki/articles/1876) is Workshop.codes editor preprocessing, not native Workshop or OverPy syntax.
- **Maintainer-only API guidance:** [Workshop.codes API 8770](https://workshop.codes/wiki/articles/8770) documents wiki JSON pagination ending in a 200 empty array. Search is capped and strips Markdown, so it cannot supply a complete raw corpus. Pagination counts and search-parameter examples conflict; the API is described as informal and search concurrency can fail. Keep this material in refresh tooling documentation, outside runtime skill loading.

The shared references should organize these semantic clusters once, with compact API-specific exceptions nearby. OverPy can link into them while retaining ownership of source syntax and compiler behavior. The detailed ledger remains the traceable source inventory for rewriting and later validation.
