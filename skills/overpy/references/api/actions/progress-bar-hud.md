# progressBarHud

`progressBarHud(visibleTo, value=0, text=null, location=HudPosition.LEFT, sortOrder=0, progressBarColor=Color.WHITE, textColor=Color.WHITE, reevaluation=ProgressHudReeval.VISIBILITY_VALUES_AND_COLOR, specVisibility=SpecVisibility.DEFAULT)`


Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` |  |
| `value` | `unsigned float` |  Default: `0`. |
| `text` | `Object` |  Default: `null`. |
| `location` | `HudPosition` |  Default: `HudPosition.LEFT`. |
| `sortOrder` | `float` |  Default: `0`. |
| `progressBarColor` | `Color` |  Default: `Color.WHITE`. |
| `textColor` | `Color` |  Default: `Color.WHITE`. |
| `reevaluation` | `ProgressHudReeval` |  Default: `ProgressHudReeval.VISIBILITY_VALUES_AND_COLOR`. |
| `specVisibility` | `SpecVisibility` |  Default: `SpecVisibility.DEFAULT`. |

Returns: `void`.
Native operation: [Create Progress Bar HUD Text](../../../../overwatch-workshop/references/api/actions/create-progress-bar-hud-text.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
