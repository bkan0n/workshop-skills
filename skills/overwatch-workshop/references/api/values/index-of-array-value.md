# Index Of Array Value

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Index Of Array Value(array, value)`

The index of a value within the array or -1 if no such value can be found. **Does not support nested arrays.**
Warning: if the array contains `true`, it will match against any truthy value, and `true` will match against any truthy value in the array.

| Argument | Type | Meaning |
| --- | --- | --- |
| `array` | `Array<Object>` | The array in which to search for the specified value. |
| `value` | `Object` | The value for which to search. |

Returns: `int`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
