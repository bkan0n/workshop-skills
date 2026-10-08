# Resources, handles and cleanup

Creation is not a harmless statement that can be repeated forever. Persistent objects consume capacity, and many Create/Start actions silently fail when their budget is exhausted. Define an owner, cleanup trigger and storage location for each resource before introducing a loop.

## Handle families

| Resource | Capture immediately | Targeted cleanup |
| --- | --- | --- |
| Persistent effect/beam/projectile effect | Last Created Entity | Destroy Effect |
| Icon | Last Created Entity | Destroy Icon |
| HUD, in-world text, progress-bar variants | Last Text ID | Matching Destroy text action |
| Added health pool | Last Created Health Pool | Remove Health Pool From Player |
| Damage/healing modification | Corresponding Last … Modification ID | Corresponding Stop … Modification |
| Damage/heal over time | Corresponding Last … Over Time ID | Corresponding Stop … Over Time |
| Assist relationship | Last Assist ID | Stop Assist |
| Dummy bot | Last Created Entity for its player reference | Destroy Dummy Bot by team/slot, or coordinated bot ownership |

The Last… values are scoped to creation by Event Player or global execution. A later creation in that context can overwrite them. Save the appropriate value directly after creation, before another creator or a Wait. Do not substitute Last Created Entity for a text ID.

Keep only handles belonging to the feature. Destroy All Effects and similar broad cleanup can remove another subsystem's objects. An archived update says Destroy Effect accepts an array; a per-ID bounded loop remains useful when exact compatibility matters. Clear tracking storage after destruction. A failed creation must not cause a stale Last… handle to be registered as a new resource; the archive does not establish a universal success-result API, so budget conservatively and verify action-specific failure behavior.

The [owned effect example](../examples/native-owned-effect.workshop) retains global owner/ID/deadline arrays so departure cleanup can run after player variables disappear. Its fixed 32-effect allocation is an example-local budget, not a general guarantee in an existing mode.

## Controls without IDs

Virtual held buttons, camera, acceleration, facing, forced position/throttle/hero, scaling and similar controls use matching Stop actions rather than object handles. Decide whether release, death, hero change, cancellation or timeout ends them. An aborting Wait or a changed event filter can skip trailing cleanup. Use a separately reachable cleanup path when that matters. Match reset may also require deliberate state initialization; do not assume every Stop restores a previous custom setting.

Statuses and DoT/HoT expire after a duration or explicit cleanup. A duration of 9999 is a long finite time, not a semantic infinity. Nonrecoverable added health pools shrink and vanish as damaged. Remove/Clear APIs generally remove the scripted instance, not every natural hero effect with a similar name.

## Dated capacity reference

These are archived limits, not a claim about every future patch. Measure count before/after creation and cleanup in the target environment.

| Resource | Archived capacity | Source/date |
| --- | --- | --- |
| Effects family | 128; 256 with extension; older overview includes beams/icons/created projectiles | Create Effect 2024-11-26; Basics 2023-04-11 |
| Text family | 128 shared HUD/IWT/progress-bar entries in older overview; newer text guide describes an IWT combination | Basics 2023-04-11; text tips 2025-04-15; scope needs retest |
| Damage modifications | 64 active | 2024-11-26 |
| Healing modifications | 64 active | 2024-11-26 |
| Health pools | 16 per health type per player, including base/ability pools | 2025-06-14 |
| Subroutines | 128 names; one matching event declaration per name | 2021-03-18 |
| Arrays | 1,000 entries | 2024-11-26 |
| Preloaded heroes/skins | 12 combinations including those already in use | 2024-11-26 |

Entity Count, Text Count and Assist Count are useful diagnostics, but do not assume their categories and all action limits are identical. Play Effect is transient, needs no destruction, and does not consume Create Effect's persistent limit; that does not establish unlimited rendering/server capacity.

## Projectile leak report

The OW2 registry reports that a non-null projectile owner leaving or being swapped before a Create Projectile/Homing Projectile expires can make the projectile disappear without releasing its entity slot. Visual disappearance is therefore not proof of cleanup. Source-suggested alternatives are null ownership or custom behavior around Create Projectile Effect; each changes attribution or implementation and needs testing. Keep finite lifetimes and inspect Entity Count across departure/hero-change reproductions. Do not promise that destroying a visual fixes this reported internal leak.

Offline source details: [effects/resources](wiki/effects-resources.md) and [projectiles](wiki/projectiles.md).

## Evidence

Snapshot **2026-09-29**: [effect lifecycle](https://workshop.codes/wiki/articles/4342), [cleanup guide](https://workshop.codes/wiki/articles/4849), [array destruction](https://workshop.codes/wiki/articles/8473) (2026-03-17), [Last Created Entity](https://workshop.codes/wiki/articles/4679), [Last Text ID](https://workshop.codes/wiki/articles/6960), [health pools](https://workshop.codes/wiki/articles/6164), [damage modifiers](https://workshop.codes/wiki/articles/4445), [healing modifiers](https://workshop.codes/wiki/articles/4453), [DoT](https://workshop.codes/wiki/articles/4446), [HoT](https://workshop.codes/wiki/articles/4452), [assists](https://workshop.codes/wiki/articles/4524), [bots](https://workshop.codes/wiki/articles/4341), [overview limits](https://workshop.codes/wiki/articles/1840), [text tips](https://workshop.codes/wiki/articles/5734), [subroutines](https://workshop.codes/wiki/articles/1292), [arrays](https://workshop.codes/wiki/articles/4572), [preload](https://workshop.codes/wiki/articles/4401), [Play Effect](https://workshop.codes/wiki/articles/9268). Projectile leak is a **source-reported bug, not locally reproduced**, in [9463](https://workshop.codes/wiki/articles/9463), edited 2026-08-13.
