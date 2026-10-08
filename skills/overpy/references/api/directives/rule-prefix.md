# #!rulePrefix


Sets a prefix for all subsequent rules in the current file and its included child files (unless overridden). The prefix is applied to the rule name using the rule prefix template.

If a `#!rulePrefix` directive is in an included file, it only takes effect for the rules within that file (and its child includes, if they don't have their own `#!rulePrefix`), after the directive.

Example:

```hs
#!rulePrefix "Effects"

rule "Spawn particles":
    #compiled rule name: [Effects] Spawn particles
```

To clear the prefix for subsequent rules, use an empty string:

```hs
#!rulePrefix ""
```


Editor snippet template (dollar placeholders are not source syntax):

```text
rulePrefix "$0"
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
