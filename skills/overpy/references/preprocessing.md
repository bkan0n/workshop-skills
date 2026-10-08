# Macros, enums, and preprocessing

Use these features to organize source and generate repeated code. They do not create a new Workshop runtime. Snippets here are fragments; the [subroutine](../examples/subroutine.opy) and [project](../examples/project/main.opy) examples contain complete uses.

## Prefer AST macros for inline expressions and actions

```opy
macro BONUS = 20
macro scaled(value, factor=2):
    value * factor
macro Player.showValue(value):
    smallMessage(self, "Value: {}".format(value))
```

An AST macro preserves grouping when substituted into a larger expression. Member macros use `self` for the receiver and may use default or keyword arguments. They inline at the call site; repeated uses of a parameter can repeat an expensive or changing expression. If one runtime sample is required, store it deliberately or use the appropriate capture mechanism, not the mere existence of a macro.

Choose a subroutine when runtime reuse is needed and its no-parameter/context constraints fit. Choose a macro when source parameters or expression results are needed. Neither supplies ordinary Python stack-local variables.

`#!define` is textual substitution. A definition such as `#!define sum(a,b) a+b` can change precedence in `sum(3,4)*3`. If textual substitution is necessary, parenthesize arguments and the whole expansion. AST macros avoid this particular problem.

## Enums are inline source values

```opy
enum Phase:
    SETUP = 1
    ACTIVE
    FINISHED
```

An omitted value increments the prior value, or starts at zero. Existing enums can be extended. `len(Phase)` and `Phase.toArray()` expose their membership. An enum member defined as a live expression remains a live expression wherever expanded; it is not initialized once at match start. Do not treat hero ordering or numeric enum ordinals as permanently stable game data.

`#!allowMacroRedeclaration` permits redefinition of macros, textual definitions, and enum members. Use it only when intentional composition depends on it; otherwise duplicate definitions help reveal mistakes.

## Compiler directives and file scope

`#!include` and `#!mainFile` implement the [project workflow](project-workflow.md). `#!rulePrefix` affects subsequent rules in the current file/child includes and restores the outer prefix after an include. `#!rulePrefixTemplate` sets a single global formatting expression. Prefixes can make generated source traceable without hand-editing every rule name.

Optimization directives can be block-scoped, while aggressive size optimization is project-wide. Read [diagnostics](diagnostics.md) before changing them. `#!debugElementCount` adds generated element-count comments. `#!writeToOutputFile` requests a `.ws.txt` artifact in the extension workflow; the CLI's explicit `-o` and API output handling remain caller-controlled.

## Script macros and hooks

`#!define name(x) __script__("script.js")` evaluates JavaScript during compilation, with macro arguments supplied to the script. The final expression is the result; a top-level `return` is not the documented interface. OverPy supplies vector/enum conveniences inside that interpreter. This does not let the Workshop run arbitrary JavaScript.

`#!postCompileHook "hooks/output.js"` transforms the generated Workshop string exposed as `content`. Its final expression becomes the output; the path is relative to the compilation root, and only one hook is permitted. A hook can invalidate otherwise accepted output, so inspect and validate the post-hook text. Preserve hooks and their inputs in reproducible builds.

The pinned interpreter imposes execution and memory limits. Do not assume Node.js packages, filesystem APIs, or browser globals are available inside scripts. Use the [exact catalog](api/index.md) and the pinned source for supported directives; do not expand a textual macro workaround into a universal requirement.

## Compiler-provided helpers

Helpers such as `compressed`, `splitDictArray`, `tabular`, HUD macros, and text-measurement utilities synthesize Workshop expressions/actions. Use them only when their cataloged types and preconditions fit. Compression trades source data for decoding work; font-specific width helpers depend on the documented font; generated HUD helpers can consume multiple resources. Check generated output and the shared [performance](../../overwatch-workshop/references/performance-debugging.md) and [resource](../../overwatch-workshop/references/resources.md) references before treating source brevity as runtime efficiency.

Evidence: [upstream preprocessing](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#preprocessing), [directives](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/opy/preprocessing.ts), [QuickJS implementation](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/quickjs.ts). These are source/compiler facts at the pinned release.
