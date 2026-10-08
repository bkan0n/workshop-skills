# Compare

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Compare(value, comparison, value)`

Whether the comparison of the two inputs is true.

| Argument | Type | Meaning |
| --- | --- | --- |
| `value` | `Object \| Array` | The left-hand side of the comparison. This may be any value type if the operation is == or !=. Otherwise, real numbers are expected. |
| `comparison` | `__Operator__` |  |
| `value` | `Object \| Array` | The right-hand side of the comparison. This may be any value type if the operation is == or !=. Otherwise, real numbers are expected. |

Returns: `bool`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
