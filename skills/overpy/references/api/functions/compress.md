# compress

`compress(array)`


Compresses the specified array of numbers or vectors into a string. Strings take much fewer elements, so use this function if you are running out of elements.

Note that numbers will get rounded to 3 decimal places, and vectors to 2 decimal places.

Use the `decompressNumbers()` or `decompressVectors()` function to get the original array back.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `array` | `Array` | An array of literal numbers or vectors to be compressed. The array must be a literal array, not a variable. |

Returns: `String`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
