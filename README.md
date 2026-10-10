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

## Next exercises

- [ ] Create a small Python script with a test, run it, and commit
- [ ] Research what Claude agents can do and summarize it here
- [ ] Fill in `CLAUDE.md` once real code exists
