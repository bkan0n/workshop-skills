# hudSubtext

`hudSubtext(visibleTo=getAllPlayers(), text, location=HudPosition.LEFT, sortOrder=0, color=Color.WHITE, reevaluation=HudReeval.VISIBILITY_SORT_ORDER_STRING_AND_COLOR, specVisibility=SpecVisibility.DEFAULT)`


Built-in macro for `hudText` to reduce the number of arguments.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will see the hud text. Default: `getAllPlayers()`. |
| `text` | `Object` | The text to be displayed. |
| `location` | `HudPosition` | The location on the screen where the text will appear. Default: `HudPosition.LEFT`. |
| `sortOrder` | `float` | The sort order of the text relative to other text in the same location. A higher sort order will come after a lower sort order. Default: `0`. |
| `color` | `Color` | The color of the text. Default: `Color.WHITE`. |
| `reevaluation` | `HudReeval` | Specifies which of this action's inputs will be continuously reevaluated. Default: `HudReeval.VISIBILITY_SORT_ORDER_STRING_AND_COLOR`. |
| `specVisibility` | `SpecVisibility` | Whether spectators can see the text or not. Optional argument. Default: `SpecVisibility.DEFAULT`. |

Returns: `void`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
hudText($visibleTo, null, null, $text, $location, $sortOrder, null, null, $color, $reevaluation, $specVisibility)
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
