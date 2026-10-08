# Loop If

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Loop If(condition)`

Restarts the action list from the beginning if this action's condition evaluates to true. If it does not, execution continues with the next action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `condition` | `bool` | Specifies whether the loop will occur. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
