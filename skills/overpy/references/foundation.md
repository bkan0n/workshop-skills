# OverPy foundation

This release targets **OverPy 9.7.17**. Its source tag resolves to commit `5a7d0e294b8cad73b9701987bb584d0551d7fa4d`. Exact names and defaults come from the bundled [API index](api/index.md); an English Workshop name converted to camelCase is not reliable enough to invent a call.

## Source language and engine

- Declare stored state with `globalvar` or `playervar`; use `eventPlayer.name` for a player variable. A local-looking assignment inside a rule does not create a Python local.
- A `rule "name":` contains indented annotations and actions. Use explicit `@Event global` or `@Event eachPlayer` when that makes context clear. Match discrete event names to the catalog.
- `def name():` declares a Workshop subroutine, with no runtime parameters or return value. Use an AST `macro` for parameterized inline source. Inlining can repeat evaluation; it does not capture values.
- Functions are often receiver methods: `eventPlayer.teleport(...)`. Others become operators, variables, enums, or helpers. Names beginning with internal compiler markers are not public source syntax.
- `false`, `true`, and `null` are lowercase. Collections, comparisons, missing values, and vectors retain engine semantics; see [Workshop values](../../overwatch-workshop/references/values-arrays.md).

## Decisions that change behavior

`wait()` defaults to `0.016` seconds and `Wait.IGNORE_CONDITION` in this compiler. Choose an explicit duration and mode when cancellation or repetition matters; consult [waits](../../overwatch-workshop/references/waits.md). Do not insert waits into every rule or remove them to save elements.

`.concat()` and `.exclude()` produce values; `.append()` and `.remove()` on a variable emit mutations. `range()` is a loop-only construct lowered to Workshop For; inspect its bounds and declared counter rather than treating it as a Python range object. Runtime lambdas in `.filter()`/`.map()` describe array evaluation, not general Python closures. Read [control and collections](control-collections.md) when these appear.

`evalOnce()` and reevaluation flags control captured versus changing values; `updateEveryFrame()` affects update frequency. Writing a macro around an expression does not freeze it. Use the shared [reevaluation reference](../../overwatch-workshop/references/reevaluation.md).

The compiler can fold expressions, replace patterns, remove empty rules, and synthesize actions or rules. `#!optimizeStrict` preserves selected coercion-sensitive cases; smaller output need not run faster. Investigate a compiler-versus-engine discrepancy with [diagnostics](diagnostics.md), without treating every unexpected behavior as an optimizer bug.

## Work and validation

Keep `.opy` and its included files as the maintained source. Compile to Workshop text in the game's text language, then import that output. Decompilation is useful for migration and investigation; it does not recover original macros or file organization.

When tools are available, use the project's installed, pinned compiler; compile the real entry point with its root path, check warnings, and inspect the relevant generated actions. Without tools, provide useful code labeled **uncompiled** and an exact validation procedure from [project workflow](project-workflow.md). Never claim a compiler or in-game run that did not occur.

Evidence: [pinned upstream README](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md), [standalone exports](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/overpy_standalone.ts). Source and compiler evidence describe this pin; engine claims inherit the Workshop references' evidence dates.
