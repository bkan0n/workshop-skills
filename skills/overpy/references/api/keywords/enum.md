# enum

Declares an enum. For example:
```c
enum GameStatus:
    GAME_NOT_STARTED,
    GAME_IN_PROGRESS = 3,
    GAME_STARTED

enum Team:
    HUMANS = Team.2,
    ZOMBIES = Team.1
```

The enum can then be accessed like other enums: `GameStatus.GAME_STARTED`.

If no value is specified, the value is the last specified value plus 1 (if the last specified value is a number), or 0 if it is the first enum member.

An enum can also be used as a type, such as `enum["Value 1", "Value 2"]`.


Editor snippet template (dollar placeholders are not source syntax):

```text
enum $0
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
