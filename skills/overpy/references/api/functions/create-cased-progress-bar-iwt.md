# createCasedProgressBarIwt

`createCasedProgressBarIwt(textCount=3, visibleTo=getAllPlayers(), text, position, scale, clipping=Clip.NONE, textColor=Color.WHITE, reevaluation=ProgressWorldTextReeval.VISIBILITY_POSITION_VALUES_AND_COLOR, nonTeamSpectators=SpecVisibility.DEFAULT)`


Overlays multiple progress bars to create lowercase text based on fullwidth characters.

The first argument is the number of texts to use (2 to 4). Usually 3 is enough, but 4 may be needed if kerning is bad (with 'f', 'r' or 't' chars).

Note however that after a formatter or a texture, there may be a extra space.

As it is a progress bar, just add a bunch of newlines at the beginning of the string to make the bar not visible.

Note: all the text must be in the top-level (literal) string. Text used with formatters '{}' will not be lowercased.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `textCount` | `IntLiteral` | The amount of texts used to overlay. Default: `3`. |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will see the progress bar HUD text. Default: `getAllPlayers()`. |
| `text` | `String` | The text to be displayed. Must be a literal custom string, not a variable. |
| `position` | `Position \| Player` | The text's position. If this value is a player, then the text will appear above the player's head. Otherwise, the value is interpreted as a position in the world. |
| `scale` | `float` | The text's scale. |
| `clipping` | `Clip` | Specifies whether the text can be seen through walls or is instead clipped. Default: `Clip.NONE`. |
| `textColor` | `Color` | The color of the text to be created. If a particular team is chosen, the effect will either be red or blue, depending on whether the team is hostile to the viewer. Default: `Color.WHITE`. |
| `reevaluation` | `ProgressWorldTextReeval` | Specifies which of this action's inputs will be continuously reevaluated. The text will keep asking for and using new values from reevaluated inputs. Default: `ProgressWorldTextReeval.VISIBILITY_POSITION_VALUES_AND_COLOR`. |
| `nonTeamSpectators` | `SpecVisibility` | Whether non-team spectators can see the text or not. Default: `SpecVisibility.DEFAULT`. |

Returns: `void`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
