# Start Forcing Player Position

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Forcing Player Position(player, position, reevaluate)`

Starts forcing a player to be in a given position. If reevaluation is enabled, then the position is evaluated every frame, allowing the player to be moved around over time.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player whose position will be forced. (The reevaluation option does not apply to this value.) |
| `position` | `Position` | The position the player will occupy. If reevaluation is enabled, this value can be used to move the player around over time. |
| `reevaluate` | `bool` | If this value is true, then the position will be reevaluated and applied to the player every frame. If this value is false, then the position is only evaluated once when the action begins. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
