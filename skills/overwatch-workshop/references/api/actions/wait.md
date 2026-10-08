# Wait

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Wait(time, waitBehavior)`

Pauses the execution of the action list. Unless the wait is interrupted, the remainder of the actions will execute after the pause.

| Argument | Type | Meaning |
| --- | --- | --- |
| `time` | `unsigned float` | The duration of the pause. |
| `waitBehavior` | `Wait` | Specifies if and how the wait can be interrupted. If the condition list is ignored, the wait will not be interrupted. Otherwise, the condition list will determine if and when the action list will abort or restart. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
