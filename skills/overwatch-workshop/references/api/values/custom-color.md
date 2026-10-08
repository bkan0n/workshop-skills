# Custom Color

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Custom Color(red, green, blue, alpha)`

A custom color with the specified red, green, blue and alpha values.

| Argument | Type | Meaning |
| --- | --- | --- |
| `red` | `unsigned int` | The red component of a color, from 0 to 255. |
| `green` | `unsigned int` | The green component of a color, from 0 to 255. |
| `blue` | `unsigned int` | The blue component of a color, from 0 to 255. |
| `alpha` | `unsigned int` | The alpha component of a color. 255 is perfectly opaque while 0 is perfectly invisible. |

Returns: `Color`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
