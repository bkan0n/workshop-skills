# Apply Impulse

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Apply Impulse(player, direction, speed, relativity, motion)`

Applies an instantaneous change in velocity to the movement of one or more players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose velocity will be changed. |
| `direction` | `Direction` | The unit direction in which the impulse will be applied. This value is normalized internally. |
| `speed` | `float` | The magnitude of the change to the velocities of the player or players. |
| `relativity` | `Relativity` | Specifies whether direction is relative to world coordinates or the local coordinates of the player or players. |
| `motion` | `Impulse` | Specifies whether existing velocity that is counter to direction should first be cancelled out before applying the impulse. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
