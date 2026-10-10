# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- Run the script: `python3 greeter/greet.py NAME` (`-h`/`--help` prints usage)
- Run all tests: `python3 -m pytest`
- Run a single test: `python3 -m pytest greeter/test_greet.py::test_greet_returns_greeting`

## Architecture

- `greeter/greet.py` — `greet(name)` builds the greeting; `main(argv)` is the CLI entry point (returns an exit code).
- `greeter/test_greet.py` — pytest tests for both.
