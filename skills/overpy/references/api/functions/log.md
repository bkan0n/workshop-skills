# log

`log(number, base=Math.E)`


Built-in macro to calculate the logarithm of the specified number. Accurate to an error of 0.01 for values up to 1 million. Thanks to lucid and LazyLion for the formula.

Be wary of floating point precision errors, and use the `round()` function if you must compare the output. For example, `log(10000, 10)` will not give exactly 4.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `number` | `unsigned float` | The number to get the logarithm of. |
| `base` | `unsigned float` | The base of the logarithm. Default: `Math.E`. |

Returns: `float`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
