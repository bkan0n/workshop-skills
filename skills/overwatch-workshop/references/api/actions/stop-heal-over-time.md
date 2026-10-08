# Stop Heal Over Time

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Stop Heal Over Time(healOverTimeId)`

Stops an instance of heal over time started by the start heal over time action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `healOverTimeId` | `HotId` | Specifies which heal over time instance to stop. This id may be last heal over time id or a variable into which last heal over time id was earlier stored. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
