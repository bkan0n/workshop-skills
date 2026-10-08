# LosCheck

The built-in `LosCheck` enum.


| Native English choice | OverPy symbol | Note |
| --- | --- | --- |
| `Off` | `LosCheck.OFF` | Line of sight is never blocked, allowing results through walls. |
| `Surfaces` | `LosCheck.SURFACES` | Line of sight is blocked by ceilings, walls, floors, platforms, and any fixed object that blocks projectiles. |
| `Surfaces And All Barriers` | `LosCheck.SURFACES_AND_ALL_BARRIERS` | Line of sight is blocked by ceilings, walls, floors, platforms, any fixed object that blocks projectiles, and all barriers. |
| `Surfaces And Enemy Barriers` | `LosCheck.SURFACES_AND_ENEMY_BARRIERS` | Line of sight is blocked by ceilings, walls, floors, platforms, any fixed object that blocks projectiles, and barriers created by the enemy team. |

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
