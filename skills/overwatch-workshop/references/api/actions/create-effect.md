# Create Effect

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create Effect(visibleTo, type, color, position, radius, reevaluation)`

Creates an in-world effect entity. This effect entity will persist until destroyed. To obtain a reference to this entity, use the last created entity value. This action will fail if too many entities have been created.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will be able to see the effect. |
| `type` | `Effect` | The type of effect to be created. |
| `color` | `Color` | The color of the effect to be created. If a particular team is chosen, the effect will either be red or blue, depending on whether the team is hostile to the viewer. Does not apply to sound effects. Does not support Custom Color. |
| `position` | `Position \| Player` | The effect's position. If this value is a player, then the effect will move along with the player. Otherwise, the value is interpreted as a position in the world. |
| `radius` | `unsigned float` | The radius of this effect. |
| `reevaluation` | `EffectReeval` | Specifies which of this action's inputs will be continuously reevaluated. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
