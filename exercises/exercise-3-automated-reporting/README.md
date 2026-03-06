# Exercise 3: Automated Reporting Solution

## Mediterranean Insurance Group (MIG) - Quarterly Claims Report Automation

---

## Objective

Review existing quarterly claims datasets, define a standard periodic report structure, automatically generate a structured quarterly claims report, and demonstrate how to update it when new data arrives -- all without manual rework.

By the end of this exercise you will have:

1. Explored and understood four quarters of claims data.
2. Defined a reusable report structure with precise key performance indicator (KPI) formulas.
3. Generated a full Q4 2025 quarterly claims report in Markdown.
4. Created an HTML companion with interactive charts.
5. Simulated a new quarter arriving and regenerated the report effortlessly.
6. Built a Python automation script Pierre can run every quarter.

**Estimated total time: 55 minutes**

---

## Background

Pierre Dupont is an Actuarial Analyst based in MIG's Marseille office. Every quarter he spends nearly two full days manually assembling the claims report for senior management. The process involves:

- Pulling data from four CSV extracts (one per quarter).
- Calculating KPIs by hand in spreadsheets.
- Writing commentary about trends and anomalies.
- Formatting everything into a presentable document.
- Rebuilding charts from scratch each time.

Pierre wants to automate this end-to-end. When new quarterly data lands in the `data/` folder, the report and charts should regenerate automatically with updated numbers, trends, and commentary -- zero manual rework.

---

## Prerequisites

- OpenAI Codex CLI installed and configured.
- A terminal open in this exercise folder (`exercise-3-automated-reporting/`).
- Python 3.9+ available (for the final automation script).

---

## Data Overview

The `data/` folder contains:

| File | Description |
|------|-------------|
| `claims_q1_2025.csv` | Q1 2025 claims data (Jan -- Mar) |
| `claims_q2_2025.csv` | Q2 2025 claims data (Apr -- Jun) |
| `claims_q3_2025.csv` | Q3 2025 claims data (Jul -- Sep) |
| `claims_q4_2025.csv` | Q4 2025 claims data (Oct -- Dec) |
| `report_template.md` | Report structure template with KPI definitions |

Each CSV contains 120-150 individual claims across MIG's four markets (Spain, France, Italy, Portugal) and five product lines (Motor, Home, Health, Commercial, Life).

---

## Step-by-Step Instructions

### Step 1: Explore the Data (~5 min)

**Goal:** Understand what data is available before building anything.

Open OpenAI Codex in this exercise directory and type the following prompt:

```text
Read all CSV files in the data/ folder and the report template. Give me a summary of what data we have across the 4 quarters, including total claims, total amounts, and any notable patterns you see at first glance.
```

**What to expect:**

OpenAI Codex will read all four CSV files and the report template, then produce a summary similar to:

- Total number of claims per quarter (expect 120-150 each).
- Grand totals for reported amounts, paid amounts, and reserves.
- A note about which product lines and regions appear most frequently.
- Early observations on seasonal patterns (e.g., more motor claims in Q1/Q4).

**What to look for:**

- Does Codex correctly identify all four quarters?
- Does it flag the seasonal differences?
- Does it mention the fraud flags and claim statuses?

<details>
<summary>💡 Example output from this step</summary>

**Quarterly Overview:**

```
Quarter      Claims    Reported (EUR)        Paid (EUR)      Reserved (EUR)
--------------------------------------------------------------------------------
Q1 2025         132      2.060.150,00        596.750,00         502.650,00
Q2 2025         126      1.665.250,00        393.850,00         437.900,00
Q3 2025         136      2.351.800,00        560.350,00         768.450,00
Q4 2025         133      2.092.150,00        562.700,00         578.550,00
--------------------------------------------------------------------------------
TOTAL           527      8.169.350,00      2.113.650,00       2.287.550,00
```

**Claims by Product Line (all quarters):**

