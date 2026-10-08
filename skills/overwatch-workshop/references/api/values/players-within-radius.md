# Players Within Radius

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Players Within Radius(center, radius, team, losCheck)`

An array containing all players within a certain distance of a position, optionally restricted by team and line of sight.

**Note**: This function picks up dead players. Use `getRealPlayersInRadius()` instead.

| Argument | Type | Meaning |
| --- | --- | --- |
| `center` | `Position` | The center position from which to measure distance. |
| `radius` | `unsigned float` | The radius in meters inside which players must be in order to be included in the resulting array. |
| `team` | `Team` | The team or teams to which a player must belong to be included in the resulting array. |
| `losCheck` | `LosCheck` | Specifies whether and how a player must pass a line-of-sight check to be included in the resulting array. |

Returns: `Array<Player>`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
