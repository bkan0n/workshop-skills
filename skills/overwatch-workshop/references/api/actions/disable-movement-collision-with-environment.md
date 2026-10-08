# Disable Movement Collision With Environment

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Disable Movement Collision With Environment(player, includeFloors)`

Causes a player or players to stop colliding with the environment (walls, ceilings, certain objects, etc.)

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose movement collision is affected. |
| `includeFloors` | `bool` | If true, collision with the floors is also disabled. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
