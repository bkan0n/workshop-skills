# #!translations


Setups the translation system. Arguments are the language codes separated by spaces.

For example:

`#!translations en fr es zh_cn`

Only the es_mx, es_es, zh_cn and zh_tw languages can be specified fully. For the rest, you can only specify the first two letters.

To translate a string, wrap it with the "\_" function, such as `_("You have ${} money").format(money)`. Note that the formatter has to be outside of the function. You can also use the "t" string modifier, such as `t"${} money".format(money)`.

If two strings are the same but have to be translated differently, you can add a context string as the first argument, such as `_("the direction", "left")`.

Lastly, if a translated string is stored in a variable, you **have** to use the "\_" function when displaying it, such as `hudHeader(text=_(someVariable))`. Else, "TLErr" will be displayed. Note that you also have to use the "\_" function when storing the string in the variable, else "0" will be displayed.

OverPy will generate and parse .po files for each language based on the name of the main file. You can then use an online editor to edit those files. Leading and trailing whitespace is automatically stripped from the string when put into translation files.

**WARNING**: A translated string cannot be used as a normal string **when stored in a variable**, as it becomes a string array. This means you cannot use `.replace()`, `.charAt()`, etc. When translating your gamemode, look out for these functions.

This also means that, when used in a variable, you cannot use a translated string as an argument of a string: `"{}{}".format(t"string", 1234)` will not work. Instead, do `t"string{}".format(1234)`. The translated string must always be top-level. You will also get "TLErr" if trying to use a translated string as an argument for another function.

You can also potentially save a lot of elements by using the #!translateWithPlayerVar directive (see the associated documentation).

**Note**: The way string formatting works is via the .replace() function and some constants. This means you cannot have the following in your translated strings if using formatters:

- `(0.00, 1.00, 0.00)` (`Vector.UP`)
- `(0.00, -1.00, 0.00)` (`Vector.DOWN`)
- `(1.00, 0.00, 0.00)` (`Vector.LEFT`)
- `(-1.00, 0.00, 0.00)` (`Vector.RIGHT`)
- `(0.00, 0.00, 1.00)` (`Vector.FORWARD`)
- `(0.00, 0.00, -1.00)` (`Vector.BACKWARD`)
- `1876650.25`, `1876651.25`, `1876652.25`, `1876653.25`, `1876654.25`, `1876655.25`, `1876656.25`, `1876657.25`, `1876658.25`, `1876659.25`


Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
