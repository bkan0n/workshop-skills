# receiver.startThrottleInDirection

`<Player | Array<Player>>.startThrottleInDirection(direction, magnitude, relativity, behavior=Throttle.REPLACE_EXISTING, reevaluation=ThrottleReeval.DIRECTION_AND_MAGNITUDE)`

Receiver: `Player | Array<Player>`. The receiver supplies the first compiler argument.

Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `direction` | `Direction` |  |
| `magnitude` | `unsigned float` |  |
| `relativity` | `Relativity` |  |
| `behavior` | `Throttle` |  Default: `Throttle.REPLACE_EXISTING`. |
| `reevaluation` | `ThrottleReeval` |  Default: `ThrottleReeval.DIRECTION_AND_MAGNITUDE`. |

Returns: `void`.
Native operation: [Start Throttle In Direction](../../../../overwatch-workshop/references/api/actions/start-throttle-in-direction.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
