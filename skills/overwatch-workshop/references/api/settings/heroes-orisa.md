# Settings: heroes.orisa

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

Hero settings require a team wrapper: `heroes.<team>.orisa`. Replace `<team>` with `allTeams`, `ffa`, `team1`, `team2`. Native team labels: `allTeams` = General; `ffa` = Team FFA; `team1` = Team 1; `team2` = Team 2. The heading identifies a schema fragment, not a complete object path.

```json
{
  "values": {
    "ability1Cooldown%": {
      "en-US": "Fortify Cooldown Time",
      "exclude": [
        "lucio",
        "soldier",
        "wreckingBall",
        "zenyatta"
      ],
      "values": "__percent__"
    },
    "ability2Cooldown%": {
      "en-US": "Javelin Spin Cooldown Time",
      "exclude": [
        "bastion",
        "venture",
        "zenyatta"
      ],
      "values": "__percent__"
    },
    "ammoClipSize%": {
      "en-US": "Ammunition Clip Size Scalar",
      "exclude": [
        "brigitte",
        "dva",
        "hanzo",
        "freja",
        "hazard",
        "kiriko",
        "moira",
        "reinhardt",
        "sigma"
      ],
      "values": "__percent__"
    },
    "combatUltGen%": {
      "en-US": "Ultimate Generation - Combat Terra Surge",
      "values": "__percent__"
    },
    "damageDealt%": {
      "en-US": "Damage Dealt",
      "values": "__percent__"
    },
    "damageReceived%": {
      "en-US": "Damage Received",
      "values": "__percent__"
    },
    "enableAbility1": {
      "en-US": "Fortify",
      "values": "__boolOnOff__"
    },
    "enableAbility2": {
      "en-US": "Javelin Spin",
      "exclude": [
        "bastion",
        "venture"
      ],
      "values": "__boolOnOff__"
    },
    "enableHeadshotsOnly": {
      "en-US": "Receive Headshots Only",
      "values": "__boolOnOff__"
    },
    "enableInfiniteAmmo": {
      "en-US": "No Ammunition Requirement",
      "exclude": [
        "brigitte",
        "dva",
        "freja",
        "hazard",
        "hanzo",
        "kiriko",
        "moira",
        "reinhardt",
        "sojourn",
        "sigma"
      ],
      "values": "__boolOnOff__"
    },
    "enableMelee": {
      "en-US": "Quick Melee",
      "values": "__boolOnOff__"
    },
    "enablePrimaryFire": {
      "en-US": "Primary Fire",
      "exclude": [
        "mauga"
      ],
      "values": "__boolOnOff__"
    },
    "enableRolePassive": {
      "en-US": "Role Passives",
      "values": "__boolOnOff__"
    },
    "enableSecondaryFire": {
      "en-US": "Energy Javelin",
      "include": [
        "bastion",
        "brigitte",
        "dmon",
        "domina",
        "dva",
        "doomfist",
        "echo",
        "freja",
        "hazard",
        "junkerQueen",
        "lucio",
        "mauga",
        "mizuki",
        "orisa",
        "pharah",
        "reinhardt",
        "sierra",
        "sigma",
        "sojourn",
        "soldier",
        "sombra",
        "vendetta",
        "wreckingBall",
        "ramattra",
        "lifeweaver",
        "venture",
        "juno"
      ],
      "values": "__boolOnOff__"
    },
    "enableSpawningWithUlt": {
      "en-US": "Spawn With Ultimate Ready",
      "values": "__boolOnOff__"
    },
    "enableUlt": {
      "en-US": "Ultimate Ability Terra Surge",
      "values": "__boolOnOff__"
    },
    "healingDealt%": {
      "en-US": "Healing Dealt",
      "values": "__percent__"
    },
    "healingReceived%": {
      "en-US": "Healing Received",
      "values": "__percent__"
    },
    "health%": {
      "en-US": "Health",
      "values": "__percent__"
    },
    "jumpVerticalSpeed%": {
      "en-US": "Jump Vertical Speed",
      "values": "__percent__"
    },
    "movementGravity%": {
      "en-US": "Movement Gravity",
      "values": "__percent__"
    },
    "movementSpeed%": {
      "en-US": "Movement Speed",
      "values": "__percent__"
    },
    "passiveHealthRegen": {
      "en-US": "Passive Health Regeneration",
      "values": "__boolOnOff__"
    },
    "passiveUltGen%": {
      "en-US": "Ultimate Generation - Passive Terra Surge",
      "values": "__percent__"
    },
    "projectileGravity%": {
      "en-US": "Projectile Gravity",
      "exclude": [
        "ana",
        "bastion",
        "brigitte",
        "dva",
        "doomfist",
        "echo",
        "freja",
        "genji",
        "hazard",
        "kiriko",
        "lucio",
        "cassidy",
        "mercy",
        "moira",
        "pharah",
        "reaper",
        "reinhardt",
        "roadhog",
        "sojourn",
        "soldier",
        "symmetra",
        "venture",
        "winston",
        "zenyatta",
        "juno",
        "hazard"
      ],
      "values": "__percent__"
    },
    "projectileSpeed%": {
      "en-US": "Projectile Speed",
      "exclude": [
        "brigitte",
        "reaper",
        "winston"
      ],
      "values": "__percent__"
    },
    "secondaryFireCooldown%": {
      "en-US": "Energy Javelin Cooldown Time",
      "include": [
        "bastion",
        "brigitte",
        "doomfist",
        "domina",
        "echo",
        "freja",
        "lucio",
        "mizuki",
        "orisa",
        "pharah",
        "reinhardt",
        "sierra",
        "sigma",
        "soldier",
        "sombra",
        "wreckingBall",
        "ramattra",
        "lifeweaver",
        "venture",
        "juno",
        "shion"
      ],
      "values": "__percent__"
    },
    "ultGen%": {
      "en-US": "Ultimate Generation Terra Surge",
      "values": "__percent__"
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
