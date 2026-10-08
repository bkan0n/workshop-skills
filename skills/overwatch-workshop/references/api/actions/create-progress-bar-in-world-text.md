# Create Progress Bar In-World Text

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create Progress Bar In-World Text(visibleTo, value, text, position, scale, clipping, progressBarColor, textColor, reevaluation, specVisibility)`

Creates a progress bar in-world text visible to the specific players at a specific position in the world. This text will persist until destroyed. To obtain a reference to this text, use the getLastTextId() Value. This action will fail if too many text elements have been created.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will see the progress bar HUD text. |
| `value` | `unsigned float` | The value of the progress bar to be displayed as a percentage from 0 to 100. |
| `text` | `Object` | The text to be displayed (can be blank) |
| `position` | `Position \| Player` | The text's position. If this value is a player, then the text will appear above the player's head. Otherwise, the value is interpreted as a position in the world. |
| `scale` | `float` | The text's scale. |
| `clipping` | `Clip` | Specifies whether the text can be seen through walls or is instead clipped. |
| `progressBarColor` | `Color` | The color of the progress bar text to be created. If a particular team is chosen, the effect will either be red or blue, depending on whether the team is hostile to the viewer. |
| `textColor` | `Color` | The color of the text to be created. If a particular team is chosen, the effect will either be red or blue, depending on whether the team is hostile to the viewer. |
| `reevaluation` | `ProgressWorldTextReeval` | Specifies which of this action's inputs will be continuously reevaluated. The text will keep asking for and using new values from reevaluated inputs. |
| `specVisibility` | `SpecVisibility` | Whether spectators can see the text or not. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
