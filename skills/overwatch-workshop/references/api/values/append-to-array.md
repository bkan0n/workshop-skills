# Append To Array

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Append To Array(array, value)`

A copy of an array with one or more values appended to the end.

| Argument | Type | Meaning |
| --- | --- | --- |
| `array` | `Array` | The array to which to append. |
| `value` | `Object \| Array<Object>` | The value to append to the end of the array. If this value is itself an array, each element is appended. |

Returns: `Array`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
