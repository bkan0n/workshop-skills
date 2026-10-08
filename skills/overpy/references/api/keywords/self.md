# self

In a member macro, refers to the member itself. For example:
```
macro Array.reverse():
    sorted(self, key=lambda _, i: -i)
```
If calling `A.reverse()`, `self` will be replaced by `A`.


Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
