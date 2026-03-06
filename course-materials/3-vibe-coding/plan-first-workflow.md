# The "Plan First" Workflow

> **Type:** Reference | **Prerequisites:** [Building an Insurance App](README.md)

In the [previous section](README.md) you used `Shift+Tab` to switch to Plan mode -- a quick way to ask Codex to show its approach before acting. That works well for focused tasks like "add a filter to the dashboard."

For larger projects, Plan mode alone is not enough. Building a claims triage tool from scratch, adding a full reporting section, or restructuring a multi-page dashboard needs a stricter workflow so you stay in control of key decisions.

This is the **"Plan First" workflow**: separate planning from execution so that Codex never builds anything you have not reviewed and approved first.

*(Note: This workflow is adapted from the community-driven [Boris Tane workflow](https://boristane.com/blog/how-i-use-claude-code/).)*

---

## The Core Principle: Never Build Without an Approved Plan

A common pattern is to describe what you want, wait for the result, discover it is wrong, and repeat. This wastes time and tokens. For anything beyond a simple change, follow this structured pipeline instead:

**Research -> Plan -> Annotate -> Implement -> Iterate**

### Phase 1: Research

Before making any changes, ask Codex to study the relevant parts of your project and write up its findings.

**Sample Prompt:**
> "Read the entire dashboard project in depth. Understand how the charts, filters, and data flow work. When you are done, write a detailed report of your findings in `research.md`."

**Why this matters:**
Without explicit instructions to read thoroughly and document its understanding, Codex may skim the surface. The `research.md` file gives you a concrete artifact to review before any code changes begin.

### Phase 2: Planning

Once you confirm the research is accurate, ask for an implementation plan.

**Sample Prompt:**
> "I want to add a reinsurance treaty comparison section to the dashboard. It should show a table of treaty structures, a bar chart comparing retention levels, and a summary card with the total ceded premium. Write a detailed `plan.md` document outlining how to implement this. Do not implement yet."

The output should be a detailed markdown file that explains the approach, lists which files will change, and notes key trade-offs. You can reference existing components (for example: "Follow the same approach as the existing claims-by-region chart").

### The Annotation Cycle

This is where you add the most value. Do not steer the implementation through chat messages. Instead:

1. Open `plan.md` in your text editor.
2. Add notes directly into the document (e.g., "Use EUR formatting here", "No, this should show gross written premium not net", "Remove this section -- we do not need the trend chart").
3. Go back to OpenAI Codex and say:
   > "I added a few notes to the plan. Address all the notes and update the document accordingly. **Do not implement yet.**"

Repeat this 1 to 3 times until the plan matches your expectations. The markdown file becomes shared, editable context that is easier to review than a long chat history.

### The Todo List

Before implementation begins, ask Codex to add a checklist:

> "Add a detailed todo list to the plan, with all the phases and individual tasks necessary to complete the plan. Do not implement yet."

This gives you a progress tracker during the actual building phase.

### Phase 3: Implementation

When the plan is right, give Codex the go-ahead. Since all decisions have been made, execution becomes straightforward.

**Sample Prompt:**
> "Implement it all. When you finish a task or phase, mark it as completed in the plan document. Do not stop until all tasks and phases are completed."

If Codex makes a mistake during execution, give brief feedback ("the chart should be wider", "wrong folder, move it to the reports section"). Because Codex has the full plan context, short corrections are usually enough.

---

## When to Use This vs. Plan Mode

| Situation | Use |
|-----------|-----|
| Add a single chart to an existing dashboard | `Shift+Tab` Plan mode |
| Fix a layout issue or change colours | Direct prompt (no planning needed) |
| Build a new multi-section feature | Plan First workflow |
| Start an app from scratch with 5+ requirements | Plan First workflow |
| Restructure an existing project | Plan First workflow (start with Research) |

The rule of thumb: if you can describe the task in 2-3 sentences, Plan mode is fine. If you need a paragraph or more, use Plan First.

---

## Why This Works

- **Scope Control:** The "Do not implement yet" guardrail prevents Codex from going down the wrong path and wasting your time and tokens.
- **Shared Context:** `plan.md` is a persistent file that you can edit and review as a whole, rather than losing decisions in a long chat thread.
- **Context Window Efficiency:** Even when the conversation gets long, the plan document survives context compaction in full fidelity.
- **Your Expertise Matters:** The annotation cycle is where your domain knowledge -- insurance products, regulatory requirements, business logic -- shapes the result. Codex handles the technical how; you decide the what.

The creative work happens during the annotation cycle. Implementation should be boring.

---

## Next Step

Proceed to [Building Skills](building-skills.md) to learn how to package repeatable workflows into reusable skill files.
