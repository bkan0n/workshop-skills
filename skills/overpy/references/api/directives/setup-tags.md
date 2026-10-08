# #!setupTags

Add a rule to obtain an unsanitized '<' character which can be used to create <tx> and <fg> tags.

**WARNING**: The inserted rule creates a dummy bot then immediately destroys it. This has the side effect of triggering each-player rules and may break your gamemode (though if properly coded, it shouldn't).

The `__holygrail__` variable can be used to obtain the raw '<' character, although it is not necessary as OverPy will automatically take care of the conversion, meaning you can put raw texture tags in strings.

For color, use the <fgRRGGBBAA> tag, where RR/GG/BB are the hex color value, and AA is the hex transparency value (00 = transparent, FF = opaque).
Example: `print('<fgFF0000FF>Red text</fg>')`.

For textures, use the <TX> standalone tag, with the texture id as seen in https://workshop.codes/wiki/articles/tx-reference-sheet.
Example: `print('<TXC0000000002DD21>')` will display the mouse cursor texture.

Additionally, you can use the `Texture` enum (such as `Texture.MOUSE_CURSOR`), and OverPy will automatically optimize it.

OverPy will also replace `'<tx1234>'` to the correct full texture id, but only if the entire tag is inside a string (`'<tx{}>'.format(id)` will not work, but `'<tx{}>'.format(1234)` will).

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
