# #!replaceEmptyStringByEmptyArray


Replaces all instances of "" (empty string) by [] (empty array). WARNING: This might break your code in some cases (eg, `.concat([])` won't work because it unrolls the array)! Only use this if you are sure that it won't cause issues in your gamemode. Size optimizations must be enabled.


Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
