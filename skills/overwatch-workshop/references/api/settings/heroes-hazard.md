# Settings: heroes.hazard

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

Hero settings require a team wrapper: `heroes.<team>.hazard`. Replace `<team>` with `allTeams`, `ffa`, `team1`, `team2`. Native team labels: `allTeams` = General; `ffa` = Team FFA; `team1` = Team 1; `team2` = Team 2. The heading identifies a schema fragment, not a complete object path.

```json
{
  "values": {
    "ability1Cooldown%": {
      "en-US": "Violent Leap Cooldown Time",
      "exclude": [
        "lucio",
        "soldier",
        "wreckingBall",
        "zenyatta"
      ],
      "values": "__percent__"
    },
    "ability1Distance%": {
      "en-US": "Violent Leap Distance",
      "values": "__percent__"
    },
    "ability2Cooldown%": {
      "en-US": "Jagged Wall Cooldown Time",
      "exclude": [
        "bastion",
        "venture",
        "zenyatta"
      ],
      "values": "__percent__"
    },
    "ability2Health%": {
      "en-US": "Jagged Wall Health",
      "values": "__percent__"
    },
    "ability2Kb%": {
      "en-US": "Jagged Wall Knockback",
      "values": "__percent__"
    },
    "combatUltGen%": {
      "en-US": "Ultimate Generation - Combat Downpour",
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
      "en-US": "Violent Leap",
      "values": "__boolOnOff__"
    },
    "enableAbility2": {
      "en-US": "Jagged Wall",
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
      "en-US": "Spike Guard",
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
      "en-US": "Ultimate Ability Downpour",
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
      "en-US": "Ultimate Generation - Passive Downpour",
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
    "secondaryFireCost%": {
      "en-US": "Spike Guard Resource Cost",
      "values": "__percent__"
    },
    "secondaryFireMovementSpeedPenalty%": {
      "en-US": "Spike Guard Movement Speed Penalty",
      "values": "__percent__"
    },
    "secondaryFireRegen%": {
      "en-US": "Spike Guard Resource Regeneration",
      "values": "__percent__"
    },
    "ultGen%": {
      "en-US": "Ultimate Generation Downpour",
      "values": "__percent__"
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
