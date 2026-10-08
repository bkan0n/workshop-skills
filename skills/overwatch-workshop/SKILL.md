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

When choosing functions for a feature, start with [functions by task](references/api/usage/index.md), select one relevant group, then open only the exact entries needed. For a known name, use [API lookup](references/api/index.md). Do not load all function groups or the full catalog into context.

Use [wiki articles](references/wiki/index.md) for narrow source details and the [full local archive](references/wiki/archive/index.md) for original article text. Every article body is installed; a known article ID opens `references/wiki/archive/<id>.md` directly. Read the local files instead of visiting or scraping Workshop.codes. Original URLs inside quoted source are attribution, not retrieval instructions. Source refresh is a maintainer release task, not part of using this skill. Do not infer an API from a plausible English name or import assumptions from Python/JavaScript.

Write the requested dialect. For native output, use [native authoring](references/native-authoring.md) and identify complete programs versus fragments. Use the wiki’s behavior directly, preserving explicit prerequisites and historical or patched labels. When reporting checks on newly written code, state the checks actually performed.

The installed Workshop.codes wiki is the trusted source of truth for runtime behavior. Its current local articles take precedence over derivative guides and summaries. The pinned compiler catalog supplies names and syntax. Do not routinely ask the user to retest wiki claims. See [compatibility](references/compatibility.md) for source priority and historical techniques.
