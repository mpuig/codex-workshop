# Exercise 0: Executive Onramp (Zero to One)

**Duration:** ~90 minutes  
**Difficulty:** Beginner to Intermediate  

---

## Objective

Get from zero to practical value with OpenAI Codex in one session.

This exercise is designed for senior consulting profiles who are:

- Interested in generative AI and tools like OpenAI Codex or Codex
- Strong in business judgment but not hands-on with coding
- Looking for immediate, client-ready outcomes

By the end of this exercise, you will have:

1. Produced high-quality outputs using copy/paste prompts
2. Learned a repeatable prompt framework for executive work
3. Practiced iterative refinement and critical challenge
4. Built a personal "prompt playbook" for client delivery

---

## Exercise Design: Two Blocks

### Block A: Copy/Paste Wins

Fast confidence wins. You copy prompts exactly, get strong results, and see what good looks like.

### Block B: Guided Thinking

Progressive challenge. We remove scaffolding step by step so you decide what to ask and how to steer output quality.

---

## Prerequisites

- OpenAI Codex installed and configured
- Terminal open in the repository root
- No coding experience required

Recommended folder context:

```text
<your-project-folder>/codex-workshop
```

---

## Working Data (No Additional Data Setup Needed)

Use existing repository context files:

- `company-context/COMPANY.md`
- `company-context/MARKET.md`
- `company-context/PERSONAS.md`
- `company-context/PRODUCTS.md`

These files provide enough business context to create executive-grade outputs without writing code.

---

## Block A: Copy/Paste Wins

### Step A1: Board-ready summary (~10 min)

**Goal:** Generate a concise board briefing from source files.

**Prompt to copy/paste:**

```text
Read company-context/COMPANY.md, company-context/MARKET.md, and company-context/PRODUCTS.md.
Create a one-page board briefing for MIG's executive committee with:
1) Current position (where MIG stands now)
2) Top 3 opportunities in the next 12 to 18 months
3) Top 3 risks in the next 12 to 18 months
4) 5 concrete actions for the next quarter

Constraints:
- Maximum 300 words
- Use bullet points
- Include specific numbers where available
- Keep language direct and non-technical
```

**What to look for:**

- Clear structure and concise language
- Specific facts and numbers
- Action-oriented recommendations

---

### Step A2: Turn insight into a 3-slide storyline (~10 min)

**Goal:** Move from analysis to client communication.

**Prompt to copy/paste:**

```text
Using the previous board briefing, create a 3-slide storyline for a Partner update.

Format:
- Slide 1: Situation and why it matters now
- Slide 2: What is changing in the market and where MIG should play
- Slide 3: Recommended decisions and next 90-day plan

For each slide provide:
- Slide title
- 3 to 4 bullets
- Speaker notes (2 to 3 lines)
```

**What to look for:**

- Tight narrative flow across slides
- Business language suitable for clients and steering committees
- Clear "so what" on every slide

---

### Step A3: Draft a senior stakeholder email (~10 min)

**Goal:** Convert the storyline into executive communication.

**Prompt to copy/paste:**

```text
Draft an email from a Managing Director to a client CEO.

Context:
- Purpose: align on priority decisions before next steering committee
- Tone: confident, concise, practical
- Length: 180 to 220 words

Include:
1) A sharp opening with context
2) Three recommendations (business-focused)
3) A clear ask for the upcoming meeting
4) Subject line options (3)
```

**What to look for:**

- Credible executive tone
- No generic filler
- Explicit decision asks

---

### Step A4: Stress-test the recommendation (~10 min)

**Goal:** Use Codex as a thinking challenger, not only a drafting tool.

**Prompt to copy/paste:**

```text
Challenge the recommendations you just gave me.

Provide:
1) The 5 strongest objections a skeptical CFO or COO could raise
2) For each objection: why it is valid, what evidence is missing, and how to address it
3) A revised recommendation set that is more robust

Be direct. Avoid polite filler.
```

**What to look for:**

- Quality of counterarguments
- Evidence gaps identified clearly
- Improved recommendations after challenge

---

## Block B: Guided Thinking

This block progressively removes scaffolding.

### Step B1: Fill-in prompt framework (~15 min)

**Goal:** Learn a reusable prompt structure for executive work.

Use this template and complete the blanks:

