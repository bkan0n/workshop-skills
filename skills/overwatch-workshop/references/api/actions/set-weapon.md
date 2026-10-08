# Set Weapon

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Weapon(player, weapon)`

Sets the weapon of one or more players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose weapon will be set. |
| `weapon` | `unsigned int` | The number of the weapon to be equipped. 1 is the first weapon, and 2 is the second. If the specified weapon does not exist, players will use the default weapon. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
