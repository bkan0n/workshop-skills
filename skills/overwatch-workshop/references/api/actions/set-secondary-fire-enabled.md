# Set Secondary Fire Enabled

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Secondary Fire Enabled(player, enabled)`

Enables or disables secondary fire for one or more players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose access to secondary fire is affected. |
| `enabled` | `bool` | Specifies whether the player or players are able to use secondary fire. Expects a boolean value such as true, false, or compare. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
