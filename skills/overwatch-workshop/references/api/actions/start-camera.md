# Start Camera

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Camera(player, eyePosition, lookAtPosition, blendSpeed)`

Places your camera at a location, facing a direction.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose cameras will be placed at the location. |
| `eyePosition` | `Position` | The position of the camera. Reevaluates continuously. |
| `lookAtPosition` | `Position` | Where the camera looks at. Reevaluates continuously. |
| `blendSpeed` | `unsigned float` | How fast to blend the camera movement as positions change. 0 means do not blend at all, and just change positions instantly. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
