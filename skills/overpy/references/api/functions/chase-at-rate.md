# chaseAtRate

`chaseAtRate(variable, destination, rate, reevaluation=ChaseRateReeval.DESTINATION_AND_RATE)`


Gradually modifies the value of a variable at a specific rate.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `variable` | `Variable` | The variable to chase. |
| `destination` | `float \| Vector` | The value that the variable will eventually reach. The type of this value may be either a number or a vector, though the variable's existing value must be of the same type before the chase begins. |
| `rate` | `float` | The amount of change that will happen to the variable's value each second. |
| `reevaluation` | `ChaseRateReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. Default: `ChaseRateReeval.DESTINATION_AND_RATE`. |

Returns: `void`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
