# receiver.any

`<Array>.any(lambda?)`

Receiver: `Array`. The receiver supplies the first compiler argument.

Whether the lambda function evaluates to true for any element of the array. If no lambda is provided, checks whether any element is truthy. Returns false for an empty array.

Example: `getAllPlayers().any(lambda player: player.A == 2)`

With index: `array.any(lambda elem, idx: elem > idx)`

Without lambda: `array.any()` (equivalent to `array.any(lambda x: x)`)

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `lambda` | `Lambda` | The lambda function that is evaluated for each element of the array. Must return a boolean. If omitted, defaults to the element itself. Optional; upstream describes the omitted expression as `<current array element>`. This label is not literal source syntax. |

Returns: `bool`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
