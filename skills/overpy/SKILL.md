---
name: overpy
description: Write, explain, compile, decompile, and debug OverPy (.opy) programs for Overwatch Workshop. Use for OverPy syntax, projects, compiler diagnostics, and generated Workshop behavior.
license: GPL-3.0-only
compatibility: Requires the matched overwatch-workshop skill and a host that can read both skill roots. Markdown guidance works offline; compilation is optional and uses OverPy 9.7.17.
metadata:
  # x-release-please-start-version
  workshop-skills-version: '0.1.0'
  workshop-skills-requires-workshop: '0.1.0'
  # x-release-please-end
---

# OverPy

Use OverPy for the requested source language. It looks like Python but compiles to Workshop; Python libraries and runtime assumptions do not apply.

## Required reading

<!-- x-release-please-start-version -->
Resolve the `overwatch-workshop` skill from the host's skill listing or the packaged sibling [Workshop entry point](../overwatch-workshop/SKILL.md). Verify its name and `metadata.workshop-skills-version: '0.1.0'`. Read its [foundation](../overwatch-workshop/references/foundation.md) and this skill's [foundation](references/foundation.md), reusing files already read in this task. The sibling links describe the bundle layout; if the host installs roots elsewhere, resolve Workshop links against the verified Workshop root.
<!-- x-release-please-end -->

If the companion is missing or incompatible, identify the missing version/access requirement and ask for the matched bundle to be exposed. Continue supported language work while stating that shared runtime guidance is unavailable. Do not pretend the companion was read.

## Select the needed reference

For one named API, follow its entry and native-semantics link first. Open a broader guide only when needed; do not reread the shared foundation or collect unrelated references.

| Need | Read |
| --- | --- |
| Rules, declarations, expressions, or Python-looking code | [Language](references/language.md) |
| Arrays, loops, switches, dictionaries, and subroutines | [Control and collections](references/control-collections.md) |
| Multiple files, settings, installation, CLI, or API | [Project and compiler workflow](references/project-workflow.md) |
| Macros, enums, script preprocessing, generated rules | [Preprocessing](references/preprocessing.md) |
| Text formatting, localization, or translation files | [Strings and translations](references/strings-translations.md) |
| Warning, compile failure, optimization, or surprising output | [Diagnostics and transformations](references/diagnostics.md) |
| Existing Workshop text to convert | [Decompilation](references/decompilation.md) |
| Exact function, receiver, argument, enum, annotation, directive, or setting | [API index](references/api/index.md), then the relevant entry |
| Small complete source to adapt | [Examples](references/examples.md) |

Engine timing, event context, cleanup, geometry, and live values belong in Workshop's focused references. Read the relevant topic when the requested feature touches it; do not load both skills' entire reference trees.

Deliver source in the requested dialect. State whether it was actually compiled, which version/language checked it, and any remaining runtime uncertainty. When a compiler exists, inspect diagnostics and generated code for the behavior at issue. Compilation alone does not verify a live match.
