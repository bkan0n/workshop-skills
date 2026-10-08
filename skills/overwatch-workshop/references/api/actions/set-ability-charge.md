# Set Ability Charge

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Ability Charge(player, button, chargeCount)`

Set the ability charge count for one or more players. Affects abilities such as Tracer's Blink, Junkrat's Mines, etc.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose ability charge count will be modified. |
| `button` | `Button` | The logical button associated with the ability to be modified. |
| `chargeCount` | `unsigned int` | The charge count that will be set. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
