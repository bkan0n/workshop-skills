# Player Variable

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Player Variable(player, variable)`

The current value of a player variable, which is a variable that belongs to a specific player.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player whose variable value to acquire. |
| `variable` | `PlayerVariable` | The variable whose value to acquire. |

Returns: `Value`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
