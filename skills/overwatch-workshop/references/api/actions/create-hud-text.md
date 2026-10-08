# Create HUD Text

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create HUD Text(visibleTo, header, subheader, text, location, sortOrder, headerColor, subheaderColor, textColor, reevaluation, specVisibility)`

Creates hud text visible to specific players at a specific location on the screen. This text will persist until destroyed. To obtain a reference to this text, use the last text id value. This action will fail if too many text elements have been created.

Note: you can use the macros `hudHeader`, `hudSubheader` and `hudSubtext` to reduce the number of arguments.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will see the hud text. |
| `header` | `Object` | The text to be displayed (can be blank) |
| `subheader` | `Object` | The subheader text to be displayed (can be blank) |
| `text` | `Object` | The body text to be displayed (can be blank) |
| `location` | `HudPosition` | The location on the screen where the text will appear. |
| `sortOrder` | `float` | The sort order of the text relative to other text in the same location. A higher sort order will come after a lower sort order. |
| `headerColor` | `Color` | The color of the header. |
| `subheaderColor` | `Color` | The color of the subheader. |
| `textColor` | `Color` | The color of the text. |
| `reevaluation` | `HudReeval` | Specifies which of this action's inputs will be continuously reevaluated. |
| `specVisibility` | `SpecVisibility` | Whether spectators can see the text or not. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
