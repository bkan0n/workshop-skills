# Start Accelerating

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Accelerating(player, direction, rate, maxSpeed, relativity, reevaluation)`

Starts accelerating one or more players in a specified direction.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players that will begin accelerating. |
| `direction` | `Direction` | The unit direction in which the acceleration will be applied. This value is normalized internally. |
| `rate` | `unsigned float` | The rate of acceleration in meters per second squared. This value may need to be quite high in order to overcome gravity and/or surface friction. |
| `maxSpeed` | `unsigned float` | The speed at which acceleration will stop for the player or players. It may not be possible to reach this speed due to gravity and/or surface friction. |
| `relativity` | `Relativity` | Specifies whether direction is relative to world coordinates or the local coordinates of the player or players. |
| `reevaluation` | `AccelReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
