# receiver.getRealPlayerClosestToReticle

`<Player>.getRealPlayerClosestToReticle(team=Team.ALL)`

Receiver: `Player`. The receiver supplies the first compiler argument.

The alive and spawned player closest to the reticle of the specified player, optionally restricted by team.

Note: the workshop `Player Closest To Reticle` function targets dead and unspawned players (at 0,0,0). Use this function instead.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `team` | `Team` | The team or teams on which to search for the closest player. Default: `Team.ALL`. |

Returns: `Player`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
sorted([p for p in getLivingPlayers($team) if p.hasSpawned() and p != $self], key=lambda x: angleBetweenVectors($self.getFacingDirection(), x - $self.getEyePosition()))[0]
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
