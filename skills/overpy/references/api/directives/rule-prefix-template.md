# #!rulePrefixTemplate


Defines a global template for how rule prefixes are applied to rule names. Can only be defined once. Has effect on all rules, even those declared before this directive.

The template is an OverPy expression with the following variables:

- `$rule`: the current rule name
- `$isDelimiter`: true if the rule is @Delimiter
- `$prefix`: the current prefix (set via `#!rulePrefix`)
- `$file`: the file name without extension
- `$path`: the relative path to the main file (backslashes replaced by slashes)
- Titlecase/lower/upper variations: `$prefixTitle`, `$prefixUpper`, `$prefixLower`, `$fileTitle`, `$fileUpper`, `$fileLower`, `$pathTitle`, `$pathUpper`, `$pathLower`

Examples :

- `#!rulePrefixTemplate f"[{$prefix}] {$rule}" if $prefix and $rule else $rule` (default): adds the prefix in square brackets before the rule name, if the prefix and rule name are not empty. This is the default if this directive is unspecified.
- `#!rulePrefixTemplate f"[{$pathTitle.replace('_', ' ')}] {$rule}" if $rule and not $isDelimiter else $rule`": if you have an `heroes/junker_queen.opy` file, will yield rule names like "[Heroes/Junker Queen] Spawn particles". This is the default if the directive is specified without an expression (just `#!rulePrefixTemplate`).

The expression has to evaluate to a string without arguments.


Editor snippet template (dollar placeholders are not source syntax):

```text
rulePrefixTemplate $0
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
