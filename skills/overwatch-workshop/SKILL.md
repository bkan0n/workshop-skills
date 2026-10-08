---
name: overwatch-workshop
description: Use when writing, explaining, or debugging native Overwatch Workshop rules, events, actions, values, custom games, or engine behavior underlying another Workshop language.
license: GPL-3.0-only
compatibility: Requires a host that can read bundled Markdown references. No compiler, network, script runner, or OverPy skill is required for ordinary use.
metadata:
  # x-release-please-start-version
  workshop-skills-version: '0.1.0'
  # x-release-please-end
---

# Overwatch Workshop

Read [the foundation](references/foundation.md) once for the current task, then only the relevant routes. This skill owns engine semantics and native authoring; it stands alone. A language compiler can change representation, but does not replace the engine model.

Use [API lookup](references/api/index.md) for exact names/signatures and [wiki evidence](references/wiki/index.md) for narrow source details. Do not infer an API from a plausible English name or import assumptions from Python/JavaScript. Normal use is offline; tools are optional.

Write the requested dialect. For native output, use [native authoring](references/native-authoring.md) and identify complete programs versus fragments. Explain the validation actually performed: compiler acceptance, archived documentation, and game testing are separate. When a dated exception affects the answer, give its source/date and a focused check. Do not label code game-verified because it compiles.

The references rewrite Workshop.codes evidence from the **2026-09-29 snapshot**; ordinary engine claims are archived documentation unless a more specific label is given. Source edits are not test dates. See [compatibility](references/compatibility.md) for conflicts and historical techniques.
