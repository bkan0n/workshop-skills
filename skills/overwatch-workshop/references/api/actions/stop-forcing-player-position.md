# Stop Forcing Player Position

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Stop Forcing Player Position(player)`

Cancels the behavior of `startForcingPosition()` for the specified player or players. Regular movement will resume from the last forced position(s).

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose positions will stop being forced. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
