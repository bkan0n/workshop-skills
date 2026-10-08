# Start Holding Button

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Holding Button(player, button)`

Forces one or more players to hold a button virtually until stopped by the stop holding button action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players who are holding a button virtually. |
| `button` | `Button` | The logical button that is being held virtually. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
