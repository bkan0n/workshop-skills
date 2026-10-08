# Set Ability Resource

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Ability Resource(player, button, resourcePercent)`

Set the ability resource percentage for one or more players. Affects abilities such as Dva's Defense Matrix, Pharah's Hover Jets, etc.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose ability resource percentage will be modified. |
| `button` | `Button` | The logical button associated with the ability to be modified. |
| `resourcePercent` | `unsigned float` | The percentage of resource that will be set with respect to each player's ability resource capacity. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
