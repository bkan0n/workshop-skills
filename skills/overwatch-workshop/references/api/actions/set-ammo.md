# Set Ammo

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Ammo(player, clip, ammo)`

Sets the ammo of one or more players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose ammo will be set. |
| `clip` | `unsigned int` | The index of the clip whose ammo will be set. 0 is the first clip, and 1 is the second (only used for Bastion's Sentry gun and Baptiste's Heal Grenades). |
| `ammo` | `unsigned int` | The ammo that will be set. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
