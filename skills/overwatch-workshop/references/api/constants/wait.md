# Wait

The built-in `Wait` enum.


| Native English choice | OverPy symbol | Note |
| --- | --- | --- |
| `Abort When False` | `Wait.ABORT_WHEN_FALSE` | The execution of the action list is aborted if any condition on this rule becomes false. |
| `Ignore Condition` | `Wait.IGNORE_CONDITION` | The execution of the action list is never interrupted. |
| `Restart When True` | `Wait.RESTART_WHEN_TRUE` | The execution of the action list restarts from the first action if the condition list transitions from false to true or if the rule's event occurs again with true conditions. |

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
