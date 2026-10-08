# Settings: heroes.pharah

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

Hero settings require a team wrapper: `heroes.<team>.pharah`. Replace `<team>` with `allTeams`, `ffa`, `team1`, `team2`. Native team labels: `allTeams` = General; `ffa` = Team FFA; `team1` = Team 1; `team2` = Team 2. The heading identifies a schema fragment, not a complete object path.

```json
{
  "values": {
    "ability1Acceleration%": {
      "en-US": "Jump Jet Acceleration Scalar",
      "values": "__percent__"
    },
    "ability1Cooldown%": {
      "en-US": "Jump Jet Cooldown Time",
      "exclude": [
        "lucio",
        "soldier",
        "wreckingBall",
        "zenyatta"
      ],
      "values": "__percent__"
    },
    "ability1RefuelScalar": {
      "en-US": "Jump Jet Refuel Scalar",
      "values": "__percent__"
    },
    "ability2Cooldown%": {
      "en-US": "Concussive Blast Cooldown Time",
      "exclude": [
        "bastion",
        "venture",
        "zenyatta"
      ],
      "values": "__percent__"
    },
    "ability2Kb%": {
      "en-US": "Concussive Blast Knockback Scalar",
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
      "en-US": "Ultimate Generation - Combat Barrage",
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
      "en-US": "Jump Jet",
      "values": "__boolOnOff__"
    },
    "enableAbility2": {
      "en-US": "Concussive Blast",
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
    "enablePassive": {
      "en-US": "Hover Jets",
      "include": [
        "mercy",
        "echo",
        "pharah",
        "juno"
      ],
      "values": "__boolOnOff__"
    },
    "enablePassiveUnlimitedFuel": {
      "en-US": "Hover Jets Unlimited Fuel",
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
      "en-US": "Jet Dash",
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
      "en-US": "Ultimate Ability Barrage",
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
    "passiveExtraFuel%": {
      "en-US": "Hover Jets Extra Fuel Scalar",
      "values": "__percent__"
    },
    "passiveHealthRegen": {
      "en-US": "Passive Health Regeneration",
      "values": "__boolOnOff__"
    },
    "passiveMaxTime%": {
      "en-US": "Hover Jets Maximum Time",
      "values": "__percent__"
    },
    "passiveMaximumTime%": {
      "en-US": "Jump Jet Acceleration Scalar",
      "values": "__percent__"
    },
    "passiveRechargeRate%": {
      "en-US": "Hover Jets Recharge Rate",
      "values": "__percent__"
    },
    "passiveUltGen%": {
      "en-US": "Ultimate Generation - Passive Barrage",
      "values": "__percent__"
    },
    "passiveVerticalSpeed%": {
      "en-US": "Hover Jets Vertical Speed Scalar",
      "values": "__percent__"
    },
    "primaryFireKb%": {
      "en-US": "Rocket Launcher Knockback Scalar",
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
      "en-US": "Jet Dash Cooldown Time",
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
      "en-US": "Ultimate Generation Barrage",
      "values": "__percent__"
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