| Product Line | Count | Reported (EUR) | Paid (EUR) |
|-------------|-------|---------------|-----------|
| Motor | 180 | 1.681.300 | 583.350 |
| Home | 125 | 1.695.200 | 521.400 |
| Health | 113 | 752.800 | 272.900 |
| Commercial | 66 | 2.301.150 | 394.000 |
| Life | 43 | 1.738.900 | 342.000 |

**Claims by Country (all quarters):**

| Country | Count | Reported (EUR) | Paid (EUR) |
|---------|-------|---------------|-----------|
| Spain | 163 | 2.285.550 | 593.950 |
| France | 159 | 2.420.950 | 715.050 |
| Italy | 125 | 1.808.850 | 432.800 |
| Portugal | 80 | 1.654.000 | 371.850 |

**Status Distribution:** Paid 51,8% | Open 15,9% | Reserved 13,7% | Under Investigation 10,4% | Denied 8,2%

**Fraud Flags:** Clean 95,8% | Suspected 2,7% | Confirmed 1,5%

**Seasonal Pattern (Motor claims per quarter):**
- Q1 2025: 54 Motor claims (41% of quarter) -- winter peak
- Q2 2025: 38 Motor claims (30% of quarter) -- seasonal low
- Q3 2025: 37 Motor claims (27% of quarter) -- seasonal low
- Q4 2025: 51 Motor claims (38% of quarter) -- winter peak

</details>

---

### Step 2: Define the Report Structure (~10 min)

**Goal:** Establish a precise, reusable report blueprint before generating content.

Type the following prompt:

```text
Based on report_template.md, create a comprehensive quarterly claims report structure.
Include these sections:
1) Executive Summary
2) Key KPIs (total claims, total paid, average claim cost, loss ratio, claims frequency)
3) Trends vs previous quarter and year-over-year (YoY)
4) Breakdown by product line
5) Breakdown by region
6) Top 10 largest claims
7) Fraud detection summary
8) Recommendations
Define the exact KPI formulas.
```

**What to expect:**

A detailed report blueprint that includes:

- Section-by-section outline with descriptions of what goes in each.
- KPI definitions with explicit formulas, for example:
  - **Loss Ratio** = Total Paid Amount / Total Reported Amount
  - **Average Claim Cost** = Total Paid Amount / Number of Settled Claims
  - **Claims Frequency** = Number of Claims / Number of Active Policies (estimated)
  - **Settlement Rate** = Settled Claims / Total Claims
  - **Denial Rate** = Denied Claims / Total Claims
- Trend calculation methodology (quarter-over-quarter, QoQ, and year-over-year, YoY).
- Table formats for the product line and region breakdowns.

**What to look for:**

- Are the KPI formulas precise and unambiguous?
- Does the structure cover all eight sections requested?
- Is the format professional enough for senior management?

<details>
<summary>💡 Example output from this step</summary>

**Report Blueprint (8 sections):**

```
1. Executive Summary          -- 3-5 sentence overview, key highlights
2. Key Performance Indicators -- Dashboard table with QoQ and YoY comparisons
3. Trend Analysis             -- Four-quarter rolling view, commentary
4. Product Line Breakdown     -- Motor, Home, Health, Commercial, Life
5. Regional Breakdown         -- Spain, France, Italy, Portugal
6. Top 10 Largest Claims      -- Ranked by reported amount
7. Fraud Detection Summary    -- Confirmed, suspected, by product line
8. Recommendations            -- 3-5 data-driven priority actions
```

**KPI Definitions with Formulas:**

