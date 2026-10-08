# goto

Goes to the specified label. Labels can only be placed after the `goto` statement, in the current rule. For example, `goto lbl_1` will continue execution from the `lbl_1:` instruction. Dynamic gotos, although not recommended, can be declared with the `loc+` keyword, such as `goto loc+A` which will move execution 3 actions after the `goto` instruction.

Editor snippet template (dollar placeholders are not source syntax):

```text
goto $0
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
