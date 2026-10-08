# receiver.getOppositeTeam

`<Player>.getOppositeTeam()`

Receiver: `Player`. The receiver supplies the first compiler argument.

Gets the opposite team of the team of a player. If the team is `Team.ALL`, it returns `Team.ALL`.

Returns: `Team`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
getOppositeTeam($self.getTeam())
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
