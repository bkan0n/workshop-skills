# receiver.reverse

`<Array>.reverse()`

Receiver: `Array`. The receiver supplies the first compiler argument.

Reverses the array.

Returns: `Array`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
sorted($self, key=lambda _, i: -i)
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
