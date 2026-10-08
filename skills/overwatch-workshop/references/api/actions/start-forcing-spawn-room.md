# Start Forcing Spawn Room

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Forcing Spawn Room(team, room)`

Forces a team to spawn in a particular spawn room, regardless of the spawn room normally used by the game mode. This action only has an effect in assault, hybrid, and payload maps.

| Argument | Type | Meaning |
| --- | --- | --- |
| `team` | `Team` | The team whose spawn room will be forced. |
| `room` | `unsigned int` | The number of the spawn room to be forced. 0 is the first spawn room, 1 the second, and 2 is the third. If the specified spawn room does not exist, players will use the normal spawn room. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
