# Heal

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Heal(player, healer, amount)`

Provides an instantaneous heal to one or more players. This heal will not resurrect dead players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose health will be restored. |
| `healer` | `Player` | The player who will receive credit for the healing. A healer of null indicates no player will receive credit. |
| `amount` | `float` | The amount of healing to apply. This amount may be modified by buff or debuffs. Healing is capped by each player's max health. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
