# Start Throttle In Direction

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Throttle In Direction(player, direction, magnitude, relativity, behavior, reevaluation)`

Sets or adds to the throttle (directional input control) of a player or players such that they begin moving in a particular direction. Any previous throttle in direction is cancelled.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose throttle will be set or added to. |
| `direction` | `Direction` | The unit direction in which the throttle will be set or added to. This value is normalized internally. |
| `magnitude` | `unsigned float` | The amount of throttle (or change to throttle). A value of 1 denotes full throttle. |
| `relativity` | `Relativity` | Specifies whether direction is relative to world coordinates or the local coordinates of the player or players. |
| `behavior` | `Throttle` | Specifies whether preexisting throttle is replaced or added to. |
| `reevaluation` | `ThrottleReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
