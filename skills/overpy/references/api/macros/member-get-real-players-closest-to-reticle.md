# receiver.getRealPlayersClosestToReticle

`<Player>.getRealPlayersClosestToReticle(team=Team.ALL)`

Receiver: `Player`. The receiver supplies the first compiler argument.

The alive and spawned players closest to the reticle of the specified player, optionally restricted by team and sorted by ascending distance to reticle.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `team` | `Team` | The team or teams on which to search for the closest player. Default: `Team.ALL`. |

Returns: `Player`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
sorted([p for p in getLivingPlayers($team) if p.hasSpawned() and p != $self], key=lambda x: angleBetweenVectors($self.getFacingDirection(), x - $self.getEyePosition()))
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
