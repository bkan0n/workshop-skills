# Visuals, strings and presentation

<!-- wiki-source-updates:start -->

## Current wiki sources

Before using facts or values covered by these sources, read the corresponding current article. Its text takes precedence over copied details below; use this guide for the overall pattern.

- [OW2 Workshop Changes/Bugs](wiki/archive/9694.md)

<!-- wiki-source-updates:end -->

## Choose the presentation's lifetime and audience

Persistent effects, beams, icons, HUDs and in-world text need saved handles and explicit cleanup. Play Effect is transient; it does not use the Create Effect capacity or require destruction. Big Message and Small Message have a documented fixed four-second duration. Do not repeatedly send a message to simulate a permanent label: the Small Message article reports excessive calls removing viewers from the lobby, with no reliable safe threshold. Prefer a reevaluating HUD for persistent diagnostics. See [resources](resources.md).

Specify viewers separately from subjects. A HUD visible to all players can describe one Event Player; that does not make it personal to each viewer. Local Player can supply viewer-specific data to a shared visual, but cannot be stored in a server variable. Input Binding String also resolves the viewer's binding and cannot be stored. Keep these values in supported visual expressions. Local Player effects have the spectator and replay limitations described in the linked article.

A player-valued Position can follow that player or place text above their head. Position Of(player) is an explicit world vector whose update depends on reevaluation. Their behavior is not interchangeable for every action. For Play Effect the player position is sampled at playback; for continuing visuals read the exact position/reevaluation contract. [Reevaluation](reevaluation.md) explains how to freeze an offset while retaining a live subject.

## Strings and localization

Custom String uses positional placeholders such as `{0}`. Put changing values in those arguments instead of constructing a new persistent text object on every change. Comparisons are documented as case-sensitive. Strings use UTF-8; count characters and bytes separately when evaluating limits or serialized data.

The API article documents **128 characters per Custom String node** and a 511-byte resulting string limit. A newer tutorial retains the per-node limit but explicitly says the old total 511-byte limit was removed. Follow the newer guide’s removal of the total 511-byte limit; retain the per-node limit. Nest string nodes when necessary, and test large text and joining cost. A four-icon/texture limit is also documented, but later texture-tag workarounds complicate that claim; do not promise arbitrary rendering capacity. [Compatibility](compatibility.md) records these conflicts.

Use localized strings where their provided phrase matches the intended message; custom strings do not acquire translations automatically. The tutorial's preference against localized strings is advice, not an engine prohibition. Do not present OverPy helpers or Workshop.codes translation directives as native Workshop syntax. If custom translation is required, design and test each language path explicitly.

The strings tutorial reports censorship depending on the language of the host who last loaded/edited the code. Replaced characters can corrupt data encoded in strings, including apparent numeric output. Encoding is therefore a data-integrity design, not merely a way to save elements: round-trip the alphabet in relevant locales and retain a failure check. The source suggests nonalphanumeric alphabets, but that suggestion is not a guarantee against future filtering.

## HUD and in-world layout

| Symptom or requirement | Documented behavior and response |
| --- | --- |
| A supposedly absent header shows `0` | Direct Null/empty header hides it; a variable containing Null is reported to render as zero. Test the actual expression shape. |
| One HUD moves when another is added | Alignment and centering depend on the whole screen-location group. Test the complete HUD set and killfeed/objective UI together. |
| Right HUD moves below killfeed | Negative sort order is reported to keep it above the killfeed; higher sort orders follow lower ones within a location. |
| Text width changes with language/glyph | Unsupported glyphs can switch the entire string to a fallback font. Manual space alignment is language-sensitive. |
| Leading newline renders a square | The tutorial recommends a leading space before the newline. |
| In-world padding disappears | OW2 reportedly strips trailing spaces. A verified nonprinting terminal character can retain padding; do not blindly copy the source's mislabeled U+00AD “zero-width space,” which is a soft hyphen. |
| Multiline overlays do not align | Match anchors and line counts. Ordinary and progress-bar in-world text have different vertical anchoring/font/size behavior. |

