# Events, control flow and subroutines

## Triggering and event subjects

Ongoing conditions are rising-edge triggers, not per-frame loops. With conditions, the rule becomes eligible when all become true; at least one must become false before it can rearm. Without conditions, Global runs on server start and Each Player on each player's load. Discrete events test their conditions when the event occurs; a condition becoming true later does not recreate the missed event.

| Event family | Event Player | Other relevant context |
| --- | --- | --- |
| Dealt Damage / Dealt Knockback | Attacker | Victim, Event Ability, Event Direction; damage also amount/critical flag |
| Took Damage / Received Knockback | Victim | Attacker and corresponding event details |
| Dealt Healing | Healer | Healee, Event Healing, Event Was Health Pack, ability/direction |
| Received Healing | Healee | Healer and healing details |
| Dealt Final Blow | Final-blow attacker | Dying Victim; self-kill can make them equal |
| Died | Dying Victim | Final-blow Attacker |
| Earned Elimination | Credited player | Credited Victim; do not equate credit with final blow |
| Joined / Left | Joining/leaving player reference | Departed player data is already unavailable at Left |
| Subroutine | Inherited from caller | Inherits the caller's contextual values |

Use only values documented for the triggering event. Event Player does not become a For loop's target or a Filtered Array's Current Array Element. Event Ability has hero-specific Null/wrong-button reports: a Null result does not prove that no ability caused damage. See [combat](combat-heroes.md).

## Event occupation and cancellation

For Wait modes, tick rounding and repetition while held, read [waits](waits.md). The following concerns event accounting and invocation lifetime.

Do not add a Wait to every rule. The performance tutorial reports that an occupied damage-event invocation drops additional triggers for the same context. Dealt Damage is scoped per attacker, so one attacker hitting several victims can lose victim events while waiting. Took Damage has independent victim contexts, but changing to it is not automatically equivalent if the feature owns attacker state. Keep critical event accounting short; transfer selected work/state to a separately paced process when its loss/aggregation policy is explicit.

Hero/slot event filters are also reported to abort active actions when the selected hero/slot changes. Ignore Condition does not establish immunity to every lifecycle transition. Avoid making cleanup depend only on a delayed filtered invocation. See [state/lifecycle](state-lifecycle.md).

## Loops and subroutines

`While/End` repeats a local block. `Break` leaves its current loop; `Continue` resumes the innermost loop. For's stop is exclusive, checked before the first iteration; step sign decides when it has passed the stop. For whole-rule Loop behavior and paced repetition, see [waits](waits.md#timing-and-loops). For Player Variable uses the first supplied player only. Shared global loop indices are unsafe for independently interleaved player routines.

`Call Subroutine` pauses the caller until completion. `Start Rule` continues the caller concurrently. Both inherit context; neither supplies ordinary parameters. Start Rule's already-running policy applies to the same player/global entity: Restart Rule replaces the existing invocation and context, whereas Do Nothing preserves it. A nonexistent subroutine match is ignored. Store shared inputs carefully if a concurrent routine reads them later.

## Concurrent restart hazard

Pinned upstream OverPy documentation reports that repeatedly using Start Rule with **Restart Rule** on a subroutine whose previous invocation still has remaining Wait duration accumulates toward a server crash, even when measured load is low. It reports the accumulation as shared across subroutines, with roughly 465 restarts in its investigation. **That number is a reported failure observation, not a safe operating budget.**

Avoid a design that continually replaces waiting invocations merely to reset a timer. Prefer one long-lived paced worker that reads the latest target/deadline, or Do Nothing while the worker is active when ignoring retriggers matches the intended behavior. If each request must be retained, use an explicit queue with a defined capacity and consumer. Choose the alternative that matches the mode’s request and cancellation policy. Ordinary completion followed by a new call is distinct from replacing an invocation still waiting.

Evidence: upstream README [restart warning, lines 1155–1165](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#L1155), pinned revision inspected 2026-10-07, documented compiler warning. The separate numeric Wait Until warning is covered under [Wait Until predicates](waits.md#wait-until-predicates).

Offline source details: [execution and event evidence](wiki/execution.md).

## Evidence

Wiki sources: [ongoing player](wiki/articles/4824.md#wiki-4824), [ongoing global](wiki/articles/4825.md#wiki-4825), [damage dealer](wiki/articles/4820.md#wiki-4820), [damage receiver](wiki/articles/4819.md#wiki-4819), [healing](wiki/articles/7450.md#wiki-7450), [received healing](wiki/articles/4813.md#wiki-4813), [final blow](wiki/articles/1736.md#wiki-1736), [death](wiki/articles/4818.md#wiki-4818), [elimination credit](wiki/articles/4814.md#wiki-4814), [For](wiki/articles/4383.md#wiki-4383), [player For](wiki/articles/4384.md#wiki-4384), [Call](wiki/articles/6041.md#wiki-6041), [Start](wiki/articles/4455.md#wiki-4455), [Async Behavior](wiki/articles/4843.md#wiki-4843). Event loss and filter-abort are documented behavior from [server stability](wiki/articles/6064.md#wiki-6064), edited 2025-05-25.
