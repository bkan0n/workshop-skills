# Control flow and collections

Read this for loops, array transformations, dictionary lookup, or subroutine control. Examples in this page are fragments; use the complete [collections](../examples/collections.opy), [selection](../examples/selection.opy), and [subroutine](../examples/subroutine.opy) fixtures to compile.

## Branches and loops

`if` / `elif` / `else` and `while` use indented blocks. A `while` compiles to Workshop While. Repeated activity needs deliberate pacing and cancellation; a small finite calculation does not automatically need a wait. Keep the shared [execution guidance](../../overwatch-workshop/references/execution.md) authoritative.

```opy
for i in range(1, 5, 2):
    values.append(i)
```

The loop variable must be declared Workshop storage (`globalvar i` or a player variable). The structured native metadata defines an exclusive stop, checked before the body: this range therefore targets 1 and 3. The pinned README contradicts that metadata by claiming 1, 3, 5; the compiler emits native For bounds unchanged. This project follows the explicit For argument contract and flags the README example as conflicting, without claiming a game test. `range(stop)` means start 0, step 1; it is a loop-specific construct, not a Python range object. Do not use a chased variable as the loop counter: [diagnostics](diagnostics.md) explains the compiler's warning.

`loop()` restarts the rule's action list; it is not a synonym for `continue` in any arbitrary nested construct. `return` aborts the action list. Forward labels and `goto` lower to Skip instructions, are restricted to the same rule, and cannot jump backward. Prefer structured control unless the jump itself solves the task. Inspect generated Skip counts when using dynamic `goto loc + expression`.

## Array values versus stored mutations

| Intent | OverPy form | Consequence |
| --- | --- | --- |
| New appended array | `result = values.concat(item)` | Produces a value; does not mutate `values` |
| Append to stored variable | `values.append(item)` | Emits a variable modification |
| New filtered array | `result = values.filter(lambda item: item > 0)` | Produces a value |
| New mapped array | `result = values.map(lambda item, index: item + index)` | Produces a value |
| Remove from stored variable by value | `values.remove(item)` | Emits a variable modification |
| New array excluding values | `result = values.exclude(item)` | Produces a value |
| Remove a stored index | `del values[index]` | Emits indexed removal |
| Slice | `values.slice(start, count)` | Second argument is count, not end |

Lambda parameters in these operations map to Current Array Element/Index. They describe reevaluated expressions; they are not independent stored loop variables or arbitrary Python closures. Nested operations need careful context inspection. Supported comprehensions are alternative syntax, not proof that every Python comprehension construct works.

`sorted(values, key=lambda item: expression)` orders ascending by a key; it does not filter inappropriate players. Array `.reverse()` is a value expression. `len()`, `.index()`, `.last()`, indexed lookup, and missing values inherit [Workshop array semantics](../../overwatch-workshop/references/values-arrays.md), including sentinels rather than ordinary exceptions.

Two- and three-dimensional assignments are compiler transformations that reconstruct containing arrays. They can cost several operations and reevaluate expressions; do not assume constant-cost native multidimensional writes. Inspect output when indices or source values change during execution.

## Switch and dictionary lookup

A `switch` evaluates its selector for dispatch and supports `case` and `default`. **Fallthrough is enabled**: end a case with `break` when only that case should run. The [selection fixture](../examples/selection.opy) includes deliberate breaks.

A dictionary-style lookup such as `{1: 10, 2: 20, default: -1}[mode]` is compiled into arrays/indexing. The dictionary must be accessed; it is not a standalone mutable Python dictionary. Without `default`, an absent key returns `null`. Use this for a mapping, not for runtime object ownership or a general hash table.

## Subroutines and concurrency

```opy
def recordUse():
    eventPlayer.uses += 1

rule "Call":
    @Event eachPlayer
    recordUse()
```

The call uses the caller's context. It does not create parameter/local-variable frames. A normal call and `startRule(...)` differ: the latter starts simultaneous execution and has an already-running policy. Its pinned default is `StartRuleBehavior.RESTART`; specify the intended policy rather than relying on that default. Repeatedly restarting a waiting subroutine has an upstream crash warning; see [diagnostics](diagnostics.md). Shared context and ownership remain in [Workshop execution](../../overwatch-workshop/references/execution.md).

Evidence: [upstream control flow](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#control-flow), [advanced constructs](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#advanced-constructs), and [action metadata](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts).
