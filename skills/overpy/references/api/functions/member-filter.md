# receiver.filter

`<Array>.filter(lambda)`

Receiver: `Array`. The receiver supplies the first compiler argument.

A copy of the specified array with any values that do not match the lambda condition removed.

Example: `getAllPlayers().filter(lambda player: player.A == 2)`

With index: `array.filter(lambda elem, idx: elem > idx)`

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `lambda` | `Lambda` | The lambda function that is evaluated for each element of the copied array. If it returns true, the element is kept; otherwise, it is removed. |

Returns: `Array<Object>`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
