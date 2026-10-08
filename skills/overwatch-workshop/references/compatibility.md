# Compatibility and source priority

<!-- wiki-source-updates:start -->

## Current wiki sources

Before using facts or values covered by these sources, read the corresponding current article. Its text takes precedence over copied details below; use this guide for the overall pattern.

- [OW2 Workshop Changes/Bugs](wiki/archive/9694.md)

<!-- wiki-source-updates:end -->

The installed Workshop.codes wiki is the trusted source of truth for Workshop runtime behavior. Its full article bodies, source dates and hash records are bundled in the [local archive](wiki/archive/index.md). Read the relevant local article; ordinary skill use needs no website access.

## Use the source appropriate to the question

1. **Runtime behavior, limits and exceptions:** follow the current bundled wiki article, including its explicit conditions, units, hero/form/button distinctions, and patched or historical labels. The article takes precedence over a derivative guide or summary in this skill.
2. **Names and syntax:** use the pinned [API catalog](api/index.md) for argument order, compiler types and OverPy spellings. Compiler metadata does not override the wiki’s runtime facts.
3. **Compiler behavior:** use the OverPy guides for the pinned compiler’s warnings, transformations, preprocessing and accepted syntax.

Use wiki claims directly when answering a question; routine use does not require asking the user to retest them. When reporting checks on newly written code, state only the checks actually performed. A compiler check should be described as a compiler check.

## Find the relevant exception

The [compatibility catalog](wiki/compatibility.md) collects focused articles. The [OW2 changes and bugs article](wiki/articles/9463.md) and its [full source](wiki/archive/9463.md) contain the current bundled registry, including conditions attached to each entry. Follow these entries when they differ from an older summary.

- For chased-variable notification and reevaluation, start with [reevaluation](reevaluation.md), then the linked wiki entry.
- For projectile ownership and resource lifetime, start with [resources](resources.md#projectile-leak-report).
- For health, ammo, cooldowns and event attribution, read [combat and heroes](combat-heroes.md) and the exact hero/API entry. Preserve read-versus-write and weapon/form distinctions.
- For category ordering, Combo defaults and import/export issues, use [match and settings](match-settings.md) with the current registry.
- For string limits, local-player visuals and screen projection, use [visuals and strings](visuals-strings.md) with the dedicated article.

If two wiki passages differ, consult the complete articles for their scope and explicit corrections. Identify the specific discrepancy rather than attaching a generic uncertainty disclaimer to unrelated facts. For example, the [string guide](wiki/archive/5734.md) explicitly removes the older total 511-byte limit while preserving the per-node distinction; native [For documentation](wiki/archive/4383.md) supplies the exclusive-stop contract even where a compiler README example differs.

## Keep explicit historical status

The [historical catalog](wiki/historical.md) retains techniques the wiki marks patched or broken. Preserve the scope and dates of those labels:

- [Base-health pool removal](wiki/archive/6790.md) is marked patched on **2025-05-07**, version 2.16.0-138051. Use normal health-pool ownership and Set Max Health for new work.
- [The Stadium workaround](wiki/archive/7385.md) is marked broken as of **2025-10-01**, with a spawn-preventing soft lock.
- [Texture sanitization](wiki/archive/6560.md) distinguishes the Season 17 issue patched **2025-08-05** from a separate bypass described through **2025-08-08**. Keep those histories separate and preserve the setup’s dummy-bot side effects.

Do not infer deprecation merely from an old edit date, an alias, or a sparse description.

## Preserve measurement context

Measured wiki data remains useful with its supplied units and conditions:

- [Projectile measurements](wiki/archive/2041.md) describe **December 2023** data; absent cells are not zero. [Projectile size](wiki/archive/8242.md) is expressed as radius, not diameter.
- [Weapon offsets](wiki/archive/9331.md) use idle animation, FOV 103 and the selected weapon/hand.
- [Health-pack positions](wiki/archive/1976.md) are keyed by mode, map, submap and size. [Payload timing](wiki/archive/1714.md) depends on speed settings.
- [Comparison tables](wiki/archive/7978.md) identify measurements from **2024-04-22**, patch 2.10.0.0.124591; preserve the listed harness values.
- [Hero colors](wiki/archive/8507.md) include ordered arrays and explicit hero keys; retain the stated ordering when using an array.

Linked media and external share codes remain source references rather than installed assets. The bundled article text and extracted tables are available locally.
