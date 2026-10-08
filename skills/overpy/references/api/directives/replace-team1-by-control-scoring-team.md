# #!replaceTeam1ByControlScoringTeam


Replaces all instances of `Team.1` by `getControlScoringTeam()`. Size optimizations must be enabled.

This directive should only be used if the gamemode cannot be played in Control.

If you want to make sure this gamemode is not mistakenly played, you can add the following rule:

```thon
rule "Integrity check":
    @Condition getControlScoringTeam() != Team.1
    print("This gamemode cannot be played!")
```


Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
