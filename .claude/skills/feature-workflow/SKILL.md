---
name: feature-workflow
description: This repo's end-to-end workflow for any new feature or bug fix — branch off main, clarify "done", implement with tests, run pytest, review with the code-reviewer subagent (max 3 rounds), update docs, and open a PR without merging. Use whenever the user asks to add, change, or fix behavior in this repo (e.g. "add a --shout flag", "fix the blank-name bug"), unless they say to skip the workflow.
---

# Feature / bug-fix workflow

Follow these steps for every change unless the user says otherwise.

## 1. Branch

Create a new branch off an up-to-date `main`. Never commit directly to `main`.

```bash
git fetch origin
git checkout main && git pull --ff-only
git checkout -b <short-kebab-name>   # e.g. add-shout-flag
```

## 2. Clarify "done"

If the request doesn't say what the expected behavior, exit codes, or output are,
state your assumptions before coding. Follow the repo's existing CLI conventions:
exit `0` on success and `2` on usage errors; normal output on stdout; errors and
usage on stderr (except `--help`, which prints to stdout).

## 3. Implement with tests

Add or update tests in `greeter/test_greet.py` for every new behavior and edge case,
including failure paths (unknown flags, blank or whitespace-only input, missing
arguments, flags combined with a name).

## 4. Run tests

```bash
python3 -m pytest
```

All tests must pass before moving on.

## 5. Review with the `code-reviewer` subagent

Launch the `code-reviewer` agent (defined in `.claude/agents/code-reviewer.md`). It
checks correctness, edge cases, exit codes, stdout/stderr and test coverage, and
labels each finding:

- **bug** — must fix
- **nit (fix)** — quick, and improves clarity or test coverage
- **nit (skip)** — a matter of taste (naming, wording); listed for the record only

Tell it which round this is and, from round 2 on, what you changed since the last round.

## 6. Fix loop — max 3 review rounds

- Fix every **bug**, re-run the tests, and send the changes back to the reviewer.
- If bugs remain after round 3, **stop and report to the user** instead of opening a PR.
- **Nits:** fix `nit (fix)` items; skip `nit (skip)` items and list them in the PR
  description. Do not ask the user about nits — decide using this rule.
- **Do not start a new review round for nits alone.** If the only changes since the
  last review are nit fixes, re-run the tests and move on to the PR.

Keep the reviewer's final summary — it goes into the PR description.

## 7. Update docs

If usage changed, update the **Commands** and **Architecture** sections of `CLAUDE.md`
and the usage notes in `README.md`.

## 8. Push and open a PR

Only when the review has no remaining bugs and all tests pass.

```bash
git push -u origin <branch>
gh pr create --base main --title "<title>" --body "<body>"
```

The PR description must include:

- a short summary of the change
- the reviewer's final summary (including any nits left unfixed and why)
- how it was tested

## 9. Stop at the PR

Do not merge. Give the user the PR link — they review and merge on GitHub.
