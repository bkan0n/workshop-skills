# Settings: gamemodes.snowballFfa

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

```json
{
  "defaultFfaPlayers": 12,
  "en-US": "Snowball Deathmatch",
  "values": {
    "disabledMaps": {
      "en-US": "disabled maps"
    },
    "enableEnemyHealthBars": {
      "en-US": "Enemy Health Bars",
      "values": "__boolOnOff__"
    },
    "enableHeroSwitching": {
      "en-US": "Allow Hero Switching",
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
    "enableRandomHeroes": {
      "en-US": "Respawn As Random Hero",
      "values": "__boolOnOff__"
    },
    "enableSkins": {
      "en-US": "Skins",
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
    "heroLimit": {
      "en-US": "Hero Limit",
      "values": {
        "1PerGame": {
          "en-US": "1 Per Game"
        },
        "1PerTeam": {
          "en-US": "1 Per Team"
        },
        "2PerGame": {
          "en-US": "2 Per Game"
        },
        "2PerTeam": {
          "en-US": "2 Per Team"
        },
        "off": {
          "en-US": "Off"
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
    "randomHeroRoleLimitPerTeam": {
      "en-US": "Random Hero Role Limit Per Team",
      "values": "__int__"
    },
    "respawnTime%": {
      "en-US": "Respawn Time Scalar",
      "values": "__percent__"
    },
    "roleLimit": {
      "en-US": "Limit Roles",
      "values": {
        "1Tank2Offense2Support": {
          "en-US": "1 Tank 2 Offense 2 Support"
        },
        "2OfEachRolePerTeam": {
          "en-US": "2 Of Each Role Per Team"
        },
        "off": {
          "en-US": "Off"
        }
      }
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
    "tankPassiveHealthBonus": {
      "en-US": "Tank Role Passive Health Bonus",
      "values": {
        "1Tank2Offense2Support": {
          "en-US": "1 Tank 2 Offense 2 Support"
        },
        "alwaysEnabled": {
          "en-US": "Always Enabled"
        },
        "disabled": {
          "en-US": "Disabled"
        }
      }
    },
    "teamOverlay": {
      "en-US": "Team Overlay",
      "values": "__boolOnOff__"
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
