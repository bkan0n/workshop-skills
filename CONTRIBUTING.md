# Contributing

Keep Workshop engine knowledge under `overwatch-workshop`; OverPy references should explain language/compiler differences and link to the shared behavior. Preserve source dates, claim IDs, uncertainty, and the difference between compilation and game testing. See [maintenance](docs/maintaining.md) for source updates and [installation](INSTALL.md) for trying a skill locally.

Run `npm run check` and `npm run build` before submitting changes. Do not update generated Markdown independently of its reviewed source data.

## Commit messages and releases

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commits merged to `main`. When squash-merging a pull request, use its Conventional Commit title as the squash commit message. Release Please reads the merged commit history, not merely a PR label.

| Example | Release effect |
| --- | --- |
| `fix(workshop): correct the captured-value explanation` | Patch release |
| `docs(overpy): clarify compiler setup` | Patch release; documentation changes are releasable in this knowledge repository |
| `feat(workshop): add a debugging reference` | Minor release |
| `feat!: change the companion compatibility contract` | Breaking release; minor while below 1.0, major at or above 1.0 |
| `ci: update a pinned action` | Included in a later release, but does not request one on its own |

Use `!` or a `BREAKING CHANGE:` footer when the installed skill/dependency contract breaks compatibility. Scopes are optional. Describe what users gain or what behavior is corrected; do not prefix ordinary documentation changes with `feat:` solely to force a version bump.

Release Please keeps one release PR up to date. Review its changelog and synchronized versions, then merge it when ready. GitHub Actions builds and checks the draft assets; publish the draft only after those checks pass. Both skills share one version. Their version is independent of the OverPy compiler version and wiki snapshot date.

Do not manually bump every version field or rewrite historical evaluation records. Release Please updates the marked current-version blocks and configured JSON fields. Its updater tests check that the compiler and source pins stay unchanged. See [the release process](docs/maintaining.md#github-releases) for repository setup and recovery.
