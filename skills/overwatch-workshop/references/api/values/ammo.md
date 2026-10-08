# Ammo

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Ammo(player, clip)`

The current ammo of a player.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player whose ammo to acquire. |
| `clip` | `unsigned int` | The index of the clip to be acquired. 0 is the first clip, and 1 is the second (only used for Bastion's Sentry gun and Baptiste's Heal Grenades). |

Returns: `unsigned float`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
