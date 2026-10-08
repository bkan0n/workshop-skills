# Start Healing Modification

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Healing Modification(receivers, healers, healingPercent, reevaluation)`

Starts modifying how much healing one or more receivers will receive from one or more healers. A reference to this healing modification can be obtained from the last healing modification id value. This action will fail if too many healing modifications have been started.

| Argument | Type | Meaning |
| --- | --- | --- |
| `receivers` | `Player \| Array<Player>` | The player or players whose incoming healing will be modified (when healed by the healers). |
| `healers` | `Player \| Array<Player>` | The player or players whose outgoing healing will be modified (when healing the receivers). |
| `healingPercent` | `unsigned float` | The percentage of healing that will apply to receivers when healed by healers. |
| `reevaluation` | `HealingReeval` | Specifies which of this action's inputs will be continuously reevaluated. This action will keep asking for and using new values from reevaluated inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
