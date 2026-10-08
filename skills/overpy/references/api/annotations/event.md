# @Event

Defines the event type for the current rule. If omitted, default to `global`. Not applicable for subroutines.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `type` | `not specified` | The type of the event. |

`type` choices: `global`, `eachPlayer`, `playerDealtDamage`, `playerDealtFinalBlow`, `playerDealtHealing`, `playerDealtKnockback`, `playerDied`, `playerEarnedElimination`, `playerJoined`, `playerLeft`, `playerReceivedHealing`, `playerReceivedKnockback`, `playerTookDamage`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
