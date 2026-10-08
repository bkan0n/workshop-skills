# buttonToString

`buttonToString(button)`


Displays a button with [ ] if not a texture, and replaces LSHIFT/LCONTROL/LALT by SHIFT/CTRL/ALT.

You will likely want to use this instead of `inputBindingString()`.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `button` | `Button` | The button to display. |

Returns: `String`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
["{0}(0.00, 1.00, 0.00)[{0}](0.00, 1.00, 0.00)[SHIFT](0.00, 1.00, 0.00)[CTRL](0.00, 1.00, 0.00)[ALT]".format(b).split(Vector.UP[0])[
            strLen("\\{0}{0}{0}{0}{0}{0}{0}".format(b)) % 7 == 1 and
            abs("00LSHIFT0LCONTROL0LALT".split(null[0]).index(b))
        ] for b in inputBindingString($button)]
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
