# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- Run the script: `python3 greeter/greet.py [--shout] NAME` (`--shout` uppercases the greeting; `-h`/`--help` prints usage)
- Run all tests: `python3 -m pytest`
- Run a single test: `python3 -m pytest greeter/test_greet.py::test_greet_returns_greeting`

## Architecture

- `greeter/greet.py` — `greet(name, shout=False)` builds the greeting (uppercased when `shout`); `main(argv)` is the CLI entry point (returns an exit code).
- `greeter/test_greet.py` — pytest tests for both.

## Workflow for new features and bug fixes

Follow these steps for every change unless the user says otherwise.

1. **Branch** — create a new branch off an up-to-date `main` (e.g. `add-shout-flag`). Never commit directly to `main`.
2. **Clarify "done"** — if the request doesn't say what the expected behavior, exit codes, or output are, state your assumptions before coding.
3. **Implement with tests** — add or update tests in `greeter/test_greet.py` for every new behavior and edge case.
4. **Run tests** — `python3 -m pytest` must pass before moving on.
5. **Review with the `code-reviewer` subagent** — defined in `.claude/agents/code-reviewer.md`. It checks correctness, edge cases, exit codes, stdout/stderr and test coverage, and labels each finding **bug** (must fix) or **nit** (optional).
6. **Fix loop** — fix every **bug**, re-run the tests, and send the changes back to the reviewer. **Max 3 review rounds.** If bugs remain after round 3, stop and report to the user instead of opening a PR.
7. **Update docs** — update the Commands/Architecture sections above and `README.md` if usage changed.
8. **Push and open a PR** — only when the review has no remaining bugs and all tests pass. The PR description must include:
   - a short summary of the change
   - the reviewer's final summary (including any nits left unfixed and why)
   - how it was tested
9. **Stop at the PR** — do not merge. The user reviews and merges on GitHub.
