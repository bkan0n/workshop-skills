# Destroy Effect

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Destroy Effect(entity)`

Destroys an effect entity that was created by create effect or Create Beam Effect.

| Argument | Type | Meaning |
| --- | --- | --- |
| `entity` | `EntityId` | Specifies which effect entity to destroy. This entity may be last created entity or a variable into which last created entity was earlier stored. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
