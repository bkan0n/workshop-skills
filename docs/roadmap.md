# Companion skills and verification roadmap

These are future scopes, not installed or advertised skills. The initial Workshop and OverPy foundations already retain the engine facts and small examples that larger systems use.

## Workshop.codes web editor

Purpose: author and debug programs in the Workshop.codes web editor, including its own preprocessing and workflow.

Dependency: the Workshop runtime foundation. OverPy is a different authoring language and does not supply this editor's grammar.

Future material includes mixins, parameters/defaults, `@include`, `@contents`, editor-specific `@if`, `@for`, and `@each`, and inspection of their generated native output. Start with local archived articles [1876](../skills/overwatch-workshop/references/wiki/archive/1876.md) and [2082](../skills/overwatch-workshop/references/wiki/archive/2082.md), preserving incomplete-documentation flags. A future design should define actual editor operations, representative tasks, and validation before this becomes a discoverable skill.

The wiki API is maintainer source tooling and is not part of this editor skill. Use the documented API for source retrieval, never website scraping.

## Complex-system companions

Purpose: design, integrate, and debug substantial modes and interacting systems.

Dependencies: Workshop; OverPy when it is the authoring language. Candidate scopes are mode/state-machine architecture, boss and combat systems, larger UI/state flows, deeper performance diagnosis, and appropriately sourced pathfinding or compression. Each should have its own concrete task examples and evaluation cases before it becomes a skill. Keep shared engine explanations in Workshop.

## Verification improvements

- Add focused in-game reproductions for uncertain timing, notification, geometry, resource cleanup, and hero exceptions. Record game patch, test date, setup, observation, and scope.
- Resolve conflicting examples by evidence rather than source edit dates.
- Extend controlled agent evaluations with real authoring/debugging tasks and compare quality plus the reference context read.
- Review source changes from the API/compiler diff queues, keeping historical evidence while clearly identifying superseded behavior.

No in-game test or future companion is claimed complete by these stubs.
