# Else If

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Else If(condition)`

Denotes the beginning of a series of actions that will only execute if the specified condition is true and the previous If or Else If action's condition was false.

| Argument | Type | Meaning |
| --- | --- | --- |
| `condition` | `bool` | If this evaluates to true, execution continues with the next action. Otherwise, execution jumps to the next else if, else, or end action at the current level. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
