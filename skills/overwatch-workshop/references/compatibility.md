# Compatibility, conflicts and verification

This package rewrites an archived Workshop.codes snapshot captured **2026-09-29** and uses pinned OverPy metadata/documentation where identified. Article edit time is not necessarily the date a behavior was tested. None of the archived engine claims becomes independently game-verified merely because multiple articles agree. The package build/authoring date is also not a game compatibility claim.

Offline evidence: [compatibility reports](wiki/compatibility.md), [historical techniques](wiki/historical.md), and [source index](wiki/index.md).

## Read evidence by what it establishes

| Evidence label | What it supports | What it does not establish |
| --- | --- | --- |
| Structured API metadata | Names, argument order/types/defaults, supported translation data at the pinned revision | Every game behavior, hero exception or current patch result |
| Archived documentation | What a named source reported, with its date and context | A fresh game test or a guarantee across environments |
| Source-reported bug/workaround | A concrete failure or proposed mitigation worth testing | That it still happens, or that the workaround covers all cases |
| Historical/patched/broken | An explicit source warning makes a preserved technique unsuitable as current advice | That all neighboring API features are broken |
| Compiler/decompiler acceptance | The pinned tool accepts that fixture in the tested direction | Native game import, runtime correctness, capacity or performance |
| Game-verified | A recorded patch, environment, steps and observed result | General compatibility outside the recorded case |

Prefer the [API catalog](api/index.md) for exact native signatures and the [wiki supplements](wiki/index.md) for behavioral evidence and measured data. When a source uses OverPy syntax, translate concepts deliberately; do not paste it as native Workshop. Workshop.codes web-editor directives are a separate preprocessing system, not part of this skill's native authoring workflow.

## Known source conflicts

