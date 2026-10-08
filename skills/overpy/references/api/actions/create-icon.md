# createIcon

`createIcon(visibleTo, position, icon, reevaluation?, color?, showWhenOffscreen=true)`


Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` |  |
| `position` | `Position \| Player` |  |
| `icon` | `Icon` |  |
| `reevaluation` | `IconReeval` |  Upstream marks this optional but its default `VISIBLE TO AND POSITION` does not match the declared enum. Supply a valid explicit argument; do not copy that default as source. |
| `color` | `Color` |  Upstream marks this optional but its default `VISIBILITY_POSITION_AND_COLOR` does not match the declared enum. Supply a valid explicit argument; do not copy that default as source. |
| `showWhenOffscreen` | `bool` |  Default: `true`. |

Returns: `void`.
Native operation: [Create Icon](../../../../overwatch-workshop/references/api/actions/create-icon.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
