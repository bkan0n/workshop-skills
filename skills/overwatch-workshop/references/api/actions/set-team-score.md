# Set Team Score

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Team Score(team, score)`

Sets the score for one or both teams. This action has no effect in free-for-all modes or modes without a team score.

| Argument | Type | Meaning |
| --- | --- | --- |
| `team` | `Team` | The team or teams whose score will be set. |
| `score` | `int` | The score that will be set. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
