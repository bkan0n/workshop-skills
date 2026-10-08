# Reevaluation and observation

<!-- wiki-source-updates:start -->

## Current wiki sources

Before using facts or values covered by these sources, read the corresponding current article. Its text takes precedence over copied details below; use this guide for the overall pattern.

- [OW2 Workshop Changes/Bugs](wiki/archive/9694.md)

<!-- wiki-source-updates:end -->

A parameter expression can be sampled when an action starts, reevaluated later, or evaluated for each viewer. These are separate choices. Do not assume that changing a variable automatically updates every action that once used it.

## Decide what should remain live

| Mechanism | What it controls | Common mistake |
| --- | --- | --- |
| Action's Reevaluation setting | Which supported inputs are repeatedly read | Expecting an unselected input to change, or assuming every input is included |
| Evaluate Once(expression) | Captures that subexpression's first value for that action/condition | Freezing the entire player-following position when only a loop offset should be fixed |
| Update Every Frame(expression) | Raises observation/update frequency | Treating frequency as mutation, or applying it broadly without measuring cost |
| A stored variable | Captures the value assigned at that time | Expecting an earlier assigned position to remain attached to the player |
| Local Player | Supplies the current visual viewer | Storing it in a server variable or using it as general server event context |

For example, each effect in a creation loop may need a fixed per-iteration offset but a live player position. Freeze the offset with Evaluate Once while leaving Position Of(player) live and enabling the effect's position reevaluation. If the loop index remains live, every effect can later converge to the final index. If the whole expression is frozen, the effect stops following the player.

## Action-specific contracts

- Effects, beams, icons, HUD and in-world text expose different reevaluation enums. Read the exact entry before promising that color, string, visibility, radius or position updates.
- Start Camera's eye/look-at positions continuously reevaluate. Its blend speed of zero changes position instantly.
- Start Transforming Throttle's axis scalars and relative direction continuously update. Start Throttle In Direction instead has selectable direction/magnitude reevaluation.
- Start Forcing Player Position can reevaluate Position every frame, but **Player is not reevaluated**. Changing a variable used as Player does not retarget the already-running force.
- Chases support only numbers/vectors and require the existing variable to match the destination's type before starting. Rate-based and duration-based chases have their own input selections. Stopping leaves the current value.
- A health pool's Max Health reevaluates only if both Recoverable and Reevaluation are true. A nonrecoverable pool shrinks/disappears as damaged.

## Value changes are not always notifications

The rolling OW2 bug registry reports that a chased variable does not notify rule conditions or Wait Until until it reaches the destination. An endlessly moving destination may therefore prevent a threshold observer from firing even while the displayed number crosses it.

For a correctness-critical threshold, do not rely solely on a chased-variable condition. Use a separately paced rule that explicitly reads the value in an action-side If, and define the maximum acceptable detection delay. Wait Until relies on notification; Update Every Frame changes update frequency rather than supplying a separate threshold observer.

Separately, the performance tutorial reports that changing one array member invalidates conditions referring to other members of the same variable. Splitting unrelated high-frequency state can reduce unnecessary reconsideration; it also changes the state model, so retain coordinated updates where they are needed.

## Keep loop counters separate from chased state

Pinned upstream documentation reports that using a chased variable as a For counter can make the loop fail, even if the rule containing the Chase is disabled. Use a dedicated counter that is never referenced by a Chase; snapshot the chased value into a separate variable when the loop needs a stable bound. Do not assume disabling runtime execution removes this interaction.

Evidence: [upstream warning, lines 1138–1153](https://github.com/Zezombye/overpy/blob/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/README.md#L1138), revision **5a7d0e294b8cad73b9701987bb584d0551d7fa4d**, inspected 2026-10-07. For numeric Wait Until predicates, also see the [Wait Until caveat](waits.md#wait-until-predicates).

## Server versus visual evaluation

One global HUD using Local Player can render different values for each viewer and save text objects. Local Player and Input Binding String cannot be stored. Spectator/replay behavior has archived limitations. The bug registry reports Is Waiting For Players as false during visual/client evaluation and suggests mirroring it into a server-updated global variable. Such mirroring is an explicit snapshot/update process, not a different spelling of the original value.

Update Every Frame is reported to move some logical updates from 12.5 Hz to 62.5 Hz and visual updates toward client frame rate. Use it where smoothness/precision matters, then measure server and client cost separately. See [visuals](visuals-strings.md) and [performance](performance-debugging.md).

Offline source details: [execution](wiki/execution.md), [camera/UI](wiki/camera-ui.md), and [compatibility evidence](wiki/compatibility.md).

## Evidence

Wiki sources: [Evaluate Once](wiki/articles/4788.md#wiki-4788), [Update Every Frame](wiki/articles/4789.md#wiki-4789), [Local Player](wiki/articles/4807.md#wiki-4807), [Input Binding String](wiki/articles/4775.md#wiki-4775) (all edited 2024-11-26), [forced position](wiki/articles/4449.md#wiki-4449), [camera](wiki/articles/7648.md#wiki-7648) (2025-12-01), [throttle transform](wiki/articles/4457.md#wiki-4457), [rate chase](wiki/articles/6027.md#wiki-6027), [duration chase](wiki/articles/4336.md#wiki-4336), [health pools](wiki/articles/6164.md#wiki-6164) (2025-06-14). Notification/client-value exceptions: [OW2 changes/bugs](wiki/articles/9463.md#wiki-9463). Array invalidation: [stability guide](wiki/articles/6064.md#wiki-6064), edited 2025-05-25.
