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

For every new feature or bug fix, unless the user says otherwise, follow the
`feature-workflow` skill (`.claude/skills/feature-workflow/SKILL.md`). In short:
branch off an up-to-date `main` → clarify "done" → implement with tests → `python3 -m pytest`
→ review with the `code-reviewer` subagent (max 3 rounds; fix every bug, nits per the skill;
if bugs remain after round 3, stop and report instead of opening a PR)
→ update docs → push and open a PR → stop at the PR (never merge).
