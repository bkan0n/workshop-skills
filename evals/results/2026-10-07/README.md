# Exploratory evaluation results — October 7, 2026

Four runs answered the same `wait-repeat` prompt: no domain skill, the prior search-based skill, the initial new Workshop skill, and a revised new Workshop skill. One additional run tested health lookup with the matched Workshop/OverPy pair. These are performed runs, not proposed tests.

All four native answers explained condition activation and provided a paced loop that cancels on release. Later checks accepted all four with pinned OverPy 9.7.17, with no reported warnings or hidden warnings. No game tests ran. These results support the tested examples; they do not establish statistical superiority, broad skill coverage, or token savings.

## Answers and grading

The [machine-readable results](results.json) contain dimension scores, evidence, reading totals, prompt differences, and the status of every case. The [case rubrics](../../cases.json) score semantic reasoning, dialect/API correctness, focused retrieval, uncertainty, and validation honesty from 0–2. Grading was a post-hoc project-agent review, not an independent blinded panel.

| Run and raw answer/read record | Semantics | Dialect/API | Retrieval | Uncertainty | Validation honesty | Applicable total |
| --- | --- | --- | --- | --- | --- | --- |
| [No skill](raw/baseline-wait.json) | 2 | 2 | N/A | 1 | 2 | 7/8 |
| [Prior search skill](raw/old-wait.json) | 2 | 2 | 1 | 2 | 2 | 9/10 |
| [New Workshop, initial](raw/new-wait.json) | 2 | 2 | 1 | 2 | 2 | 9/10 |
| [New Workshop, revised routing](raw/new-revised-wait.json) | 2 | 2 | 1 | 2 | 2 | 9/10 |
| [Matched pair, health lookup](raw/pair-health.json) | 2 | 2 | 1 | 2 | 2 | 9/10 |

The baseline's retrieval dimension is inapplicable because that condition deliberately prohibited domain reference reads. Its answer correctly described the loop, but promised 0.1-second increments without the archived tick-rounding caveat. The three skill-assisted timing answers distinguished a requested 0.1-second wait from the documented approximately 0.112-second ordinary-map delay. None claimed to have compiled or game-tested its answer while producing it; later compiler checks are separate evidence.

The initial new run loaded the broad execution guide. The revised run selected the narrower waits guide, but also read the examples index, two fixtures, and more exact API/index entries. Both received a retrieval score of 1: relevant evidence was found, but the record leaves room for more selective reading. The prior skill also found relevant evidence, with substantial search-result material and a repeated skill-body load.

The pair run correctly connected `player.getHealth()` to native `Health`, including armor and shields. It resolved the matching Workshop version, read each foundation once, and avoided native-authoring guidance. Its broader combat guide and catalog-index reads were unnecessary for such a narrow mapping question, so retrieval also scored 1.

The pair prompt differed from `cases.json`:

> My OverPy player.getHealth() call compiles. Does using OverPy change what armor and shields count toward? Explain briefly and cite the relevant local reference.

Its reference to a successful compile therefore came from the prompt premise. The pair agent did not run a compiler. This is a related smoke test, not an exact repeat of the catalogued prompt or a comparison against baseline/old-skill health answers.

## Reported reading sizes

These values describe reported displayed reference material. They are **not token counts**. Full-file values for the revised and pair runs were measured as file bytes despite the raw field name `characters_read_estimate`. Earlier reports supplied character estimates without a confirmed measurement method. Partial-read and search sizes are reported character estimates; the pair's partial values were estimated manually.

| Condition | Full files | Full-file size sum | Partial reads and size | Search calls and output size |
| --- | --- | --- | --- | --- |
| No skill | 0 | 0 domain-reference characters | 0 | 0 |
| Prior search skill | 8 | 12,970 reported characters | 0 | 6; 12,346 reported characters |
| New Workshop, initial | 11 | 24,815 reported characters | 3; 234 reported characters | 0 |
| New Workshop, revised | 18 | 27,047 **bytes** | 2; 60 reported characters | 0 |
| Matched pair | 11 | 26,524 **bytes** | 2; 1,511 reported characters | 0 |

The prior run totals 25,316 reported characters across its listed files and search results. It additionally reported reloading the 1,856-character skill body through the skill loader; including that known repeat gives approximately 27,172 characters, before unmeasured wrappers or bootstrap instructions. The initial new run totals 25,049 reported characters. This single observation does not establish a meaningful or general efficiency advantage. Mixed byte/character measurements prevent an equivalent combined character total for the revised and pair runs.

The records do not measure full conversational context, prompts, answers, reasoning, tool wrappers, all repeated reads, or mandated generic bootstrap instructions. No model tokenizer was used. File size and archive size are not substitutes for actual context-token measurements.

## Compiler evidence and limits

| Native answer | Accepted by pinned OverPy | Warnings / hidden warnings | Reported elements |
| --- | --- | --- | --- |
| No skill | Yes | 0 / 0 | 10 |
| Prior search skill | Yes | 0 / 0 | 10 |
| New Workshop, initial | Yes | 0 / 0 | 13 |
| New Workshop, revised | Yes | 0 / 0 | 13 |

The new answers include an explicit initialization rule. Element counts are compiler outputs, not measurements of runtime performance. Raw compiler records are preserved for the [first three conditions](raw/compiler-results.json) and the [revised condition](raw/new-revised-compiler.json). This report used those performed checks and did not rerun compilation.

Runs used the same inherited model/settings according to orchestration, but the exact model ID, reasoning configuration, and sampling parameters were not captured. Exact evaluated file snapshots were also not saved. The raw JSON preserves answers and reported file reads; relative read paths refer to each run's fixture layout, which `results.json` explains. Machine-local absolute paths have been sanitized.

After these runs, the project added further instructions to start named-API questions with the exact reference, stop reading once sufficiently supported, and avoid rereading the shared foundation. It also corrected an OverPy link to the waits reference. Those final routing edits were **not re-evaluated**, so no measured improvement is claimed for them.

Only `wait-repeat` ran with its exact catalogued prompt. `overpy-routing` ran as the documented variant. The other 13 cases remain **unrun**: wait-overuse, event-context, array-copy, reevaluation, owner-leaves, raycast-miss, hero-exception, invented-api, python-confusion, missing-companion, missing-compiler, conflicting-source, and simple-native-routing.
