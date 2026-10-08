# Play Effect

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Play Effect(visibleTo, type, color, position, radius)`

Plays an effect at a position in the world. The lifetime of this effect is short, so it does not need to be updated or destroyed.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will be able to see the effect. |
| `type` | `DynamicEffect` | The type of effect to be created. |
| `color` | `Color` | The color of the effect to be created. If a particular team is chosen, the effect will either be red or blue, depending on whether the team is hostile to the viewer. Does not support Custom Color. |
| `position` | `Position` | The effect's position. If this value is a player, then the effect will play at the player's position. Otherwise, the value is interpreted as a position in the world. |
| `radius` | `unsigned float` | The effect's radius in meters. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
