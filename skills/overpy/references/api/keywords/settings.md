# settings

Declares custom game settings. Must be followed by an object containing the settings, or by a string containing the path to a JSON file (it must be named 'settings.opy.json' to get the autocompletion).

The settings are parsed with OverPy's parser, meaning you can do things such as:

```
macro VERSION = "1.4.3"
macro DEBUG = false
macro CLIP_SIZE_MULTIPLIER = 2
enum HeroUltModifiers:
    ASHE = 400

settings {
    /* comment */
    "main": {
        "modeName": w"Tower Meifense",
        "description": f"Tower Meifense by Zezombye v{VERSION}",
    },
    "gamemodes": {
        "general": {
            "respawnTime%": 50 if DEBUG else 100,
        }
    },
    "heroes": {
        "allTeams": {
            "ashe": {
                "ammoClipSize%": 100 * CLIP_SIZE_MULTIPLIER,
                "ultDuration%": HeroUltModifiers.ASHE
            },
        }
    }
}
```

Note that every value has to eventually resolve to a dict/array/string/number/boolean through the optimizer (you can't do `200 * A` where `A` is a variable).

There are quite a lot of changes regarding the syntax, and it is recommended that you edit settings within Overwatch, then use the decompile command to convert to OverPy.


Editor snippet template (dollar placeholders are not source syntax):

```text
settings $0
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
