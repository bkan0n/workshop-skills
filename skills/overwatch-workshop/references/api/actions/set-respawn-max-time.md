# Set Respawn Max Time

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Respawn Max Time(player, time)`

Sets the duration between death and respawn for one or more players. For players that are already dead when this action is executed, the change takes effect on their next death.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose respawn max time is being defined. |
| `time` | `unsigned int` | The duration between death and respawn in seconds. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
