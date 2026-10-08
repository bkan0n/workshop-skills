# Has Spawned

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Has Spawned(entity)`

Whether an entity has spawned in the world. Results in false for players who have not chosen a hero yet.

| Argument | Type | Meaning |
| --- | --- | --- |
| `entity` | `Player` | The player, icon entity, or effect entity whose presence in world to check. |

Returns: `bool`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
