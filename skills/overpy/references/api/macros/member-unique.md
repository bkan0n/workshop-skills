# receiver.unique

`<Array>.unique()`

Receiver: `Array`. The receiver supplies the first compiler argument.

Returns a copy of the array with duplicate values removed (the first value is kept).

Thanks to LazyLion for the formula.

Returns: `Array`.

Macro expansion (compiler implementation; not a second runtime function):

```opy
[elem for elem, idx in $self if $self.index(elem) == idx]
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
