# Mapped Array

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Mapped Array(array, condition)`

A copy of the specified array with the values mapped according to the mapping expression that is evaluated for each element.

| Argument | Type | Meaning |
| --- | --- | --- |
| `array` | `Array` | The array whose copy will be mapped. |
| `condition` | `Object \| Array` | The mapping expression that is evaluated for each element of the copied array. Use the current array element value to reference the element of the array currently being considered. |

Returns: `Array`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
