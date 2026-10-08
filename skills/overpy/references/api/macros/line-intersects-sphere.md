# lineIntersectsSphere

`lineIntersectsSphere(lineStart, lineDirection, sphereCenter, sphereRadius)`


Built-in macro to determine whether a line intersects a sphere. Can be used to check if a player is looking at a specific point. Note that this function is inaccurate if the line starting point is already inside the sphere.

Thanks to Mira for the formula.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `lineStart` | `Position` | The starting position of the line. It must be outside the sphere for the function to work. |
| `lineDirection` | `Direction` | The direction from the starting position to the ending position of the line. |
| `sphereCenter` | `Position` | The center of the sphere. |
| `sphereRadius` | `unsigned float` | The radius of the sphere. |

Returns: `bool`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
angleBetweenVectors($lineStart, $lineDirection) <= asinDeg($sphereRadius / distance($lineStart, $sphereCenter))
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
