# Preload Hero

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Preload Hero(player, hero)`

Preemptively loads the specified hero or heroes into memory using the skins of the specified player or players, available memory permitting. Useful whenever rapid hero changing is possible and the next hero is known.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players who will begin preloading a hero or heroes. Only one preload hero action will be active at a time for a given player. |
| `hero` | `Hero \| Array<Hero>` | The hero or heroes to begin preloading for the specified player or players. When multiple heroes are specified in an array, the heroes towards the beginning of the array are prioritized. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
