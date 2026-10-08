# Project and compiler workflow

Read this to create or compile a project, configure settings, or reproduce a compiler result. The skill itself needs no runtime. Use the project's existing compiler/tool conventions; the reference version is **9.7.17**.

## Keep source and output separate

Maintain `.opy` files, settings, macros, and translations in version control. Treat generated Workshop text as an artifact. Compile the real entry point rather than an arbitrary included file. The [complete project example](../examples/project/main.opy) includes a constants file and a settings file.

`#!include "relative/file.opy"` inserts a file relative to the including file. Directory includes exist, but explicit includes make the intended source set easier to review. In a child module, put `#!mainFile "../main.opy"` at the very beginning when compilation should redirect to the entry point. This is source inclusion, not a Python import/module system. Shared declarations remain shared compiler state.

`settings { ... }` supports compile-time expressions and macros; every resulting value must reduce to supported literal data. Runtime variable expressions do not belong there. Alternatively use `settings "mode.opy.json"`. The `.opy.json` suffix enables upstream editor completion; valid JSON avoids disagreement with JSON tooling. A complete settings document must specify a game mode, as the checked example does.

Look up canonical keys in the [settings catalog](api/index.md). The compiler deliberately accepts unknown settings as native labels, which may not translate. Successful compilation therefore does not validate arbitrary setting spelling in the game. `#!extension` selects a Workshop extension; preserve its budget and source requirements. The pinned README mentions `#!extensions`, but that plural directive is rejected by 9.7.17; the singular form is confirmed by a compiler probe.

## VS Code route

The official extension works with `.opy` files. Its Compile command produces Workshop text; Decompile reads copied Workshop text into source. Match the extension's Workshop language setting to the game's text language. Compile-on-save and whether only the main file is saved are configurable. Record the installed extension/compiler version when reproducing a discrepancy.

Warnings can indicate engine hazards rather than syntax errors. Read them before pasting. Do not add `disableInspector()` by habit: debugging may need the inspector. An editor's autocomplete or LSP suggestion is useful lookup assistance, not evidence of game behavior.

## Pinned CLI route

If installation is needed within the user's authorized project setup, use its package manager and an exact dependency, for example `pnpm add -D overpy@9.7.17`. A lockfile and `pnpm exec overpy --version` make the tool selection explicit. Do not use an unpinned one-off download as proof that the pinned examples pass.

With the local package installed:

```sh
pnpm exec overpy compile -i main.opy -o main.workshop.txt -l en-US
pnpm exec overpy decompile -i imported.workshop.txt -o imported.opy -l en-US
```

The CLI supports `--root` and `--main-file` for explicit import resolution. When input is a file, defaults are its directory and basename; for stdin they are the current directory and `stdin.opy`. CLI warnings go to stderr; exit code zero can still have warnings. Inspect stderr and output. After compilation, paste the full generated text into the appropriate Workshop/custom-game import surface and verify the target behavior in a test match.

The language option selects Workshop source/output tokens, not the translated strings shown to players. Player translations are a separate [workflow](strings-translations.md).

## JavaScript API route

This is a complete Node.js CommonJS procedure for an existing `main.opy`; the target project must already provide the pinned package. It is tool guidance, not a Workshop program.

```js
const fs = require('node:fs');
const path = require('node:path');
const overpy = require('overpy');
async function main() {
  await overpy.readyPromise;
  const source = path.resolve('main.opy');
  const result = await overpy.compile(
    fs.readFileSync(source, 'utf8'), 'en-US',
    path.dirname(source), path.basename(source)
  );
  for (const diagnostic of result.encounteredWarnings) {
    console.error(diagnostic.message ?? String(diagnostic));
  }
  fs.writeFileSync('main.workshop.txt', result.result);
  console.error(`Elements: ${result.nbElements}`);
}
main().catch(error => { console.error(error); process.exitCode = 1; });
```

The published package's entry point is standalone. The upstream repository's root entry point is the VS Code extension; when building upstream source, use its standalone target instead. Retain the companion `quickjs-ng.wasm` file. Await initialization once and do not call `computeCustomGameSettingsSchema()` again afterward. Compile calls share upstream state: run fixture jobs serially or in separate processes rather than assuming concurrent calls are isolated.

For a repeatable result, record source/entry point, included inputs, package version and integrity, compiler language, directives, warnings, and generated output. Upstream source for this pin is commit `5a7d0e294b8cad73b9701987bb584d0551d7fa4d`. Missing tools mean **uncompiled**, not unusable: provide these steps and identify which diagnostics or generated actions still need checking.

Evidence: [pinned npm/CLI documentation](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#npm-usage), [CLI implementation](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/cli.ts), [standalone initialization](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/overpy_standalone.ts).
