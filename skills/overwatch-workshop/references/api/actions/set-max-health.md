# Set Max Health

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Max Health(player, healthPercent)`

Sets the max health of one or more players as a percentage of their max health. This action will ensure that a player's current health will not exceed the new max health.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose max health will be set. |
| `healthPercent` | `unsigned float` | The percentage of raw max health to which the player or players will set their max health. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
