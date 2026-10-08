# Stop Assist

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Stop Assist(assistId)`

Stops an assist that was started by the Start Assist Action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `assistId` | `AssistId` | Specifies which assist instance to stop. This ID may be Last Assist ID or a Variable into which Last Assist ID was earlier stored. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
