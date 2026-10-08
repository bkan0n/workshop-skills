# #!optimizeStrict

Disables some optimizations that may cause issues in extreme cases of type conversion. For example:

- A*0 can return vect(0,0,0) instead of 0
- A+0 and A*1 can return 0 if A is not a number
- A or true should return A instead of true if A is truthy

Those optimizations (and others) will be disabled so that the behavior of the gamemode will not be altered.

This directive is added by default upon decompilation. Only remove it if you are sure that your gamemode does not rely on type conversion tricks. It is recommended to use a website such as http://diffchecker.com to compare the differences in the output when enabling/disabling this directive.

This directive is effective for the current block, up until the end of the block or the next `#!disableOptimizeStrict` directive.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
