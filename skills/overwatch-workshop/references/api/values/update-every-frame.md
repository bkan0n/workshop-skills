# Update Every Frame

Native Workshop value. Signature labels below describe argument order; replace them with expressions.

`Update Every Frame(value)`

Increases the update frequency of the provided value to once per tick. Useful for smoothing the appearance of certain Values, such as getPosition(), that normally only update every few ticks. Applies to rule conditions as well as reevaluating action parameters. The value is interpolated client-side if the framerate is higher than the tick rate. May increase server load and/or lower frame rate.

| Argument | Type | Meaning |
| --- | --- | --- |
| `value` | `Object \| Array` | The value that will be updated once per tick. |

Returns: `Object | Array`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/values.ts). Generated from pinned initialized exports. Engine behavior is not independently game-tested.
