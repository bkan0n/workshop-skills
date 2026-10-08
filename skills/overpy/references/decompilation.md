# Decompiling and inspecting native code

Read this to migrate an existing Workshop mode, explain generated code, or isolate a compiler/runtime discrepancy.

## Preserve the native input

Save the original complete Workshop text and its language before conversion. Include settings, variables, and subroutine declarations when they are part of the source. A share code is not the source text; export/copy it through the game's workflow first. See [native authoring](../../overwatch-workshop/references/native-authoring.md).

Use the pinned compiler's CLI:

```sh
pnpm exec overpy decompile -i original.workshop.txt -o migrated.opy -l en-US
pnpm exec overpy compile -i migrated.opy -o rebuilt.workshop.txt -l en-US
```

Use the actual source token language in the first command and intended game token language in the second. A parse failure in the wrong language is not evidence that the original mode is invalid. `decompileAllRules(content, language, options)` is the equivalent synchronous API after `readyPromise` resolves.

Keep explicit variable/subroutine indices during an initial migration when other code or established layouts depend on them. CLI options `--ignore-variable-index` and `--ignore-subroutine-index` deliberately omit those indices; choose them only when remapping is acceptable.

## What a roundtrip proves

Successful decompilation and recompilation establish that the pinned compiler can consume and emit these representations. They do not prove the input is accepted by the current game or that execution is equivalent. The compiler may fold expressions, restructure control flow, rename representations, or expose unsupported constructs.

Check the affected event, condition, action order, waits, variable indices, settings, and resource cleanup in the generated output. Byte-for-byte equality is not required. Conversely, a nonempty output is not enough to claim preserved semantics. A focused comparison of relevant actions plus an in-game reproduction is stronger evidence when behavior matters.

The decompiler adds `#!optimizeStrict` to protect selected coercion-sensitive behavior. Keep it until the consequences of removing it have been reviewed. See [diagnostics](diagnostics.md).

## Adopt the source you intend to maintain

Native text cannot reconstruct original macro definitions, include boundaries, comments, translation sources, or architectural intent that were compiled away. Once migrated, maintain the `.opy` project. Repeatedly decompiling edited game output over that source loses organization and can discard deliberate abstractions. If emergency native edits must be recovered, decompile into a separate file and port the relevant change into maintained source.

If a native construct is unsupported, preserve the input and record the exact failure, version, and language. Provide native guidance using Workshop's references where possible. Do not silently delete the construct to make a conversion compile or claim it cannot exist in Workshop because OverPy rejects it.

Evidence: [pinned migration workflow](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#installation), [CLI options](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/cli.ts), [decompiler](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/decompiler/decompiler.ts).
