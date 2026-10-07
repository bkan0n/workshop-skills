# Group 3 corpus review: long tutorials and reference catalogs

## Coverage and confidence

All **32 assigned article bodies** were read. No source files changed and no network or media fetches were performed. Five complete 18-by-18 comparison tables were read in a compact representation preserving every visible cell. All large coordinate and asset catalogs were read as catalogs; their individual values remain in the archived originals rather than being duplicated here. An initially truncated health-pack output was followed by a complete read of the omitted range.

The ledger records article-level coverage, dispositions, source anchors, useful information and uncertainties. Every runtime claim below means **documented by the archived source, not independently verified in the game**. Source edit timestamps must not be treated as behavioral verification dates.

## What belongs near the foundation

The strongest shared runtime material is not a list of API signatures. It is the set of assumptions that can make otherwise plausible code incorrect:

1. **Rule lifetime and event concurrency.** A wait can discard damage-event retriggers. Dealt Damage scopes concurrency to the attacker; Took Damage scopes it to the victim. A hero/slot event filter can abort running actions when the player changes hero/slot. These affect correctness before performance. [6064](https://workshop.codes/wiki/articles/6064)
2. **Value context and evaluation location.** Event Player is tied to an event instance, while Local Player describes a visual's viewer. Some values are unavailable or wrong during client-side visual evaluation; the bug registry suggests mirroring Is Waiting For Players into a server-updated global variable. [1840](https://workshop.codes/wiki/articles/1840), [9463](https://workshop.codes/wiki/articles/9463)
3. **State change notification differs from value movement.** The bug registry says chased variables do not notify rule conditions or Wait Until until the destination is reached. Separately, changing any member of an array can invalidate all conditions using that variable. A timer/display changing smoothly does not imply every observer is being triggered. [9463](https://workshop.codes/wiki/articles/9463), [6064](https://workshop.codes/wiki/articles/6064)
4. **Element count and execution cost are separate budgets.** Disabled content still costs elements but is documented not to run. Array/evaluate-once/settings/localized-string element costs and top-level discounts are specialized. Startup spikes, entity limits and expensive event work require separate reasoning. [4857](https://workshop.codes/wiki/articles/4857), [6064](https://workshop.codes/wiki/articles/6064), [1840](https://workshop.codes/wiki/articles/1840)
5. **Entity ownership and lifecycle matter.** Create Projectile/Homing Projectile can reportedly leak entity slots if a non-null owner leaves or changes during flight. Visual disappearance is not proof the slot was released. [9463](https://workshop.codes/wiki/articles/9463)
6. **Workshop comparisons are not ordinary cross-type algebra.** The empirical tables contain asymmetric equality, coercive boolean equality and ordering that does not agree with equality in the usual way. This rules out casual simplifications copied from Python/JavaScript. [7978](https://workshop.codes/wiki/articles/7978)
7. **Test the actual environment.** Practice range is documented to run at about one-third normal tick rate. UI output depends on viewer language, FOV, aspect ratio, spectator context and hero animation. Passing a compiler is distinct from verifying these behaviors. [6064](https://workshop.codes/wiki/articles/6064), [5734](https://workshop.codes/wiki/articles/5734), [9496](https://workshop.codes/wiki/articles/9496)

These are candidates for a very small core checklist with direct routes to focused references. Exact hero exceptions, map coordinates and asset identifiers should not consume the default context.

## Scheduling, load and debugging

[6064](https://workshop.codes/wiki/articles/6064) supplies an unusually useful collection of operational patterns:

- Gate expensive spatial/array conditions behind cheap selective checks; conditions are documented as ordered and short-circuiting.
- Stagger player initialization rather than creating all variables/effects/texts on the same tick; the example waits `Slot Of(player) * 0.016`.
- Move a suitable expensive condition into an If inside a waited loop when reduced sampling precision is acceptable. Its 0.2-second polling example is a deliberate gameplay tradeoff, not a semantics-preserving optimization.
- Prefer built-in map/filter/sort operations over manual variable loops where equivalent, and consider the invalidation cost of large aggregate state arrays.
- Keep Inspector recording for debugging, but recognize its array-heavy overhead when measuring release load.
- Treat slow-motion anti-crash behavior as a fallback that changes gameplay. Numeric thresholds and action counts are examples, not limits guaranteed for every mode.

Several source statements should remain qualified: daily/evening load variation is anecdotal; replay snapshots as the cause of periodic spikes is explicitly speculative; the purported dynamic 0–15% slowdown formula does not obviously produce the promised range with its default settings. “Wait placement does not matter” is unsafe outside the narrow workload point because waits affect event loss and interleaving.

A useful troubleshooting reference should connect symptoms to mechanisms: startup-only failure, recurring spikes, missing multi-target damage responses, a chased timer crossing a threshold without triggering, visual disappearance with increasing Entity Count, and a large array update causing unrelated conditions to reevaluate.

## Types, state and compact native recipes

[2080](https://workshop.codes/wiki/articles/2080) documents global versus per-player storage, number/vector-only chase and matching initial/destination types. Its cooldown example contains `==` where assignment was intended and omits ready-state initialization. This is evidence for rewriting and validating complete minimal examples rather than preserving educational snippets verbatim.

[7978](https://workshop.codes/wiki/articles/7978) is deep-reference material with a short core warning. Examples worth preserving explicitly:

- False equals Null and Empty Array, but Null does not equal Empty Array.
- Empty custom string and zero vector compare equal to Null Entity in one direction but not the reverse.
- Non-null Entity is reported equal to False, Null and zero.
- True equals a positive number in equality but is less than that number in ordering.

The table categories are representative harness values, not proof all members of a type compare identically. The body says **April 22, 2024, patch 2.10.0.0.124591**, despite January 2026 metadata. It also includes a reproducibility path: mode C89J3, Inspector log-file export, configurable batch sizes, explicit result delimiters and version/date recording. This can inform later verification without promising an unperformed test.

Small recipes can share one selective reference: reverse arrays by sorting on negative Current Array Index ([4826](https://workshop.codes/wiki/articles/4826)); 1-in-N actions with Random Integer(1,N)==1 ([4823](https://workshop.codes/wiki/articles/4823)); boolean XOR/XNOR through inequality/equality ([4833](https://workshop.codes/wiki/articles/4833)). The last shortcut needs boolean operands, given the cross-type table above.

## Visual evaluation, text and localization

The corpus suggests separating **text/runtime constraints** from **advanced layout recipes**.

[5734](https://workshop.codes/wiki/articles/5734) documents per-Custom-String length 128 characters, removal of an older concatenated-string limit, four icons/textures per string, join-time costs from many strings, and whole-string font fallback when any glyph is unsupported. Blizzard Global is described as the only font consistent across languages. Encoded data stored in strings can be corrupted by language-dependent censorship chosen by the host who last edited/loaded the mode. These are structural concerns, not cosmetic tips.

HUD semantics include group centering, left/right/top layer order, negative sort order to avoid killfeed displacement, direct Null versus variable-containing-Null differences, and preserving layout while toggling headers. IWT notes include stripped trailing spaces, multiline anchoring differences between normal/progress-bar text, an empirical coordinate box, and distance-dependent scale.

The same article deliberately mixes OverPy syntax and helpers with Workshop runtime observations. OverPy should own automatic string splitting and helpers such as `spacesForString`, `strVisualLength` and `createCasedProgressBarIwt`; Workshop should own rendering/reevaluation/localization semantics. Do not duplicate the complete article in both skills.

[9496](https://workshop.codes/wiki/articles/9496) provides a decision matrix: per-player text versus one Local Player text, and first-person versus custom-camera projection. Position reevaluation and Update Every Frame are required; Evaluate Once can freeze selected coordinate expressions. Local Player saves entities but has an old spectator caveat. Start Camera removes user FOV variation but does not eliminate ability-specific FOV changes. Do Not Clip avoids map/viewmodel occlusion. Distant projection reduces sway but risks leaving world bounds. Its intro still calls progress-bar variants untested although examples were added later; confidence must be recorded per variant.

## Geometry, camera and measured data

[1903](https://workshop.codes/wiki/articles/1903) contributes Workshop-specific axes, local positive X=left/Z=forward, position transforms requiring Rotation and Translation, and camera capture selecting eye rather than foot position. Generic vector teaching can shrink substantially. Overgeneralizations such as “all global vectors are positions” and “directions are always unit length” should not survive rewriting.

[2103](https://workshop.codes/wiki/articles/2103) offers a camera movement recipe using chase plus throttle/facing vectors, and a raycast-based environment-collision variant. It lacks initialization/Start Camera lifecycle and its author disclaims remembering the rationale. Keep as an unverified recipe, not a complete ready-to-run subsystem.

[4855](https://workshop.codes/wiki/articles/4855) gives the compact projectile invariant: scale speed by k and gravity by k² to preserve the arc. Its cast/restore snippet assumes 100% defaults and omits cast timing. [2041](https://workshop.codes/wiki/articles/2041) is a measured projectile catalog with speed, gravity, cast time, world-collision radius and upward launch-direction bias delta. It is explicitly December 2023 data, contains retired abilities, and has an incomplete linear-projectile section; blanks cannot become zeros.

Catalog routing should preserve measurement conditions:

- [9331](https://workshop.codes/wiki/articles/9331): weapon offsets at idle, FOV 103, right gun for dual wield; wrong in third person and not animation-aware. Calibration harness A87YG exists.
- [1976](https://workshop.codes/wiki/articles/1976): health packs keyed by mode + map/submap + size, because Deathmatch and normal versions differ.
- [4828](https://workshop.codes/wiki/articles/4828): painted objective outlines are misleading and heights vary; exact geometry is mostly remote-image-based, with mode WNSY6 for checking.

## Compatibility, bots, persistence and historical material

[9463](https://workshop.codes/wiki/articles/9463) should become a dated exception registry, not universal statements in the core. Preserve distinctions between reading ammo, setting ammo, reading max ammo and setting max ammo; likewise charge versus cooldown, existing cooldown versus ready state, alternate forms, console bindings and control schemes. Specific examples include Illari resource inversion, Genji/Soldier false cooldown display, Lifeweaver manual-swap dependence, Kiriko cross-clip writes and Orisa heat behaving as hidden ammo. Its tables carry different dates and some labels are stale.

[1882](https://workshop.codes/wiki/articles/1882) distinguishes dummy bots from lobby AI and detects AI via temporary invalid-name forcing; this side-effect-based approach needs reconciliation with other, newer bot detection articles. [9200](https://workshop.codes/wiki/articles/9200) supplies optional difficulty damage/healing multipliers, not a default-load reference.

[1840](https://workshop.codes/wiki/articles/1840) and [2004](https://workshop.codes/wiki/articles/2004) cover text export, presets and updating existing share codes. Source text is the most durable authoring artifact; old code-expiration/UI claims need dates. The Basics article has a missing worked tutorial, so it does not itself supply a complete onboarding workflow.

[6790](https://workshop.codes/wiki/articles/6790) is explicitly patched May 7, 2025; preserve health-scaling motivation but do not promote its base-pool exploit. [7385](https://workshop.codes/wiki/articles/7385) is explicitly broken October 1, 2025 and can prevent Stadium spawning. [7418](https://workshop.codes/wiki/articles/7418) describes manually enabling perks in unsupported modes, with partial/absent progression; it is a compatibility workaround and must be reconciled with the broken Stadium context.

## Assets and site material

Asset references should remain optional catalogs with applicability metadata:

- [1993](https://workshop.codes/wiki/articles/1993): persistent Create Effect versus one-shot Play Effect, visual versus audio.
- [4864](https://workshop.codes/wiki/articles/4864): first-/third-person and friendly/enemy visibility; missing previews sometimes mean unknown or same appearance, not definite absence.
- [1730](https://workshop.codes/wiki/articles/1730): 20 kinetic effect previews; static screenshots do not describe complete animations.
- [6460](https://workshop.codes/wiki/articles/6460): icon API availability, alternate-form limitations, unavailable/passive art and documented wrong button placement. Site-renderable art is not equivalent to a valid Workshop request.
- [9562](https://workshop.codes/wiki/articles/9562): tx IDs need bracket-insertion technique, are incomplete and patch-sensitive; names/tags contain errors.
- [8507](https://workshop.codes/wiki/articles/8507): color data depends on All Heroes order; copyable array and table disagree and have different hero coverage.
- [2130](https://workshop.codes/wiki/articles/2130): default controls, with incomplete Interact alt text and incorrect platform labels; prefer actual Input Binding String when displaying controls.
- [5372](https://workshop.codes/wiki/articles/5372): website Markdown only; useful for stripping/replacing site macros during conversion, not runtime foundation content.

## Concrete rewrite/verification backlog arising from this group

1. Make source ID, edit date, behavioral test date/patch, confidence and applicability separate fields in the authoring records.
2. Validate complete examples instead of passing through pseudo-code: cooldown assignment errors (2080), batch-reset error and questionable slowdown formula (6064), malformed weapon JSON/missing End (9331), unbalanced health-pack Array (1976).
3. Resolve conflicting catalog representations before choosing canonical values: Hanzo/Symmetra/Mei colors and missing heroes (8507); Mercy staff offset and table/JSON coverage (9331).
4. Keep stable principles separate from dated hero/patch exceptions, historical techniques and measured asset/map catalogs.
5. Preserve a small set of reproducible game-test cases: event loss around waits; chase notification; array invalidation; local visual evaluation/spectators; entity cleanup on leave; cross-type comparison direction; locale/FOV-sensitive UI.
6. Treat examples, metadata labels, rendered site names, and author opinions as different evidence strengths. No amount of compression should erase the distinction.
