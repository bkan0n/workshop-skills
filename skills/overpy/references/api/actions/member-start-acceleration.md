# receiver.startAcceleration

`<Player | Array<Player>>.startAcceleration(direction, rate, maxSpeed, relativity, reevaluation=AccelReeval.DIRECTION_RATE_AND_MAX_SPEED)`

Receiver: `Player | Array<Player>`. The receiver supplies the first compiler argument.

Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `direction` | `Direction` |  |
| `rate` | `unsigned float` |  |
| `maxSpeed` | `unsigned float` |  |
| `relativity` | `Relativity` |  |
| `reevaluation` | `AccelReeval` |  Default: `AccelReeval.DIRECTION_RATE_AND_MAX_SPEED`. |

Returns: `void`.
Native operation: [Start Accelerating](../../../../overwatch-workshop/references/api/actions/start-accelerating.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
