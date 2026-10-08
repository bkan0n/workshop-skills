# Settings: heroes.enabledHeroes

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

Hero settings require a team wrapper: `heroes.<team>.enabledHeroes`. Replace `<team>` with `allTeams`, `ffa`, `team1`, `team2`. Native team labels: `allTeams` = General; `ffa` = Team FFA; `team1` = Team 1; `team2` = Team 2. The heading identifies a schema fragment, not a complete object path.

```json
{
  "en-US": "enabled heroes"
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
