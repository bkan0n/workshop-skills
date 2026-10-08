# #!define

**Warning**: This directive performs a text-based replacement! Use `macro` instead, unless absolutely necessary.

Creates a macro, like in C/C++. Macros must be defined before any code. Examples:

    #!define currentSectionWalls A
    #!define GAME_NOT_STARTED 3`

Function macros are supported as well:

    #!define getFirstAvailableMei() [player for player in getPlayers(Team.2) if not player.isFighting][0]
    #!define spawnMei(type, location)     getFirstAvailableMei().meiType = type\
    wait(0.1)\
    getFirstAvailableMei().teleport(location)\
    getFirstAvailableMei().isFighting = true

Note the usage of the backslashed lines.

JS scripts can be inserted with the special `__script__` function:

    #!define addFive(x) __script__("addfive.js")

where the `addfive.js` script contains `x+5` (no `return`).

Arguments of JS scripts are inserted automatically at the beginning (so `addFive(123)` would cause `var x = 123;` to be inserted). The script is then evaluated using `eval()`.

A `vect()` function is also inserted, so that `vect(1,2,3)` returns an object with the correct properties and `toString()` function.

When resolving the macro, the indentation on the macro call is prepended to each line of the replacement.


Editor snippet template (dollar placeholders are not source syntax):

```text
define $0
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
