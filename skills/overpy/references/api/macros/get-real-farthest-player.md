# getRealFarthestPlayer

`getRealFarthestPlayer(center, team=Team.ALL)`


The alive and spawned player farthest from a position, optionally restricted by team.

Note: the workshop `Farthest Player From` function targets dead and unspawned players (at 0,0,0). Use this function instead.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `center` | `Position` | The position from which to measure distance. |
| `team` | `Team` | The team or teams from which the farthest player will come. Default: `Team.ALL`. |

Returns: `Player`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
sorted([p for p in getLivingPlayers($team) if p.hasSpawned()], key=lambda p: -distance(p, $center))[0]
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
