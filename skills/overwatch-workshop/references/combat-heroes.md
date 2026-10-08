# Combat, attribution, heroes and projectiles

## Select the actual operation

| Operation | Engine distinction |
| --- | --- |
| Damage | Applies damage subject to buffs/debuffs/armor; can kill; supplied damager receives credit |
| Heal | Healing subject to modifiers and capped by maximum; does not resurrect |
| Set Player Health | Affects living players without damage/heal credit or stat changes |
| Kill | Immediate kill request, but archived note says a zero damage modification from killer to victim prevents it |
| Respawn | Full health at an appropriate spawn, even if already alive |
| Resurrect | Instant return at death location without transition |
| Set Max Health | Percentage of raw maximum; clamps current health down to new maximum |
| Add Health Pool | Adds separately tracked health/armor/shields with recovery and depletion semantics |

Null damager/healer/killer means nobody receives that credit. It is not necessarily equivalent to a self-attributed event. Damage/Healing Dealt/Received use percentages of raw values, whereas player/barrier scaling uses multipliers. Preserve a mode's intended baselines when restoring settings rather than blindly assuming every original value was 100%.

Start Damage Modification applies to specified receiver/damager pairs and **only players**, excluding their barriers/turrets; Set Damage Dealt has broader damage reach. Modifier instances need IDs and cleanup. Set Environment Credit Player credits an environmental death only before the target next lands. Start Assist distinguishes allied-target defensive assists from enemy-target offensive assists. See [resources](resources.md) for budgets and lifetimes.

## Events and status interpretation

Read [execution context](execution.md) before choosing Event Player, Attacker, Victim, Healer or Healee. A check that the attacker is using an ultimate does not establish which attack caused a damage event. Event Ability is more specific when supported, but the archive reports Null and wrong-button values for many hero/attack combinations. Validate the exact hero, attack, form and patch; do not interpret Null as proof of “no ability.” Earned Elimination differs from Dealt Final Blow.

Set Status and natural abilities are related but not identical. Clear Status removes a Workshop-applied status, not a promise to purge every natural ability status. Burning can be visual only. Hacked blocks abilities/ultimate but does not itself disable weapon attacks. Rooted blocks self-movement while allowing aim/external movement. Invincible prevents damage; Unkillable keeps health at least one. Phased Out affects collision, attacks and raycasts. The ability-to-Has Status matrix is patch-sensitive: immobilization does not universally mean Rooted.

For Echo, Is Using Ultimate is documented to report the duplicated hero's ultimate; use Is Duplicating for Duplicate itself. Alternate form, weapon index and duplication are separate concepts. Weapon indexes are 1/2, whereas ammo clips are 0/1. A nonexistent clip does nothing for ammo setters; a nonexistent weapon selects default, and a disabled weapon cannot be selected.

## Scripted projectiles

Create Projectile/Homing Projectile can heal or damage players and owned entities. Projectile Effect is a visual entity and does not supply combat behavior by itself.

- A projectile never affects its owner, regardless of affected team. Null owner means no player credit.
- Null start position uses the owner's eye; Null direction uses facing. Relativity affects both position and direction.
- Amount is direct-hit damage/healing, or explosion-center amount. **Amount Scalar changes meaning**: critical multiplier with zero explosion radius; edge-of-explosion damage when radius is positive.
- Radius zero creates no explosion and no explosion visual/sound. Explosion impulse applies to affected targets.
- Oversize spans 0–1 but its maximum physical size differs by projectile type; speed is meters/second and lifetime seconds.
- Ricochets count environment bounces; negative gravity arcs upward. Null homing target gives straight travel, strength 0 does not track, and strength 1 reportedly never loses its target.

The arc-preservation recipe scales speed by k and gravity by k². This is a source-derived physical relationship to test with the actual projectile; it does not justify restoring global settings to 100% without tracking their prior intended values. Consult [resources](resources.md#projectile-leak-report) before assigning an owner that may leave/change during flight.

## Hero exceptions are operation-specific

A hero's ammo read, max-ammo read, ammo write and max-ammo write can have different support. The same is true for cooldown, charge and resource. The rolling registry's ammo matrix is dated **2026-08-13** and cooldown matrix **2026-05-27**; its page timestamp does not validate every older section.

Examples of source-reported exceptions: Illari's secondary resource is missing-percent rather than filled-percent; Genji/Soldier cooldown writes while ready can update only the display; Lifeweaver behavior can depend on manual weapon swapping; Kiriko's clip-zero write can affect clip one; Orisa heat behaves as hidden ammo; Ramattra alternate-form detection has reported failures. These are diagnostic candidates, not guaranteed current facts. Use [compatibility](compatibility.md) and the exact wiki entry for the target hero/API instead of copying an entire old hero table.

Offline source details: [health/damage](wiki/health-damage.md), [hero abilities](wiki/hero-abilities.md), and [projectiles](wiki/projectiles.md).

## Evidence

Snapshot **2026-09-29**, archived documentation: [Damage](https://workshop.codes/wiki/articles/7025), [Heal](https://workshop.codes/wiki/articles/4386), [Set Health](https://workshop.codes/wiki/articles/4518), [Kill](https://workshop.codes/wiki/articles/4942), [Respawn](https://workshop.codes/wiki/articles/7550), [Resurrect](https://workshop.codes/wiki/articles/7549), [Max Health](https://workshop.codes/wiki/articles/4422), [damage modification](https://workshop.codes/wiki/articles/4445), [environment credit](https://workshop.codes/wiki/articles/4523), [assist](https://workshop.codes/wiki/articles/4524), [Status](https://workshop.codes/wiki/articles/3226), [Clear Status](https://workshop.codes/wiki/articles/4337), [status matrix](https://workshop.codes/wiki/articles/2698), [Echo ultimate](https://workshop.codes/wiki/articles/6959), [Set Weapon](https://workshop.codes/wiki/articles/4484), [Set Ammo](https://workshop.codes/wiki/articles/4482), [projectile](https://workshop.codes/wiki/articles/5175), [homing projectile](https://workshop.codes/wiki/articles/4545), [projectile effect](https://workshop.codes/wiki/articles/4546), [arc recipe](https://workshop.codes/wiki/articles/4855). Hero bugs: [Event Ability](https://workshop.codes/wiki/articles/9595), [Ammo Bugs](https://workshop.codes/wiki/articles/2160), [OW2 registry](https://workshop.codes/wiki/articles/9463). All need current game verification when decisive.
