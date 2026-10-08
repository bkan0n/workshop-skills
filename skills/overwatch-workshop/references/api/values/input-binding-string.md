# Input Binding String

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Input Binding String(button)`

Converts a button parameter into a string that shows up based on the player's input bindings. This value cannot be stored in variables.

Note: the `buttonToString()` macro performs a much nicer-looking conversion.

| Argument | Type | Meaning |
| --- | --- | --- |
| `button` | `Button` | The button for the input binding that will be converted to a string. |

Returns: `String`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
