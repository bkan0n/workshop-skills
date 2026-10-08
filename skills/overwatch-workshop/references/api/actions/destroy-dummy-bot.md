# Destroy Dummy Bot

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Destroy Dummy Bot(team, slot)`

Removes the specified dummy bot from the match.

| Argument | Type | Meaning |
| --- | --- | --- |
| `team` | `Team` | The team to remove the dummy bot from. The "all" option only works in free-for-all game modes, while the "team" options only work in team-based game modes. |
| `slot` | `int` | The slot to remove the dummy bot from. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
