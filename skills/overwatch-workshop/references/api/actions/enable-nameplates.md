# Enable Nameplates

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Enable Nameplates(viewedPlayers, viewingPlayers)`

Undoes the effect of Disable Nameplates for one or more viewed players from the perspective of one or more viewing players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `viewedPlayers` | `Player \| Array<Player>` | The player or players who will have their nameplates enabled. |
| `viewingPlayers` | `Player \| Array<Player>` | The viewing player or players for whom the viewed player's nameplate will be enabled. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
