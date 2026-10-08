# Start Facing

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Facing(player, direction, turnRate, relativity, reevaluation)`

Starts turning one or more players to face the specified direction.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players who will start turning. |
| `direction` | `Direction` | The unit direction in which the player or players will eventually face. This value is normalized internally. |
| `turnRate` | `unsigned float` | The turn rate in degrees per second. |
| `relativity` | `Relativity` | Specifies whether direction is relative to world coordinates or the local coordinates of the player or players. |
| `reevaluation` | `FacingReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
