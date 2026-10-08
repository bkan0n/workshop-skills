# Player Hero Stat

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Player Hero Stat(player, hero, stat)`

Provides a statistic of the specified player's time playing a specific hero (limited to the current match). Statistics are only gathered when the game is in progress. Dummy bots do not gather statistics.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The Player whose statistic to acquire. |
| `hero` | `Hero` | The hero whose statistic to acquire |
| `stat` | `HeroStat` | The statistic to acquire. |

Returns: `unsigned float`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
