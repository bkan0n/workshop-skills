# Start Assist

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Assist(assisters, targets, reevaluation)`

Starts granting assist credit toward to one or more assisters when one or more targets are eliminated. A reference to this assist modification can be obtained from the getLastAssistId() value. This action will fail if too many assists have been started.

| Argument | Type | Meaning |
| --- | --- | --- |
| `assisters` | `Player \| Array<Player>` | The target Player or Players who will receive assist credit. |
| `targets` | `Player \| Array<Player>` | The Player or Players whose eliminations will grant assist credit to the Assisters. If the Target or Targets are allied to the Assister, this will be a defensive assist. Otherwise, this will be an offensive assist. |
| `reevaluation` | `AssistReeval` | Specifies which of this Action's Inputs will be continuously reevaluated. This Action will keep asking for and using new Values from reevaluated Inputs. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
