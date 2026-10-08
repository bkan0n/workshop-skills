# Set Global Variable

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Global Variable(variable, value)`

Stores a value into a global variable, which is a variable that belongs to the game itself.

| Argument | Type | Meaning |
| --- | --- | --- |
| `variable` | `GlobalVariable` | Specifies which global variable to store the value into. |
| `value` | `Object \| Array` | The value that will be stored. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
