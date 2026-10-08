# receiver.getEffectiveHero

`<Player>.getEffectiveHero()`

Receiver: `Player`. The receiver supplies the first compiler argument.

Gets the effective hero of a player (if playing Echo, it returns the hero they are currently duplicating).

You will likely want to use this instead of `getHero()`.

Returns: `Hero`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
$self.getHeroOfDuplication() or $self.getHero()
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
