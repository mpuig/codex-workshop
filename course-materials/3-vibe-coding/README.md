# Module 3: Building an Insurance App with Vibe Coding

> **Time:** 45 minutes | **Prerequisites:** Completion of Modules 1 and 2

## What Is Vibe Coding?

Vibe coding is building software by describing what you want in natural language. You are the product owner. Codex is the developer. You do not write a single line of code -- you describe features, review results, and iterate.

This is not a gimmick. Non-technical professionals are building real, functional applications this way. In this module, you will build a **Claims Dashboard** for MIG -- a web application that visualizes claims data with charts, filters, and summaries.

**You do not need to understand code.** You need to know what you want the app to do.

---

## The Project: MIG Claims Dashboard

You will build a web application that:

- Displays a summary of MIG's claims (total count, total value, average claim size)
- Shows charts: claims by type, claims by region, claims by status
- Lets you filter by date range, region, and claim type
- Has a clean, professional look suitable for internal use

By the end of this module, you will have a working app running on your computer.

---

## Step 1: Define Requirements

Start by telling Codex exactly what you want. Think like a product owner writing a brief.

### Sample prompt:

```text
I want to build a Claims Dashboard web application for Mediterranean
Insurance Group. I have zero coding experience, so you will handle all
the technical work. I will describe what I want, and you will build it.

Here are my requirements:

OVERVIEW:
- A web-based dashboard that displays MIG's claims data
- Should work in a browser (Chrome, Safari, Firefox)
- Professional design with MIG branding (use navy blue #1B365D and
  white as primary colors, with amber #F2A900 for highlights)

DATA:
- Create realistic sample data: 200 claims for MIG across 2024-2025
- Fields: claim_id, date_of_loss, date_reported, region (Catalonia,
  Madrid, Andalusia, Valencia, Basque Country, Galicia), product_line
  (Motor, Property, Liability, Marine, Health), claim_type, status
  (Open, Under Review, Settled, Denied, Reopened), incurred_amount_eur,
  reserve_amount_eur, claimant_name
- Make the data realistic: motor should have the most claims, some
  regions should be worse than others

DASHBOARD LAYOUT:
- Top row: 4 summary cards (Total Claims, Total Incurred, Average Claim
  Size, Open Claims %)
- Middle row: 2 charts side by side
  - Left: bar chart of claims count by region
  - Right: donut chart of claims by status
- Bottom row: 2 charts side by side
  - Left: bar chart of total incurred by product line
  - Right: line chart showing monthly claims trend over time
- Below the charts: a filterable data table showing all claims

FILTERS:
- Dropdown to filter by region
- Dropdown to filter by product line
- Date range picker for date of loss
- All charts and the table should update when filters are applied

Start by setting up the project. Use whatever technology you think is
best for a simple, self-contained dashboard that I can run locally.
```

> **Tip:** Be thorough in your initial requirements. The more specific you are, the better the first version will be. But do not worry about getting everything perfect -- you will iterate.

---

## Step 2: Let Codex Build It

After you submit your requirements, Codex will:

1. Choose an appropriate technology (likely a simple HTML/CSS/JavaScript app, or a Next.js project)
2. Create the project files
3. Generate the sample data
4. Build the dashboard with charts and layout

This may take a minute or two. Codex will explain what it is doing as it works.

### What to expect:

Codex will create several files and may ask you to confirm before proceeding. If you are in **Auto-accept** mode (Shift+Tab), it will proceed without asking.

When Codex finishes, it will tell you how to view the dashboard. Typically:

```text
Open the file dashboard.html in your browser, or run the following
command to start a local server...
```

**Open the file in your browser** and take a look at what Codex built.

---

## Step 3: Iterate on the UI

The first version will be functional but probably not exactly what you envisioned. This is normal. Now you iterate.

### Sample refinement prompts:

**Fix the layout:**
```text
The dashboard looks good but I want some changes:
- Make the summary cards at the top larger with bigger numbers
- Add a EUR symbol and European number formatting to all monetary values
- The charts are too small -- make them taller
- Add the MIG logo text "Mediterranean Insurance Group" in the header
```

**Improve the design:**
```text
The design needs to feel more polished:
- Add subtle shadows to the summary cards
- Use a light gray background (#F5F6FA) instead of white
- Make the header bar navy blue with white text
- Add a subtle border between sections
- The font should be clean and modern (use Inter or Segoe UI)
```

**Fix data display:**
```text
In the claims table at the bottom:
- Format all EUR amounts with European number formatting (1.234,56)
- Add alternating row colors for readability
- Make the status column show colored badges (green for Settled,
  amber for Under Review, red for Open, gray for Denied)
- Sort by date of loss descending by default
- Add pagination -- show 20 rows per page
```

---

## Step 4: Add Features

Once the basic dashboard looks right, add more functionality.

### Add data visualizations:

```text
Add a new section below the existing charts with:

1. A heat map table showing average claim size by region (rows) and
   product line (columns). Color cells from green (low) through yellow
   to red (high).

2. A bar chart showing the top 10 largest claims with their IDs and
   amounts.

3. A combined ratio estimate card -- assume a 30% expense ratio and
   calculate the combined ratio based on the claims data and an assumed
   EUR 150M earned premium.
```

