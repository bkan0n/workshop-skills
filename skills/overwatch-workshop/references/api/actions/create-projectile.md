# Create Projectile

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create Projectile(type, player, startPosition, direction, relativity, modifyHealthType, affectedTeam, damage, damageScalar, explosionRadius, explosionEffect, explosionSound, oversize, speed, lifetime, impulseStrength, ricochetCount, gravity)`

Creates a projectile entity that either heals or damages players and player-owned entities. This action will fail if too many entities have been created.

| Argument | Type | Meaning |
| --- | --- | --- |
| `type` | `Projectile` | The type of projectile to be created. New options can be added to this list by enabling the Projectiles workshop extension. |
| `player` | `Player \| Array<Player>` | The player who owns this projectile and will receive credit for kills. If null, the projectile will be owned by nobody. The projectile will not affect its owner. |
| `startPosition` | `Position` | The start position of the projectile. If null, the player's eye position will be used. |
| `direction` | `Direction` | The direction for the projectile to travel. If null, the player's facing direction will be used. |
| `relativity` | `Relativity` | Whether the projectile's start position and direction are relative to the player or to the world. |
| `modifyHealthType` | `ModifyHealth` | Whether the projectile will heal or damage targets it collides with. |
| `affectedTeam` | `Team` | Which team the projectile will collide with. The projectile will never affect its owner regardless of team. |
| `damage` | `unsigned float` | The amount of damage or healing the projectile will apply to targets it collides with. If explosion radius is set to an amount greater than 0, this is how much damage the explosion will do at its center. |
| `damageScalar` | `unsigned float` | If explosion radius is set to 0 this is how much to scale the damage amount for critical hits. If the explosion radius is greater than 0 this is how much damage the projectile will do at the edge of the explosion. |
| `explosionRadius` | `unsigned float` | The radius of the explosion created by this projectile. If 0, this projectile doesn't create an explosion. |
| `explosionEffect` | `DynamicEffect` | The effect to use when the projectile explodes. If explosion radius is 0 this effect will not be created. |
| `explosionSound` | `DynamicEffect` | The sound effect to use when the projectile explodes. If explosion radius is 0 this effect will not be created. |
| `oversize` | `unsigned float` | A 0 to 1 range for how oversized the projectile should be, 0 being the default size, 1 being the maximum allowed size. The maximum allowed size is different for each projectile type. |
| `speed` | `unsigned float` | The speed in meters per second that the projectile will travel along its direction. (0.1 to 1000) |
| `lifetime` | `unsigned float` | How long in seconds before the projectile expires. |
| `impulseStrength` | `unsigned float` | The strength of the impulse to apply to a target when hit by this projectile. If explosion radius greater than 0, this impulse will applied to all targets affected by the explosion. |
| `ricochetCount` | `unsigned float` | How many times the projectile will ricochet off the environment before expiring. |
| `gravity` | `float` | The amount of gravity affecting the projectile, creating an arc. If negative, the projectile will arc upwards. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
