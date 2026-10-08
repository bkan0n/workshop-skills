# #!optimizeForSizeAggressive

Enables aggressive optimizations for size, which may significantly lower the readability of the code (for now, replacing `if` by `skip if` in some cases and automatically compressing arrays).

**NOTE:** This directive is applied for the whole codebase and MUST be used alongside `#!optimizeForSize` for it to have an effect.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
