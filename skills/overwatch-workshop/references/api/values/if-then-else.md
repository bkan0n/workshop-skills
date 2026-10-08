# If-Then-Else

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`If-Then-Else(if, then, else)`

Results in the Then value when the If condition is true; otherwise, results in the Else value.

| Argument | Type | Meaning |
| --- | --- | --- |
| `if` | `bool` | If this condition evaluates to true, the result of the value is then; otherwise, the result is else. |
| `then` | `Object \| Array` | The result of the value when the if condition evaluates to true. |
| `else` | `Object \| Array` | The result of the value when the if condition evaluates to false. |

Returns: `Object | Array`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
