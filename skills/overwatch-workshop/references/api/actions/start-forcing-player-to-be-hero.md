# Start Forcing Player To Be Hero

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Forcing Player To Be Hero(player, hero)`

Starts forcing one or more players to be a specific hero and, if necessary, respawns them immediately in their current location. This will be the only hero available to the player or players until the stop forcing player to be hero action is executed.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players who will be forced to be a specific hero. |
| `hero` | `Hero` | The hero that the player or players will be forced to be. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
