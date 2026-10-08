# hudText

`hudText(visibleTo=getAllPlayers(), header=null, subheader=null, text=null, location=HudPosition.LEFT, sortOrder=0, headerColor=Color.WHITE, subheaderColor=Color.WHITE, textColor=Color.WHITE, reevaluation=HudReeval.VISIBILITY_SORT_ORDER_STRING_AND_COLOR, specVisibility=SpecVisibility.DEFAULT)`


Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` |  Default: `getAllPlayers()`. |
| `header` | `Object` |  Default: `null`. |
| `subheader` | `Object` |  Default: `null`. |
| `text` | `Object` |  Default: `null`. |
| `location` | `HudPosition` |  Default: `HudPosition.LEFT`. |
| `sortOrder` | `float` |  Default: `0`. |
| `headerColor` | `Color` |  Default: `Color.WHITE`. |
| `subheaderColor` | `Color` |  Default: `Color.WHITE`. |
| `textColor` | `Color` |  Default: `Color.WHITE`. |
| `reevaluation` | `HudReeval` |  Default: `HudReeval.VISIBILITY_SORT_ORDER_STRING_AND_COLOR`. |
| `specVisibility` | `SpecVisibility` |  Default: `SpecVisibility.DEFAULT`. |

Returns: `void`.
Native operation: [Create HUD Text](../../../../overwatch-workshop/references/api/actions/create-hud-text.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
