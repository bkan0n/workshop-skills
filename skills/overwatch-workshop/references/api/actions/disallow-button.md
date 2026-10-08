# Disallow Button

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Disallow Button(player, button)`

Disables a logical button for one or more players such that pressing it has no effect.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose button is being disabled. |
| `button` | `Button` | The logical button that is being disabled. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
