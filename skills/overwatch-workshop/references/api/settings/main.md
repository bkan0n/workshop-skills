# Settings: main

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

```json
{
  "en-US": "main",
  "values": {
    "description": {
      "en-US": "Description",
      "maxChars": 512,
      "values": "__string__"
    },
    "modeName": {
      "en-US": "Mode Name",
      "maxBytes": 129,
      "values": "__string__"
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
