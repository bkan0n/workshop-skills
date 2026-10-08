# Start Rule

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Start Rule(subroutine, ifAlreadyExecuting)`

Begins simultaneous execution of a subroutine rule (which is a rule with a Subroutine event type). Execution of the original rule continues uninterrupted. The subroutine will have access to the same contextual values (such as Event Player) as the original rule.

| Argument | Type | Meaning |
| --- | --- | --- |
| `subroutine` | `Subroutine` | Specifies which subroutine to start. If a rule with a subroutine event type specifies the same subroutine, then it will execute. Otherwise, this action is ignored. |
| `ifAlreadyExecuting` | `StartRuleBehavior` | Determines what should happen if the rule specified by the subroutine is already executing on the same player or global entity. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
