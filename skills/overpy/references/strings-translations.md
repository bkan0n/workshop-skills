# Strings and player translations

Read this when formatting UI, handling translated values, or investigating a string that compiles but displays incorrectly. Fragments below illustrate syntax; [strings.opy](../examples/strings.opy) is a complete compiler fixture. Engine display/lifetime details belong in [Workshop visuals and strings](../../overwatch-workshop/references/visuals-strings.md).

## Formatting is compiler syntax

Use quoted strings, escapes, `.format()`, or `f`-strings. `"Score: {}".format(eventPlayer.score)` and `f"Score: {eventPlayer.score}"` generate Workshop string construction. Do not assume Python string operators or formatting mini-languages. Upstream's `f` parser restricts a formatter containing a closing brace or the same quote as its surrounding string; split difficult expressions into supported forms.

The compiler can split long source strings and excess format arguments into nested Workshop strings. This removes a source-authoring inconvenience; it does **not** remove runtime rendered-byte limits or font limitations. Adjacent source literals concatenate. `\n`, `\xHH`, `\uHHHH`, and documented `\&entity;` escapes are supported.

Modifiers change different things:

| Modifier | Purpose |
| --- | --- |
| `f` | Inline expression formatters |
| `t` | Register a player-translated string |
| `l` | Native predefined localized-string vocabulary |
| `w` | Fullwidth characters |
| `b` | Prefer Blizzard Global large-letter font where supported |
| `c` | Case-preserving special Latin characters, with visual compromises |

Combined modifiers apply to the whole concatenated literal and belong on its first part. Native localized strings (`l`) and OverPy translations (`t`) are different systems. Use localized strings when intentionally using their restricted native vocabulary, not as a general arbitrary-text translator.

`#!setupTags` generates setup for supported texture/color string tags. This relies on a game workaround whose validity is patch-sensitive; consult [compatibility](../../overwatch-workshop/references/compatibility.md) before adopting it. A successful compile does not prove the generated setup still bypasses sanitization. Font/texture catalogs and syntax do not grant redistribution rights to image assets.

## Translation workflow

`#!translations en fr` enables OverPy's translation system for those languages. Mark source text with `t` or `_()`, compile the real entry point, and edit the generated `.po` files. Keep those files with the source. Compilation can update translation files, and unused translations are removed unless `#!keepUnusedTranslations` is set. The source language, player translation languages, and compiler Workshop token language are distinct choices.

Inside a display action, `t"Welcome"` can resolve for its viewer. Once stored in a variable, a translated value is an opaque translation container rather than an ordinary string. Mark it when storing and resolve with `_()` when displaying:

```opy
message = t"Welcome"
hudHeader(text=_(message))
```

Do not apply `.replace()`, `.charAt()`, or normal string formatting to that stored container. Format the translated template before storing, or do the supported final string operation after resolving in display context. Missing wrappers can display `TLErr` or `0`. A translated container cannot simply be inserted as a normal argument inside another string; refactor so the translated template is the outer text.

`_("context", "left")` distinguishes identical source strings with different meanings. Keep `.format()` outside that translation call. Translation formatting uses special placeholder values internally; the upstream README lists reserved numeric/vector text patterns. Look up that source or generated implementation when translating text that intentionally includes those exact patterns rather than assuming arbitrary replacement is safe.

## Viewer context and size tradeoffs

Translation resolution depends on client/viewer evaluation. Evaluating language-sensitive text into an ordinary server variable can choose the host/importer's language instead of each viewer's. The shared [reevaluation reference](../../overwatch-workshop/references/reevaluation.md) explains that boundary.

`#!translateWithPlayerVar` saves elements by generating a language-detection rule that affects facing on spawn. It has documented spectator limitations and can conflict with a mode's own spawn-facing logic. Do not enable it as an automatic optimization. Upstream offers `__()` to avoid the player-variable route for a particular display and a `noTlErr` option that trades diagnostics/translation behavior for a default-language spectator fallback. Preserve error checking until the display cases have been tested.

`___()` retains an unresolved translation value even in display expressions; a later `_()` performs resolution. This can avoid repeated resolution when selecting among alternatives, but inherits opaque-container restrictions. Use only for a measured need, with tests for normal players and spectators.

Evidence: [pinned string documentation](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#strings), [translation documentation](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#translations). These translation mechanisms describe the pinned compiler implementation.
