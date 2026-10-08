# For Player Variable

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`For Player Variable(controlPlayer, controlVariable, rangeStart, rangeStop, step)`

Denotes the beginning of a series of actions that will execute in a loop, modifying the control variable on each loop. The corresponding end action denotes the end of the loop. If the control variable reaches or passes the range stop value, then the loop exits, and execution jumps to the next action after the end action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `controlPlayer` | `Player` | The player whose variable is being modified in this loop. If multiple players are specified, the first player is used. |
| `controlVariable` | `PlayerVariable` | The variable being modified in this loop. It is set to the range start value when the loop begins, and the loop continues until the control variable reaches or passes the range stop value. |
| `rangeStart` | `float` | The control variable is set to this value when the loop begins. |
| `rangeStop` | `float` | If the control variable reaches or passes this value, then the loop will exit, and execution jumps to the next action after the end action. Whether this value is considered passed or not is based on whether the step value is negative or positive. If the control variable has already reached or passed this value when the loop begins, then the loop exits. |
| `step` | `float` | This value is added to the control variable when the end action is reached. If this modification causes the control variable to reach or pass the range stop value, then the loop exits, and execution jumps to the next action after the end action. Otherwise, the loop continues, and execution jumps to the next action after the for action. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
