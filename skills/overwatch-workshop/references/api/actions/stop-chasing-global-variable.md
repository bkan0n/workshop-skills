# Stop Chasing Global Variable

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Stop Chasing Global Variable(variable)`

Stops an in-progress chase of a global variable, leaving it at its current value.

| Argument | Type | Meaning |
| --- | --- | --- |
| `variable` | `GlobalVariable` | Specifies which global variable to stop modifying. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
