# Set Facing

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Facing(player, direction, relativity)`

Sets the facing of one or more players to the specified direction.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose facing will be set. |
| `direction` | `Direction` | The unit direction in which the player or players will face. This value is normalized internally. |
| `relativity` | `Relativity` | Specifies whether direction is relative to world coordinates or the local coordinates of the player or players. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
