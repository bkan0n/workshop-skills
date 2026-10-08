# Settings: gamemodes.elimination

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

```json
{
  "defaultTeam1Players": 1,
  "defaultTeam2Players": 1,
  "en-US": "Elimination",
  "values": {
    "disabledMaps": {
      "en-US": "disabled maps"
    },
    "drawTime": {
      "en-US": "Draw After Match Time Elapsed With No Tiebreaker",
      "values": "__int__"
    },
    "enableEnemyHealthBars": {
      "en-US": "Enemy Health Bars",
      "values": "__boolOnOff__"
    },
    "enableKillCam": {
      "en-US": "Kill Cam",
      "values": "__boolOnOff__"
    },
    "enableKillFeed": {
      "en-US": "Kill Feed",
      "values": "__boolOnOff__"
    },
    "enablePerks": {
      "en-US": "Enable Perks",
      "values": "__boolOnOff__"
    },
    "enableSkins": {
      "en-US": "Skins",
      "values": "__boolOnOff__"
    },
    "enableTiebreaker": {
      "en-US": "Capture Objective Tiebreaker",
      "values": "__boolOnOff__"
    },
    "enableWallhack": {
      "en-US": "Reveal Heroes",
      "values": "__boolOnOff__"
    },
    "enabledMaps": {
      "en-US": "enabled maps"
    },
    "gamemodeStartTrigger": {
      "en-US": "Game Mode Start",
      "values": {
        "allSlotsFilled": {
          "en-US": "All Slots Filled"
        },
        "immediately": {
          "en-US": "Immediately"
        },
        "manual": {
          "en-US": "Manual"
        }
      }
    },
    "healthPackRespawnTime%": {
      "en-US": "Health Pack Respawn Time Scalar",
      "values": "__percent__"
    },
    "heroPoolSize": {
      "en-US": "Limited Choice Pool",
      "values": {
        "teamSize": {
          "en-US": "Team Size"
        },
        "teamSize+1": {
          "en-US": "Team Size +1"
        },
        "teamSize+2": {
          "en-US": "Team Size +2"
        },
        "teamSize+3": {
          "en-US": "Team Size +3"
        }
      }
    },
    "heroSelectionTime": {
      "en-US": "Hero Selection Time",
      "values": "__int__"
    },
    "heroesAvailable": {
      "en-US": "Hero Selection",
      "values": {
        "any": {
          "en-US": "Any"
        },
        "limited": {
          "en-US": "Limited"
        },
        "mirroredRandom": {
          "en-US": "Random Mirrored"
        },
        "random": {
          "en-US": "Random"
        }
      }
    },
    "perkEliminationCatchupLevelAmount%": {
      "en-US": "Perk Elimination Catchup Level Amount",
      "values": "__percent__"
    },
    "perkGeneration%": {
      "en-US": "Perk Generation",
      "values": "__percent__"
    },
    "restrictPreviouslyPlayedHeroes": {
      "en-US": "Restrict Previously Used Heroes",
      "values": {
        "afterRoundPlayed": {
          "en-US": "After Round Played"
        },
        "afterRoundWon": {
          "en-US": "After Round Won"
        },
        "off": {
          "en-US": "Off"
        }
      }
    },
    "scoreToWin": {
      "en-US": "Score To Win",
      "values": "__int__"
    },
    "spawnHealthPacks": {
      "en-US": "Spawn Health Packs",
      "values": {
        "disabled": {
          "en-US": "Disabled"
        },
        "enabled": {
          "en-US": "Enabled"
        },
        "modeDependent": {
          "en-US": "Determined By Mode"
        }
      }
    },
    "teamOverlay": {
      "en-US": "Team Overlay",
      "values": "__boolOnOff__"
    },
    "tiebreakerCaptureTime": {
      "en-US": "Time To Capture",
      "values": "__int__"
    },
    "tiebreakerTime": {
      "en-US": "Tiebreaker After Match Time Elapsed",
      "values": "__int__"
    },
    "wallhackEnabledTime": {
      "en-US": "Reveal Heroes After Match Time Elapsed",
      "values": "__int__"
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
