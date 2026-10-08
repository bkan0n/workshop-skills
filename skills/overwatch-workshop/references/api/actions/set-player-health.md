# Set Player Health

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Player Health(player, amount)`

Sets the health of a player or players without affecting stats or granting damage/healing credit. This action only has an effect on living players. (For dead players, use the Resurrect Player action instead.)

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose health will be set. |
| `amount` | `unsigned float` | How much health the player or players will have. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
