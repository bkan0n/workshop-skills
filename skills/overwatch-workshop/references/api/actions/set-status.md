# Set Status

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Status(player, assister, status, duration)`

Applies a status to one or more players. This status will remain in effect for the specified duration or until it is cleared by the clear status action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players to whom the status will be applied. |
| `assister` | `Player` | Specifies a player to be awarded assist credit should the affected player or players be killed while the status is in effect. An assister of null indicates no player will receive credit. |
| `status` | `Status` | The status to be applied to the player or players. These behave similarly to statuses applied from hero abilities. |
| `duration` | `unsigned float` | The duration of the status in seconds. To have a status that lasts until a clear status action is executed, provide an arbitrarily long duration such as 99999. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
