# Match flow, custom settings and sharing

<!-- wiki-source-updates:start -->

## Current wiki sources

Before using facts or values covered by these sources, read the corresponding current article. Its text takes precedence over copied details below; use this guide for the overall pattern.

- [OW2 Workshop Changes/Bugs](wiki/archive/9694.md)

<!-- wiki-source-updates:end -->

A Workshop script runs inside a base game mode. Select that mode deliberately: objectives, team structure, score semantics, completion and respawn behavior still apply unless explicitly disabled or overridden.

## Base-mode operations

| Operation | Archived applicability |
| --- | --- |
| Declare Player Victory; Set/Modify Player Score | FFA; player score is kill count |
| Declare Team Victory; Declare Match Draw | No effect in FFA |
| Declare Round Draw | Elimination only |
| Declare Round Victory | Control and elimination |
| Set/Modify Team Score | No effect in FFA or modes without a team score |
| Start Forcing Spawn Room | Assault, hybrid and payload maps; nonexistent room falls back to normal |
| Start Game Mode | No effect if already in progress |
| Go To Assemble Heroes | Only while game is in progress |
| Restart Match | Only after match has existed for 30 seconds |

An unspecified Player Victory target can produce only “WINS!”; an unspecified Team Victory target can show DRAW with victory sound. Supply an intentional winner. Spawn rooms are zero-indexed. Prefer documented no-op diagnosis over assuming a rule failed to fire.

Disable Built-In Game Mode Completion leaves scripted completion available. Disable Scoring leaves scripted scoring available. Disable Respawning prevents automatic respawns for selected players while allowing script commands. Announcer/music suppression lasts until reenabled or match end. HUD/in-world UI suppression is another independent choice, with reported UI exceptions such as the Push robot icon.

## Time and respawns

Pause Match Time freezes the displayed match timer, **not players, objectives or progression logic**. It does not prevent the archived session-lifetime shutdown (4h30, 1h30 Practice Range). Match Time and Total Time Elapsed answer different questions; use the latter for a session-relative expiry when appropriate.

Set Match Time also affects assemble-heroes/setup phases. Set Slow Motion changes simulation for players, projectiles, effects and game-mode logic, with only up to 100% supported. Slowing the whole simulation as a load mitigation changes gameplay; it is not an invisible performance optimization.

Set Respawn Max Time applied to an already dead player affects the **next death**, not the current respawn countdown. Respawn can affect a living player and moves to spawn; Resurrect uses death position. State reset policies remain the script's responsibility.

## Workshop Settings

Using a Workshop Setting value in rules materializes the settings submenu. Use unique setting names, and group by the case-sensitive Category. Read/reuse the setting value in a purposeful initialization or live-update policy; do not confuse a lobby option with an ordinary mutable player variable.

| Setting type | Runtime value |
| --- | --- |
| Combo | Zero-based selected option index, not display text |
| Hero | Hero value |
| Integer / Real | Chosen number, inclusive minimum/maximum |
| Toggle | Boolean |

Within a category, settings use ascending sort number then alphanumerical order. The [current registry](wiki/archive/9463.md) documents alphabetical category order and a nonzero Combo default making the first choice unselectable. Follow its settings section when it differs from the older guide; use a zero default when the first Combo choice must remain selectable.

Duplicate-looking mode names can represent 5v5/6v6/LTM variants with different settings support. Numeric map suffixes can select time/variant; omitted suffix is reported to enable all variants. A settings-import error may therefore be a mode/schema mismatch rather than a rule syntax problem. The registry also reports export/import inconsistencies; consult [compatibility](compatibility.md) for the particular field instead of rewriting every settings token globally.

## Preserve and share

Keep native source text as the editable artifact. A share code snapshots the whole lobby settings configuration, excluding players/bots/AI. Before creating it, review base-mode settings, Workshop settings, debug features and datacenter preferences that would be included.

Create New Code generates a separate code. Upload to Existing Code **overwrites** its old content; choose the correct code and retain your source history. The archived PC workflow is Custom Game → Settings → Share Code → select new/existing → Continue. Importing an alphanumeric code is distinct from pasting native source text. Old code-expiration and platform UI claims are not reliable retention guarantees; see [native authoring](native-authoring.md).

Offline source details: [match/objectives](wiki/match-objectives.md) and [authoring/settings](wiki/authoring.md).

## Evidence

Wiki sources: [player victory](wiki/articles/4348.md#wiki-4348), [team victory](wiki/articles/4351.md#wiki-4351), [match draw](wiki/articles/4347.md#wiki-4347), [round draw](wiki/articles/4349.md#wiki-4349), [round victory](wiki/articles/4350.md#wiki-4350), [team score](wiki/articles/4437.md#wiki-4437), [spawn room](wiki/articles/4450.md#wiki-4450), [start](wiki/articles/4537.md#wiki-4537), [assemble](wiki/articles/4385.md#wiki-4385), [restart](wiki/articles/4539.md#wiki-4539), [completion](wiki/articles/4364.md#wiki-4364), [scoring](wiki/articles/4367.md#wiki-4367), [respawning](wiki/articles/4366.md#wiki-4366), [pause time](wiki/articles/4399.md#wiki-4399), [Set Match Time](wiki/articles/4421.md#wiki-4421), [slow motion](wiki/articles/4435.md#wiki-4435), [respawn delay](wiki/articles/4433.md#wiki-4433), [settings](wiki/articles/2168.md#wiki-2168) (2024-06-09), [OW2 registry](wiki/articles/9463.md#wiki-9463), [sharing](wiki/articles/1724.md#wiki-1724) (2022-12-02), [update code](wiki/articles/2004.md#wiki-2004), [Basics](wiki/articles/1840.md#wiki-1840) (2023-04-11).
