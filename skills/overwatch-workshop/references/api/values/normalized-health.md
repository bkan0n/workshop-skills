# Normalized Health

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Normalized Health(player)`

The current health of a player, including armor and shields, normalized between 0 and 1. (for example, 0 is no health, 0.5 is half health, 1 is full health, etc.)

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player` | The player whose normalized health to acquire. |

Returns: `unsigned float`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
