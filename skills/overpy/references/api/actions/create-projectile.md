# createProjectile

`createProjectile(type, player=null, startPosition=null, direction=null, relativity=Relativity.TO_WORLD, modifyHealthType=ModifyHealth.DAMAGE, affectedTeam=Team.ALL, damage, damageScalar=1, explosionRadius=0, explosionEffect=DynamicEffect.BAD_EXPLOSION, explosionSound=DynamicEffect.EXPLOSION_SOUND, oversize=0, speed, lifetime=Math.INFINITY, impulseStrength=0, ricochetCount=0, gravity=0)`


Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `type` | `Projectile` |  |
| `player` | `Player \| Array<Player>` |  Default: `null`. |
| `startPosition` | `Position` |  Default: `null`. |
| `direction` | `Direction` |  Default: `null`. |
| `relativity` | `Relativity` |  Default: `Relativity.TO_WORLD`. |
| `modifyHealthType` | `ModifyHealth` |  Default: `ModifyHealth.DAMAGE`. |
| `affectedTeam` | `Team` |  Default: `Team.ALL`. |
| `damage` | `unsigned float` |  |
| `damageScalar` | `unsigned float` |  Default: `1`. |
| `explosionRadius` | `unsigned float` |  Default: `0`. |
| `explosionEffect` | `DynamicEffect` |  Default: `DynamicEffect.BAD_EXPLOSION`. |
| `explosionSound` | `DynamicEffect` |  Default: `DynamicEffect.EXPLOSION_SOUND`. |
| `oversize` | `unsigned float` |  Default: `0`. |
| `speed` | `unsigned float` |  |
| `lifetime` | `unsigned float` |  Default: `Math.INFINITY`. |
| `impulseStrength` | `unsigned float` |  Default: `0`. |
| `ricochetCount` | `unsigned float` |  Default: `0`. |
| `gravity` | `float` |  Default: `0`. |

Returns: `void`.
Native operation: [Create Projectile](../../../../overwatch-workshop/references/api/actions/create-projectile.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
