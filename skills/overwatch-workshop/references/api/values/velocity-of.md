# Velocity Of

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Velocity Of(player)`

The current velocity of a player as a vector. If the player is on a surface, the y component of this velocity will be 0, even when traveling up or down a slope.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player whose velocity to acquire. |

Returns: `Velocity`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
