# Start Forcing Player Outlines

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Forcing Player Outlines(viewedPlayers, viewingPlayers, visible, color, visibility)`

Starts forcing the visibility and color of the outlines of the specified viewed player or players from the perspective of one or more viewing players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `viewedPlayers` | `Player \| Array<Player>` | The player or players who will have their outlines modified. |
| `viewingPlayers` | `Player \| Array<Player>` | The viewing player or players for whom the viewed player's outlines will be modified. |
| `visible` | `bool` | Whether or not the specified player outlines should be visible. |
| `color` | `Color` | The color of the specified player outlines, if they are visible. |
| `visibility` | `OutlineVisibility` | The visibility type of the specified player outlines, if they are visible. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
