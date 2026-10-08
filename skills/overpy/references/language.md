# Source language and declarations

Use this when starting a rule, translating native syntax, or rejecting a plausible-looking Python construct. Exact callable signatures are in the [API index](api/index.md). The snippets here are syntax fragments; [examples](examples.md) links complete compiler fixtures.

## Rules and annotations

A rule starts with `rule "Name":`; its metadata and actions are indented, normally four spaces. `#` starts a line comment and `/* ... */` a block comment. Avoid mixing indentation conventions.

```opy
rule "React to interact":
    @Event eachPlayer
    @Condition eventPlayer.hasSpawned()
    @Condition eventPlayer.isHoldingButton(Button.INTERACT)
    eventPlayer.presses += 1
```

Declare `playervar presses` elsewhere. Annotations belong inside the rule, before actions. Multiple `@Condition` annotations form the rule's condition list. An `if` inside the action body is an execution-time branch; moving it into `@Condition` changes triggering and Wait cancellation. Read [execution](../../overwatch-workshop/references/execution.md) before making that change.

`@Event global` supplies a global ongoing rule; `@Event eachPlayer` supplies per-player ongoing execution. For a discrete event, look up its exact name and available context rather than substituting `eachPlayer`. `@Team`, `@Hero`, and `@Slot` filter eligible event subjects. A slot filter and hero filter do not manufacture a spawned player.

`@Disabled` disables a rule. The optimizer can remove empty rules; `@Delimiter` retains an intentional separator, and `@Name` supplies a display name for a subroutine. These are compiler annotations, not runtime decorators.

## Variables and initialization

```opy
globalvar roundState
globalvar spawnPosition = vect(10, 0, 10)
playervar presses = 0
globalvar reservedSlot 2
```

A declaration can reserve a numeric variable index; otherwise the compiler allocates one. Default variable names may be used without declaration, but descriptive declarations make ownership clear. Keep explicit indices when interoperability or existing state requires them. A global is referenced as `roundState`, a player's variable as `eventPlayer.presses` or another player expression's member.

Declaration initializers can generate initialization rules; inspect their output if timing or resets matter. An assignment within a rule still addresses Workshop storage. It does not create block-local Python state or reset on every invocation. Player departure, hero change, and match restart need the policies in [state and lifecycle](../../overwatch-workshop/references/state-lifecycle.md).

## Expressions and calls

Use `true`, `false`, `null`, arithmetic/comparison operators, `and`, `or`, and `not`. Do not replace engine coercion with Python truth rules. The conditional expression `x if condition else y` has low precedence; parenthesize it when embedding it in arithmetic.

Use `vect(x, y, z)` and constants such as `Vector.UP`, `Hero.ANA`, `Button.INTERACT`, `Color.YELLOW`, and `Team.1`. Vector component access is `.x`, `.y`, or `.z`. These are source mappings, not Python objects or imports.

Many native functions become receiver calls, such as `eventPlayer.teleport(position)`. Others become operators (`A += 1`), values (`eventPlayer`), or renamed helpers (`len(array)`). Look up both receiver and argument order. Named arguments can specify optional fields, for example `hudHeader(text="Score", color=Color.YELLOW)`. Defaults are compiler-version facts and may include reevaluation behavior.

## Function-shaped constructs

`def name():` is a runtime subroutine with no parameters and no return value. `return` aborts the current action list. `macro name(argument):` expands source and can have parameters/defaults. These are different tools; see [control and collections](control-collections.md) and [preprocessing](preprocessing.md).

Do not invent `import random`, Python classes, arbitrary standard-library calls, or general-purpose closure behavior. The catalog includes supported module-like namespaces such as `random`; using one does not require a Python import. Check unsupported syntax with the pinned compiler before recommending a replacement.

Evidence: [upstream syntax and mapping](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#general-syntax), [annotations](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/opy/annotations.ts). Compiled examples establish accepted syntax, not lifecycle correctness in every game mode.
