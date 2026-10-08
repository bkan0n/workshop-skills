# Start Damage Over Time

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Damage Over Time(player, damager, duration, damagePerSecond)`

Starts an instance of damage over time. This dot will persist for the specified duration or until stopped by script. To obtain a reference to this dot, use the last damage over time id value.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | One or more players who will receive the damage over time. |
| `damager` | `Player` | The player who will receive credit for the damage. A damager of null indicates no player will receive credit. |
| `duration` | `unsigned float` | The duration of the damage over time in seconds. To have a dot that lasts until stopped by script, provide an arbitrarily long duration such as 99999. |
| `damagePerSecond` | `unsigned float` | The damage per second for the damage over time. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
