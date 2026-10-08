# receiver.getRealPlayersInViewAngle

`<Player>.getRealPlayersInViewAngle(team, viewAngle)`

Receiver: `Player`. The receiver supplies the first compiler argument.

The players who are within a specific view angle of a specific player's reticle, optionally restricted by team.

Note: the workshop `Players in View Angle` function targets dead and unspawned players (at 0,0,0). Use this function instead.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `team` | `Team` | The team or teams on which to consider players. |
| `viewAngle` | `float` | The view angle to compare against in degrees. |

Returns: `Array<Player>`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
[p for p in $self.getPlayersInViewAngle($team, $viewAngle) if p.isAlive() and p.hasSpawned()]
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
