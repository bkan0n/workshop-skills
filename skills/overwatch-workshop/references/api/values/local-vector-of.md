# Local Vector Of

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Local Vector Of(worldVector, relativePlayer, transformation)`

The vector in local coordinates corresponding to the provided vector in world coordinates.

| Argument | Type | Meaning |
| --- | --- | --- |
| `worldVector` | `Vector` | The vector in world coordinates that will be converted to local coordinates. |
| `relativePlayer` | `Player` | The player to whom the resulting vector will be relative. |
| `transformation` | `Transform` | Specifies whether the vector should receive a rotation and a translation (usually applied to positions) or only a rotation (usually applied to directions and velocities). |

Returns: `Vector`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
