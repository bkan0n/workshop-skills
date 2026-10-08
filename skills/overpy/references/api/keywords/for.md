# for

Denotes either:

- If an instruction, the beginning of a block that will execute in a loop, modifying the control variable on each loop. The instruction must be `for <var> in range(start, stop, step):` See also the `range` function.

- If within a list comprehension, a filtered or mapped array, such as `[i for i in x if x == 3]`.

Editor snippet template (dollar placeholders are not source syntax):

```text
for $0
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
