# Is In Line of Sight

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Is In Line of Sight(startPos, endPos, barriers)`

Whether two positions have line of sight with each other.

| Argument | Type | Meaning |
| --- | --- | --- |
| `startPos` | `Position \| Player` | The start position for the line-of-sight check. If a player is provided, a position 2 meters above the player's feet is used. |
| `endPos` | `Position \| Player` | The end position for the line-of-sight check. If a player is provided, a position 2 meters above the player's feet is used. |
| `barriers` | `BarrierLos` | Defines how barriers affect line of sight. When considering whether a barrier belongs to an enemy, the allegiance of the player provided to start pos (if any) is used. |

Returns: `bool`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