| Subject | Sources and disagreement | Guidance |
| --- | --- | --- |
| Total Custom String size | [4590](https://workshop.codes/wiki/articles/4590), 2024-11-26, says 511 runtime bytes; [5734](https://workshop.codes/wiki/articles/5734), 2025-04-15, says that total limit was removed | Keep the documented 128-character per-node distinction; do not enforce 511 as a current universal total. |
| Text capacity scope | [1840](https://workshop.codes/wiki/articles/1840), 2023-04-11, groups HUD/IWT/progress bars into 128; [5734](https://workshop.codes/wiki/articles/5734) explicitly groups IWT/progress-bar IWT | Scope remains unresolved. Budget conservatively and measure the families used. |
| Settings category order | [2168](https://workshop.codes/wiki/articles/2168), 2024-06-09, says script order; [9463](https://workshop.codes/wiki/articles/9463), edited 2026-08-13, says alphabetic | Do not promise custom category order. Verify import/UI behavior. |
| Sound color and player position | [4342](https://workshop.codes/wiki/articles/4342), 2024-11-26, says color does not apply to sounds; [2765](https://workshop.codes/wiki/articles/2765), 2024-09-08, reports explosion-sound differences by color and player versus vector | Retain the sound-specific exception and audition the intended effect. |
| Cross product worked example | [1963](https://workshop.codes/wiki/articles/1963) has a Forward/Right result inconsistent with the documented axes | Use the mathematical operation and explicit vectors; see [geometry](geometry-movement.md). Do not repeat the erroneous example. |
| Direction/angle convention | [7747](https://workshop.codes/wiki/articles/7747) and direction-value examples do not fully agree | State the chosen axes and test cardinal directions; do not silently blend formulas. |
| For/range endpoint | Workshop For documentation uses exclusive stop; pinned OverPy README's range example includes its stop | The compiler emits the bounds unchanged. Use exclusive bounds in native fixtures; the README example is conflicting evidence, not a different native loop contract. |
| Screen text spectators | [9496](https://workshop.codes/wiki/articles/9496), edited 2026-08-20, retains patch-1.59 caveats and differing visibility settings | Test each local/per-player/camera variant before claiming spectator support. |

For the range conflict, the pinned upstream example is [README lines 404–411](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#L404); native For evidence is [4383](https://workshop.codes/wiki/articles/4383). A conflict is preserved here instead of treating later edit time alone as proof of correctness.

## Reported failures that change implementation choices

| Report | Source status | Consequence |
| --- | --- | --- |
| Chased values may not notify conditions/Wait Until until destination | [9463](https://workshop.codes/wiki/articles/9463), rolling mixed-era registry, edited 2026-08-13 | Test explicit action-side observation when crossing a threshold matters; [reevaluation](reevaluation.md). |
| A variable referenced by Chase can break a For counter, even with chase rule disabled | [pinned upstream warning](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#L1138), source-reported, not locally game-tested | Reserve dedicated non-chased counters; [reevaluation](reevaluation.md). |
| Repeated Start Rule/Restart Rule while a subroutine still waits accumulates a crash | [pinned upstream warning](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#L1155), source-reported | Do not use endless restarts as a timer update mechanism; [execution](execution.md#concurrent-restart-hazard). |
| Numeric Wait Until expression differs from explicit Boolean comparison | [pinned upstream warning](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#L1167), source-reported | Express the intended numeric threshold/comparison; do not rely on numeric truthiness. |
| Projectile owner departure/hero swap leaves occupied entity slots | [9463](https://workshop.codes/wiki/articles/9463) | Consider ownership/attribution tradeoffs and test count recovery; [resources](resources.md#projectile-leak-report). |
| Is Waiting For Players is false in client visual evaluation | [9463](https://workshop.codes/wiki/articles/9463) | Mirror server state if the UI needs it; [reevaluation](reevaluation.md). |
| Hero cooldown/ammo/resource/event queries differ by hero, form and button | [9463](https://workshop.codes/wiki/articles/9463); ammo matrix dated 2026-08-13, cooldown matrix 2026-05-27; [9595](https://workshop.codes/wiki/articles/9595) Event Ability report | Separate reading from writing support; [combat](combat-heroes.md). A missing row does not prove support. |
| Filter change aborts active rule; waiting damage rule misses retriggers | [6064](https://workshop.codes/wiki/articles/6064), 2025-05-25 | Review lifecycle and loss policy before adding filters or Waits; [execution](execution.md). |
| Nonzero Combo default prevents selecting first UI choice | [9463](https://workshop.codes/wiki/articles/9463) | Verify generated settings UI; zero-based stored value and selectable choice are different concerns. |
| Season 16 settings export changes On/Off to non-importable Enabled/Disabled; some settings omitted | [9463](https://workshop.codes/wiki/articles/9463), section-specific old report | Preserve source and compare actual export/import. Do not rewrite every setting blindly. |

The upstream revision above is **5a7d0e294b8cad73b9701987bb584d0551d7fa4d** (package 9.7.17), inspected during the 2026-10-07 build. Its warnings are documentation evidence, not new engine measurements. The approximate restart count reported upstream is deliberately not a supported operating budget.

## Techniques explicitly marked historical

- **Base-health pool removal exploit:** [6790](https://workshop.codes/wiki/articles/6790) explicitly says patched on **2025-05-07**, version 2.16.0-138051. Preserve it for diagnosis of old modes, not as a current replacement for Set Max Health. Normal added-pool ownership remains useful.
- **Stadium Workshop workaround:** [7385](https://workshop.codes/wiki/articles/7385) explicitly says broken as of **2025-10-01**, with a spawn-preventing soft lock. Do not import its recipe as an active supported workflow. [7418](https://workshop.codes/wiki/articles/7418)'s perks table (2025-10-14) also distinguishes enabling a setting from usable progression; it does not repair the broken Stadium technique.
- **Texture sanitization bypasses:** [6560](https://workshop.codes/wiki/articles/6560) distinguishes a Season 17 issue patched **2025-08-05** from a different bypass it claims unpatched through **2025-08-08**. Do not mark both fixed or both current. The latter is an unverified workaround, with destructive setup steps to redesign before reuse.

Old aliases or sparse documentation are not sufficient evidence of deprecation. For example, Stop Modifying Voice Lines is retained with naming/alias uncertainty rather than labeled patched simply because its naming differs.

## Measurements are scoped data

Use the [wiki catalog](wiki/index.md) for the full tables; retain their keys, units and test conditions:

- Projectile speed/gravity/radius/cast data in [2041](https://workshop.codes/wiki/articles/2041) explicitly describes **December 2023** measurements. Missing cells are not zero. [8242](https://workshop.codes/wiki/articles/8242) lists projectile **radii**, not diameters; its external test code was not run for this package.
- Weapon offsets in [9331](https://workshop.codes/wiki/articles/9331) depend on idle animation, FOV 103 and the selected weapon/hand; do not reuse them as animation-aware third-person coordinates. Table/JSON disagreements remain unresolved.
- Health-pack positions in [1976](https://workshop.codes/wiki/articles/1976) are keyed by mode/map/submap/size. Objective bounds in [4828](https://workshop.codes/wiki/articles/4828) do not reduce to the visible ground outline. Old payload timings in [1714](https://workshop.codes/wiki/articles/1714) depend on speed settings.
- Hero colors in [8507](https://workshop.codes/wiki/articles/8507) have table/array disagreements and order-sensitive arrays. Prefer explicit hero keys. Website ability icon catalogs such as [6460](https://workshop.codes/wiki/articles/6460) do not prove an equivalent in-game API asset exists.
- Comparison tables in [7978](https://workshop.codes/wiki/articles/7978) were tested **2024-04-22**, patch 2.10.0.0.124591; the 2026 edit timestamp does not refresh that test.

Remote videos/images, external share codes and links are provenance, not automatically bundled or reproduced tests. Normal use of this skill requires no network. If current behavior is essential and no game test is available, give a source-qualified answer and a minimal test procedure rather than inventing a current result.
