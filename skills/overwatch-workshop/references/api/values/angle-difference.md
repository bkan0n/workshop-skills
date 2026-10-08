# Angle Difference

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Angle Difference(angle, angle)`

The difference in degrees between two angles. After the angles are wrapped to be within +/- 180 of each other, the result is positive if the second angle is greater than the first angle. Otherwise, the result is zero or negative.

| Argument | Type | Meaning |
| --- | --- | --- |
| `angle` | `float` | One of the two angles between which to measure the resulting angle. |
| `angle` | `float` | One of the two angles between which to measure the resulting angle. |

Returns: `float`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
