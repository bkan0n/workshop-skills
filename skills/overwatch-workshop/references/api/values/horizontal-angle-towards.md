# Horizontal Angle Towards

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Horizontal Angle Towards(player, position)`

The horizontal angle in degrees from a player's current forward direction to the specified position. The result is positive if the position is on the player's left. Otherwise, the result is zero or negative.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player from whose current facing the angle begins. |
| `position` | `Position` | The position in the world where the angle ends. |

Returns: `float`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