| KPI | Formula | Target |
|-----|---------|--------|
| Total Claims Count | Count of all claims filed in the quarter | Monitoring |
| Total Reported Amount | SUM(reported_amount_eur) | Monitoring |
| Total Paid Amount | SUM(paid_amount_eur) | Monitoring |
| Average Claim Cost | Total Paid / Count of Paid claims | Varies by product |
| Loss Ratio | Total Paid / Total Reported x 100 | See targets below |
| Settlement Rate | Count of Paid / Total Claims x 100 | > 60% |
| Denial Rate | Count of Denied / Total Claims x 100 | < 10% |
| Avg Resolution Days | AVG(resolution_days) for settled claims | < 45 days |
| Open Claims Ratio | (Open + Reserved) / Total Claims x 100 | < 30% |
| Fraud Detection Rate | (Suspected + Confirmed) / Total Claims x 100 | Monitoring |

**Loss Ratio Targets:**

| Product Line | Target | Acceptable Range |
|-------------|--------|------------------|
| Motor | 65% | 60% -- 72% |
| Home | 55% | 48% -- 62% |
| Health | 70% | 63% -- 78% |
| Commercial | 50% | 42% -- 58% |
| Life | 40% | 33% -- 48% |

</details>

---

### Step 3: Generate the Q4 2025 Report (~15 min)

**Goal:** Produce a complete, professional quarterly claims report.

Type the following prompt:

```text
Generate the full Q4 2025 Quarterly Claims Report using all available data. Compare Q4 to Q3 and to Q4 of the previous periods. Include all sections defined in the structure. Calculate all KPIs. Add professional commentary explaining the trends. Save as quarterly_report_Q4_2025.md
```

**What to expect:**

A complete Markdown file (`quarterly_report_Q4_2025.md`) containing:

- **Executive Summary:** 3-5 sentence overview of the quarter's performance.
- **KPI Dashboard:** Table with current quarter values, QoQ change (%), and YoY indicators.
- **Trend Analysis:** Commentary explaining why metrics moved (e.g., "Motor claims rose 12% QoQ, consistent with winter seasonal patterns").
- **Product Line Breakdown:** Table showing claims count, total paid, average cost, and loss ratio per product line.
- **Regional Breakdown:** Table showing performance across Spain, France, Italy, and Portugal.
- **Top 10 Largest Claims:** List with claim ID, product line, region, amount, and status.
- **Fraud Summary:** Count of suspected and confirmed fraud cases, amounts involved, detection rates.
- **Recommendations:** Data-driven suggestions for management action.

**What to look for:**

- Are the numbers accurate? Spot-check a few by looking at the CSV.
- Is the commentary insightful or generic?
- Does the report compare Q4 to Q3 and to earlier quarters?
- Is the tone appropriate for senior management?

<details>
<summary>💡 Example output from this step</summary>

**Executive Summary excerpt:**

> Q4 2025 recorded 133 claims with EUR 562.700,00 in total paid amounts, representing a -2,2% change in volume versus Q3 2025. The overall loss ratio stands at 26,9%, compared to 23,8% in the prior quarter. The settlement rate of 56,4% is below the 60% target. Commercial lines require attention due to significant reserve accumulation, while Motor claims show typical winter seasonal elevation.

**KPI Dashboard:**

| KPI | Q4 2025 | Q3 2025 | QoQ Change | Q1 2025 | Trend |
|-----|---------|---------|------------|---------|-------|
| Total Claims | 133 | 136 | -2,2% | 132 | Stable |
| Total Reported | EUR 2.092.150 | EUR 2.351.800 | -11,0% | EUR 2.060.150 | Monitoring |
| Total Paid | EUR 562.700 | EUR 560.350 | +0,4% | EUR 596.750 | Monitoring |
| Avg Claim Cost | EUR 7.503 | EUR 8.240 | -9,0% | EUR 8.907 | Monitoring |
| Loss Ratio | 26,9% | 23,8% | +12,9% | 29,0% | Monitoring |
| Settlement Rate | 56,4% | 50,0% | +12,8% | 50,8% | Monitoring |
| Denial Rate | 6,0% | 11,0% | -45,5% | 6,8% | Monitoring |
| Avg Resolution Days | 34 | 36 | -3,0% | 32 | Monitoring |

