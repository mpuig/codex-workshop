# Reading Diffs

> **Type:** Reference | **Prerequisites:** None

## What Is a Diff?

When OpenAI Codex edits a file, it shows you a **diff** -- a side-by-side comparison of what changed. Diffs are the standard way software tools show modifications to files.

A diff shows:

- **Lines removed** (prefixed with `-`, shown in red)
- **Lines added** (prefixed with `+`, shown in green)
- **Unchanged lines** for context (no prefix)

Think of it like track changes in a Word document, but for any text file.

---

## How to Read a Diff

Here is a simple example. Suppose Codex updates a claims summary:

```diff
 ## Q3 Claims Summary

-Total claims: 142
-Total incurred: EUR 2.800.000
+Total claims: 158
+Total incurred: EUR 3.150.000

 Average claim size: EUR 19.900
```

**Reading this:**

- The lines starting with `-` (red) are the **old** values being removed
- The lines starting with `+` (green) are the **new** values replacing them
- Lines with no prefix are unchanged -- they provide context so you know where the change is

In this case, OpenAI Codex updated the claims count from 142 to 158 and the incurred amount from EUR 2.800.000 to EUR 3.150.000. The average claim size line was not changed.

---

## Walkthrough: Updating Numbers in a Report

**Scenario:** You asked OpenAI Codex to update the motor portfolio loss ratios with Q4 data.

```diff
 ## Motor Portfolio - Loss Ratios by Region

 | Region | Earned Premium | Incurred Claims | Loss Ratio |
 |--------|---------------|-----------------|------------|
-| Catalonia | EUR 12.400.000 | EUR 8.680.000 | 70,0% |
-| Madrid | EUR 9.100.000 | EUR 5.915.000 | 65,0% |
-| Andalusia | EUR 7.300.000 | EUR 5.110.000 | 70,0% |
+| Catalonia | EUR 14.200.000 | EUR 10.224.000 | 72,0% |
+| Madrid | EUR 10.800.000 | EUR 6.804.000 | 63,0% |
+| Andalusia | EUR 8.500.000 | EUR 6.120.000 | 72,0% |
 | Portugal Norte | EUR 3.200.000 | EUR 2.080.000 | 65,0% |
```

**What to check:**

1. The three updated regions (Catalonia, Madrid, Andalusia) show new premium, claims, and ratio figures
2. Portugal Norte was not changed -- it stays on an unchanged line
3. Verify the ratios make sense: EUR 10.224.000 / EUR 14.200.000 = 72,0% -- correct

---

## Walkthrough: Restructuring a Section

**Scenario:** You asked OpenAI Codex to reorganize an executive summary from paragraphs to bullet points.

```diff
 ## Executive Summary

-The commercial property portfolio experienced a challenging quarter driven
-by an increase in fire-related claims in the Valencia region. Total
-incurred claims rose by 18% compared to Q2, primarily due to three large
-losses exceeding EUR 500.000 each. The combined ratio for the line
-deteriorated to 102,3%, above our target of 95%.
+- **Total incurred claims** rose 18% vs. Q2, driven by fire claims in Valencia
+- **Three large losses** exceeded EUR 500.000 each, accounting for 40% of total incurred
+- **Combined ratio** deteriorated to 102,3% (target: 95,0%)
+- **Action required:** review fire risk concentration in Valencia region
```

**What to check:**

1. The paragraph (4 red lines) was replaced with 4 bullet points (4 green lines)
2. The key facts are preserved: 18% increase, three large losses, 102,3% combined ratio
3. OpenAI Codex added a new action item -- decide if that is appropriate or if it should be removed

---

## How to Accept or Reject Changes

When Codex shows you a diff in **Edit mode**:

- **Accept** the change by pressing **Enter** or typing `y`
- **Reject** the change by pressing **Escape** or typing `n`
- **Ask for explanation** before deciding: type "explain what you changed and why"

> **Tip:** If you are unsure about a change, ask Codex to explain before accepting. You can say: "Walk me through each change in that diff before I accept it."

---

## Common Situations

| Diff pattern | What it means | What to check |
|-------------|---------------|---------------|
| Few lines changed | Small, targeted update | Verify the new values are correct |
| Major rewrite (many red, many green) | Section was restructured | Ensure no information was lost |
| Only green lines (additions) | New content added | Check it belongs in that location |
| Only red lines (deletions) | Content removed | Confirm you wanted it removed |
| Same line count, different content | In-place replacement | Compare old vs. new carefully |

---

## Key Takeaways

- `-` (red) = removed, `+` (green) = added, no prefix = unchanged context
- Always verify numbers and calculations in updated tables
- When a section is restructured, check that no information was lost
- Use Edit mode so you can review diffs before they are applied
- Ask OpenAI Codex to explain changes if anything looks unexpected
