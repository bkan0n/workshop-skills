# tabular

`tabular(variables, values, compress=false)`



Maps an array of arrays to variables (same as `splitDictArray()` with shorter syntax). For example:
```thon
tabular([waveHeroes,waveLengths], [
    Hero.ANA, 3,
    Hero.SOLDIER, 8,
    Hero.HAMMOND, null,
])
```

Will yield the following:

```thon
waveHeroes = [Hero.ANA, Hero.SOLDIER, Hero.HAMMOND]
waveLengths = [3, 8, null]
```

If the third argument is set to `true`, arrays will be compressed if they are arrays of literal numbers or vectors.


| Argument | Type | Meaning / default |
| --- | --- | --- |
| `variables` | `Dict` | A dictionary mapping the keys to the variables to be assigned to. |
| `values` | `Array<Dict>` | An array of dictionaries describing the values to be assigned to the variables. |
| `compress` | `bool` | Set to true to compress the arrays if they are arrays of literal numbers or vectors. Default: `false`. |

Returns: `void`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
