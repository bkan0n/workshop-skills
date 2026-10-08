# String Replace

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`String Replace(string, pattern, replacement)`

Results in a String Value. This String Value will be built from the specified String Value, where all occurrences of the pattern String are replaced with the replacement String.

**WARNING**: This function clamps the string to 511 bytes (in UTF-8).

| Argument | Type | Meaning |
| --- | --- | --- |
| `string` | `String` | The String Value with which to search for replacements. |
| `pattern` | `String` | The String pattern to be replaced. |
| `replacement` | `String` | The String Value with which to replace the pattern String |

Returns: `String`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports.
