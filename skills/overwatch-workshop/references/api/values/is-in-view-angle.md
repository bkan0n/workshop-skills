# Is In View Angle

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Is In View Angle(player, location, viewAngle)`

Whether a location is within view of a player.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player whose view to use for the check. |
| `location` | `Position` | The location to test if it's within view. |
| `viewAngle` | `float` | The view angle to compare against in degrees. |

Returns: `bool`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