### Add interactivity:

```text
When I click on a bar in the "claims by region" chart, the entire
dashboard should filter to show only that region's data. Clicking
again should reset the filter.
```

### Add an export feature:

```text
Add an "Export to CSV" button that downloads the currently filtered
claims data as a CSV file. Put the button next to the data table.
```

### Add a detail view:

```text
When I click on a row in the claims table, show a detail panel on the
right side with all the claim information in a nicely formatted card.
Include a timeline showing: date of loss, date reported, date of last
update.
```

---

## Step 5: Save to GitHub (Optional)

If you want to save your project and share it with colleagues, Codex can help you set up a GitHub repository.

### Sample prompt:

```text
Help me save this project to GitHub. I have a GitHub account but I have
never created a repository from the command line. Walk me through it
step by step.
```

Codex will guide you through:
1. Initializing a git repository
2. Creating a `.gitignore` file
3. Making your first commit
4. Creating a remote repository on GitHub
5. Pushing your code

---

## Step 6: Deploy (Optional)

If you want your dashboard accessible via a URL (so colleagues can view it without installing anything), Codex can help you deploy it.

### Sample prompt:

```text
I want my colleagues to be able to see this dashboard without
installing anything. What is the simplest way to deploy this as a
website they can access via a URL? I want free or very cheap hosting.
```

Codex will likely suggest options like:

- **GitHub Pages** (free, good for static HTML dashboards)
- **Vercel** (free tier, good for Next.js apps)
- **Netlify** (free tier, simple drag-and-drop deployment)

It will walk you through the deployment step by step.

---

## Mindset Tips: Think Like a PM, Not a Coder

| Do this | Not this |
|---------|----------|
| "I want a chart showing claims by region" | "Create a div with a canvas element and initialize Chart.js with..." |
| "The colors don't match our brand" | "Change the hex values in the CSS file on line 47" |
| "This is too slow when filtering" | "Optimize the JavaScript array filter function" |
| "I want users to be able to drill down into a region" | "Add an onClick event handler to each bar element" |
| "Something broke, the chart isn't showing" | (Panic) |

**You describe the what. Codex handles the how.**

---

## What to Do When Something Breaks

Things will break. A chart might not render. A filter might stop working. The layout might look wrong. This is completely normal in software development. Here is how to handle it:

### Step 1: Describe the problem

```text
Something is wrong. The bar chart for claims by region is not showing
any data. The other charts work fine. The filter dropdowns are all set
to "All". Can you fix it?
```

### Step 2: Let Codex diagnose and fix

Codex will look at the code, identify the issue, and fix it. You do not need to understand what went wrong technically.

### Step 3: If it is still broken, give more context

```text
It's still not working. Here is what I see: the chart area is blank,
there is a small error icon in the bottom left of my browser. The
region filter dropdown does show all 6 regions correctly. This
started happening after you added the heat map in the last change.
```

### Step 3,5: Clear the conversation if Codex is going in circles

If Codex seems to be repeating the same fix or going in circles, type `/clear` to reset the conversation. This gives Codex a fresh perspective on the current state of your files without the baggage of a long debugging history. Your files on disk are not affected -- only the chat history is cleared. (Your AGENTS.md rules are automatically reloaded.)

### Step 4: If you are stuck, start a fresh section

```text
Let's start the charts section from scratch. Keep all the data and
the summary cards at the top, but rebuild the chart section. Use a
simpler approach this time.
```

### The golden rule: **Do not try to debug the code yourself.** Describe what you see, what you expected, and when it started. Let Codex handle the rest.

---

## What You Can Build Next

Once you are comfortable with vibe coding, the possibilities expand significantly:

| Project Idea | Complexity | Time Estimate |
|-------------|-----------|---------------|
| Policy renewal tracker | Simple | 30 min |
| Risk assessment questionnaire (web form) | Simple | 30 min |
| Portfolio exposure map (with geographic visualization) | Medium | 45 min |
| Underwriting referral workflow tool | Medium | 1 hour |
| Claims triage scoring tool | Medium | 1 hour |
| Reinsurance treaty comparison calculator | Medium | 1 hour |
| Client reporting portal | Advanced | 2 hours |

For any of these, the approach is the same: describe what you want, let Codex build it, iterate until it is right. For medium and advanced projects, consider the [Plan First workflow](plan-first-workflow.md) to stay in control as complexity grows. If you find yourself repeating the same workflows, package them as [reusable skills](building-skills.md).

---

## Summary

In this module you learned to:

- Describe a software application in natural language
- Let Codex handle all technical implementation
- Iterate on design, functionality, and features through conversation
- Handle errors and breakages without technical knowledge
- Optionally save and deploy your application

The key takeaway: **You do not need to be a developer to build useful tools.** With OpenAI Codex, the skill that matters is clearly describing what you need -- which is exactly what you do as a consultant every day. The ability to quickly prototype dashboards, calculators, and workflow tools is a genuine superpower for non-technical professionals.

---

## Next Step

Proceed to the [Course Wrap-Up](../4-wrap-up/README.md) for a summary of what you have learned and what to do next.
