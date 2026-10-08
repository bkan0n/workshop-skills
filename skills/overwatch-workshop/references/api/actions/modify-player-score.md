# Modify Player Score

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Modify Player Score(player, score)`

Modifies the score (kill count) of one or more players. This action only has an effect in free-for-all modes.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose score will change. |
| `score` | `int` | The amount the score will increase or decrease. If positive, the score will increase. If negative, the score will decrease. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
