# Set Aim Speed

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Aim Speed(player, turnSpeedPercent)`

Sets the aim speed of one or more players to a percentage of their normal aim speed.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose aim speed will be set. |
| `turnSpeedPercent` | `unsigned float` | The percentage of normal aim speed to which the player or players will set their aim speed. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