**Product Line Breakdown:**

| Product Line | Claims | Total Paid (EUR) | Avg Cost (EUR) | Loss Ratio | vs Target |
|-------------|--------|-----------------|---------------|------------|-----------|
| Motor | 51 | 119.100 | 4.411 | 32,1% | Below target |
| Home | 29 | 139.950 | 8.232 | 35,7% | Below target |
| Health | 25 | 60.300 | 4.020 | 31,7% | Below target |
| Commercial | 17 | 120.050 | 13.339 | 19,4% | Below target |
| Life | 11 | 123.300 | 17.614 | 23,7% | Below target |

**Top 5 Largest Claims (of 10):**

| Rank | Claim ID | Product | Country | Reported (EUR) | Status |
|------|----------|---------|---------|---------------|--------|
| 1 | CLM-2025-Q4109 | Commercial | Italy | 115.800 | Reserved |
| 2 | CLM-2025-Q4131 | Life | France | 80.850 | Open |
| 3 | CLM-2025-Q4127 | Life | Portugal | 76.800 | Paid |
| 4 | CLM-2025-Q4114 | Commercial | Spain | 76.450 | Paid |
| 5 | CLM-2025-Q4126 | Life | Portugal | 63.400 | Paid |

</details>

---

### Step 4: Create Visualizations (~10 min)

**Goal:** Build a visual companion to the Markdown report.

Type the following prompt:

```text
Create an HTML companion to the report with interactive charts:
1) Claims volume trend across all 4 quarters (line chart)
2) Claims by product line per quarter (stacked bar)
3) Average claim cost by region (horizontal bar)
4) Loss ratio evolution (line chart with target line)
5) Claims status distribution (pie chart)
Save as quarterly_report_charts.html
```

**What to expect:**

An HTML file (`quarterly_report_charts.html`) that:

- Uses a JavaScript charting library (likely Chart.js or similar) loaded from a CDN.
- Contains five distinct, well-labeled charts.
- Uses MIG brand-appropriate colors and professional styling.
- Can be opened directly in any browser -- no server required.
- Includes a header with the report title and quarter.

**What to look for:**

- Open the file in your browser. Do all five charts render?
- Are the numbers consistent with the Markdown report?
- Is the layout clean and presentable?
- Do interactive elements (tooltips, legends) work?

<details>
<summary>💡 Example output from this step</summary>

Codex generates a self-contained HTML file (`quarterly_report_charts.html`) with five Chart.js charts. The file includes:

**Chart 1 -- Claims Volume Trend (line chart):**
Plots total claims per quarter: Q1=132, Q2=126, Q3=136, Q4=133. Shows the seasonal dip in Q2 and recovery in Q3-Q4.

**Chart 2 -- Claims by Product Line (stacked bar):**
Each quarter broken down by Motor, Home, Health, Commercial, and Life. Motor dominates in Q1 (54 claims, 41%) and Q4 (51 claims, 38%), while Q2 and Q3 show more balanced distributions.

**Chart 3 -- Average Claim Cost by Country (horizontal bar, Q4 2025):**
- Portugal: EUR 11.271
- Spain: EUR 8.587
- France: EUR 6.500
- Italy: EUR 6.174

Portugal's higher average is driven by several large Life and Home claims.

**Chart 4 -- Loss Ratio Evolution (line chart with 60% target line):**
All four quarters track well below the 60% overall target: Q1=29,0%, Q2=23,7%, Q3=23,8%, Q4=26,9%. The dashed red target line at 60% provides visual reference.

**Chart 5 -- Claims Status Distribution (pie chart, Q4 2025):**
- Paid: 75 (56,4%)
- Reserved: 23 (17,3%)
- Open: 16 (12,0%)
- Under Investigation: 11 (8,3%)
- Denied: 8 (6,0%)

