# Set Gravity

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Gravity(player, gravityPercent)`

Sets the movement gravity for one or more players to a percentage of regular movement gravity.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose movement gravity will be set. |
| `gravityPercent` | `unsigned float` | The percentage of regular movement gravity to which the player or players will set their personal movement gravity. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
