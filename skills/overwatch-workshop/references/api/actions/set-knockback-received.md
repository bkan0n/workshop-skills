# Set Knockback Received

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Knockback Received(player, knockbackReceivedPercent)`

Sets the knockback received of one or more players to a percentage of their raw knockback received.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose knockback received will be set. |
| `knockbackReceivedPercent` | `unsigned float` | The percentage of raw knockback received to which the player or players will set their knockback received. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
