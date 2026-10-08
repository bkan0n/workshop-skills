# Native Workshop authoring

Use native Workshop text when the user asks for code pasted directly into the game. Workshop.codes editor directives and OverPy source are different dialects; neither belongs inside a native rule. Find exact action/value/enum spelling through [API lookup](api/index.md).

For a small adaptation, start with the matching complete fixture: [once-per-press counter](../examples/native-interact-counter.workshop), [repetition while held/alive](../examples/native-held-healing.workshop), or [owned effect with cleanup](../examples/native-owned-effect.workshop). The [example index](../examples/index.md) records expected behavior and validation.

## Structure

A complete native rule contains `rule("name")`, an `event` block, optional `conditions`, and an `actions` block. Statements end with semicolons. Each Player and player-triggered events select a team and hero/slot; Global does not. Conditions compare expressions and all must pass. Actions execute in order. Structured `If`/`Else If`/`Else`, `While`, and `For` blocks close with `End;`.

Global/player declarations map numbered slots to names; access them as `Global.Name` and `Event Player.Name`. Subroutine declarations also map slots to names; a subroutine rule's event names that declaration. Subroutines have no conditions. Callers supply context implicitly, not ordinary function parameters. Use [waits](waits.md) for delay/repetition choices and [execution](execution.md) for event context or parallel calls.

Native shorthand is equivalent to long-form APIs: `Global.A = value` assigns; `+=` modifies; `Global.A[index]` indexes; `a ? b : c` chooses a value. `^` means exponentiation, not XOR. Boolean XOR can use inequality only after establishing both operands are Booleans. Custom strings use placeholders such as `Custom String("Count: {0}", Event Player.Count)`. Strings, player references and arrays do not inherit ordinary language coercion rules.

## Write and validate

1. Choose the actual base game mode and event subject. State which values exist in that context.
2. Declare state and decide reset/cleanup points. Distinguish an action result from a mutation and a one-shot action from a persistent control.
3. Build the smallest complete rule set. Use a fragment only when the insertion context is explicit; label it as a fragment.
4. Check delimiters, enum spelling, action/value positions, matching End statements, and variable/subroutine declarations. Check UI/settings text separately from rules.
5. If a suitable compiler/decompiler is present, check acceptance and diagnostics. Otherwise label the text uncompiled and provide the in-game paste/reproduction procedure. Neither route proves current engine behavior.
6. In game, use the intended map/mode and test the relevant transitions, not just initial spawn. Add concise Inspector logs or a controlled message when needed.

Do not copy tutorial snippets unquestioningly. Archived examples include missing End statements, comparison where assignment was intended, and comments claiming a loop stops despite no stop predicate. Rewritten complete fixtures are preferable.

## Import, export and preservation

Full **Copy Settings** text includes lobby settings and Workshop rules/settings. Rules, conditions and actions can also be copied separately: paste into the corresponding editor context rather than confusing a partial selection with a whole lobby export. On PC, keep source text as the durable editable artifact. In-game UI/platform details are dated; see [match and settings](match-settings.md) for share-code workflow and overwrite behavior.

A short alphanumeric import/share code is a server-hosted settings snapshot, not the native source text. To play one, create a Custom Game, open settings, select Import Code, enter it and confirm. To edit native text, use the editor's relevant paste control. Compiler output containing full settings needs the full-settings import context.

Offline source details: [authoring](wiki/authoring.md).

## Evidence

Wiki sources: [Workshop Basics](wiki/articles/1840.md#wiki-1840) (edited 2023-04-11), [C-style syntax](wiki/articles/4852.md#wiki-4852) (2024-11-26), [Subroutine](wiki/articles/1292.md#wiki-1292) (2021-03-18), [Boolean XOR/XNOR](wiki/articles/4833.md#wiki-4833), [import codes](wiki/articles/2042.md#wiki-2042) (2024-01-03), [If examples](api/actions/if.md) (2025-05-25), [variable tutorial](wiki/articles/2080.md#wiki-2080) (2024-01-28).
