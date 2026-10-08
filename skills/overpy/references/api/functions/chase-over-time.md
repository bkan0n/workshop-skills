# chaseOverTime

`chaseOverTime(variable, destination, duration, reevaluation=ChaseTimeReeval.DESTINATION_AND_DURATION)`


Gradually modifies the value of a variable over time.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `variable` | `Variable` | Specifies which variable to modify gradually. |
| `destination` | `float \| Vector` | The value that the variable will eventually reach. The type of this value may be either a number or a vector, though the variable's existing value must be of the same type before the chase begins. |
| `duration` | `float` | The amount of time, in seconds, over which the variable's value will approach the destination. |
| `reevaluation` | `ChaseTimeReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. Default: `ChaseTimeReeval.DESTINATION_AND_DURATION`. |

Returns: `void`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
