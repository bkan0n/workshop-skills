# switch

Denotes the beginning of a block that will jump execution to the `case` statement that has the value of the specified variable. If no `case` statement has the value of the specified variable, the execution goes to the `default` statement if it exists, else to the end of the block.

Editor snippet template (dollar placeholders are not source syntax):

```text
switch $0
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
