# Modify Global Variable

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Modify Global Variable(variable, operation, value)`

Modifies the value of a global variable, which is a variable that belongs to the game itself.

| Argument | Type | Meaning |
| --- | --- | --- |
| `variable` | `GlobalVariable` | The global variable to modify. |
| `operation` | `__Operation__` | The way in which the variable's value will be changed. Options include standard arithmetic operations as well as array operations for appending and removing values. |
| `value` | `Object \| Array` | The value used for the modification. For arithmetic operations, this is the second of the two operands, with the other being the variable's existing value. For array operations, this is the value to append or remove. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
