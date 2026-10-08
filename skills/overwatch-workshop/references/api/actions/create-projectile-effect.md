# Create Projectile Effect

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create Projectile Effect(visibleTo, type, friendlyTo, position, direction, oversize, reevaluation)`

Creates an in-world projectile effect entity. This effect entity will persist until destroyed. To obtain a reference to this entity, use the last created entity value. This action will fail if too many entities have been created.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will be able to see the effect. |
| `type` | `Projectile` | The type of projectile to be created. New options can be added to this list by enabling the Projectiles Workshop Extension. |
| `friendlyTo` | `Player \| Array<Player>` | One or more players who the projectile will appear friendly to. |
| `position` | `Position \| Player` | The position of the effect. |
| `direction` | `Direction` | The facing direction of the effect. |
| `oversize` | `unsigned float` | A 0 to 1 range for how oversized the projectile should be, 0 being the default size, 1 being the maximum allowed size. The maximum allowed size is different for each projectile type. |
| `reevaluation` | `ProjectileEffectReeval` | Specifies which of this action's inputs will be continuously reevaluated. The effect will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
