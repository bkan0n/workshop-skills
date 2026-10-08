# receiver.startFacing

`<Player | Array<Player>>.startFacing(direction, turnRate=Math.INFINITY, relativity=Relativity.TO_WORLD, reevaluation=FacingReeval.DIRECTION_AND_TURN_RATE)`

Receiver: `Player | Array<Player>`. The receiver supplies the first compiler argument.

Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `direction` | `Direction` |  |
| `turnRate` | `unsigned float` |  Default: `Math.INFINITY`. |
| `relativity` | `Relativity` |  Default: `Relativity.TO_WORLD`. |
| `reevaluation` | `FacingReeval` |  Default: `FacingReeval.DIRECTION_AND_TURN_RATE`. |

Returns: `void`.
Native operation: [Start Facing](../../../../overwatch-workshop/references/api/actions/start-facing.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
