# Call Subroutine

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Call Subroutine(subroutine)`

Pauses execution of the current rule and begins executing a subroutine rule (which is a rule with a subroutine event type). When the subroutine rule finishes, the original rule resumes execution. The subroutine will have access to the same contextual values (such as Event Player) as the original rule.

| Argument | Type | Meaning |
| --- | --- | --- |
| `subroutine` | `Subroutine` | Specifies which subroutine to call. If a rule with a subroutine event type specifies the same subroutine, then it will execute. Otherwise, this action is ignored. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
