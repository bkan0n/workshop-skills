# _

`_(contextOrString, string=null)`


The translation function. If two arguments are specified, the first argument (a string literal) is used as the context to disambiguate strings that are the same but must be translated differently. Else, the first argument is the string to be translated (can be a variable, in which case this function has to be used directly in the display function such as `hudText()`).

See `#!translations` for more details.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `contextOrString` | `String` | If two arguments are specified, the context (as a string literal); otherwise, the string to be translated (can be a variable). |
| `string` | `CustomStringLiteral` | The string to be translated. Must be a string literal, as there are two arguments and the context has been specified. Default: `null`. |

Returns: `String`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
