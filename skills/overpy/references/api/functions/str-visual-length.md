# strVisualLength

`strVisualLength(text)`


Returns the length (in font units) of a literal string. Note that it must use the Blizzard Global font (use the 'b' string modifier on the final string, unless displaying in a progress bar in-world text). The string is case-sensitive.

See also: `spacesForLength()` and `spacesForString()`.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `text` | `String` | The text to calculate the length of. Must be a literal custom string, not a variable. |

Returns: `unsigned int`.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
