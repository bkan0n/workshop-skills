# lerp

`lerp(start, end, t)`


Built-in macro for linear interpolation between two values. The value of `t` must be between 0 and 1.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `start` | `float` | The starting value. |
| `end` | `float` | The ending value. |
| `t` | `unsigned float` | The interpolation factor. Must be between 0 and 1. |

Returns: `float`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
$start * (1 - $t) + $end * $t
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
