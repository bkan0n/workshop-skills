# Chase Player Variable At Rate

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Chase Player Variable At Rate(player, variable, destination, rate, reevaluation)`

Gradually modifies the value of a player variable at a specific rate. (A player variable is a variable that belongs to a specific player.)

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player whose variable will gradually change. If multiple players are provided, each of their variables will change independently. |
| `variable` | `PlayerVariable` | Specifies which of the player's variables to modify gradually. |
| `destination` | `float \| Vector` | The value that the player variable will eventually reach. The type of this value may be either a number or a vector, though the variable's existing value must be of the same type before the chase begins. |
| `rate` | `float` | The amount of change that will happen to the variable's value each second. |
| `reevaluation` | `ChaseRateReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
