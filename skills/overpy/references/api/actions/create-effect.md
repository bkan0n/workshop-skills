# createEffect

`createEffect(visibleTo, type, color, position, radius, reevaluation=EffectReeval.VISIBILITY_POSITION_RADIUS_AND_COLOR)`


Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` |  |
| `type` | `Effect` |  |
| `color` | `Color` |  |
| `position` | `Position \| Player` |  |
| `radius` | `unsigned float` |  |
| `reevaluation` | `EffectReeval` |  Default: `EffectReeval.VISIBILITY_POSITION_RADIUS_AND_COLOR`. |

Returns: `void`.
Native operation: [Create Effect](../../../../overwatch-workshop/references/api/actions/create-effect.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
