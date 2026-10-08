# Shared Workshop foundation

Read this once, including when another language generates Workshop. Read deeper only for the task at hand.

## The execution model

A rule has an event, conditions, and ordered actions. **Ongoing is edge-triggered**: all conditions must become true; staying true does not repeat actions. At least one condition must become false to rearm. An unconditional Global rule initializes at server start; unconditional Each Player runs when each player loads. Event Player is the event's subject, not universally attacker, target, host, or viewer. [Ongoing events](https://workshop.codes/wiki/articles/4824), [Global](https://workshop.codes/wiki/articles/4825), [event context](https://workshop.codes/wiki/articles/1840).

Wait is a scheduling choice, not a universal fix. It changes interleaving, observation and cancellation; a wait in a damage-event handler can lose later events for its occupied context. A small bounded loop may deliberately finish immediately; indefinite repetition needs pacing. Call Subroutine waits for its callee; Start Rule runs concurrently. Both inherit event context. [Scheduling](https://workshop.codes/wiki/articles/6064), [loops](https://workshop.codes/wiki/articles/4841), [calls](https://workshop.codes/wiki/articles/6041), [starts](https://workshop.codes/wiki/articles/4455).

## State and lifetime

Choose global versus per-player storage explicitly. Array value operations normally return a copy: assign it or use a modification action. Missing values may return zero, Null, -1 or empty text, so use the API's actual contract rather than generic truthiness. Workshop cross-type comparisons have documented surprises. [Variables](https://workshop.codes/wiki/articles/2080), [append](https://workshop.codes/wiki/articles/4565), [comparisons](https://workshop.codes/wiki/articles/7978).

Distinguish captured inputs from reevaluated inputs. A changing value does not guarantee a condition receives change notification; chased-variable observers have an archived exception. Event Player is server event context; Local Player is a visual's viewer and cannot be stored. [Reevaluation](https://workshop.codes/wiki/articles/4788), [chase exception](https://workshop.codes/wiki/articles/9463), [viewer context](https://workshop.codes/wiki/articles/4807).

Creation and ongoing controls need ownership and cleanup. Save the correct Last… ID immediately, budget capacity, and retain cleanup state beyond its owner's lifetime when necessary. Player Left Match cannot read the departed player's variables. [Handles](https://workshop.codes/wiki/articles/4849), [leave](https://workshop.codes/wiki/articles/4821).

These are archived claims from snapshot **2026-09-29**, not live game verification. Compile success validates a representation; engine tests validate behavior in a particular patch/environment.

## Select a route

For a question about one named action or value, start with its exact API entry and linked evidence. Use a broader topic guide when the task crosses APIs or the narrow entry does not resolve the issue. Stop reading once the needed behavior and syntax are supported.

| Task or symptom | Read; question answered |
| --- | --- |
| Native rule, paste/import error | [Native authoring](native-authoring.md): structure and workflow |
| Fires once; repeat while held; Wait mode/timing | [Waits](waits.md): pacing, rearming and cancellation |
| Misses damage events; wrong target; subroutines | [Execution](execution.md): event scope, context and concurrent calls |
| Join/spawn/death/leave; wrong player's state | [State and lifecycle](state-lifecycle.md): initialization and ownership |
| Append did nothing; zero from missing data; comparison surprise | [Values and arrays](values-arrays.md): mutation, coercion, sentinels |
| HUD stale; all loop effects overlap; chase threshold ignored | [Reevaluation](reevaluation.md): sampled, live and notified values |
| Effect survives owner; creation fails | [Resources](resources.md): handles, budgets and cleanup |
| Raycast miss; wrong axis; movement/camera | [Geometry and movement](geometry-movement.md): coordinate roles and motion |
| Health, damage, abilities, projectiles | [Combat and heroes](combat-heroes.md): operation differences and attribution |
| Player sets, bots, spectators, hero selection | [Players and bots](players-bots.md): identity and availability |
| Scores, timers, respawn, settings, sharing | [Match and settings](match-settings.md): base-mode constraints |
| HUD, audio, text, localization, viewer-specific UI | [Visuals and strings](visuals-strings.md): presentation semantics |
| Server closes; startup spike; instrumentation | [Performance and debugging](performance-debugging.md): distinguish costs and reproduce |
| Dated bug, conflicting source, map/hero/asset data | [Compatibility](compatibility.md): evidence limits and selective catalogs |
| Exact action/value/enum or source-specific exception | [API](api/index.md), [wiki](wiki/index.md): select an entry, not the whole catalog |
