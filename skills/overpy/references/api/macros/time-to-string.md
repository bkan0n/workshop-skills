# timeToString

`timeToString(time)`


Converts a time (in seconds) to a H:MM:SS format with decimals included (unless you use the `floor()` function). For example, `timeToString(3600+120+37.65)` will return `1:02:37.65`.

| Argument | Type | Meaning / default |
| --- | --- | --- |
| `time` | `unsigned float` | The time in seconds to display. |

Returns: `String`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
"{}:{}:{}".format(
            floor($time / 3600),
            ($time % 3600 / 60 + 100).substring(true, 2),
            ($time % 60 + 100).substring(true, 9999)
        )
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
