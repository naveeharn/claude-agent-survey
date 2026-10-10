# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- Run the script: `python3 greet.py NAME`
- Run all tests: `python3 -m pytest`
- Run a single test: `python3 -m pytest test_greet.py::test_greet_returns_greeting`

## Architecture

- `greet.py` — `greet(name)` builds the greeting; `main(argv)` is the CLI entry point (returns an exit code).
- `test_greet.py` — pytest tests for both.
