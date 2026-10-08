# Detach Players

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Detach Players(children)`

Undoes the attachment caused by the 'attachTo' action for one or more players. These players will resume normal movement from their current position.

| Argument | Type | Meaning |
| --- | --- | --- |
| `children` | `Player \| Array<Player>` | The player or players that will become detached from their parent. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
