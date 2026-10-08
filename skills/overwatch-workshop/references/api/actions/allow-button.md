# Allow Button

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Allow Button(player, button)`

Undoes the effect of the disallow button action for one or more players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose button is being reenabled. |
| `button` | `Button` | The logical button that is being reenabled. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
