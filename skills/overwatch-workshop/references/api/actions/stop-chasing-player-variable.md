# Stop Chasing Player Variable

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Stop Chasing Player Variable(player, variable)`

Stops an in-progress chase of a player variable, leaving it at its current value.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player whose variable will stop changing. If multiple players are provided, each of their variables will stop changing. |
| `variable` | `PlayerVariable` | Specifies which of the player's variables to stop modifying. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
