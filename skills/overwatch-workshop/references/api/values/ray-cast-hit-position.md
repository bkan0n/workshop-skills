# Ray Cast Hit Position

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Ray Cast Hit Position(startPos, endPos, playersToInclude, playersToExclude, includePlayerOwnedObjects)`

The position where the ray cast hits a surface, object, or player (or the end pos if no hit occurs).

| Argument | Type | Meaning |
| --- | --- | --- |
| `startPos` | `Position` | The start position for the ray cast. If a player is provided, a position 2 meters above the player's feet is used. |
| `endPos` | `Position` | The end position for the ray cast. If a player is provided, a position 2 meters above the player's feet is used. |
| `playersToInclude` | `Array<Player>` | Which players can be hit by this ray cast. |
| `playersToExclude` | `Array<Player>` | Which players cannot be hit by this ray cast. This list takes precedence over players to include. |
| `includePlayerOwnedObjects` | `bool` | Whether player-owned objects (such as barriers or turrets) should be included in the ray cast. |

Returns: `Position`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
