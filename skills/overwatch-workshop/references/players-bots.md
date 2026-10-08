# Players, bots, spectators and hero availability

## Player selection

Select the population the feature really needs: all/living/dead players, a team, a hero, a radius, or an explicitly filtered array. Sorting by distance alone does not make targets eligible. A player's current team/hero/slot is mutable. Team All means both teams in team modes and the single player population in FFA; Opposite Team and Team Of can have special All behavior there. Slot numbers are per-team versus a shared FFA range. Older 0–5/team and 0–11/FFA numbers are dated capacity evidence, not proof of every current lobby configuration.

Many actions accept a player array, but API behavior differs: ordinary setters apply to every supplied player; For Player Variable uses only the first. Host Player can change when the host leaves. Event Player is the event subject; Local Player is a visual viewer. See [execution](execution.md), [state/lifecycle](state-lifecycle.md), and [API lookup](api/index.md).

## Dummy bots versus lobby AI

Create Dummy Bot creates a player-like bot that moves/fires/uses abilities only through Workshop actions. It is not the same as lobby AI. The specified slot must be free; -1 selects first available. Team All is for FFA, explicit teams for team modes. A supplied hero array chooses a random hero. Archived baseline capacity is six per team/twelve FFA independent of lobby settings; extensions add capacity, so consult [resources](resources.md) and [match/settings](match-settings.md).

Is Dummy Bot identifies dummy bots. False does **not** establish a human because lobby AI is separate. Archived AI-detection tutorials temporarily force a special name, inspect the stringified player name, then restore it; one waits 0.25 s before assigning human status. This is a side-effect workaround with ordering assumptions, not a dedicated AI predicate. Do not introduce it into ordinary player selection without a need, and do not destroy all bots to initialize an unrelated feature.

Allow time for a dummy to spawn before forcing its name. Move Player To Team and Remove Player are documented not to work on dummy bots; use dummy-specific destruction. Communicate reportedly stopped working on bots, with no patch/subtype details supplied. If the task needs it, reproduce the exact bot kind and communication first. Bot stats and AI difficulty tables also have scope/version restrictions; do not infer them from human-player behavior.

## Spectator input and presentation

A spectator host's input can be read with Is Button Held(Host Player, …). Other spectators' input is described through Local Player **inside visual-element fields**, with Not(Entity Exists(Local Player)) used as a spectator check. This is not a general server-side spectator input channel.

| Spectator action | Workshop button reported |
| --- | --- |
| Move Down / Move Up | Ability 1 / Interact |
| Move Fast / Move Slow | Secondary Fire / Primary Fire |
| Spectate Lock On | Ability 2 |
| Modify FOV | Jump |
| Disable Camera Blending | Ultimate |

Crouch/Reload/Melee mappings are unspecified. Local Player HUDs have archived spectator/replay limitations, and death spectating a player's HUD is a separate setting. Apply the documented observer-specific limits; host and spectator views differ. Use actual Input Binding String for user-facing bindings where supported, rather than hardcoded keyboard labels.

## Hero selection and spawn transitions

Set Player Allowed Heroes forces selection/respawn if the current hero becomes unavailable. Supplying **no heroes has no effect**. Reset Player Hero Availability restores the lobby's list. The recipe “temporarily remove current hero, then reset” can send a player to selection, but fails to establish that outcome if removal makes an empty allowed list. Handle single-hero modes separately and consider forced-hero state.

Start Forcing Player To Be Hero may respawn immediately **in place** and restricts availability until stopped. Stop Forcing Player To Be Hero does not respawn; choices are restored next time selection opens. Respawn and Resurrect have different placement and life-state behavior; see [combat](combat-heroes.md).

Offline source details: [players and bots](wiki/players-bots.md).

## Evidence

Wiki sources: [Team](wiki/articles/1440.md#wiki-1440), [Team Of](wiki/articles/4750.md#wiki-4750), [Opposite Team](wiki/articles/4710.md#wiki-4710), [Slots](wiki/articles/4740.md#wiki-4740), [player For](wiki/articles/4384.md#wiki-4384), [dummy creation](wiki/articles/4341.md#wiki-4341), [AI distinction](wiki/articles/7945.md#wiki-7945), [older AI detection](wiki/articles/1882.md#wiki-1882), [dummy naming](wiki/articles/4542.md#wiki-4542), [team move](wiki/articles/4540.md#wiki-4540), [Remove Player](wiki/articles/4541.md#wiki-4541), [Communicate](wiki/articles/6032.md#wiki-6032) (2025-05-24), [spectator input](wiki/articles/4830.md#wiki-4830), [Local Player](wiki/articles/4807.md#wiki-4807), [bindings](wiki/articles/4775.md#wiki-4775), [allowed heroes](wiki/articles/4426.md#wiki-4426), [selection recipe](wiki/articles/4856.md#wiki-4856), [forced hero](wiki/articles/4448.md#wiki-4448), [stop force](wiki/articles/4469.md#wiki-4469).
