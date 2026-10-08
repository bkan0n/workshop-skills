# Players in View Angle

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Players in View Angle(player, team, viewAngle)`

The players who are within a specific view angle of a specific player's reticle, optionally restricted by team.

**Note**: This function picks up dead and unspawned players. Use `.getRealPlayersInViewAngle()` instead.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player whose view to use for the check. |
| `team` | `Team` | The team or teams on which to consider players. |
| `viewAngle` | `float` | The view angle to compare against in degrees. |

Returns: `Array<Player>`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
