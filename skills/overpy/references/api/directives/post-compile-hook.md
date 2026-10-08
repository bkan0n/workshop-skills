# #!postCompileHook


Specifies a JavaScript file to be executed after compilation, with the compiled code as a `content` variable. The script must return the modified code.

Please do not use this directive to work around OverPy bugs; instead, report the bugs so they can be fixed at the source.

Example:

```js
#!postCompileHook "hook.js"

//In hook.js:

content = content.toLowerCase();
content = content.replace(/abc/g, "def");
// In case content becomes a
// JS interpreter object, which can
// happen if the last operation is a
// replace or match
content.toString();
```


Editor snippet template (dollar placeholders are not source syntax):

```text
postCompileHook "$0"
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
