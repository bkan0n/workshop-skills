# Has Status

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Has Status(player, status)`

Whether the specified player has the specified status, either from the set status action or from a non-scripted game mechanic.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player whose status to check. |
| `status` | `Status` | The status to check for. |

Returns: `bool`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
