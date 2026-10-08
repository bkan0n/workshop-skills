# getRealClosestPlayers

`getRealClosestPlayers(center, team=Team.ALL)`


The alive and spawned players closest to a position, optionally restricted by team and sorted by ascending distance.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `center` | `Position` | The position from which to measure proximity. |
| `team` | `Team` | The team or teams from which the closest player will come. Default: `Team.ALL`. |

Returns: `Player`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
sorted([p for p in getLivingPlayers($team) if p.hasSpawned()], key=lambda p: distance(p, $center))
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
