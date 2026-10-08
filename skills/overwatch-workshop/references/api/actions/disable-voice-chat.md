# Disable Voice Chat

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Disable Voice Chat(player, teamVoiceChat, matchVoiceChat, groupVoiceChat)`

Disables voice chat for one or more players until reenabled

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players who will have their text chat disabled. |
| `teamVoiceChat` | `bool` | Whether or not team voice chat will be disabled. |
| `matchVoiceChat` | `bool` | Whether or not match voice chat will be disabled. |
| `groupVoiceChat` | `bool` | Whether or not group voice chat will be disabled. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
