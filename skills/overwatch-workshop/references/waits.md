# Waits, timing and paced repetition

An ongoing rule fires when all conditions become true; remaining true does not repeat it. At least one condition must become false before rearming. For once per press, use [the interact counter](../examples/native-interact-counter.workshop). For repeated work while held/alive, adapt [held healing](../examples/native-held-healing.workshop): perform the work, Wait, then Loop If Condition Is True. These are complete native fixtures; [validation status](../examples/index.md) is separate from game verification.

## Choose cancellation deliberately

| Wait mode | Documented behavior | Use with care |
| --- | --- | --- |
| Ignore Condition | Continues despite rule-condition changes | Cleanup may remain reachable, but owner/filter lifetime still matters. |
| Abort When False | Aborts when any rule condition becomes false | Appropriate when ending now cannot skip required cleanup. |
| Restart When True | Restarts at the first action on false→true condition transition, or a repeated event with true conditions | Initialization and created resources must tolerate restarting. |

For held repetition, include the actual held/alive requirements in the rule's conditions. Abort When False stops promptly when either fails; looping while conditions remain true enables repetition. If the loop owns an effect, modifier or held input, aborting can skip its trailing Stop/Destroy. Give that resource a separately reachable [cleanup path](resources.md) instead. Ignore Condition is not immunity to every lifecycle transition: hero/slot filters can abort actions when the selection changes.

A Wait yields the current action list. Other rules/state can change before it resumes. Recheck current state afterward where needed; explicitly save a snapshot when the original value is required. Do not add a Wait to every rule: occupied damage-event contexts can lose retriggers. Read [event scope](execution.md) if every hit must be counted.

## Timing and loops

`Wait(0, …)` is not a no-op. The archive documents ordinary-map minimum **0.016 seconds**, with durations rounded upward to 16 ms multiples: `0.030→0.032`, `0.1→0.112`, `0.250→0.256`. A requested 0.250-second interval is therefore not an exact four-updates-per-second guarantee. Practice Range is reported at roughly one-third the normal tick rate; test on the intended map/environment.

`Loop` restarts the whole action list and requires a Wait to have executed since the start. `Loop If` uses its own predicate; `Loop If Condition Is True/False` checks the rule's conditions. A small bounded loop can deliberately finish without a Wait; indefinite repetition needs pacing. Use [execution](execution.md) for block loops and subroutines, not merely to choose a delay.

## Wait Until predicates

Wait Until continues when its predicate is true **or its timeout expires**, independently of the rule's conditions, and can complete in zero ticks. Check the predicate afterward if proceeding requires success rather than timeout. It is not guaranteed ordinary polling: the archive reports chased variables not notifying conditions/Wait Until until the destination is reached. See [reevaluation](reevaluation.md) when observing a chase.

Pinned upstream documentation also reports a numeric Wait Until expression differing from an explicit Boolean comparison. Express the intended numeric requirement (`value > threshold` or `value != 0`, predicate fragments) rather than relying on implicit truthiness; preserve Boolean flags as Booleans. This does not prove every numeric predicate fails in every observer.

## Evidence

Archived snapshot **2026-09-29**: [ongoing player](https://workshop.codes/wiki/articles/4824), [Wait](https://workshop.codes/wiki/articles/4480), [Wait Behaviour](https://workshop.codes/wiki/articles/4854), [loops](https://workshop.codes/wiki/articles/4841), [Wait Until](https://workshop.codes/wiki/articles/9298), edited 2026-07-16. Filter-abort/event-loss/tick-rate reports: [stability guide](https://workshop.codes/wiki/articles/6064), 2025-05-25; chase observation: [OW2 bugs](https://workshop.codes/wiki/articles/9463), 2026-08-13. Numeric predicate report: [pinned upstream warning](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#L1167), inspected 2026-10-07. All are documentation evidence, **not independently game-verified**. Offline details: [execution sources](wiki/execution.md).
