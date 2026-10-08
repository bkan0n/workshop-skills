# #!translateWithPlayerVar


Stores the player's language in a variable using a rule which uses the `.startFacing()` function when the player spawns (the language is determined based on the player's facing direction).

If using translations, this can save a lot of elements. However, it will make translated strings not display correctly for spectators; you will have to wrap them with the `__` function (which behaves the same as the `_` function, except it will not use the `__languageIndex__` player variable).

If your gamemode changes the facing direction on spawn, you must modify it so that it changes it once `eventPlayer.__languageIndex__ != 1.1`.

You can specify `noDetectionRule` to not create the rule which sets the variable to the player's language, in which case you'll have to define the rule yourself; the variable must be set to the language as defined in the order specified in the `#!translations` directive, where the first language is index 1, and must be set to 1 by default if no language could be determined.

You can also specify `noTlErr` to have spectators view the default language when viewing a translated string (the `__languageIndex__` variable is now 0-indexed instead of 1-indexed). Keep in mind that, if translations aren't used properly, you may not see it if you playtest with the default language.


Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
