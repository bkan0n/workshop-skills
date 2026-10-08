# Is True For Any

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Is True For Any(array, condition)`

Whether the specified condition evaluates to true for any value in the specified array.

| Argument | Type | Meaning |
| --- | --- | --- |
| `array` | `Array` | The array whose values will be considered. |
| `condition` | `bool` | The condition that is evaluated for each element of the specified array. Use the current array element value to reference the element of the array currently being considered. |

Returns: `bool`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
