# Agent evaluation procedure

`cases.json` contains realistic prompts and grader rubrics. Give the agent only the prompt, selected skill condition, and necessary raw examples—not the rubric or intended answer. Use a fresh conversation for each run.

Compare the same prompt/artifacts using the same model/settings with:

1. No Workshop/OverPy skill.
2. The prior search-based skill, when available locally.
3. The new Workshop skill or matched pair.

Limit runs to reading references and producing code/analysis in a temporary workspace. Compilation is permitted when requested and available; do not publish modes or claim a game session ran. Missing dependency/compiler and source conflicts are intentional cases.

Score each applicable dimension 0–2: semantic reasoning, correct dialect/API, focused retrieval, uncertainty handling, and validation honesty. A zero for semantics or invented APIs fails the case regardless of total. Judge behavior and reasoning, not exact wording; multiple valid solutions can pass.

Record prompt ID, skill versions, available model/settings information, files actually read, output, diagnostics, scores with evidence, and limitations. Distinguish full-file character estimates, partial search output, and actual tokenizer measurements. Package size does not measure context use.

`results/` contains only performed runs. Cases absent from results remain unrun. Routine CI checks structure and compiler fixtures, not paid model or in-game evaluations.

Performed results: [October 7, 2026 exploratory comparison and matched-pair smoke test](results/2026-10-07/README.md), with raw answers, reported reads, grading, and compiler evidence.
