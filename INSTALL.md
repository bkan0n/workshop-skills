# Install the skills

For native Workshop, extract `workshop-skills-0.1.0.zip`. For OverPy, extract `workshop-overpy-skills-0.1.0.zip`, which includes its required Workshop companion.

Place each skill directory in your agent's supported skill location. Keep the matched pair as siblings:

```text
<your agent's skill directory>/
  overwatch-workshop/SKILL.md
  overwatch-workshop/references/...
  overpy/SKILL.md
  overpy/references/...
```

Keep each directory's bundled references and examples. Enable both skills when working in OverPy. Install version 0.1.0 of both; this release does not claim compatibility with another Workshop skill of the same name. Replace an older copy using your host's normal skill management, preserving any personal modifications first.

A host that isolates skill directories must explicitly expose both roots to the agent. SKILL.md metadata does not automatically install or resolve dependencies. If your host cannot read companion files, use a host-supported shared skill location; do not compensate by copying shared prose into OverPy.

Normal use needs only Markdown/file access. Node, Python, the OverPy compiler, and network access are not required to read the skills. Compilation is an optional project tool; the agent should state when code has not been compiled. No game behavior in this initial release is claimed to have been independently tested in-game.

For a source checkout, install or link the directories under `skills/` in the same layout. Build tools and the raw research archive do not belong in the agent's skill directory. `RELEASE.json` in each archive identifies versions, source locks, and file hashes; `SHA256SUMS` accompanies the downloads.
