# Start Damage Modification

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Damage Modification(receivers, damagers, damagePercent, reevaluation)`

Starts modifying how much damage one or more receivers will receive from one or more damagers. A reference to this damage modification can be obtained from the last damage modification id value. This action will fail if too many damage modifications have been started.

| Argument | Type | Meaning |
| --- | --- | --- |
| `receivers` | `Player \| Array<Player>` | The player or players whose incoming damage will be modified (when attacked by the damagers). |
| `damagers` | `Player \| Array<Player>` | The player or players whose outgoing damage will be modified (when attacking the receivers). |
| `damagePercent` | `unsigned float` | The percentage of damage that will apply to receivers when attacked by damagers. |
| `reevaluation` | `DamageReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
