# print

`print(text)`


Creates an orange HUD text at the top left. Should be used for quick debugging of a value.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `text` | `Object` | The text to be displayed (can be blank) |

Returns: `void`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
hudText(getAllPlayers(), $text, Math.FUCKTON_OF_SPACES, null, HudPosition.LEFT, -9999, Color.ORANGE, null, null, HudReeval.VISIBILITY_AND_STRING, SpecVisibility.DEFAULT)
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
