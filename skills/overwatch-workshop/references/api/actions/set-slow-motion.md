# Set Slow Motion

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Slow Motion(speedPercent)`

Sets the simulation rate for the entire game, including all players, projectiles, effects, and game mode logic.

| Argument | Type | Meaning |
| --- | --- | --- |
| `speedPercent` | `unsigned float` | The simulation rate as a percentage of normal speed. Only rates up to 100% are allowed. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
