# Context Window Management

> **Type:** Reference | **Prerequisites:** None

## What the Context Window Is

The context window is Codex's working memory for the current session. It includes recent messages, relevant file content, and instructions.

As sessions get longer, responses can become slower and less precise because more context has to be carried forward.

---

## Signals You Should Restart the Session

- Responses are noticeably slower.
- Codex repeats earlier suggestions.
- Codex misses constraints you already gave.
- You are switching to a different task/domain.

---

## Recommended Workflow

1. Finish one task and save outputs to files.
2. Start a new Codex session in the same project folder.
3. Continue with the next task using saved files as explicit inputs.

This keeps context focused and reduces token waste.

---

## AGENTS.md and Session Restarts

`AGENTS.md` remains your persistent project instruction source. Keep stable rules there so they are available every new session.

Examples:

- Formatting conventions
- Terminology standards
- Compliance guardrails
- Output quality criteria

---

## Cost/Quality Tradeoff

Many short, focused sessions are usually cheaper and higher quality than one long, overloaded session.

---

## Key Takeaways

- Treat sessions as task-scoped, not day-scoped.
- Save intermediate artifacts early.
- Restart sessions intentionally between major work phases.
- Keep durable instructions in `AGENTS.md`.
