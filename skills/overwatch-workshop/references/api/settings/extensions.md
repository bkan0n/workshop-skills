# Settings: extensions

Normalized schema from the pinned compiler. Keys describe the OverPy settings object; `en-US` fields give native labels. This JSON is reference data, not a pasteable preset. `values` describes nested choices or accepted types; internal type tokens are compiler constraints. Keep unspecified settings from the user's preset.

```json
{
  "en-US": "extensions",
  "values": {
    "beamEffects": {
      "en-US": "Beam Effects",
      "points": 2
    },
    "beamSounds": {
      "en-US": "Beam Sounds",
      "points": 1
    },
    "buffAndDebuffSounds": {
      "en-US": "Buff and Debuff Sounds",
      "points": 2
    },
    "buffStatusEffects": {
      "en-US": "Buff Status Effects",
      "points": 2
    },
    "debuffStatusEffects": {
      "en-US": "Debuff Status Effects",
      "points": 2
    },
    "energyExplosionEffects": {
      "en-US": "Energy Explosion Effects",
      "points": 4
    },
    "explosionSounds": {
      "en-US": "Explosion Sounds",
      "points": 2
    },
    "kineticExplosionEffects": {
      "en-US": "Kinetic Explosion Effects",
      "points": 4
    },
    "playMoreEffects": {
      "en-US": "Play More Effects",
      "points": 1
    },
    "projectiles": {
      "en-US": "Projectiles",
      "points": 4
    },
    "spawnMoreDummyBots": {
      "en-US": "Spawn More Dummy Bots",
      "points": 2
    }
  }
}
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
