# Performance and debugging

Separate four questions: does the text parse, does the logic express the intended behavior, does the game implement that behavior in the target patch, and does the full mode fit its runtime/resource budget? A compiler acceptance result answers only part of the first question. A small successful game test does not establish performance under the intended player count.

## Diagnose the failure before optimizing

| Observation | First useful check |
| --- | --- |
| Import/parser error | Native dialect, declaration names, block End structure, supported settings/mode variant; [native authoring](native-authoring.md) |
| Ongoing rule runs once | Condition rearming versus explicit repetition; [execution](execution.md) |
| Damage totals miss targets while a rule waits | Event-instance occupation and per-attacker/per-victim scope; [execution](execution.md) |
| Delayed action uses wrong person or state | Event context, changed shared inputs and post-Wait validity; [state/lifecycle](state-lifecycle.md) |
| Following effect freezes or collapses to last loop offset | Reevaluation flags and placement of Evaluate Once; [reevaluation](reevaluation.md) |
| Chased value crosses threshold without triggering | Archived chase notification bug; use a minimal reproduction before changing scheduling |
| Objects stop appearing or count grows after departures | Capacity, stale Last Created handle, ownership/cleanup, reported projectile leak; [resources](resources.md) |
| Hero query always returns zero/Null | Read versus write support and exact hero/form/button; [combat](combat-heroes.md) |
| Server fails with many players | Simultaneous startup, high-frequency events, object counts, workload bursts, persistent leaks |

Reproduce with one feature, one subject and a visible expected state. Record the game patch, mode/map, player/bot count, trigger sequence, expected result and observed result. Add concise Inspector logs at state transitions. Use a small HUD for live state when appropriate; sending Small Message on every tick is itself a reported failure risk. Keep diagnostic instrumentation removable and avoid logging full growing arrays every tick.

## Measure three different budgets

**Element count** measures script representation, not elapsed execution. Archived counting rules charge disabled code; removing execution via `disabled` does not reclaim elements. Nested expressions and special values change the count, so a table of stock action costs is not a universal per-action formula. The element-count guide describes top-level argument discounts and nested hero-literal adjustments; use the [bundled counting reference](wiki/articles/4857.md) when exact accounting matters, and compare the compiler/game result for the actual expression tree.

**Runtime load** depends on active work, frequency, contexts and engine behavior. Disabled rules/actions/conditions are reported not to execute despite retaining element cost. Server Load is described as instance CPU load; Server Load Average and Peak cover the preceding two seconds. Near/over 100 indicates increased shutdown risk, not a deterministic safe/unsafe switch. Sample sustained behavior and bursts, and leave headroom rather than tuning to one passing reading.

**Resource counts** track objects such as effects and text, whose capacity and lifetime are separate from element count. A low-load mode can still exhaust an object pool. Track the families used, compare counts before/after repeated spawn/despawn/leave cycles, and confirm cleanup returns them to baseline. Read the exact Count value's scope; Entity Count documentation and projectile bug reports do not supply a fully reconciled universal object census.

## Reduce work while preserving semantics

1. **Keep event accounting short.** A Wait inside an occupied damage-event rule can drop later events. Copy or aggregate the information needed by a slower consumer only after deciding how bursts and ordering should work. Do not call dropped events an equivalent optimization.
2. **Gate expensive conditions.** Conditions are documented as ordered and short-circuiting. Put cheap/selective checks before costly array/spatial expressions when the result is unchanged. Hero/slot filters can reduce scope but also abort active rules on changes; review cleanup before adding them.
3. **Choose a needed update rate.** A paced loop with action-side If can reduce repeated expensive checks, at the cost of reaction delay and missed short-lived states. Define that tradeoff explicitly. Update Every Frame belongs on values whose smoothness/precision warrants it.
4. **Batch bursts.** A small bounded waitless loop is useful; a huge burst may exceed a tick's work budget. Process bounded batches and yield when simultaneous completion is unnecessary. Yield placement affects state visibility and event handling, so it is not a purely cosmetic change.
5. **Reduce redundant invalidation.** The archive reports that changing one array index can reconsider conditions observing other indices of the same variable. Separate independent hot state when useful. Prefer built-in mapped/filtered/sorted operations to manual loops when their semantics match; their relative cost is still workload-dependent.
6. **Control startup.** Initialize only when the required player/entity state exists. Stagger nonessential expensive work if many players arrive together. The tutorial's slot-based delay is an example, not a universal scheduling contract; remain correct across slot changes and late joins.
7. **Measure Inspector overhead.** Recording is reported especially expensive for array modifications. Enable it around a problem, then disable it for representative release load measurements. Do not compare instrumented and uninstrumented runs as if they were identical.

Do not optimize by converting every repeated rule into many subroutine restarts: an upstream report documents an accumulating crash with Start Rule/Restart Rule while a prior invocation waits. See the [restart hazard](execution.md#concurrent-restart-hazard).

## Validation plan for a real mode

Exercise one player, the intended maximum population, late join, death/respawn, hero/team changes, departure during active work, and repeated start/stop cycles. Check resource baselines after cleanup. Test bursts such as multi-target damage and simultaneous initialization. Repeat timing tests on the target map type: the archive reports Practice Range at approximately 20.8333 ticks/s versus 62.5 elsewhere, so a range result is not a timing contract for a normal lobby.

An archived guide proposes lowering slow motion under load as a fallback. This changes gameplay and is not guaranteed crash prevention. Its numeric thresholds and alternate formula are not validated universal settings. Reports attributing periodic spikes to replay snapshots or time-of-day traffic are hypotheses/anecdotes, not proven causes; measure your reproduction before adopting them.

When reporting results, distinguish: reviewed structure, parser/compiler acceptance with pinned version, native round-trip acceptance, and actual in-game tests with patch and observations. List unavailable checks plainly. Keep a regression case for every reproduced bug instead of upgrading an old wiki report to verified behavior because it sounds plausible.

Offline source details: [performance evidence](wiki/performance.md).

## Evidence

Snapshot **2026-09-29**, archived documentation: [server stability tutorial](https://workshop.codes/wiki/articles/6064), edited 2025-05-25; [element count](https://workshop.codes/wiki/articles/4857), 2024-11-26; [stock action costs](https://workshop.codes/wiki/articles/2112), 2024-03-16; [Server Load](https://workshop.codes/wiki/articles/4735), [Average](https://workshop.codes/wiki/articles/4736), [Peak](https://workshop.codes/wiki/articles/4737), [Disable Inspector Recording](https://workshop.codes/wiki/articles/4370), [Enable Inspector Recording](https://workshop.codes/wiki/articles/4381), [Entity Count](https://workshop.codes/wiki/articles/4806) (2024-11-26); [Small Message](https://workshop.codes/wiki/articles/9529), 2026-08-27. Performance recommendations derived from these reports remain workload- and patch-sensitive; no live-game measurements are claimed by this package.
