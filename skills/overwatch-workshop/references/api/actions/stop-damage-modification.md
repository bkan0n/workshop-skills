# Stop Damage Modification

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Stop Damage Modification(damageModificationId)`

Stops a damage modification that was started by the start damage modification action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `damageModificationId` | `DamageModificationId` | Specifies which damage modification instance to stop. This id may be last damage modification id or a variable into which last damage modification id was earlier stored. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
