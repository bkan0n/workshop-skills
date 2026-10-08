# receiver.format

`<String>.format(value, ...)`

Receiver: `String`. The receiver supplies the first compiler argument.

The values that will be converted to text and used to replace the format placeholders (such as `{}` or `{0}`). Only usable on a string. Can have as much arguments as there are placeholders. The n-th argument replaces the n-th placeholder.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `value` | `Object` | The value used to replace the matching placeholder. |

Returns: `String`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
