# Settings: lobby

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

```json
{
  "en-US": "lobby",
  "values": {
    "allowPlayersInQueue": {
      "description": {
        "en-US": "Whether to allow players in 'While you wait'."
      },
      "en-US": "Allow Players Who Are In Queue",
      "values": "__boolYesNo__"
    },
    "dataCenterPreference": {
      "en-US": "Data Center Preference",
      "values": {
        "argentina": {
          "en-US": "Argentina"
        },
        "australia": {
          "en-US": "Australia"
        },
        "australia2": {
          "en-US": "Australia 2"
        },
        "australia3": {
          "en-US": "Australia 3"
        },
        "bahrain": {
          "en-US": "Bahrain"
        },
        "bestAvailable": {
          "en-US": "Best Available"
        },
        "brazil": {
          "en-US": "Brazil"
        },
        "brazil2": {
          "en-US": "Brazil 2"
        },
        "chile": {
          "en-US": "Chile"
        },
        "chinaBeijing": {
          "en-US": "China - Beijing"
        },
        "chinaHangzhou": {
          "en-US": "China - Hangzhou"
        },
        "chinaHangzhou2": {
          "en-US": "China - Hangzhou 2"
        },
        "finland2": {
          "en-US": "Finland 2"
        },
        "france": {
          "en-US": "France"
        },
        "germany": {
          "en-US": "Germany"
        },
        "germany2": {
          "en-US": "Germany 2"
        },
        "ireland": {
          "en-US": "Ireland"
        },
        "japan": {
          "en-US": "Japan"
        },
        "japan2": {
          "en-US": "Japan 2"
        },
        "netherlands": {
          "en-US": "Netherlands"
        },
        "peru": {
          "en-US": "Peru"
        },
        "singapore": {
          "en-US": "Singapore"
        },
        "singapore2": {
          "en-US": "Singapore 2"
        },
        "southKorea": {
          "en-US": "South Korea"
        },
        "southKorea2": {
          "en-US": "South Korea 2"
        },
        "southKorea3": {
          "en-US": "South Korea 3"
        },
        "taiwan": {
          "en-US": "Taiwan"
        },
        "taiwan2": {
          "en-US": "Taiwan 2"
        },
        "usCentral": {
          "en-US": "USA - Central"
        },
        "usEast": {
          "en-US": "USA - East"
        },
        "usEast2": {
          "en-US": "USA - East 2"
        },
        "usNorthwest": {
          "en-US": "USA - Northwest"
        },
        "usSouthwest": {
          "en-US": "USA - Southwest"
        },
        "usWest": {
          "en-US": "USA - West"
        },
        "usWest2": {
          "en-US": "USA - West 2"
        }
      }
    },
    "enableMatchVoiceChat": {
      "en-US": "Match Voice Chat",
      "values": "__boolEnabled__"
    },
    "ffaSlots": {
      "en-US": "Max FFA Players",
      "values": "__int__"
    },
    "mapRotation": {
      "en-US": "Map Rotation",
      "values": {
        "afterGame": {
          "en-US": "After A Game"
        },
        "afterMirrorMatch": {
          "en-US": "After A Mirror Match"
        },
        "paused": {
          "en-US": "Paused"
        }
      }
    },
    "minimumLatencyInNs": {
      "en-US": "Minimum Latency milliseconds",
      "values": "__int__"
    },
    "pauseGameOnDisconnect": {
      "en-US": "Pause Game On Player Disconnect",
      "values": "__boolYesNo__"
    },
    "returnToLobby": {
      "en-US": "Return To Lobby",
      "values": {
        "afterGame": {
          "en-US": "After A Game"
        },
        "afterMirrorMatch": {
          "en-US": "After A Mirror Match"
        },
        "never": {
          "en-US": "Never"
        }
      }
    },
    "spectatorSlots": {
      "en-US": "Max Spectators",
      "values": "__int__"
    },
    "swapTeamsAfterMatch": {
      "en-US": "Swap Teams After Match",
      "values": "__boolYesNo__"
    },
    "team1Slots": {
      "en-US": "Max Team 1 Players",
      "values": "__int__"
    },
    "team2Slots": {
      "en-US": "Max Team 2 Players",
      "values": "__int__"
    },
    "teamBalancing": {
      "en-US": "Team Balancing",
      "values": {
        "afterGame": {
          "en-US": "After A Game"
        },
        "afterMirrorMatch": {
          "en-US": "After A Mirror Match"
        },
        "off": {
          "en-US": "Off"
        }
      }
    },
    "useExperimentalUpdate": {
      "en-US": "Use Experimental Update If Available",
      "values": "__boolYesNo__"
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
