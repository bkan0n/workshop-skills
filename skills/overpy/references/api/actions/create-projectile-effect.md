# createProjectileEffect

`createProjectileEffect(visibleTo, type, friendlyTo, position, direction, oversize=0, reevaluation=ProjectileEffectReeval.VISIBILITY_FRIENDLINESS_POSITION_DIRECTION_AND_SIZE)`


Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` |  |
| `type` | `Projectile` |  |
| `friendlyTo` | `Player \| Array<Player>` |  |
| `position` | `Position \| Player` |  |
| `direction` | `Direction` |  |
| `oversize` | `unsigned float` |  Default: `0`. |
| `reevaluation` | `ProjectileEffectReeval` |  Default: `ProjectileEffectReeval.VISIBILITY_FRIENDLINESS_POSITION_DIRECTION_AND_SIZE`. |

Returns: `void`.
Native operation: [Create Projectile Effect](../../../../overwatch-workshop/references/api/actions/create-projectile-effect.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
