# receiver.applyImpulse

`<Player | Array<Player>>.applyImpulse(direction, speed, relativity, motion=Impulse.CANCEL_CONTRARY_MOTION_XYZ)`

Receiver: `Player | Array<Player>`. The receiver supplies the first compiler argument.

Runtime meaning and argument semantics are documented in the native operation linked below.

| Argument | Type | OverPy / default |
| --- | --- | --- |
| `direction` | `Direction` |  |
| `speed` | `float` |  |
| `relativity` | `Relativity` |  |
| `motion` | `Impulse` |  Default: `Impulse.CANCEL_CONTRARY_MOTION_XYZ`. |

Returns: `void`.
Native operation: [Apply Impulse](../../../../overwatch-workshop/references/api/actions/apply-impulse.md).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
