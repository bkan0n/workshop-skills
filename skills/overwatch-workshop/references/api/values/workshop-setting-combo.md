# Workshop Setting Combo

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Workshop Setting Combo(category, name, default, options, sortOrder)`

Provides the value (a choice of Custom Strings) of a new option setting that will appear in the Workshop Settings card as a combo box. This value returns the index of the selected choice.

| Argument | Type | Meaning |
| --- | --- | --- |
| `category` | `CustomStringLiteral` | The name of the category in which this setting will be found. Must be a custom string literal with 128 characters or less. |
| `name` | `CustomStringLiteral` | The name of this setting. Must be a custom string literal with 128 characters or less. |
| `default` | `UnsignedIntLiteral` | The default value for this setting. |
| `options` | `Array<CustomStringLiteral>` | The options for this setting. |
| `sortOrder` | `IntLiteral` | A sort order for this setting (within the category). Settings with the same sort order are ordered alphabetically. |

Returns: `unsigned int`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
