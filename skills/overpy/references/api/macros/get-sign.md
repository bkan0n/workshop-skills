# getSign

`getSign(number)`


Built-in macro for calculating the sign of a number. Returns -1, 0 or 1.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `number` | `float` | The number to calculate the sign of. |

Returns: `int`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
$number * Math.INFINITY * Math.INFINITY / Math.INFINITY / 10
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
