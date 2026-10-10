# What Claude agents can do (October 2026)

A short survey, researched on 2026-10-11 from official Anthropic docs and
announcements. Features change often, so check the linked sources.
Tags: **[beta]**, **[preview]** = research preview, **[experimental]**,
**[changed]** = recently changed or removed.

## Claude Code

- **Surfaces.** Claude Code is an agentic coding tool that reads your codebase,
  edits files, runs commands, and works with git (branches, commits, PRs). It
  runs in the terminal, VS Code/Cursor, JetBrains, the desktop app, and the
  browser at claude.ai/code; the desktop app is **[beta]** on Ubuntu/Debian. [1]
- **CLI automation.** `claude -p` runs non-interactively, so you can pipe logs
  in or run it in CI. Routines run on a schedule in the cloud, and `/loop`
  repeats a prompt inside a session. [1]
- **Subagents.** Specialized helpers, each with its own context window, system
  prompt, tool access, and permissions. You define them as Markdown files with
  YAML frontmatter in `.claude/agents/` (project) or `~/.claude/agents/` (user).
  Only `name` and `description` are required. Built-ins include Explore, Plan,
  and general-purpose. You invoke one by naming it in a prompt, by @-mention,
  or with `claude --agent`. [2]
- **Agent teams** **[experimental]**: several Claude Code sessions with a lead,
  a shared task list, and direct messages between teammates. Off by default;
  turn on with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. [3]
- **CLAUDE.md.** A Markdown file of instructions Claude reads at the start of
  every session. It can live at org, user (`~/.claude/CLAUDE.md`), project, or
  local (`CLAUDE.local.md`) scope. It supports `@path` imports, and
  `.claude/rules/` holds path-scoped rules. `/init` generates a starter file.
  Claude can also read `AGENTS.md`, and it keeps its own **auto memory**
  alongside. [4]
- **GitHub integration.** The `anthropics/claude-code-action@v1` GitHub Action
  answers `@claude` mentions in issues and PRs (interactive mode) or runs a
  `prompt` on any event, including cron (automation mode). Set it up with
  `/install-github-app`. **[changed]** The `@beta` version was replaced by v1:
  `mode` was removed and `direct_prompt` became `prompt`. [5]
- **Code Review** **[preview]**: managed multi-agent PR review for Team and
  Enterprise plans. It posts severity-tagged inline comments and reads
  `CLAUDE.md` and `REVIEW.md`. **[changed]** Since July 2026, `@claude review`
  no longer subscribes the PR to future reviews; use `@claude review always`
  for that. [6]

## Claude Agent SDK

- Gives you Claude Code's tools, agent loop, and context management as a
  Python or TypeScript library. It includes built-in tools, hooks, subagents,
  MCP, permissions, sessions, skills, and plugins. **[changed]** It replaces
  the older "Claude Code SDK" packages, and a migration guide covers the move.
  Use API-key authentication: third-party products may not offer claude.ai
  login unless Anthropic approved it. [7]
- **Managed Agents** **[beta]**, the hosted alternative: Anthropic runs the
  agent loop in a cloud sandbox or a self-hosted one. Requests need the
  `managed-agents-2026-04-01` beta header, and dreaming is a more limited
  **[preview]**. [8]

## Agents in the Claude apps

- **Cowork**: hand off multi-step knowledge work such as files, research,
  spreadsheets, and slides. It can use the browser, scheduled tasks, subagents,
  plugins and skills, and connectors (MCP). Paid plans only, on desktop, web,
  mobile, and the Chrome side panel (which surfaces you get depends on your plan). **[changed]** Cowork is being merged into
  the main chat ("Claude Cowork is now just Claude"). [9][10]
- **Computer use** **[beta]**: Claude clicks, types, and opens apps on your
  computer when connectors or the browser can't do the job. Pro and Max only,
  in the desktop app on macOS and Windows. [11]
- **Claude in Chrome**: a browser extension that reads pages, clicks, types,
  navigates, and fills forms. **[changed]** It became generally available on
  every paid plan on 2026-08-26, after a pilot. [12][13]

## Sources

1. [Claude Code overview](https://code.claude.com/docs/en/overview)
2. [Create custom subagents](https://code.claude.com/docs/en/sub-agents)
3. [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams)
4. [How Claude remembers your project (memory)](https://code.claude.com/docs/en/memory)
5. [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)
6. [Code Review](https://code.claude.com/docs/en/code-review)
7. [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
8. [Claude Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview)
9. [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
10. [Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)
11. [Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)
12. [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
13. [Claude in Chrome is generally available](https://claude.com/blog/claude-in-chrome-generally-available)
