# Set Healing Received

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Healing Received(player, healingReceivedPercent)`

Sets the healing received of one or more players to a percentage of their raw healing received.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose healing received will be set. |
| `healingReceivedPercent` | `unsigned float` | The percentage of raw healing received to which the player or players will set their healing received. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
