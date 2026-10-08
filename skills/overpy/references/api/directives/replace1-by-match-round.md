# #!replace1ByMatchRound


Replaces all instances of 1 by `getMatchRound()`, if replacement by `true` is impossible. Size optimizations must be enabled.

This directive should only be used if the gamemode cannot be played in Assault, Hybrid, Escort (with the competitive ruleset) or Control.

If you want to make sure these gamemodes are not mistakenly played, you can add the following rule:

```thon
rule "Integrity check":
    @Condition getMatchRound() > 1
    print("This gamemode cannot be played!")
```


Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
