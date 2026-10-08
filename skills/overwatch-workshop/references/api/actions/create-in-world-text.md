# Create In-World Text

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create In-World Text(visibleTo, text, position, scale, clipping, reevaluation, color, specVisibility)`

Creates in-world text visible to specific players at a specific position in the world. This text will persist until destroyed. To obtain a reference to this text, use the getLastTextId() value. This action will fail if too many text elements have been created.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will see the in-world text. |
| `text` | `Object` | The text to be displayed. |
| `position` | `Position \| Player` | The text's position. If this value is a player, then the text will appear above the player's head. Otherwise, the value is interpreted as a position in the world. |
| `scale` | `float` | The text's scale. |
| `clipping` | `Clip` | Specifies whether the text can be seen through walls or is instead clipped. |
| `reevaluation` | `WorldTextReeval` | Specifies which of this action's inputs will be continuously reevaluated. The text will keep asking for and using new values from reevaluated inputs. |
| `color` | `Color` | Specifies the color of the in-world text to use. |
| `specVisibility` | `SpecVisibility` | Whether spectators can see the text or not. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
