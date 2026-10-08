# receiver.map

`<Array>.map(lambda)`

Receiver: `Array`. The receiver supplies the first compiler argument.

A copy of the specified array with the values mapped according to the lambda function that is evaluated for each element.

Example: `getAllPlayers().map(lambda player: player.A + 2)`

With index: `array.map(lambda elem, idx: elem + idx)`

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `lambda` | `Lambda` | The lambda function that is evaluated for each element. The return value is used as the new element. |

Returns: `Array<Object>`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
