# Is Communicating

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Is Communicating(player, type)`

Whether a player is using a specific communication type (such as emoting, using a voice line, using a spray, etc.).

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player whose communication status to check. |
| `type` | `Comms` | The type of communication to consider. The duration of emotes is exact, the duration of voice lines is assumed to be 4 seconds, and all other durations are assumed to be 2 seconds. |

Returns: `bool`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
