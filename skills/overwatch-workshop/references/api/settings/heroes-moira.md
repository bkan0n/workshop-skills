# Settings: heroes.moira

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

Hero settings require a team wrapper: `heroes.<team>.moira`. Replace `<team>` with `allTeams`, `ffa`, `team1`, `team2`. Native team labels: `allTeams` = General; `ffa` = Team FFA; `team1` = Team 1; `team2` = Team 2. The heading identifies a schema fragment, not a complete object path.

```json
{
  "values": {
    "ability1Cooldown%": {
      "en-US": "Fade Cooldown Time",
      "exclude": [
        "lucio",
        "soldier",
        "wreckingBall",
        "zenyatta"
      ],
      "values": "__percent__"
    },
    "ability2Cooldown%": {
      "en-US": "Biotic Orb Cooldown Time",
      "exclude": [
        "bastion",
        "venture",
        "zenyatta"
      ],
      "values": "__percent__"
    },
    "ability2MaxDamage%": {
      "en-US": "Biotic Orb Max Damage Scalar",
      "values": "__percent__"
    },
    "ability2MaxHealing%": {
      "en-US": "Biotic Orb Max Healing Scalar",
      "values": "__percent__"
    },
    "combatUltGen%": {
      "en-US": "Ultimate Generation - Combat Coalescence",
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
      "en-US": "Fade",
      "values": "__boolOnOff__"
    },
    "enableAbility2": {
      "en-US": "Biotic Orb",
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
    "enableInfiniteUlt": {
      "en-US": "Infinite Ultimate Duration",
      "include": [
        "ashe",
        "baptiste",
        "bastion",
        "doomfist",
        "emre",
        "genji",
        "junkrat",
        "moira",
        "soldier",
        "torbjorn",
        "widowmaker",
        "winston",
        "wreckingBall",
        "ramattra",
        "venture",
        "shion"
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
      "en-US": "Secondary Fire",
      "include": [
        "anran",
        "baptiste",
        "genji",
        "illari",
        "kiriko",
        "cassidy",
        "mei",
        "mercy",
        "moira",
        "roadhog",
        "symmetra",
        "torbjorn",
        "winston",
        "zarya",
        "zenyatta"
      ],
      "values": "__boolOnOff__"
    },
    "enableSpawningWithUlt": {
      "en-US": "Spawn With Ultimate Ready",
      "values": "__boolOnOff__"
    },
    "enableUlt": {
      "en-US": "Ultimate Ability Coalescence",
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
      "en-US": "Ultimate Generation - Passive Coalescence",
      "values": "__percent__"
    },
    "primaryFireMaximumTime%": {
      "en-US": "Biotic Energy Maximum",
      "values": "__percent__"
    },
    "primaryFireRechargeRate%": {
      "en-US": "Biotic Energy Recharge Rate",
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
    "ultDuration%": {
      "en-US": "Ultimate Duration",
      "include": [
        "ashe",
        "baptiste",
        "bastion",
        "doomfist",
        "emre",
        "genji",
        "junkrat",
        "mauga",
        "moira",
        "soldier",
        "torbjorn",
        "widowmaker",
        "winston",
        "wreckingBall",
        "ramattra",
        "venture"
      ],
      "values": "__percent__"
    },
    "ultGen%": {
      "en-US": "Ultimate Generation Coalescence",
      "values": "__percent__"
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
