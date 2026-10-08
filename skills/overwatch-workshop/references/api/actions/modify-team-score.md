# Modify Team Score

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Modify Team Score(team, score)`

Modifies the score of one or both teams. This action has no effect in free-for-all modes or modes without a team score.

| Argument | Type | Meaning |
| --- | --- | --- |
| `team` | `Team` | The team or teams whose score will be changed. |
| `score` | `int` | The amount the score will increase or decrease. If positive, the score will increase. If negative, the score will decrease. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
