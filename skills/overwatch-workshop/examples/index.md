# Native examples

These are complete small native Workshop rule sets, not complete lobby/settings exports. Paste into the Workshop rule editor of a suitable custom game. They are original examples based on the linked archived behavior. Compiler checks and actual game tests are separate.

| Fixture | Demonstrates | Expected observation |
| --- | --- | --- |
| [Interact counter](native-interact-counter.workshop) | Per-player initialization and ongoing-condition rearming | Holding Interact increments once; release/repress increments again; another player has independent state |
| [Held healing](native-held-healing.workshop) | Intentional repeated work with abortable waiting | While alive/held, heals immediately then repeatedly; releasing or dying ends the invocation |
| [Owned effect](native-owned-effect.workshop) | Global handle registry, expiry and departure cleanup | A sphere follows its creator, then is removed after about two seconds or departure; registry arrays shrink together |

The healing cadence uses a requested 0.250-second Wait, not a guarantee of exactly four ticks per second: normal-map tick rounding applies. Its abort path owns no persistent object requiring later cleanup. A new heal does not resurrect a dead player.

The effect example bounds its own effects at 32, below documented baseline capacity in an otherwise empty example. That is **not a general creation-success check** when integrated into a larger mode. Coordinate the whole mode's resource budget; a failed Create action and stale Last Created ID must not be registered as a successful new object. The three parallel arrays are updated together without an intervening Wait; cleanup iterates backward. A player-local ID would be insufficient after leave. This example expires on time/departure, not death; change the policy explicitly if death should also remove the effect.

Validation on **2026-10-07**: all three fixtures passed decompile/recompile checks using pinned **OverPy 9.7.17**, revision `5a7d0e294b8cad73b9701987bb584d0551d7fa4d`. The compiler emitted no warnings, but recorded expected hidden type-check diagnostics: one for the counter fixture and two for the owned-effect fixture; held healing had none. The canonical harness checks those expectations and fails on unexpected diagnostics. Complete declarations/control-flow blocks were also reviewed. Game import and behavior are **not tested**; tool acceptance does not establish either. The repository's canonical example harness retains the detailed acceptance results.

Evidence: snapshot **2026-09-29**; [ongoing player](https://workshop.codes/wiki/articles/4824), [Wait](https://workshop.codes/wiki/articles/4480), [Wait Behaviour](https://workshop.codes/wiki/articles/4854), [Heal](https://workshop.codes/wiki/articles/4386), [cleanup pattern](https://workshop.codes/wiki/articles/4849), [leave](https://workshop.codes/wiki/articles/4821), [For](https://workshop.codes/wiki/articles/4383), [Operation](https://workshop.codes/wiki/articles/1435). These sources are archived documentation, not local game-test results.
