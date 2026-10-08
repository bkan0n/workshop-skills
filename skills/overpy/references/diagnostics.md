# Diagnostics and generated behavior

Read this for compiler errors/warnings, code that compiles but behaves incorrectly, or a suspected optimization change.

## Separate the failure layers

1. **Parse/name/type failure:** reduce the source to the smallest failing rule; check indentation, declared storage, the function's receiver, argument types, and exact enum names in the [API index](api/index.md). Python-like spelling is not authority.
2. **Source resolution/configuration failure:** verify entry point, include-relative paths, settings mode, compiler language, installed version, and any script hooks. Compile the real project root as described in [workflow](project-workflow.md).
3. **Accepted source with warnings:** inspect every diagnostic and its source location. The CLI can exit zero while emitting warnings. A warning suppression is not a repair or proof of safety.
4. **Accepted source with wrong output:** compare the relevant generated actions with the intended control flow and captured values. Reduce compiler directives/macros until the transformation is clear.
5. **Plausible output with wrong game behavior:** investigate [event execution](../../overwatch-workshop/references/execution.md), [reevaluation](../../overwatch-workshop/references/reevaluation.md), [state lifecycle](../../overwatch-workshop/references/state-lifecycle.md), and [performance/debugging](../../overwatch-workshop/references/performance-debugging.md). Compiler success cannot decide these alone.

Report the actual command/API, version, token language, diagnostics, and the boundary of the check. If no compiler ran, label source uncompiled.

## Compiler warnings with engine implications

These warning names and explanations come from the pinned upstream source; the engine reports have not been independently retested by this skill project.

| Warning | Why to investigate | Focused response |
| --- | --- | --- |
| `w_wait_until` | Wait Until may not accept a nonzero number as boolean true | Supply an explicit boolean comparison with the intended threshold; a stored boolean may justify a narrow suppression |
| `w_ow2_rule_condition_chase` | A chased variable may fail to trigger an ongoing condition during intermediate movement | Investigate notification/recheck behavior; stopping at a meaningful threshold is one upstream workaround; wrapping with `updateEveryFrame` alone is not established as a cure |
| `w_chased_var_in_for` | A variable mentioned in a chase can fail as a For counter, even with that chase in a disabled rule | Give the loop a separate declared counter |
| `w_start_rule_crash` | Repeated Restart calls interrupting a subroutine's remaining Wait are reported to accumulate toward a crash | Reconsider restart frequency/policy and model cancellation explicitly; an archived restart count is not a safe budget |
| `w_unsuitable_event` | A value/action does not suit the rule's event context | Fix the event or data source instead of replacing missing context with a guess |
| `w_type_check` | Supplied expression differs from the function's expected type | Verify intended coercion and generated action; do not globally suppress type checks |

Use `@SuppressWarnings warning_name` on the specific reviewed rule if justified. `#!suppressWarnings` affects the project more broadly. Record the reason and a reproduction that supports the exception; do not suppress warnings solely to make validation pass. The checked examples include a deliberate warning case to prove warnings are examined.

## Optimizations are transformations, not runtime tests

By default the compiler folds constant calculations, removes no-op/empty output, and substitutes recognized function patterns. Inspect the emitted text rather than assuming one source line always corresponds to one native action.

`#!disableOptimizations` is a useful comparison when minimizing a suspected optimizer defect. `#!optimizeStrict` disables selected coercion-sensitive substitutions: for instance, multiplying a vector by zero differs from replacing it with numeric zero. Decompilation enables strict optimization to reduce that risk. Removing it requires checking the mode's intentional type tricks.

`#!optimizeForSize` favors lower element count, which may increase runtime evaluation. `#!optimizeForSizeAggressive` is a project-wide stronger mode and requires size optimization. Ordinary optimization/size/strict directives take effect from their declaration in their block scope and have corresponding reversal directives; do not assume a directive inserted deep in a rule controls every file.

Replacement directives such as substituting a mode-dependent value for numeric zero require their documented base-mode invariants. Read that directive's [catalog entry](api/index.md) before using it. A smaller build whose replacement premise is false is incorrect.

`#!debugElementCount` and compile-result `nbElements` measure static elements. They do not measure execution frequency, server cost, client rendering, or resource lifetime. HUD debug helpers also allocate display resources. Remove or manage instrumentation with the same ownership discipline as production UI.

## A useful minimal reproduction

Preserve only the implicated event, variable declarations, conditions, wait/reevaluation choice, and action. Keep the original input/output language and compiler options. Compare generated code with a direct native version only when the two share the same event context and settings. State which difference was observed, then test that specific behavior in-game when possible. Do not call a roundtrip equivalent merely because both sides compile.

Evidence: [common warnings](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#common-warnings), [optimization documentation](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#optimizations), [compiler](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/compiler/compiler.ts).
