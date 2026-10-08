# Chase Global Variable Over Time

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Chase Global Variable Over Time(variable, destination, duration, reevaluation)`

Gradually modifies the value of a global variable over time. (A global variable is a variable that belongs to the game itself.)

| Argument | Type | Meaning |
| --- | --- | --- |
| `variable` | `GlobalVariable` | Specifies which global variable to modify gradually. |
| `destination` | `float \| Vector` | The value that the global variable will eventually reach. The type of this value may be either a number or a vector, though the variable's existing value must be of the same type before the chase begins. |
| `duration` | `float` | The amount of time, in seconds, over which the variable's value will approach the destination. |
| `reevaluation` | `ChaseTimeReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
