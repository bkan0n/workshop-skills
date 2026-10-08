# Set Environment Credit Player

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Environment Credit Player(target, environmentCreditPlayer)`

Sets the player who will receive credit if the specified target player or players die to the environment before landing on the ground.

| Argument | Type | Meaning |
| --- | --- | --- |
| `target` | `Player \| Array<Player>` | The target player or players whose death is being considered. |
| `environmentCreditPlayer` | `Player` | The Player who will receive credit if the target player or players die to the environment before landing on the ground. An environment credit player of null indicates no player will receive credit. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
