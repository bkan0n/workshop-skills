# macro

Declares a macro, which is an inline function or constant. For example:

```thon
macro BOSS_HP = 1000+getNumberOfPlayers()*300

macro add(a, b):
    a + b
```
The macro can then be used like a function: `add(C, D)` will yield `C + D` and `BOSS_HP` will get replaced by `1000+getNumberOfPlayers()*300`.

Note that, unlike `#!define`, macros will not mess up the order of operations:

```thon
#!define add_define(a, b) a+b
macro add_macro(a, b):
    a + b

rule "":
    A = add_define(A, B) * C #will be interpreted as A + (B * C)
    A = add_macro(A, B) * C #will be interpreted as (A + B) * C
```

You can also declare member macros, where `self` refers to the member. For example:
```thon
macro Player.setPowerLevel(powerLevel):
    self.setMaxHealth(powerLevel*200)
    self.setDamageDealt(powerLevel*2)

macro Vector.sum = self.x + self.y
```

`A.setPowerLevel(2)` will yield `A.setMaxHealth(400)` and `A.setDamageDealt(4)`.

Default parameters can also be specified, and just like normal functions, you can use keyword arguments:

```thon
macro Player.setPowerLevel(powerLevel=1, damageDealt=null):
    self.setMaxHealth(powerLevel*200)
    self.setDamageDealt(damageDealt or powerLevel*2)

rule "":
    A.setPowerLevel(damageDealt=3)
```


Editor snippet template (dollar placeholders are not source syntax):

```text
macro $0
```

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports.
