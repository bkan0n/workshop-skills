# Create Icon

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Create Icon(visibleTo, position, icon, reevaluation, color, showWhenOffscreen)`

Creates an in-world icon entity. This icon entity will persist until destroyed. To obtain a reference to this entity, use the getLastCreatedEntity() value. This action will fail if too many entities have been created.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will be able to see the icon. |
| `position` | `Position \| Player` | The icon's position. If this value is a player, then the icon will appear above the player's head. Otherwise, the value is interpreted as a position in the world. |
| `icon` | `Icon` | The icon to be created. |
| `reevaluation` | `IconReeval` | Specifies which of this action's inputs will be continuously reevaluated. The icon will keep asking for and using new values from reevaluated inputs. |
| `color` | `Color` | The color of the icon to be created. If a particular team is chosen, the effect will either be red or blue, depending on whether the team is hostile to the viewer. |
| `showWhenOffscreen` | `bool` | Should this icon appear even when it is behind you? |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
