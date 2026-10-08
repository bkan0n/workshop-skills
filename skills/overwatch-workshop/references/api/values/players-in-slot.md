# Players In Slot

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Players In Slot(slot, team)`

The player or array of players who occupy a specific slot in the game.

| Argument | Type | Meaning |
| --- | --- | --- |
| `slot` | `unsigned int` | The slot number from which to acquire a player or players. In team games, each team has slots 0 through 5. In free-for-all games, slots are numbered 0 through 11. |
| `team` | `Team` | The team or teams from which to acquire a player or players. |

Returns: `Player | Array<Player>`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
