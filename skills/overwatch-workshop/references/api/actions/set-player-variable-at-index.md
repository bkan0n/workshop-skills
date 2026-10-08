# Set Player Variable At Index

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Player Variable At Index(player, variable, index, value)`

Finds or creates an array on a player variable, which is a variable that belongs to a specific player, then stores a value in the array at the specified index.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player whose variable will be modified. If multiple players are provided, each of their variables will be set. |
| `variable` | `PlayerVariable` | Specifies which player variable's value is the array to modify. If the variable's value is not an array, then its value becomes an empty array. |
| `index` | `unsigned int` | The index of the array to modify. If the index is beyond the end of the array, the array is extended with new elements given a value of zero. |
| `value` | `Object \| Array` | The value that will be stored into the array. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
