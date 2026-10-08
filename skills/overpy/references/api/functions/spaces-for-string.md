# spacesForString

`spacesForString(text)`


Returns a string made of spaces that is the same length as the provided string. The provided string must be a literal string.

**NOTE**: The displayed string MUST be in the Blizzard Global font (use the 'b' string modifier on the final string, unless using a progress bar). **The casing of the string is also respected**.

This is useful to do alignment tricks.

This function is the equivalent of `spacesForLength(strVisualLength(str))`, however it can also be used with translated strings, in which case it will also return a translated string.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `text` | `String` | The text to get spaces of. Must be a literal custom string, not a variable. |

Returns: `String`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
