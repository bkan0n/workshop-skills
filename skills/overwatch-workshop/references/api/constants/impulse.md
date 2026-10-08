# Impulse

The built-in `Impulse` enum.


| Native English choice | OverPy symbol | Note |
| --- | --- | --- |
| `Cancel Contrary Motion` | `Impulse.CANCEL_CONTRARY_MOTION` | **Legacy, use `CANCEL_CONTRARY_MOTION_XYZ` instead.**  If the target is moving against the direction of the impulse, this relative velocity is negated before the impulse is applied. Horizontal velocity (XZ) and vertical velocity (Y) are processed separately. |
| `Cancel Contrary Motion XYZ` | `Impulse.CANCEL_CONTRARY_MOTION_XYZ` | If the target is moving against the direction of the impulse, this relative velocity is negated before the impulse is applied. Horizontal and vertical velocity (XYZ) are processed together. |
| `Incorporate Contrary Motion` | `Impulse.INCORPORATE_CONTRARY_MOTION` | The impulse is added directly to the velocity of the target, so if the target is moving against the direction of the impulse, it might seem like the impulse has less of an effect. |

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
