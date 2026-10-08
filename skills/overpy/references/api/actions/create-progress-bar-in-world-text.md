# createProgressBarInWorldText

`createProgressBarInWorldText(visibleTo=getAllPlayers(), value=0, text=null, position, scale=1, clipping=Clip.NONE, progressBarColor=Color.WHITE, textColor=Color.WHITE, reevaluation=ProgressWorldTextReeval.VISIBILITY_POSITION_VALUES_AND_COLOR, specVisibility=SpecVisibility.DEFAULT)`


Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` |  Default: `getAllPlayers()`. |
| `value` | `unsigned float` |  Default: `0`. |
| `text` | `Object` |  Default: `null`. |
| `position` | `Position \| Player` |  |
| `scale` | `float` |  Default: `1`. |
| `clipping` | `Clip` |  Default: `Clip.NONE`. |
| `progressBarColor` | `Color` |  Default: `Color.WHITE`. |
| `textColor` | `Color` |  Default: `Color.WHITE`. |
| `reevaluation` | `ProgressWorldTextReeval` |  Default: `ProgressWorldTextReeval.VISIBILITY_POSITION_VALUES_AND_COLOR`. |
| `specVisibility` | `SpecVisibility` |  Default: `SpecVisibility.DEFAULT`. |

Returns: `void`.
Native operation: [Create Progress Bar In-World Text](../../../../overwatch-workshop/references/api/actions/create-progress-bar-in-world-text.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
