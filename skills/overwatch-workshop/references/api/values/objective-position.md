# Objective Position

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Objective Position(number)`

The position in the world of the specified objective (either a control point, a payload checkpoint, or a payload destination). Valid in assault, escort, hybrid, and control.

| Argument | Type | Meaning |
| --- | --- | --- |
| `number` | `unsigned int` | The index of the objective to consider, starting at 0 and counting up. Each control point, payload checkpoint, and payload destination has its own index. |

Returns: `Position`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
