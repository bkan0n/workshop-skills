# Create Dummy Bot

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create Dummy Bot(hero, team, slot, position, facing)`

Adds a new bot to the specified slot on the specified team so long as the slot is available. This bot will only move, fire, or use abilities if executing workshop actions.

| Argument | Type | Meaning |
| --- | --- | --- |
| `hero` | `Hero` | The hero that the bot will be. If more than one hero is provided, one will be chosen at random. |
| `team` | `Team` | The team on which to create the bot. The "all" option only works in free-for-all game modes, while the "team" options only work in team-based game modes. |
| `slot` | `int` | The player slot which will receive the bot (-1 for first available slot). Up to 6 bots may be added to each team, or 12 bots to the free-for-all team, regardless of lobby settings. |
| `position` | `Position` | The initial position where the bot will appear. |
| `facing` | `Direction` | The initial direction that the bot will face. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
