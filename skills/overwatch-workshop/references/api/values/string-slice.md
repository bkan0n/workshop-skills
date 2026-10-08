# String Slice

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`String Slice(string, substringStartIndex, substringLength)`

The substring of the provided string.

| Argument | Type | Meaning |
| --- | --- | --- |
| `string` | `String` | The string value from which to build the substring. |
| `substringStartIndex` | `unsigned int` | Specifies the character that will start the substring (with 0 as the first character, 1 as the second character, etc.). |
| `substringLength` | `unsigned int` | Specifies the number of characters in the substring. |

Returns: `String`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
