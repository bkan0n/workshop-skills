# Start Heal Over Time

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Heal Over Time(player, healer, duration, healingPerSecond)`

Starts an instance of heal over time. This healing will persist for the specified duration or until stopped by script. To obtain a reference to this healing, use the last heal over time id value.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | One or more players who will receive the heal over time. |
| `healer` | `Player` | The player who will receive credit for the healing. A healer of null indicates no player will receive credit. |
| `duration` | `unsigned float` | The duration of the heal over time in seconds. To have a healing that lasts until stopped by script, provide an arbitrarily long duration such as 99999. |
| `healingPerSecond` | `unsigned float` | The healing per second for the heal over time. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
