# Attach Players

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Attach Players(child, parent, offset)`

Attaches the player (the 'child') to another player (the 'parent'). Once attached, the child will be unable to move freely until detached or teleported away. Multiple children may be attached to the same parent, but not vice versa.

| Argument | Type | Meaning |
| --- | --- | --- |
| `child` | `Player` | The player that will attach to the parent. This player will be unable to move freely until detached or teleported away. |
| `parent` | `Player` | The player to whom the child will attach. This player's movement will be unaffected and will determine the child's position. |
| `offset` | `Position` | The coordinates of the child relative to the parent. For example, `vect(1,2,0)` would be above and to the left of the parent's head. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