The file uses MIG brand colours (navy `#1e3a5f`, green `#2d6a4f`, orange `#e07b39`) and can be opened directly in any browser without a server.

</details>

---

### Step 5: Simulate New Data Arrival (~5 min)

**Goal:** Prove that the workflow handles new data without starting from scratch.

Type the following prompt:

```text
Now imagine Q1 2026 data just arrived. Generate a sample Q1 2026 dataset with realistic seasonal patterns (more motor claims in winter, similar volume to Q1 2025 with 5% growth). Save it as claims_q1_2026.csv. Then regenerate the report comparing Q1 2026 to Q4 2025 and Q1 2025.
```

**What to expect:**

1. A new file `data/claims_q1_2026.csv` with ~130-160 claims (5% more than Q1 2025).
2. An updated report (`quarterly_report_Q1_2026.md`) that:
   - Uses Q1 2026 as the current quarter.
   - Compares to Q4 2025 (previous quarter) and Q1 2025 (year-over-year).
   - Recalculates all KPIs with the new data.
   - Provides fresh commentary on the new trends.

**What to look for:**

- Does the Q1 2026 data show realistic winter patterns (elevated motor claims)?
- Does the report correctly identify YoY growth of approximately 5%?
- Did Codex reuse the same report structure, or did it invent a new one?

<details>
<summary>💡 Example output from this step</summary>

**Synthetic Data Generation:**

```
Generated 138 claims for Q1 2026
Growth vs Q1 2025: 138 vs 132 (+4,5%)
```

The generated `claims_q1_2026.csv` follows the same schema as existing files, with realistic seasonal patterns (elevated Motor claims in winter).

**Q1 2026 vs Q4 2025 vs Q1 2025 Comparison:**

| KPI | Q1 2026 | Q4 2025 | QoQ Change | Q1 2025 | YoY Change |
|-----|---------|---------|------------|---------|------------|
| Total Claims | 138 | 133 | +3,8% | 132 | +4,5% |
| Total Paid (EUR) | 1.055.100 | 562.700 | +87,5% | 596.750 | +76,8% |
| Loss Ratio | 26,3% | 26,9% | -2,2% | 29,0% | -9,2% |
| Settlement Rate | 44,2% | 56,4% | -21,6% | 50,8% | -12,9% |
| Avg Claim Cost (EUR) | 17.297 | 7.503 | +130,5% | 8.907 | +94,2% |
| Avg Resolution Days | 42 | 34 | +20,3% | 32 | +29,8% |

**Key Observations:**
- YoY claims growth of +4,5% aligns with the ~5% portfolio expansion target
- Motor share in Q1 2026 = 36%, confirming winter seasonal pattern (Q1 2025 was 41%)
- The report reuses the identical structure from Q4 2025 -- no manual reformatting needed

</details>

---

### Step 6: Build the Automation Script (~10 min)

**Goal:** Create a standalone script Pierre can run each quarter without OpenAI Codex.

Type the following prompt:

```text
Create a Python script called generate_report.py that takes a quarter (e.g., 'Q4_2025') as input and automatically generates both the Markdown report and HTML charts. It should read the relevant data files, calculate all KPIs, and produce the outputs. Pierre should be able to run this whenever new data arrives.
```

**What to expect:**

A Python script (`generate_report.py`) that:

- Accepts a command-line argument for the target quarter (e.g., `python generate_report.py Q4_2025`).
- Reads all available CSV files from the `data/` folder.
- Calculates every KPI from the report structure.
- Generates a Markdown report file.
- Generates an HTML charts file.
- Prints a summary to the console.
- Handles edge cases (missing data, first quarter with no prior period).

**How to verify it works:**

```bash
python generate_report.py Q4_2025
```

This should produce output files matching what OpenAI Codex generated in Steps 3 and 4.

<details>
<summary>💡 Example output from this step</summary>

**Running the script:**

