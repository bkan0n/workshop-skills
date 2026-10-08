# compressed

`compressed(array)`


Compresses in-place the specified array of numbers or vectors into a string, then returns the decompressed array. Strings take much fewer elements, so use this function if you are running out of elements.

Note that numbers will get rounded to 3 decimal places, and vectors to 2 decimal places.

This function is only effective once the array has at least 5 vectors or 7 numbers (depending on the complexity; use `#!debugElementCount` to compare).

This function can be more effective than `compress()` and `decompressNumbers()` / `decompressVectors()`, as it can apply optimizations if all numbers have a low amount of significant digits or if they are all positive.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `array` | `Array` | An array of literal numbers or vectors to be compressed and immediately decompressed. The array must be a literal array, not a variable. |

Returns: `Array`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
