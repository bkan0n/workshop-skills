# Evaluate Once

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Evaluate Once(inputValue)`

Makes a copy of the provided value. Useful for selectively not reevaluating certain parts of a value, such as creating effects in a loop.

| Argument | Type | Meaning |
| --- | --- | --- |
| `inputValue` | `Object \| Array` | The value that will be only evaluated once. |

Returns: `Object | Array`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
