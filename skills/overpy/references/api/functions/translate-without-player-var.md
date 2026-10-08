# __

`__(contextOrString, string=null)`


Same as the `_` function, but if using `#!translateWithPlayerVar`, it will ignore that directive. Use this if you want a string to be translated for spectators.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `contextOrString` | `String` | If two arguments are specified, the context (as a string literal); otherwise, the string to be translated (can be a variable). |
| `string` | `CustomStringLiteral` | The string to be translated. Must be a string literal, as there are two arguments and the context has been specified. Default: `null`. |

Returns: `String`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
