# createInWorldText

`createInWorldText(visibleTo=getAllPlayers(), text, position, scale, clipping=Clip.NONE, reevaluation=WorldTextReeval.VISIBILITY_POSITION_STRING_AND_COLOR, color=Color.WHITE, specVisibility=SpecVisibility.DEFAULT)`


Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` |  Default: `getAllPlayers()`. |
| `text` | `Object` |  |
| `position` | `Position \| Player` |  |
| `scale` | `float` |  |
| `clipping` | `Clip` |  Default: `Clip.NONE`. |
| `reevaluation` | `WorldTextReeval` |  Default: `WorldTextReeval.VISIBILITY_POSITION_STRING_AND_COLOR`. |
| `color` | `Color` |  Default: `Color.WHITE`. |
| `specVisibility` | `SpecVisibility` |  Default: `SpecVisibility.DEFAULT`. |

Returns: `void`.
Native operation: [Create In-World Text](../../../../overwatch-workshop/references/api/actions/create-in-world-text.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
