# Values, comparisons and arrays

## Returned value versus stored state

`Append To Array`, `Remove From Array`, Filtered/Mapped/Sorted/Randomized Array and Array Slice return values. They do not silently mutate the variable used as input. Assign the result, or use the matching Modify Variable action. Append with an array appends its elements; to retain that array as one nested entry, supply an outer array containing it.

Native **action fragment** (requires `Global.Items` declaration/initialization):

```text
Global.Items = Append To Array(Global.Items, 7);
Modify Global Variable(Items, Append To Array, 8);
```

Both statements modify storage; merely evaluating `Append To Array(Global.Items, 7)` does not. `Remove From Array By Index` and `Remove From Array By Value` are different Modify Variable operations. Remove backwards when deleting multiple indices so later entries do not shift past an unvisited index.

Set Variable At Index replaces a non-array variable with an empty array, then writes. Both indexed Set and Modify extend beyond the array end with zeros. This can hide a wrong index and overwrite an earlier scalar. Check bounds/types when the index is calculated from user or runtime data.

## Array evaluation context

Current Array Element and Current Array Index belong to the currently evaluated map/filter/sort expression. They are not Event Player. Filter explicitly for eligibility before sorting: Sorted Array ranks ascending but does not remove dead, allied or otherwise inappropriate players. Compose filter predicates with And/Or and explicit grouping. A nearest target still needs an empty-result policy.

Array Slice takes `(array, start, count)`, not a Python-style end index. Overrunning returns fewer elements. Sorting on negative Current Array Index is a compact reverse-array technique. A one-in-N choice can use inclusive Random Integer(1, N) == 1, with positive N.

## Quiet failure values

| Operation | Archived result to account for |
| --- | --- |
| First Of / Last Of empty array; missing Value In Array | 0 |
| Index Of Array Value with no match | -1 |
| Count Of a non-array, including a string | 0 |
| Random Value In Array with non-array input | The input itself |
| Divide or Modulo by zero | 0 |
| Ray Cast Hit Player with no player hit | Null; see [geometry](geometry-movement.md) |

A zero can be valid data as well as a missing-result sentinel. Verify membership, count, bounds or Entity Exists as appropriate before consuming the result. Do not use Count Of to measure a string: use String Length.

Vectors support componentwise vector multiplication; that is neither Dot Product nor Cross Product. Dividing a vector by a number scales it. Keep units and types explicit rather than relying on permissive coercion.

## Comparisons require care

Native Workshop comparisons are not ordinary Python/JavaScript cross-type algebra. The empirical [comparison tables](https://workshop.codes/wiki/articles/7978) report False equal to Null and Empty Array, while Null is not equal to Empty Array. They also report asymmetric empty-string/zero-vector comparisons with Null Entity, and surprising entity/Boolean comparisons. Equality and ordering are not interchangeable tests of the same cross-type ordering.

Those tables describe representative harness values tested **2024-04-22, patch 2.10.0.0.124591**, despite a 2026 page edit. They do not prove every member of a labeled type behaves identically, and contain no separate `!=` table. Avoid algebraic rewrites based on symmetry/transitivity without a typed argument. Check player existence with the intended entity API, not a general truthiness shortcut. Keep numeric state numeric and flags Boolean.

Index Of Array Value has an additional archived quirk: a 1D-array search target reportedly uses its first member while searching a flattened source; vectors/nested-array targets use strict matching. Treat nested/array-as-key searches as a focused verification case, not a generic dictionary operation.

Offline source details: [state/arrays](wiki/state-arrays.md) and [comparison/math evidence](wiki/comparisons-math.md).

## Evidence and limits

Snapshot **2026-09-29**, archived documentation: [Append](https://workshop.codes/wiki/articles/4565), [Remove](https://workshop.codes/wiki/articles/4731), [Slice](https://workshop.codes/wiki/articles/4574), [Map](https://workshop.codes/wiki/articles/4742), [Sort](https://workshop.codes/wiki/articles/4741), [combined filtering](https://workshop.codes/wiki/articles/1994), [indexed Set](https://workshop.codes/wiki/articles/4415), [indexed Modify](https://workshop.codes/wiki/articles/4394), [First](https://workshop.codes/wiki/articles/4611), [Last](https://workshop.codes/wiki/articles/4684), [indexed retrieval](https://workshop.codes/wiki/articles/4757), [Count](https://workshop.codes/wiki/articles/9067), [Random Value](https://workshop.codes/wiki/articles/4726), [Divide](https://workshop.codes/wiki/articles/4594), [Modulo](https://workshop.codes/wiki/articles/4694), [Multiply](https://workshop.codes/wiki/articles/6962), [reverse recipe](https://workshop.codes/wiki/articles/4826), [random recipe](https://workshop.codes/wiki/articles/4823), [array search](https://workshop.codes/wiki/articles/8904). Array's archived capacity is 1,000 entries; use [resources](resources.md) for dated limits and [wiki lookup](wiki/index.md) for individual exceptions.
