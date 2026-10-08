# Damage

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Damage(player, damager, amount)`

Applies instantaneous damage to one or more players, possibly killing the players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players who will receive damage. |
| `damager` | `Player` | The player who will receive credit for the damage. A damager of null indicates no player will receive credit. |
| `amount` | `float` | The amount of damage to apply. This amount may be modified by buffs, debuffs, or armor. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
