# Complete examples and their limits

These files are small, complete compiler inputs, not fragments to concatenate blindly. Each starts its own declarations and rules. The repository's example harness compiles them with **OverPy 9.7.17, en-US**, checks expected diagnostics and selected generated actions, and checks that packaged copies match canonical fixtures.

| Example | Demonstrates | Important boundary |
| --- | --- | --- |
| [Interact counter](../examples/interact-counter.opy) | Player storage, annotations, and one increment per activation | Rule rearming is engine behavior; a Wait is not required merely because a rule exists |
| [Collections](../examples/collections.opy) | Copy-returning filter/map/concat, mutation, and native For lowering | The stop bound follows native structured metadata; the README's inclusive-looking example conflicts with it |
| [Subroutine and member macro](../examples/subroutine.opy) | Runtime call versus parameterized source expansion | Called player context is inherited; no Python stack locals are created |
| [Selection](../examples/selection.opy) | Switch breaks and dictionary default | Switch permits fallthrough; dictionary syntax is a compiler lowering |
| [Formatted HUD](../examples/strings.opy) | `f` formatting and HUD macro defaults | A display is a resource; use shared cleanup guidance when extending this into a lifecycle feature |
| [Captured offset](../examples/captured-offset.opy) | A snapshot inside a live position expression; saved effect ID and delayed cleanup | This small player-owned example does not solve departure cleanup; use a global owner registry for that requirement |
| [Project entry point](../examples/project/main.opy) | Include, entry-point metadata, settings, and constant macros | Keep [constants](../examples/project/constants.opy) and [settings](../examples/project/mode.opy.json) alongside it |

The counter, subroutine, and string examples produce expected **hidden** `w_type_check` diagnostics for dynamic string arguments in this compiler. Their emitted warning lists are empty. These hidden diagnostics are recorded rather than presented as a perfectly warning-free result. Unexpected warnings or changed hidden diagnostics fail the repository harness.

For departure-safe resource cleanup, adapt the matched Workshop skill's [native owned-effect example](../../overwatch-workshop/examples/native-owned-effect.workshop) using the [decompilation workflow](decompilation.md). Preserve its global owner/ID registry and cleanup logic; translating syntax should not weaken lifetime guarantees.

The maintainer-only suite additionally checks an explicit `w_wait_until` warning and rejects a nonexistent function and a parameterized subroutine. Those failing inputs are not shipped here as recommended authoring examples.
