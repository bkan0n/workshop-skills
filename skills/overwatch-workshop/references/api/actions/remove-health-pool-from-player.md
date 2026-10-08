# Remove Health Pool From Player

Native Workshop action. Signature labels below describe argument order; replace them with expressions.

`Remove Health Pool From Player(healthPoolId)`

Removes a health pool that was added via the Add Health Pool action.

| Argument | Type | Meaning |
| --- | --- | --- |
| `healthPoolId` | `HealthPoolId` | Specifies a health pool created by the Add Health Pool action. (Health pool IDs may be obtained using the Last Created Health Pool Value.) |

Returns: `void`. Types are OverPy's model of native inputs.

Source: [OverPy 9.7.17](https://github.com/Zezombye/overpy/tree/5a7d0e294b8cad73b9701987bb584d0551d7fa4d/src/data/actions.ts). Generated from pinned initialized exports.
