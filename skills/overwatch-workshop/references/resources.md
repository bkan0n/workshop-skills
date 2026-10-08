# Resources, handles and cleanup

<!-- wiki-source-updates:start -->

## Current wiki sources

Before using facts or values covered by these sources, read the corresponding current article. Its text takes precedence over copied details below; use this guide for the overall pattern.

- [OW2 Workshop Changes/Bugs](wiki/archive/9694.md)

<!-- wiki-source-updates:end -->

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

Keep only handles belonging to the feature. Destroy All Effects and similar broad cleanup can remove another subsystem's objects. Destroy Effect accepts an array; use a per-ID bounded loop when cleanup requires work specific to each object. Clear tracking storage after destruction. A failed creation must not cause a stale Last… handle to be registered as a new resource; the archive does not establish a universal success-result API, so budget conservatively and verify action-specific failure behavior.

The [owned effect example](../examples/native-owned-effect.workshop) retains global owner/ID/deadline arrays so departure cleanup can run after player variables disappear. Its fixed 32-effect allocation is an example-local budget; account for the rest of the mode’s effects separately.

## Controls without IDs

Virtual held buttons, camera, acceleration, facing, forced position/throttle/hero, scaling and similar controls use matching Stop actions rather than object handles. Decide whether release, death, hero change, cancellation or timeout ends them. An aborting Wait or a changed event filter can skip trailing cleanup. Use a separately reachable cleanup path when that matters. Match reset may also require deliberate state initialization; do not assume every Stop restores a previous custom setting.

Statuses and DoT/HoT expire after a duration or explicit cleanup. A duration of 9999 is a long finite time, not a semantic infinity. Nonrecoverable added health pools shrink and vanish as damaged. Remove/Clear APIs generally remove the scripted instance, not every natural hero effect with a similar name.

## Dated capacity reference

These are archived limits, not a claim about every future patch. Measure count before/after creation and cleanup in the target environment.

| Resource | Archived capacity | Source/date |
| --- | --- | --- |
| Effects family | 128; 256 with extension; older overview includes beams/icons/created projectiles | Create Effect 2024-11-26; Basics 2023-04-11 |
| Text family | 128 shared HUD/IWT/progress-bar entries in older overview; newer text guide describes an IWT combination | Basics 2023-04-11; text tips 2025-04-15; see the current linked text-family documentation |
| Damage modifications | 64 active | 2024-11-26 |
| Healing modifications | 64 active | 2024-11-26 |
| Health pools | 16 per health type per player, including base/ability pools | 2025-06-14 |
| Subroutines | 128 names; one matching event declaration per name | 2021-03-18 |
| Arrays | 1,000 entries | 2024-11-26 |
| Preloaded heroes/skins | 12 combinations including those already in use | 2024-11-26 |

Entity Count, Text Count and Assist Count are useful diagnostics, but do not assume their categories and all action limits are identical. Play Effect is transient, needs no destruction, and does not consume Create Effect's persistent limit; that does not establish unlimited rendering/server capacity.

## Projectile leak report

The OW2 registry reports that a non-null projectile owner leaving or being swapped before a Create Projectile/Homing Projectile expires can make the projectile disappear without releasing its entity slot. Visual disappearance is therefore not proof of cleanup. Source-suggested alternatives are null ownership or custom behavior around Create Projectile Effect; each changes attribution or implementation. Keep finite lifetimes and inspect Entity Count across departure/hero-change reproductions. Do not promise that destroying a visual fixes this reported internal leak.

Offline source details: [effects/resources](wiki/effects-resources.md) and [projectiles](wiki/projectiles.md).

## Evidence

Wiki sources: [effect lifecycle](wiki/articles/4342.md#wiki-4342), [cleanup guide](wiki/articles/4849.md#wiki-4849), [array destruction](wiki/articles/8473.md#wiki-8473) (2026-03-17), [Last Created Entity](wiki/articles/4679.md#wiki-4679), [Last Text ID](wiki/articles/6960.md#wiki-6960), [health pools](wiki/articles/6164.md#wiki-6164), [damage modifiers](wiki/articles/4445.md#wiki-4445), [healing modifiers](wiki/articles/4453.md#wiki-4453), [DoT](wiki/articles/4446.md#wiki-4446), [HoT](wiki/articles/4452.md#wiki-4452), [assists](wiki/articles/4524.md#wiki-4524), [bots](wiki/articles/4341.md#wiki-4341), [overview limits](wiki/articles/1840.md#wiki-1840), [text tips](wiki/articles/5734.md#wiki-5734), [subroutines](wiki/articles/1292.md#wiki-1292), [arrays](wiki/articles/4572.md#wiki-4572), [preload](wiki/articles/4401.md#wiki-4401), [Play Effect](wiki/articles/9268.md#wiki-9268). Projectile ownership behavior is documented in the [current registry](wiki/articles/9463.md#wiki-9463).
