# claude-agent-survey

My personal notes and experiments while learning how to work with **Claude agents**.

## Why this repo exists

I had never used an AI agent before. This repo is my study space: a place to try
small tasks with Claude, see how it plans and uses tools, and write down what I learn.

## What is an agent?

A normal chatbot answers with text, and then you do the work yourself. An agent does
the work itself, in a loop:

1. **Goal** – I describe the outcome I want.
2. **Act** – Claude uses tools (read/edit files, run shell commands, search the web).
3. **Check** – It verifies the result (runs tests, reads errors) and fixes problems.
4. **Report** – It hands back the finished work and a short summary.

## Project contents

| Path | What it is |
|------|------------|
| `greeter/greet.py` | A small CLI that greets someone by name |
| `greeter/test_greet.py` | pytest tests for the greeter |
| `CLAUDE.md` | Guidance the agent reads when working in this repo |

### Try the greeter

```bash
python3 greeter/greet.py naveeharn   # -> Hello, naveeharn!
python3 -m pytest                    # run all tests
```

A missing or blank name prints an error and exits with code `2`.

## Tips I'm following

- Say what "done" looks like, not just the topic.
- Give context: language, constraints, things to avoid.
- Start small, review the result, then iterate.
- Ask Claude to explain or show what it changed.
- Keep `CLAUDE.md` up to date — it's the project guidance the agent reads every time.

## Learning log

| # | Exercise | What I learned |
|---|----------|----------------|
| 1 | Asked Claude to write this README and commit it | An agent can edit files and run git on my machine from a single request |
| 2 | Built a greet script with tests, on a branch merged via PR #1 | Work on a branch, review in a PR, iterate (blank-name bug fix, move into `greeter/`), then merge |

## Next exercises

- [x] Create a small Python script with a test, run it, and commit
- [ ] Research what Claude agents can do and summarize it here
- [x] Fill in `CLAUDE.md` once real code exists
