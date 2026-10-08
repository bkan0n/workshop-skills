# Create Beam Effect

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create Beam Effect(visibleTo, type, startPosition, endPosition, color, reevaluation)`

Creates an in-world beam effect entity. This effect entity will persist until destroyed. To obtain a reference to this entity, use the last created entity value. This action will fail if too many entities have been created.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will be able to see the effect. |
| `type` | `Beam` | The type of effect to be created. |
| `startPosition` | `Position` | The effect's start position. If this value is a player, then the effect will move along with the player. Otherwise, the value is interpreted as a position in the world. |
| `endPosition` | `Position` | The effect's end position. If this value is a player, then the effect will move along with the player. Otherwise, the value is interpreted as a position in the world. |
| `color` | `Color` | The color of the beam to be created. If a particular team is chosen, the effect will either be red or blue, depending on whether the team is hostile to the viewer. Does not apply to sound effects. Only the "good" and "bad" beam effects can have color applied. |
| `reevaluation` | `EffectReeval` | Specifies which of this action's inputs will be continuously reevaluated. The effect will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
