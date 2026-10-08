# Start Modifying Hero Voice Lines

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Modifying Hero Voice Lines(player, pitchScalar, reevaluation)`

Modifies the way hero voice lines sound for a player or players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose voice line sound will be modified. |
| `pitchScalar` | `unsigned float` | The amount that the pitch of the voice will be raised (up to 1.5) or lowered (down to 0.5). |
| `reevaluation` | `bool` | If true, Pitch Scalar is evaluated and updated every frame. If false, Pitch Scalar is evaluated once when the action executes. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
