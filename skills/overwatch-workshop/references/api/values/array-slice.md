# Array Slice

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Array Slice(array, startIndex, count)`

A copy of the specified array containing only values from a specified index range. **Does not support nested arrays.**

| Argument | Type | Meaning |
| --- | --- | --- |
| `array` | `Array<Object>` | The array from which to make a copy. |
| `startIndex` | `unsigned int` | The first index of the range. |
| `count` | `unsigned int` | The number of elements in the resulting array. The resulting array will contain fewer elements if the specified range exceeds the bounds of the array. |

Returns: `Array<Object>`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
