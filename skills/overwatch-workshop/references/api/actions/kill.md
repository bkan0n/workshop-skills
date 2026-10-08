# Kill

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Kill(player, killer)`

Instantly kills one or more players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players who will be killed. |
| `killer` | `Player` | The player who will receive credit for the kill. A killer of null indicates no player will receive credit. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
