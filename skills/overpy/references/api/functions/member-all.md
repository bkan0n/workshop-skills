# receiver.all

`<Array>.all(lambda?)`

Receiver: `Array`. The receiver supplies the first compiler argument.

Whether the lambda function evaluates to true for every element of the array. If no argument is provided, checks whether every element is truthy. Returns true for an empty array.

Example: `getAllPlayers().all(lambda player: player.A == 2)`

With index: `array.all(lambda elem, idx: elem > idx)`

Without lambda: `array.all()` (equivalent to `array.all(lambda x: x)`)

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `lambda` | `Lambda` | The lambda function that is evaluated for each element of the array. Must return a boolean. If omitted, defaults to the element itself. Optional; upstream describes the omitted expression as `<current array element>`. This label is not literal source syntax. |

Returns: `bool`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
