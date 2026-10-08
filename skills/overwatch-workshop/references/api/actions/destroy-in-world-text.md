# Destroy In-World Text

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Destroy In-World Text(textId)`

Destroys in-world text that was created by create in-world text.

| Argument | Type | Meaning |
| --- | --- | --- |
| `textId` | `TextId` | Specifies which in-world text to destroy. This id may be last text id or a variable into which last text id was earlier stored. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
