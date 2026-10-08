# Create Progress Bar HUD Text

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create Progress Bar HUD Text(visibleTo, value, text, location, sortOrder, progressBarColor, textColor, reevaluation, specVisibility)`

Creates a progress bar HUD text visible to specified players at a specific location on the screen. This text will persist until destroyed. To obtain a reference to this text, use the getLastTextId() value. This action will fail if too many text elements have been created.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will see the Progress Bar HUD text. |
| `value` | `unsigned float` | The value of the progress bar to be displayed as a percentage from 0 to 100. |
| `text` | `Object` | The text to be displayed (can be blank) |
| `location` | `HudPosition` | The location on the screen where the text will appear. |
| `sortOrder` | `float` | The sort order of the text relative to other text in the same location. Text with a higher sort order will come after the text with a lower sort order. |
| `progressBarColor` | `Color` | The color of the progress bar to be created. If a particular team is chosen, the effect will either be red or blue, depending on whether the team is hostile to the viewer. |
| `textColor` | `Color` | The color of the text to be created. If a particular team is chosen, the effect will either be red or blue, depending on whether the team is hostile to the viewer. |
| `reevaluation` | `ProgressHudReeval` | Specifies which of this action's inputs will be continuously reevaluated. The text will keep asking for and using new values from reevaluated inputs. |
| `specVisibility` | `SpecVisibility` | Whether spectators can see the text or not. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
