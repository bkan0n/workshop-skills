# Set Damage Dealt

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Damage Dealt(player, damageDealtPercent)`

Sets the damage dealt of one or more players to a percentage of their raw damage dealt.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose damage dealt will be set. |
| `damageDealtPercent` | `unsigned float` | The percentage of raw damage dealt to which the player or players will set their damage dealt. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