```bash
$ python generate_report.py Q4_2025

MIG Quarterly Claims Report Generator
=====================================
Target quarter: Q4_2025

Loading data from 5 quarterly files...
  Q1 2025: 132 claims loaded
  Q1 2026: 138 claims loaded
  Q2 2025: 126 claims loaded
  Q3 2025: 136 claims loaded
  Q4 2025: 133 claims loaded

KPI Summary for Q4 2025:
  Total Claims:       133
  Total Reported:     EUR 2.092.150,00
  Total Paid:         EUR 562.700,00
  Avg Claim Cost:     EUR 7.502,67
  Loss Ratio:         26,9%
  Settlement Rate:    56,4%
  Denial Rate:        6,0%
  Avg Resolution:     34 days

Markdown report saved: quarterly_report_Q4_2025.md
HTML charts saved:    quarterly_report_Q4_2025_charts.html

Done! Both files generated successfully.
```

**Script capabilities (~250 lines, standard library only):**
- Accepts any quarter as CLI argument (e.g., `Q4_2025`, `Q1_2026`)
- Auto-discovers all CSV files in `data/`
- Computes all KPIs with QoQ and YoY comparisons
- Generates a Markdown report (Executive Summary, KPIs, Product Line, Regional, Top 10)
- Generates an HTML dashboard with 5 Chart.js charts
- No external packages required (`csv`, `os`, `sys`, `json`, `collections`, `datetime`)
- Handles missing prior-period data gracefully (first quarter scenario)

</details>

---

## What You Will Learn

By completing this exercise, you will have practiced:

| Skill | Where It Appears |
|-------|------------------|
| Multi-file data exploration | Step 1 |
| Defining report structures and KPI formulas | Step 2 |
| Automated data analysis across time periods | Step 3 |
| Generating professional reports from raw data | Step 3 |
| Creating data visualizations with code | Step 4 |
| Handling new data without manual rework | Step 5 |
| Building reusable automation scripts | Step 6 |
| Iterative prompting and refinement | All steps |

---

## Troubleshooting Tips

### "Codex says it cannot read the files"
Make sure you launched OpenAI Codex from the `exercise-3-automated-reporting/` directory (or its parent). OpenAI Codex needs the files to be within its working context. You can also provide absolute paths in your prompt.

### "The KPI numbers do not match when I spot-check"
This can happen if Codex misinterprets which column to use. Clarify in your prompt:
- **Reported amount** = `reported_amount_eur` (initial estimate of the claim).
- **Paid amount** = `paid_amount_eur` (actual disbursement, 0 if not yet paid).
- **Reserved amount** = `reserved_amount_eur` (funds set aside for open claims).

### "The HTML charts are blank when I open the file"
Check that your browser is not blocking the CDN script (e.g., Chart.js). If you are behind a corporate proxy, ask Codex to embed the library inline instead of loading from a CDN.

### "The report structure changed between Step 3 and Step 5"
OpenAI Codex does not automatically remember earlier outputs across separate sessions. If you are in the same session, it should be consistent. If you started a new session, paste the report structure or refer to the saved file: "Use the same structure as quarterly_report_Q4_2025.md."

### "The Python script fails to run"
Check which Python version you have (`python --version` or `python3 --version`). The script may require `pandas` -- install it with `pip install pandas` if needed. If Codex generated the script using only the standard library, ensure the CSV parsing logic handles the date formats correctly.

### "I want to customize the report further"
Great -- that is encouraged. Try follow-up prompts like:
- "Add a section comparing loss ratios to industry benchmarks."
- "Include a heatmap of claims by region and product line."
- "Generate a PDF version of the report."

---

## Summary

This exercise demonstrates a realistic actuarial workflow: taking raw quarterly data and transforming it into a management-ready report with commentary and visualizations. The key insight is that once the structure is defined, regenerating the report with new data becomes a single prompt -- saving Pierre nearly two days of work every quarter.

**Next exercise:** Exercise 4 (coming soon).
