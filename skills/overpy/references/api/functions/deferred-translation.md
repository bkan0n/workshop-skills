# ___

`___(contextOrString, string=null)`


Same as the `_` function, but will never resolve the translation, even if in a display action. You must wrap it with the `_` function to resolve it.

This is useful when several strings are used in a single display action. For example:

`bigMessage(text=[t"Choice 1", t"Choice 2"][eventPlayer.choice])`

This will add the code to resolve the translation twice, but it can be optimized to:

`bigMessage(text=_([___("Choice 1"), ___("Choice 2")][eventPlayer.choice]))`

Wrapping a string with `___` has the same caveats as putting a translated string in a variable: you must treat it as an opaque value and not do any operations on it, and display it with the `_` function. But, since it is still a value, array indexing is still possible.


| Argument | Type | Meaning / default |
| --- | --- | --- |
| `contextOrString` | `String` | If two arguments are specified, the context (as a string literal); otherwise, the string to be translated (can be a variable). |
| `string` | `CustomStringLiteral` | The string to be translated. Must be a string literal, as there are two arguments and the context has been specified. Default: `null`. |

Returns: `String`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
