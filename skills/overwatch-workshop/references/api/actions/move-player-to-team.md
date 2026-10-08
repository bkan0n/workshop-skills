# Move Player to Team

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Move Player to Team(player, team, slot)`

Moves one or more players to the specified team and slot. This action can fail if the specified slot is not available. This action doesn't work on dummy bots.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players to move. |
| `team` | `Team` | The team on which to move the Player. The "all" option only works in free-for-all game modes, while the "team" options only work in team-based game modes. |
| `slot` | `int` | The player slot which will receive the player (-1 for first available slot). |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
