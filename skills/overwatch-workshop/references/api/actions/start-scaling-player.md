# Start Scaling Player

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Scaling Player(player, scale, reevaluation)`

Starts modifying the size of a player or players (including model, movement collision, hit detection, and certain abilities). Note that large players placed into complex environments will severely impact server load, so consider also applying the Disable Movement Collision With Environment action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose size will be modified. |
| `scale` | `unsigned float` | The multiplier applied to the size of the player or players (0.5 halves the size, 2.0 doubles the size, etc.). |
| `reevaluation` | `bool` | If this value is true, then scale will be reevaluated and applied to the player or players every frame. If this value is false, then the scale is only evaluated once when the action begins. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
