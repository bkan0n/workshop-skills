# Wait Until

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Wait Until(continueCondition, timeout)`

Waits until the Continue Condition is true or Timeout seconds elapse. The rule conditions are ignored during this wait.

| Argument | Type | Meaning |
| --- | --- | --- |
| `continueCondition` | `bool` | If this value becomes true, the wait concludes, and the next action in the action list begins executing. |
| `timeout` | `unsigned float` | If this many seconds elapse, the wait concludes, and the next action in the action list begins executing. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
