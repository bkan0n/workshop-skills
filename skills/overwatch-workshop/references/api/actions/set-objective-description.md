# Set Objective Description

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Objective Description(visibleTo, text, reevaluation)`

Sets the text at the top center of the screen that normally describes the objective to a message visible to specific players.

| Argument | Type | Meaning |
| --- | --- | --- |
| `visibleTo` | `Player \| Array<Player>` | One or more players who will see the message. |
| `text` | `Object` | The message to be displayed. |
| `reevaluation` | `HudReeval` | Specifies which of this action's inputs will be continuously reevaluated. The message will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
