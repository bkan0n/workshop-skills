# Chase Global Variable At Rate

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Chase Global Variable At Rate(variable, destination, rate, reevaluation)`

Gradually modifies the value of a global variable at a specific rate. (A global variable is a variable that belongs to the game itself.)

| Argument | Type | Meaning |
| --- | --- | --- |
| `variable` | `GlobalVariable` | Specifies which global variable to modify gradually. |
| `destination` | `float \| Vector` | The value that the global variable will eventually reach. The type of this value may be either a number or a vector, though the variable's existing value must be of the same type before the chase begins. |
| `rate` | `float` | The amount of change that will happen to the variable's value each second. |
| `reevaluation` | `ChaseRateReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
