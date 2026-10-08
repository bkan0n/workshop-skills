# receiver.append

`<Array>.append(value)`

Receiver: `Array`. The receiver supplies the first compiler argument.

Appends the specified value to the specified array. Note that this function is really the equivalent of `extend()`, that is, `[1,2].append([3,4])` will produce `[1,2,3,4]` instead of `[1,2,[3,4]]`. Modifies the array in-place; use `concat` to instead return a copy of the array.

Example: `A.append(3)`

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `value` | `Object \| Array<Object>` | The value to append to the end of the array. If this value is itself an array, each element is appended. |

Returns: `void`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
