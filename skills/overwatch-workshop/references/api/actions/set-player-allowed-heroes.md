# Set Player Allowed Heroes

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Set Player Allowed Heroes(player, hero)`

Sets the list of heroes available to one or more players. If a player's current hero becomes unavailable, the player is forced to choose a different hero and respawn at an appropriate spawn location.

| Argument | Type | Meaning |
| --- | --- | --- |
| `player` | `Player \| Array<Player>` | The player or players whose hero list is being set. |
| `hero` | `Hero \| Array<Hero>` | The hero or heroes that will be available. If no heroes are provided, the action has no effect. |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
