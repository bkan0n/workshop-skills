# Install the skills

Install `overwatch-workshop` for native Workshop. For OverPy, install **both** `overwatch-workshop` and `overpy` from the same release. The OverPy skill's dependency metadata describes compatibility; it does not automatically install Workshop.

<!-- x-release-please-start-version -->
This checkout contains skill release **0.1.0**.
<!-- x-release-please-end -->

## Install from this local checkout with `npx skills`

These commands work from the repository root. They use the local `skills/` directory; no published repository address is needed. `npx` requires Node/npm and may download the Skills CLI. The CLI discovers the two nested `SKILL.md` files and can list them before installation. [CLI source formats and options](https://github.com/vercel-labs/skills#source-formats), [discovery implementation](https://github.com/vercel-labs/skills/blob/main/src/skills.ts).

```sh
# Discover the available skills without installing them.
npx skills add ./skills --list

# Native Workshop only, targeting Codex.
npx skills add ./skills --skill overwatch-workshop --agent codex

# OverPy: explicitly select the matched pair.
npx skills add ./skills --skill overwatch-workshop --skill overpy --agent codex
```

Choose the one installation command that matches your workflow. For a project installation, select **Project** if prompted; its destination is relative to your current directory. To install for use across projects, add `--global`:

```sh
npx skills add ./skills --skill overwatch-workshop --skill overpy --agent codex --global
```

To install into another project, run the command from that project and replace `./skills` with the path to this checkout's `skills` directory. Quote paths containing spaces. The CLI supports `--copy` for copies instead of agent-directory symlinks and `--yes` to skip prompts; the examples leave prompts enabled so you can review scope and replacements. [Installation behavior](https://github.com/vercel-labs/skills/blob/main/src/add.ts).

Use your agent's CLI identifier with `--agent`. Current mappings include:

| Agent | Identifier | Project location | Global location |
| --- | --- | --- | --- |
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` | `~/.claude/skills/` |
| Cursor | `cursor` | `.agents/skills/` | `~/.cursor/skills/` |

These are the Skills CLI's current defaults, verified October 7, 2026; configuration can affect some destinations. Agents sharing `.agents/skills/` may discover the same installation. See the [agent configuration](https://github.com/vercel-labs/skills/blob/main/src/agents.ts) for other hosts and overrides.

## Install from GitHub

Run these commands from the project where you want to use the skills. They install from [bkan0n/workshop-skills](https://github.com/bkan0n/workshop-skills):

```sh
npx skills add bkan0n/workshop-skills --list

# Native Workshop only.
npx skills add bkan0n/workshop-skills --skill overwatch-workshop --agent codex

# OverPy with its required Workshop companion.
npx skills add bkan0n/workshop-skills --skill overwatch-workshop --skill overpy --agent codex
```

The same agent and scope options apply. Use a matched release archive below when you want a specific published version rather than the repository's current contents.

## Manual copy or archive extraction

From a source checkout, copy the complete `skills/overwatch-workshop/` directory to your host's supported skill location. For OverPy, also copy the complete `skills/overpy/` directory into that **same parent directory**.

For ZIP packages built locally in `dist/` or downloaded from a published [GitHub release](https://github.com/bkan0n/workshop-skills/releases), extract the appropriate archive. Until the first release is published, use a checkout or the GitHub installation commands above.

<!-- x-release-please-start-version -->
- Native Workshop: `workshop-skills-0.1.0.zip`.
- Matched Workshop and OverPy pair: `workshop-overpy-skills-0.1.0.zip`.
<!-- x-release-please-end -->

Place the extracted skill folders in the host's skill location, preserving all bundled `references/`, `examples/`, and other skill files:

```text
<your host's skill directory>/
  overwatch-workshop/
    SKILL.md
    references/...
    examples/...
  overpy/
    SKILL.md
    references/...
    examples/...
```

Copying only `SKILL.md` breaks the reference links. The Workshop skill's `references/wiki/archive/` contains all 630 full article bodies and must be copied with it. These are optional references read one article at a time. Keep the package's license and source notices with your retained distribution. `RELEASE.json` identifies versions, source locks, and file hashes; `SHA256SUMS` accompanies built packages. Build tools, dependency caches, and raw API page caches do not belong in the installed skill directories.

## Confirm setup and update the pair

Refresh your host's skill list or start a new session as its setup requires. Confirm `overwatch-workshop` is available; for OverPy, confirm both names and that the agent can read their references. For CLI-managed installations, `npx skills list --agent codex` lists project installations; add `--global` to inspect global installations. [Skills CLI commands](https://github.com/vercel-labs/skills#other-commands).

A host that isolates skill directories must expose both roots and allow the OverPy skill to read the Workshop companion. Enable both skills for OverPy work. If the host cannot follow companion paths, configure a supported shared location before relying on the pair.

Before updating, preserve personal modifications and check for older copies of either skill in other project/global locations. Update both from the same source release and confirm their version metadata agrees. Reinstall from the updated local checkout or chosen published source, or replace the complete manually installed folders with the matched archive; avoid merging new files into an old folder and leaving obsolete references behind. An unrelated Workshop skill with the same name is not an interchangeable companion.

Normal use needs only Markdown/file access. Node, Python, the OverPy compiler, and network access are not required to read the installed skills. Compilation is an optional project tool; the agent should state when code has not been compiled. The installed wiki is the source of truth for runtime behavior; use its local articles directly.
