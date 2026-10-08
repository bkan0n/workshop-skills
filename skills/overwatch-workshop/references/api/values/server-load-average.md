# Server Load Average

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Server Load Average`

Provides a percentage representing the average CPU load of the current game instance over the last two seconds. As this number approaches or exceeds 100, it becomes increasingly likely that the instance will be shut down because it is consuming too many resources.

Returns: `unsigned float`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
