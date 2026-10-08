# Stop Forcing Player Outlines

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Stop Forcing Player Outlines(viewedPlayers, viewingPlayers)`

Cancels the behavior of Start Forcing Player Outlines for the specified viewed player or players from the perspective of one or more viewing players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `viewedPlayers` | `Player \| Array<Player>` | The player or players who will have their outlines reset. |
| `viewingPlayers` | `Player \| Array<Player>` | The viewing player or players for whom the viewed player's outlines will be reset. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
