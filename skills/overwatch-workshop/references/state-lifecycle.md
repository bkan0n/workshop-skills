# State, initialization and player lifecycle

A global variable has one game-wide instance. A player variable has a separate instance for each player. Choose ownership from the feature: a team's score, shared queue or resource registry belongs globally; an individual cooldown or selection usually belongs to the player. Do not put independently interleaved player loop indices in one global variable.

## Initialization is a lifecycle choice

Unconditional Ongoing Global initializes at server start; unconditional Ongoing Each Player runs as each player loads. Joining, loading, selecting a hero, spawning, being alive, dying and leaving are distinct transitions. Has Spawned is documented false before hero selection. A condition using it is not a substitute for a documented “every respawn” event. Gate hero-dependent work on the actual required state, and decide which values persist across death versus reset.

Initialize arrays as arrays, counters as numbers, and chased positions as vectors. A chase cannot safely begin with a scalar where its destination is a vector. If other rules depend on several initial assignments, publish an explicit ready flag after them and gate those rules on it. This is a design pattern, not a claim that textual rule order alone makes arbitrary concurrent startup safe.

## Reset and cleanup matrix

| Transition | Decide explicitly |
| --- | --- |
| Death | Should a cooldown continue? Should movement/input/visual ownership end? |
| Hero change or forced hero | Which ability-specific state is invalid? Can an event filter abort pending actions? |
| Team/slot change | Which team registry, UI audience, score and event filter need refreshing? |
| Leave | Where can cleanup still find the IDs after player variables vanish? |
| Match phase/restart | Which base-mode settings and shared state must be reinitialized? |

Player Left Match retains a triggering reference but the archive says the player's variables and other information are **already unavailable**. Store handles and enough ownership data in a global registry before departure if cleanup must survive it. For long-lived objects, do not rely exclusively on `Wait; Destroy(Event Player.savedId)` in a player rule. An entity-existence check plus global ownership record can drive a separate cleanup rule. The [owned effect example](../examples/native-owned-effect.workshop) demonstrates that pattern with global arrays and expiry.

A player reference is not a permanent account identity. Host Player may change when the host leaves. Slot numbering is team-relative in team modes and shared in FFA; a slot alone can be ambiguous without its team and lifecycle. Recompute dynamic audiences or use action reevaluation when the UI should track current players.

## Persistent controls are state too

Forced facing/position/throttle, held buttons, forced hero availability, camera, scaling, statuses and modifiers survive their start action. Associate each start with an end condition and owner. On cancellation, ensure the relevant Stop/Clear action still has a route to execute. If several features can modify the same property, use a coordinator or explicitly defined precedence; blindly restoring 100% or stopping all modifiers can overwrite another feature's intent.

Stopping a chase retains its current value. Stopping forced position resumes movement there. Stopping forced hero restores choices the next time hero select opens, without itself respawning. These are different reset semantics, not universal “undo to prior value” behavior.

Offline source details: [state/array evidence](wiki/state-arrays.md) and [player lifecycle](wiki/players-bots.md).

## Evidence

Archived documentation, snapshot **2026-09-29**: [variables](https://workshop.codes/wiki/articles/2080) (2024-01-28), [ongoing player](https://workshop.codes/wiki/articles/4824), [ongoing global](https://workshop.codes/wiki/articles/4825), [Has Spawned](https://workshop.codes/wiki/articles/4616), [Player Left Match](https://workshop.codes/wiki/articles/4821), [Host Player](https://workshop.codes/wiki/articles/4631), [slots](https://workshop.codes/wiki/articles/4740), [stop chase](https://workshop.codes/wiki/articles/4464), [stop forced position](https://workshop.codes/wiki/articles/4470), [stop forced hero](https://workshop.codes/wiki/articles/4469). Filter cancellation is reported by [server stability](https://workshop.codes/wiki/articles/6064) (2025-05-25), not game-tested here. Ownership/coordinator advice is a conservative engineering pattern derived from these lifecycle constraints.
