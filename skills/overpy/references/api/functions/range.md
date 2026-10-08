# range

`range(start, stop, step)`


Only usable inside a `for` instruction, such as `for i in range(1,3,2)`. If only 2 arguments are provided, they are treated as `range(start, stop)`. If only one argument is provided, it is treated as `range(stop)`.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `start` | `float` | The control variable is set to this value when the loop begins. If omitted, defaults to 0. |
| `stop` | `float` | If the control variable reaches or passes this value, then the loop will exit, and execution jumps to the next action after the end action. Whether this value is considered passed or not is based on whether the step value is negative or positive. If the control variable has already reached or passed this value when the loop begins, then the loop exits. |
| `step` | `float` | This value is added to the control variable when the end action is reached. If this modification causes the control variable to reach or pass the range stop value, then the loop exits, and execution jumps to the next action after the end action. Otherwise, the loop continues, and execution jumps to the next action after the for action. |

Returns: `Iterator`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
