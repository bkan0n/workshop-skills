# getRealPlayersInRadius

`getRealPlayersInRadius(center, radius, team=Team.ALL, losCheck=LosCheck.OFF)`


An array containing all players within a certain distance of a position, optionally restricted by team and line of sight.

Note: the workshop `Players In Radius` function targets dead players. Use this function instead.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `center` | `Position` | The center position from which to measure distance. |
| `radius` | `unsigned float` | The radius in meters inside which players must be in order to be included in the resulting array. |
| `team` | `Team` | The team or teams to which a player must belong to be included in the resulting array. Default: `Team.ALL`. |
| `losCheck` | `LosCheck` | Specifies whether and how a player must pass a line-of-sight check to be included in the resulting array. Default: `LosCheck.OFF`. |

Returns: `Array<Player>`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
[p for p in getPlayersInRadius($center, $radius, $team, $losCheck) if p.isAlive() and p.hasSpawned()]
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
