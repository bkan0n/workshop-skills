# Value In Array

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Value In Array(array, index)`

The value found at a specific element of an array. Results in 0 if the element does not exist.

| Argument | Type | Meaning |
| --- | --- | --- |
| `array` | `Array` | The array whose element to acquire. |
| `index` | `unsigned int` | The index of the element to acquire. |

Returns: `Object | Array`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
