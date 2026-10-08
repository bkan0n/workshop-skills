# arrayToString

`arrayToString(array, maxLength=12)`


Displays an array (otherwise, casting an array to a string will only display the first value). The second argument is the maximum length of the array (arrays can go up to 1000, which would generate a lot of elements). If the array length is above the maximum length, an ellipsis (...) will be displayed along with the amount of elements remaining.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `array` | `Array<Object>` | The array to be displayed. If not an array, it will be displayed normally. |
| `maxLength` | `IntLiteral` | The maximum length of the array. If the array is longer than this, an ellipsis (...) will be displayed. Must be a literal number, not a variable. Default: `12`. |

Returns: `String`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
