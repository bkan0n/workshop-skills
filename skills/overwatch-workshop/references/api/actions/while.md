# While

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`While(condition)`

Denotes the beginning of a series of actions that will execute in a loop as long as the specified condition is true. The next end action at the current level denotes the end of the loop. If the condition evaluates to false when execution is at the top of the loop, then the loop exits, and execution jumps to the next action after the end action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `condition` | `bool` | If this evaluates to true, execution continues with the next action. Otherwise, execution jumps to the next end action at the current level. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
