# Sorted Array

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Sorted Array(array, valueRank)`

A copy of the specified array with the values sorted according to the value rank that is evaluated for each element.

| Argument | Type | Meaning |
| --- | --- | --- |
| `array` | `Array<Object>` | The array whose copy will be sorted. |
| `valueRank` | `Object` | The value that is evaluated for each element of the copied array. The array is sorted by this rank in ascending order. Use the current array element value to reference the element of the array currently being considered. |

Returns: `Array<Object>`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