The tutorial describes HUD left below right below top in layer order. Header, message, ordinary text and progress-bar text use different fonts; its only font claimed consistent across languages is Blizzard Global. Those details are renderer-dependent. Prefer a design that tolerates text-width changes over hand-spaced columns unless you have tested the target languages.

For in-world text, explicitly choose clipping, spectator visibility, size, viewer set and reevaluation. Progress-bar in-world text is reported larger than ordinary in-world text for the same size and bottom-anchored across added lines; ordinary text shifts with line count. A single shared anchor plus matched line counts is a useful layout strategy. Do not assume the same pixel width or height across the two families.

## Screen-anchored world text

The archived camera-plane technique projects world text using the camera's eye, forward, right and up vectors. Its screen coordinates have origin at the crosshair, **positive X right and positive Y up**; these are not Workshop's world axes. Position must reevaluate and use Update Every Frame; freeze only the intended offsets. Do Not Clip avoids geometry/viewmodel occlusion.

The guide's suggested bounds ±2.5 X and ±1.25 Y assume minimum FOV and 16:9. Its offsets/distances are tuned constants, not universal screen pixels. Distant projection reduces sway but risks world bounds. A custom camera is reported to stabilize user-configured FOV near 102.5°, while hero abilities can still change FOV. Test aspect ratios, abilities, camera transitions and map edges. The article includes both per-player and global Local Player approaches, but mixes August 2026 edits with a patch-1.59 spectator caveat and explicitly incomplete progress-bar testing. Read its [bundled screen-projection supplement](wiki/articles/9496.md) before adapting a full projection system.

## Effects, audio and outlines

Team colors are viewer-relative. Play Effect does not support Custom Color according to its API article. Generic Create Effect documentation says color does not affect sounds, but the explosion-sound reference reports Team 1/Team 2 differences and White as the loudest enemy variant. It also reports a different or absent sound when passing Event Player rather than Position Of(Event Player). Treat this as a sound-specific compatibility exception requiring audition in the target patch, not a universal color rule.

Start Forcing Player Outlines specifies viewed and viewing players separately. Its archived update table reports delayed changes: teammates may require proximity or a line-of-sight/FOV change, living enemies may not update, and dead cases differ. The rolling bug registry also reports reload/fade behavior. Account for the documented viewer/target transition rules when updating outlines.

Texture/color-tag catalogs describe available data and version-sensitive bypasses; they do not establish supported native APIs or perpetual identifiers. The historical tag setup destroys all dummy bots, so importing it wholesale can destroy unrelated state. Use [compatibility](compatibility.md) and the [wiki index](wiki/index.md) to inspect the dated technique and catalogs before proposing it.

Offline source details: [camera/UI](wiki/camera-ui.md), [text/localization](wiki/text-localization.md), and [effects/resources](wiki/effects-resources.md).

## Evidence

Wiki sources: [Create HUD Text](wiki/articles/4343.md#wiki-4343), [Create In-World Text](wiki/articles/4345.md#wiki-4345), [Create Effect](wiki/articles/4342.md#wiki-4342), [Local Player](wiki/articles/4807.md#wiki-4807), [Input Binding String](wiki/articles/4775.md#wiki-4775), [Custom String](wiki/articles/4590.md#wiki-4590) (edited 2024-11-26); [strings/HUD tips](wiki/articles/5734.md#wiki-5734), 2025-04-15; [screen projection](wiki/articles/9496.md#wiki-9496), 2026-08-20; [Big Message](wiki/articles/6037.md#wiki-6037), 2025-05-24; [Small Message](wiki/articles/9529.md#wiki-9529), 2026-08-27; [Play Effect](wiki/articles/9268.md#wiki-9268), 2026-07-10; [explosion sounds](wiki/articles/2765.md#wiki-2765), 2024-09-08; [outlines](wiki/articles/8803.md#wiki-8803), 2026-04-24; [OW2 bugs](wiki/articles/9463.md#wiki-9463); [texture/color tags](wiki/articles/6560.md#wiki-6560), source claim through 2025-08-08. Linked remote media remains outside the installed article bundle.
