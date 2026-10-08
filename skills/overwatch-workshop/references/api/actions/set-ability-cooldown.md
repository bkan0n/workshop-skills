# Set Ability Cooldown

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Ability Cooldown(player, button, cooldown)`

Set the ability cooldown time for one or more players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose ability cooldown time will be modified. |
| `button` | `Button` | The logical button associated with the ability to be modified. |
| `cooldown` | `unsigned float` | The cooldown time that will be set in seconds. Max of 1000. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
