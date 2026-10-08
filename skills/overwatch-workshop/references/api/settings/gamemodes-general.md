# Settings: gamemodes.general

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

```json
{
  "en-US": "General",
  "values": {
    "baseScoreForKillingBountyTarget": {
      "en-US": "Base Score for Killing a Bounty Target",
      "values": "__int__"
    },
    "bountyIncreasePerKillAsBountyTarget": {
      "en-US": "Bounty Increase per Kill as Bounty Target",
      "values": "__int__"
    },
    "captureSpeed%": {
      "en-US": "Capture Speed Modifier",
      "values": "__percent__"
    },
    "controlPointA": {
      "en-US": "Control Point A",
      "values": "__boolOnOff__"
    },
    "controlPointB": {
      "en-US": "Control Point B",
      "values": "__boolOnOff__"
    },
    "controlPointC": {
      "en-US": "Control Point C",
      "values": "__boolOnOff__"
    },
    "controlPointD": {
      "en-US": "Control Point D",
      "values": "__boolOnOff__"
    },
    "controlPointE": {
      "en-US": "Control Point E",
      "values": "__boolOnOff__"
    },
    "difficulty": {
      "en-US": "Difficulty",
      "values": {
        "expert": {
          "en-US": "EXPERT"
        },
        "hard": {
          "en-US": "HARD"
        },
        "legendary": {
          "en-US": "LEGENDARY"
        },
        "normal": {
          "en-US": "NORMAL"
        }
      }
    },
    "disabledMaps": {
      "en-US": "disabled maps"
    },
    "doorHealth%": {
      "en-US": "Door Health Scalar",
      "values": "__percent__"
    },
    "drawTime": {
      "en-US": "Draw After Match Time Elapsed With No Tiebreaker",
      "values": "__int__"
    },
    "enableBlitzFlagLocations": {
      "en-US": "Blitz Flag Locations",
      "values": "__boolOnOff__"
    },
    "enableCompetitiveRules": {
      "en-US": "Competitive Rules",
      "values": "__boolOnOff__"
    },
    "enableDropFlagOnDmg": {
      "en-US": "Damage Interrupts Flag Interaction",
      "values": "__boolOnOff__"
    },
    "enableEndless": {
      "en-US": "Endless Mode",
      "values": "__boolOnOff__"
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
    "enableMercyRezKillCancel": {
      "en-US": "Mercy Resurrect Counteracts Kills",
      "values": "__boolOnOff__"
    },
    "enablePerks": {
      "en-US": "Enable Perks",
      "values": "__boolOnOff__"
    },
    "enableRandomHeroes": {
      "en-US": "Respawn As Random Hero",
      "values": "__boolOnOff__"
    },
    "enableSelfInitiatedRespawn": {
      "en-US": "Self Initiated Respawn",
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
    "enableTrainingPartner": {
      "en-US": "Training Partner",
      "values": "__boolOnOff__"
    },
    "enableWallhack": {
      "en-US": "Reveal Heroes",
      "values": "__boolOnOff__"
    },
    "enabledMaps": {
      "en-US": "enabled maps"
    },
    "firstActiveControlPoint": {
      "en-US": "First Active Control Point",
      "values": {
        "a": {
          "en-US": "A"
        },
        "b": {
          "en-US": "B"
        },
        "c": {
          "en-US": "C"
        },
        "d": {
          "en-US": "D"
        },
        "e": {
          "en-US": "E"
        },
        "random": {
          "en-US": "Random"
        }
      }
    },
    "flagCarrierAbilities": {
      "en-US": "Flag Carrier Abilities",
      "values": {
        "all": {
          "en-US": "All"
        },
        "none": {
          "en-US": "None"
        },
        "restricted": {
          "en-US": "Restricted"
        }
      }
    },
    "flagDroppedLockTime": {
      "en-US": "Flag Dropped Lock Time",
      "values": "__float__"
    },
    "flagPickupTime": {
      "en-US": "Flag Pickup Time",
      "values": "__float__"
    },
    "flagReturnTime": {
      "en-US": "Flag Return Time",
      "values": "__float__"
    },
    "flagScoreRespawnTime": {
      "en-US": "Flag Score Respawn Time",
      "values": "__float__"
    },
    "gameLengthInMn": {
      "en-US": "Game Length In Minutes",
      "values": "__int__"
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
    "nbBountyTargets": {
      "en-US": "Bounty Target Count",
      "values": "__int__"
    },
    "needsImbalancedTeamScoreToWin": {
      "en-US": "Imbalanced Team Score To Win",
      "values": "__boolOnOff__"
    },
    "payloadSpeed%": {
      "en-US": "Payload Speed Modifier",
      "values": "__percent__"
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
    "respawnSpeedBuffDuration": {
      "en-US": "Respawn Speed Buff Duration",
      "values": "__float__"
    },
    "respawnTime%": {
      "en-US": "Respawn Time Scalar",
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
    "scorePerKill": {
      "en-US": "Score per Kill",
      "values": "__int__"
    },
    "scorePerKillAsBountyTarget": {
      "en-US": "Score per Kill as Bounty Target",
      "values": "__int__"
    },
    "scoreToWin": {
      "en-US": "Score To Win",
      "values": "__int__"
    },
    "scoringSpeed%": {
      "en-US": "Scoring Speed Modifier",
      "values": "__percent__"
    },
    "setValidControlPoints": {
      "en-US": "Limit Valid Control Points",
      "values": {
        "all": {
          "en-US": "All"
        },
        "first": {
          "en-US": "First"
        },
        "second": {
          "en-US": "Second"
        },
        "third": {
          "en-US": "Third"
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
    "spawnTrainingBots": {
      "en-US": "Spawn Training Bots",
      "values": "__boolOnOff__"
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
    "team1ScoreToWin": {
      "en-US": "Team 1 Score To Win",
      "values": "__int__"
    },
    "team2ScoreToWin": {
      "en-US": "Team 2 Score To Win",
      "values": "__int__"
    },
    "teamNeedsFlagAtBaseToScore": {
      "en-US": "Team Needs Flag At Base To Score",
      "values": "__boolOnOff__"
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
    "trainingBotsRespawnTime%": {
      "en-US": "Training Bot Respawn Time Scalar",
      "values": "__percent__"
    },
    "ts1PushSpeedModifier%": {
      "en-US": "TS-1 Push Speed Modifier",
      "values": "__percent__"
    },
    "ts1WalkSpeedModifier%": {
      "en-US": "TS-1 Walk Speed Modifier",
      "values": "__percent__"
    },
    "wallhackEnabledTime": {
      "en-US": "Reveal Heroes After Match Time Elapsed",
      "values": "__int__"
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
