# sorted

`sorted(array, key=lambda item: item)`


A copy of the specified array with the values sorted according to the lambda function that is evaluated for each element.

Example: `sorted(getAllPlayers(), key=lambda x: x.getScore())`

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `array` | `Array<Object>` | The array whose copy will be sorted. |
| `key` | `Lambda` | The lambda function that is evaluated for each element of the copied array. The array is sorted by this rank in ascending order. Can be omitted if the array is sorted without a special key (equivalent to `lambda x: x`). Default: `lambda item: item`. |

Returns: `Array<Object>`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
