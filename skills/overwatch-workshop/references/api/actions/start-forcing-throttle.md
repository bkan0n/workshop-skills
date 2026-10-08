# Start Forcing Throttle

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Forcing Throttle(player, minForward, maxForward, minBackward, maxBackward, minSideways, maxSideways)`

Defines minimum and maximum movement input values for one or more players, possibly forcing or preventing movement.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose movement will be forced or limited. |
| `minForward` | `unsigned float` | Sets the minimum run forward amount. 0 allows the player or players to stop while 1 forces full forward movement. |
| `maxForward` | `unsigned float` | Sets the maximum run forward amount. 0 prevents the player or players from moving forward while 1 allows full forward movement. |
| `minBackward` | `unsigned float` | Sets the minimum run backward amount. 0 allows the player or players to stop while 1 forces full backward movement. |
| `maxBackward` | `unsigned float` | Sets the maximum run backward amount. 0 prevents the player or players from moving backward while 1 allows full backward movement. |
| `minSideways` | `unsigned float` | Sets the minimum run sideways amount. 0 allows the player or players to stop while 1 forces full sideways movement. |
| `maxSideways` | `unsigned float` | Sets the maximum run sideways amount. 0 prevents the player or players from moving SIDEWAYS while 1 allows full sideways movement. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