```text
You are my [ROLE].
Task: [WHAT YOU NEED]
Audience: [WHO WILL READ THIS]
Decision needed: [WHAT DECISION SHOULD BE MADE]
Context files: [FILES OR FACTS]
Constraints:
- Length: [X words]
- Tone: [TONE]
- Format: [TABLE / BULLETS / EMAIL / SLIDE OUTLINE]
- Must include: [NUMBERS, RISKS, ASSUMPTIONS, OPTIONS]

Before answering:
1) Ask up to 3 clarifying questions if needed
2) State assumptions
3) Then provide the deliverable
```

**Practice prompt:**

```text
Apply this template to produce a steering committee pre-read for MIG's Portugal growth plan.
```

---

### Step B2: Improve a weak prompt (~15 min)

**Goal:** Build prompt quality judgment.

Start with this weak prompt:

```text
Can you analyze MIG and tell me what to do in Portugal?
```

Your task:

1. Rewrite it into a high-quality executive prompt
2. Explain why your rewritten version is better
3. Run your rewritten prompt

**Quality checklist:**

- Specific objective
- Explicit audience
- Decision framing
- Output format constraints
- Data/context references

---

### Step B3: Multi-turn refinement (~15 min)

**Goal:** Learn how to iterate in short, high-leverage turns.

Round sequence:

1. Ask for first output  
2. Critique it using this exact structure:  
   - "Keep:"  
   - "Change:"  
   - "Remove:"  
   - "Add:"  
3. Ask for revision with tighter constraints

**Prompt to run:**

```text
Create a decision memo for a Partner meeting on MIG's strategic priorities.
Maximum 400 words.
```

Then refine with:

```text
Revise using this feedback:
Keep: [what worked]
Change: [what needs adjustment]
Remove: [what is unnecessary]
Add: [what is missing]

Constraints:
- Keep under 300 words
- Include 3 quantified assumptions
- End with a clear decision recommendation
```

---

### Step B4: Open challenge (~20 min)

**Goal:** Apply everything with minimal scaffolding.

Scenario:

You have a client steering committee tomorrow. You need a practical briefing pack in 20 minutes.

Your task:

Create your own prompt (no template provided) that asks OpenAI Codex to produce:

- A one-page executive brief
- A risk register (top 8 risks)
- A 90-day action plan with owners

Constraints:

- Must be readable by non-technical executives
- Must include specific numbers from available context
- Must distinguish facts vs assumptions

---

## Scoring (Simple Executive Rubric)

Score each participant on 4 dimensions, each from 0 to 10 (total score: 40):

| Dimension | What "10" Looks Like |
|---|---|
| Clarity of ask | Prompt is precise, scoped, and unambiguous |
| Business relevance | Output is decision-oriented, not generic |
| Actionability | Clear next steps, owners, and timeline |
| Critical thinking | Risks, assumptions, and trade-offs are explicit |

Suggested interpretation:

- 32-40: Strong executive operator
- 24-31: Good foundation, improve prompt precision
- <24: Repeat Block B with tighter constraints

---

## Common Pitfalls (And Fixes)

1. **Prompt too broad**
- Fix: add audience, decision, format, and word limit.

2. **Output sounds generic**
- Fix: require specific numbers and named assumptions.

3. **No decision recommendation**
- Fix: explicitly ask for a recommendation and rationale.

4. **Too much text, low signal**
- Fix: request bullets, max length, and a prioritized top-5.

5. **No challenge of first draft**
- Fix: always add one "challenge this recommendation" turn.

---

## Facilitator Notes (Optional)

For workshop delivery:

- Run Block A in plenary (fast momentum, shared confidence)
- Run Block B in pairs (peer critique improves prompt quality)
- End with 5-minute playback per participant:  
  "Best prompt I wrote" and "biggest improvement I made"

---

## Deliverables to Keep

By the end, each participant should save:

1. `executive_brief.md`
2. `three_slide_storyline.md`
3. `stakeholder_email.md`
4. `risk_challenge.md`
5. `my_prompt_playbook.md` (top 5 reusable prompts)

---

## Next Step

After Exercise 0, continue with:

- `exercises/exercise-1-data-insight-tool/` for structured data analysis
- `exercises/exercise-2-claims-triage/` for rule-driven process automation
- `exercises/exercise-3-automated-reporting/` for full reporting automation
