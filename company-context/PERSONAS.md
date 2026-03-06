# MIG Stakeholder Personas

These personas represent key stakeholders within Mediterranean Insurance Group. They reflect the range of roles, geographies, experience levels, and pain points that consultants would encounter during an engagement.

---

## 1. Ana Martinez -- Regional Claims Manager, Barcelona

### Profile

| Attribute | Detail |
|---|---|
| **Full Name** | Ana Martinez Puig |
| **Title** | Regional Claims Manager, Catalonia & Aragon |
| **Location** | Barcelona HQ, Avinguda Diagonal 477 |
| **Age** | 42 |
| **Tenure at MIG** | 15 years (joined 2011 as claims adjuster) |
| **Education** | Law degree, Universitat de Barcelona; CPCU designation |
| **Direct Reports** | 20 claims adjusters + 3 team leads |
| **Languages** | Catalan (native), Spanish (native), English (professional), French (basic) |

### Role and Responsibilities

Ana manages the largest regional claims operation in MIG, handling approximately 45.000 motor and home claims per year across Catalonia and Aragon. Her team of 20 adjusters processes everything from minor windshield replacements to complex water damage and multi-vehicle accidents. She reports to Marta Oliveira (COO) and works closely with the fraud detection team and external loss adjusters.

Her responsibilities include:
- Daily triage and assignment of incoming claims
- Monitoring team caseloads and cycle times
- Authorizing settlements above EUR 5.000 (her approval threshold is EUR 25.000)
- Managing relationships with 35 repair shops and 12 loss-adjusting firms in the region
- Monthly performance reporting to the COO
- Participating in the Tramuntana Claims Automation workstream as a business sponsor

### A Day in Ana's Life

Ana arrives at 8:15 AM and immediately checks the overnight claims queue. There are 47 new motor claims and 18 new home claims from the previous evening and overnight. She opens the legacy AS/400 claims system (which she accesses through a green-screen terminal emulator) and begins triaging.

She spends the first hour manually reviewing each claim notification, reading the FNOL (First Notice of Loss) descriptions, and assigning them to adjusters based on complexity, geography, and current caseloads. There is no automated routing -- it is entirely based on her judgment and a mental model of each adjuster's workload.

By 10:00 AM she is in a meeting with three adjusters discussing a batch of suspicious motor claims from a particular repair shop. She suspects fraud but the data is scattered across the claims system, the finance system, and paper files. Building a case requires manually cross-referencing claim numbers, repair invoices, and policyholder histories.

After lunch, she reviews 12 settlement authorizations, each requiring her to open the claim file, check the policy terms, verify the adjuster's documentation, and sign off digitally (by updating a status field in the system -- there is no actual digital signature workflow). She estimates she spends 3 hours per day on approvals that could be automated.

At 3:30 PM she joins the weekly Tramuntana project call. The IT team presents a prototype of the new automated triage tool. Ana is cautiously optimistic but skeptical -- she has seen three previous "modernization" initiatives fail to deliver.

### Pain Points

1. **Manual triage is the bottleneck.** Every claim must be manually reviewed, classified, and assigned. Ana estimates that 60% of motor claims (low-value, straightforward, no injury) could be auto-routed or even auto-settled, but the current system has no rules engine.

2. **Legacy systems are fragile and disconnected.** The AS/400 claims system does not integrate with the policy administration system (SAP), the finance system, or the document management system. Ana's team routinely re-keys data across systems.

3. **No real-time visibility into performance.** Ana produces monthly reports by exporting data to Excel and manually calculating KPIs (cycle time, settlement amounts, adjuster productivity). This takes her an entire Friday afternoon every month. She cannot see real-time dashboards.

4. **Fraud detection is reactive, not proactive.** MIG has no automated fraud-scoring model. Fraud is identified by experienced adjusters who "notice something off." Ana estimates 3-5% of claims have some fraudulent element, but only about 1,2% are formally flagged.

5. **Team burnout and retention.** Adjusters handle an average of 190 open cases each. Industry benchmark is 120-150. Two adjusters resigned in the past six months, citing workload and outdated tools. Hiring replacements takes 4-6 months.

### What Ana Needs

- **An automated claims triage system** that classifies incoming claims by complexity and routes them to the right adjuster (or to straight-through processing for simple cases).
- **A unified claims dashboard** showing real-time KPIs: open cases by adjuster, average cycle time, settlement amounts, and fraud flags.
- **Fraud scoring at FNOL** -- a model that flags suspicious claims at intake so adjusters can prioritize investigation.
- **Reduced manual data entry** through system integration between claims, policy admin, and finance.

### Attitude Toward Technology and Change

Ana is pragmatic and results-oriented. She is not opposed to technology -- in fact, she actively advocates for it -- but she has been burned by past failures. She will judge any new tool by one criterion: "Does this make my adjusters' lives easier and help us close claims faster?" She is deeply protective of her team and will push back on any initiative that increases their workload in the short term, even if it promises long-term benefits.

### Quotes

> "I've been hearing about 'digital transformation' for five years. My adjusters are still copying data between three different screens to process a single claim."

> "Give me a system that can auto-approve a EUR 400 windshield replacement and I'll buy the project team dinner for a month."

> "I don't need AI to replace my team. I need it to handle the 60% of claims that don't require human judgment, so my people can focus on the ones that do."

---

## 2. Luca Rossi -- Underwriting Director, Milan

### Profile

| Attribute | Detail |
|---|---|
| **Full Name** | Luca Rossi |
| **Title** | Underwriting Director, Commercial Lines, Italy |
| **Location** | Milan office, Via Torino 25 |
| **Age** | 51 |
| **Tenure at MIG** | 8 years (joined 2018 from Generali) |
| **Education** | Economics degree, Bocconi University; ACII Chartered Insurer |
| **Direct Reports** | 6 senior underwriters + 2 underwriting assistants |
| **Languages** | Italian (native), English (fluent), Spanish (conversational) |

### Role and Responsibilities

Luca leads commercial property and casualty underwriting for MIG's Italian operation, managing a portfolio of EUR 48 million in GWP. His team underwrites risks ranging from small retail shops to mid-size manufacturing facilities across Northern and Central Italy. He reports to Jean-Pierre Moreau (CCO) with a dotted line to the Group Head of Underwriting in Barcelona.

His responsibilities include:
- Setting underwriting guidelines and risk appetite for Italian commercial lines
- Reviewing and authorizing complex or high-value risks (his authority is EUR 500K per risk)
- Managing broker relationships (MIG Italy works with 45 broker firms)
- Pricing and portfolio analysis
- Ensuring compliance with Italian regulatory requirements (IVASS)
- Contributing to group-wide underwriting standards and tool development

### A Day in Luca's Life

Luca's morning begins with a review of the previous day's submissions. His team received 14 new broker submissions overnight, ranging from a small restaurant in Florence (EUR 1.200 premium) to a mid-size furniture manufacturer near Bergamo (EUR 85.000 premium).

For each submission, the underwriter must manually review the broker's submission documents (usually a PDF or Word document with the client's details), consult the rating manual (a 200-page Excel workbook maintained by the Barcelona actuarial team), assess the risk, and produce a quote. The furniture manufacturer submission includes a 15-page risk survey, three years of loss history, and photographs of the premises.

By 10:00 AM Luca is on a call with a broker from Milan who is frustrated that a quote he requested six days ago has not been returned. Luca apologizes -- the underwriter handling it was out sick and there was no system to reassign the case. He promises to turn it around by end of day.

At 11:30 AM he opens the monthly portfolio report. He wants to understand how the Italian commercial book is performing by industry segment. But the data is in three places: the policy system (SAP) has the premium data, the claims system (AS/400 for older policies, Guidewire for newer ones) has the loss data, and the broker correspondence is in Outlook. He spends an hour building a pivot table in Excel, reconciling policy numbers across systems.

After lunch, he has a meeting with the risk engineering team about a large warehouse risk in Turin. The risk engineer's report is a 30-page PDF with fire protection details, building plans, and photos. Luca reads it on screen, makes notes in a separate document, and manually enters key data points into his pricing spreadsheet.

At 4:00 PM he joins a call with Sofia Papadopoulos (Chief Actuary) in Barcelona to discuss proposed rate changes for the Italian SME segment. Sofia presents analysis showing that water damage frequency has increased 18% in Northern Italy over the past three years. They debate whether to increase rates by 5% or tighten underwriting criteria. The conversation is data-rich but all the supporting analysis lives in Sofia's actuarial models, which Luca cannot access directly.

### Pain Points

1. **Spreadsheet-based pricing is error-prone and slow.** The commercial lines rating tool is a 12MB Excel workbook with 47 tabs, nested VLOOKUPs, and macros that occasionally break. Different underwriters have different local versions. There is no single source of truth.

2. **No integrated view of risk.** To assess a commercial risk properly, Luca needs data from the policy system, claims system, risk engineering reports, broker submissions, external data (company financials, flood maps, fire statistics), and his own experience. None of these are connected.

3. **Quote turnaround is too slow.** Average time from broker submission to quote is 4,2 business days. For complex risks it can be 8-10 days. Brokers expect 2 days for standard risks. MIG is losing business to faster competitors.

4. **Portfolio monitoring is manual and backward-looking.** Luca can only assess portfolio performance after month-end, when finance produces the management accounts. He has no ability to monitor loss ratios, exposure accumulations, or pricing adequacy in real time.

5. **Broker relationship management is ad hoc.** There is no CRM system for broker interactions. Broker correspondence lives in individual underwriters' Outlook inboxes. If an underwriter leaves, the relationship history goes with them.

### What Luca Needs

- **A modern underwriting workbench** that consolidates submission data, rating tools, risk engineering reports, and claims history in a single interface.
- **Automated data enrichment** -- pulling external data (company financials, geospatial risk data, weather patterns) into the underwriting workflow automatically.
- **Real-time portfolio analytics** -- dashboards showing loss ratios by segment, geographic exposure accumulations, and pricing adequacy indicators.
- **Faster quote generation** -- ideally a system that can auto-quote simple SME risks (below EUR 3.000 premium) with underwriter review only for exceptions.

### Attitude Toward Technology and Change

Luca is a seasoned underwriter who values judgment and relationships. He respects data but trusts experience. He is not resistant to technology -- he actively wants better tools -- but he is wary of systems that try to replace underwriting judgment with algorithms. He is most receptive to tools that enhance his team's capabilities rather than constrain them. He has a strong voice in the organization and his buy-in is essential for any underwriting transformation initiative.

### Quotes

> "I have six underwriters, each with their own version of the rating spreadsheet. Last month we found a formula error in one version that had been underpricing warehouse risks by 12% for three months. That's not sustainable."

> "A broker called me yesterday asking about a quote from two weeks ago. I had to search through three people's email inboxes to find the submission. We look unprofessional."

> "I don't want a black box that tells me what price to charge. I want a system that gives me all the relevant information in one place so I can make a better decision, faster."

---

## 3. Isabel Santos -- Head of Strategy, Lisbon

### Profile

| Attribute | Detail |
|---|---|
| **Full Name** | Isabel Cristina Santos Ferreira |
| **Title** | Head of Strategy and Business Development |
| **Location** | Lisbon office, Avenida da Liberdade 110 |
| **Age** | 38 |
| **Tenure at MIG** | 3 years (joined 2023, previously at Oliver Wyman Lisbon) |
| **Education** | Economics degree, Nova SBE; MBA, London Business School |
| **Direct Reports** | 4 strategy analysts |
| **Languages** | Portuguese (native), English (fluent), Spanish (fluent), French (professional) |

### Role and Responsibilities

Isabel leads MIG's group-level strategy function, reporting directly to CEO Elena Vidal. She is responsible for corporate strategy, market analysis, M&A integration (currently overseeing the LusoProtect integration), and identifying growth opportunities across MIG's footprint. She joined MIG from Oliver Wyman, where she spent eight years advising European insurers on growth strategy and digital transformation.

Her responsibilities include:
- Developing and maintaining MIG's 5-year strategic plan
- Leading the LusoProtect post-merger integration (PMI) from a strategy and commercial perspective
- Market analysis and competitive intelligence across all four countries
- Evaluating new market entry opportunities (MIG is considering expansion into Greece and Croatia)
- Supporting the CEO and board on strategic decisions
- Coordinating with the external strategy advisor on ongoing transformation initiatives

### A Day in Isabel's Life

Isabel starts her day at 8:00 AM with a call to Barcelona. Elena Vidal wants an updated view on the Portuguese market, specifically how MIG+LusoProtect's combined market share compares to Fidelidade (the market leader) in the Lisbon metro area. Isabel asks one of her analysts to pull the data. The analyst explains it will take two days: MIG Portugal data is in SAP, LusoProtect data is still in SiGeSeg, and market-level data must be sourced from the Portuguese insurance association (ASF) website, which publishes quarterly with a 3-month lag.

At 9:30 AM she chairs the weekly LusoProtect integration steering committee. The meeting brings together 12 people from IT, operations, HR, finance, and commercial. Key issues this week: the product harmonization workstream is behind schedule (LusoProtect's motor policy wordings differ significantly from MIG's), agent attrition in Porto is running at 15% (double the expected rate), and IT integration costs are EUR 2,3 million over budget.

After the meeting, Isabel works on a board presentation analyzing MIG's competitive position in urban markets. She needs to compare MIG's market share, growth rates, customer demographics, and product penetration against Mapfre, Generali, Allianz, and local digital players across Barcelona, Madrid, Milan, Lisbon, and Marseille. The data comes from a mix of sources: internal MIG data (which she extracts via ad hoc SQL queries that her analyst writes), industry reports (from Swiss Re, EIOPA, and local regulators), and broker intelligence. Synthesizing all of this into a coherent strategic picture is painstaking manual work.

At 2:00 PM she has a video call with the external strategy consultants in Madrid to discuss the scope of a potential new workstream on digital distribution strategy. She needs to brief the consultants on MIG's current direct-to-consumer performance, channel economics, and customer acquisition costs -- but much of this data is not readily available and will require collaboration with IT, marketing, and finance to assemble.

At 4:30 PM she reviews a market entry feasibility study for Greece. One of her analysts has produced a 45-page PowerPoint with market sizing, regulatory analysis, competitive landscape, and entry options. Isabel gives feedback and asks for a deeper dive on distribution options and potential acquisition targets.

### Pain Points

1. **Data assembly is the strategy team's biggest time sink.** Isabel estimates her team spends 60% of their time finding, cleaning, and reconciling data, and only 40% on actual analysis and strategic thinking. Internal data is siloed across systems, and external market data is scattered across multiple sources and formats.

2. **LusoProtect integration lacks a single source of truth.** Integration progress is tracked in a mix of Excel trackers, PowerPoint updates, and SharePoint documents. There is no real-time integration dashboard. Isabel learns about problems in weekly meetings, not as they happen.

3. **Competitive intelligence is fragmented and manual.** There is no centralized system for tracking competitor moves, pricing changes, product launches, or regulatory developments across four countries. Isabel's team maintains a "competitor tracker" spreadsheet that is perpetually out of date.

4. **Market analysis tools are limited.** The strategy team uses Excel and PowerPoint for everything. There is no access to business intelligence tools (Tableau, Power BI) or market modeling software. Isabel has requested a BI license three times; IT has not prioritized it.

5. **Cross-country comparison is difficult.** Each country has different reporting standards, product definitions, and data structures. Comparing "motor insurance market share in urban areas" across Spain, Italy, Portugal, and France requires normalizing data from four different sources with different methodologies.

### What Isabel Needs

- **A unified strategic data platform** that combines internal performance data with external market data, updated regularly and accessible through self-service dashboards.
- **Automated competitive intelligence** -- monitoring competitor filings, press releases, product launches, and pricing changes across all four markets.
- **Integration tracking tools** -- a real-time dashboard for LusoProtect PMI showing milestone progress, synergy realization, risk flags, and financial impact.
- **Scenario modeling capability** -- tools to model market entry scenarios, acquisition valuations, and strategic investment cases without building everything from scratch in Excel.

### Attitude Toward Technology and Change

Isabel is the most digitally fluent persona in this set. She is comfortable with data, technology, and ambiguity. She strongly advocates for analytics and digital investment and has the CEO's ear. Her main risk is execution bias: she focuses on the "what" and "why" and may underestimate the change management needed for the "how."

### Quotes

> "I spent three days last month trying to answer a simple question: what is our market share by product line in cities with more than 500.000 people? The answer should be available in two clicks."

> "The LusoProtect integration is the most important strategic initiative we have, and we're managing it with spreadsheets and weekly meetings. We need real-time visibility."

> "Every board meeting, Elena asks me to compare our performance to Mapfre and Generali. Every time, I build the comparison from scratch because the data sources have changed. There has to be a better way."

---

## 4. Pierre Dupont -- Actuarial Analyst, Marseille

### Profile

| Attribute | Detail |
|---|---|
| **Full Name** | Pierre Michel Dupont |
| **Title** | Actuarial Analyst, Southern France Region |
| **Location** | Marseille office, Rue de la Republique 45 |
| **Age** | 27 |
| **Tenure at MIG** | 2,5 years (joined July 2023, first job after university) |
| **Education** | Master's in Actuarial Science, ISFA Lyon; passed 4 of 7 Institut des Actuaires exams |
| **Direct Reports** | None (individual contributor) |
| **Languages** | French (native), English (professional), Spanish (basic) |

### Role and Responsibilities

Pierre is a junior actuary in MIG's group actuarial team, physically based in Marseille but reporting to Sofia Papadopoulos (Chief Actuary) in Barcelona. He is one of 14 actuaries in the group function. His primary focus is on reserving and quarterly reporting for the French and Portuguese portfolios, with some involvement in pricing support for motor insurance.

His responsibilities include:
- Quarterly reserve calculations for motor and home lines in France and Portugal
- Preparing actuarial exhibits and commentary for the quarterly reporting pack
- Running loss development triangle analyses
- Supporting the annual Solvency II technical provisions calculation
- Ad hoc pricing analysis when requested by underwriting teams
- Maintaining actuarial data extracts and reconciling data between source systems and actuarial models

### A Day in Pierre's Life

It is the second week of January -- quarter-end reporting season, the busiest time for actuaries. Pierre arrives at 8:30 AM and opens his laptop. He has three monitors: one showing Excel (always), one showing the SAS actuarial modeling environment, and one with Outlook.

His first task is to update the loss development triangles for French motor insurance. He needs claims data as of December 31 from the claims system. He submits a data request to the IT data team via email (there is no self-service data access for actuaries). The standard turnaround is 48 hours. He submitted this request three days ago and it has not arrived yet. He sends a follow-up email.

While waiting, he works on the Portuguese motor reserve. The LusoProtect claims data arrived last week, but it is in a different format from MIG's standard extract. Pierre spends two hours reformatting the data in Excel -- converting date formats, mapping claim status codes (LusoProtect uses a different coding scheme), and reconciling paid amounts against finance records. He finds a EUR 340.000 discrepancy and spends another hour investigating. It turns out to be a currency conversion issue in the extract (LusoProtect's system stores some historical claims in escudos, the pre-euro Portuguese currency).

After lunch, the French motor data arrives. Pierre loads it into his SAS model, which runs a chain-ladder projection. The model takes 20 minutes to execute. While it runs, he begins writing the actuarial commentary for last quarter's results -- a Word document that explains reserve movements, highlights unusual claims, and identifies emerging trends. He writes this from scratch each quarter; there is no template or automation.

At 3:00 PM he joins a call with Sofia in Barcelona. She reviews his preliminary French motor reserve estimate. She notices that he has not adjusted for a change in case reserve practices that was implemented in October. Pierre did not know about this change -- it was communicated in an email to the French claims team that was not shared with actuarial. He will need to redo the analysis with an adjustment.

At 5:00 PM he is still at his desk, manually formatting an Excel report that consolidates reserving results across all lines and countries. The report has a specific layout required by the CFO's team: color-coded cells, conditional formatting, specific number formats, and embedded charts. Pierre estimates he spends 6-8 hours per quarter on formatting alone.

He leaves at 7:30 PM, knowing he will need to work Saturday to meet the Tuesday deadline.

### Pain Points

1. **No self-service data access.** Pierre cannot query the source systems directly. Every data extract requires a request to IT, with a 48-hour (often longer) turnaround. During quarter-end, the queue of data requests backs up and delays cascade through the actuarial process.

2. **Manual data wrangling consumes enormous time.** Pierre estimates he spends 65% of his time on data extraction, cleaning, formatting, and reconciliation, and only 35% on actual actuarial analysis. The LusoProtect data integration has made this worse.

3. **Actuarial tools are outdated.** MIG's actuarial team uses SAS (on-premise, version 9.4) and Excel. Pierre learned R and Python at university but is not allowed to install them on his work laptop (IT security policy). He knows he could automate much of his repetitive work with Python but cannot access the tools.

4. **Quarterly reporting is a manual grind.** The quarterly actuarial reporting pack is a 60-page Excel workbook that takes the actuarial team approximately 320 person-hours to produce. Most of this time is spent on data assembly and formatting, not analysis.

5. **Knowledge is tribal and undocumented.** Critical actuarial assumptions (like the case reserve practice change) are communicated informally and inconsistently. There is no central documentation of model assumptions, methodology choices, or data adjustments. When Pierre's senior colleague went on maternity leave, key knowledge about the Italian reserving model was temporarily lost.

6. **No coding environment.** Pierre is proficient in R (from his master's program) and has self-taught basic Python. He believes he could automate 70% of his quarterly reporting workflow with Python scripts. But IT policy prohibits installing unapproved software, and the request he submitted eight months ago to approve Python has not been actioned.

### What Pierre Needs

- **Self-service data access** -- direct, query-based access to claims and policy data (ideally through the Snowflake platform being piloted) so he does not depend on IT for every data extract.
- **A modern analytical environment** -- approval to use Python or R, ideally with Jupyter notebooks, for actuarial analysis and automation.
- **Automated reporting pipelines** -- tools that can automatically pull data, run standard calculations, and generate formatted reports, reducing the 320 person-hours per quarter to something manageable.
- **Documentation and knowledge management** -- a centralized repository for actuarial assumptions, methodology notes, and model documentation.

### Attitude Toward Technology and Change

Pierre is the most enthusiastic about technology among the four personas. He is a digital native who is genuinely frustrated by the gap between what he learned at university (Python, R, modern data tools) and what he is allowed to use at work (SAS 9,4 and Excel). He is eager to automate, eager to learn, and eager to prove himself. However, he is junior and somewhat hesitant to push back on established processes or challenge senior colleagues. He needs a sponsor (like Sofia Papadopoulos) to champion his ideas.

### Quotes

> "I wrote a Python script at home that does in 10 minutes what takes me 4 hours in Excel at work. But I can't use it because Python isn't on the approved software list."

> "Every quarter I spend a full day reformatting numbers in Excel so the cells are the right shade of blue and the charts have the right fonts. There has to be a better use of an actuary's time."

> "I joined MIG because I wanted to do actuarial science. Instead, I spend most of my time doing data plumbing. I love the company, but if the tools don't improve, I'll have to consider my options."

> "The LusoProtect data is like a puzzle where half the pieces are from a different puzzle. Last week I found claims from 1998 still denominated in escudos."

---

## Persona Interaction Map

These four personas interact in ways that reflect MIG's organizational dynamics:

```text
                        Elena Vidal (CEO)
                              |
                    Isabel Santos (Strategy)
                       /            \
                      /              \
    Sofia Papadopoulos              Marta Oliveira (COO)
    (Chief Actuary)                        |
          |                          Ana Martinez (Claims)
    Pierre Dupont
    (Actuarial Analyst)

    Jean-Pierre Moreau (CCO)
          |
    Luca Rossi (Underwriting)
```

**Key interactions:**
- **Ana ↔ Pierre:** Ana's claims data is Pierre's input for reserving. When claims data quality is poor or late, Pierre's actuarial analysis is delayed. They interact primarily through data extracts rather than directly.
- **Luca ↔ Pierre:** Luca requests ad hoc pricing analyses from Pierre's team. Pierre sometimes supports Italian commercial lines pricing during peak periods.
- **Isabel ↔ Ana:** Isabel needs claims performance data for her strategic analyses. Ana is a key source of ground-truth insight about operational challenges.
- **Isabel ↔ Luca:** Isabel relies on Luca for commercial market intelligence in Italy. Luca provides broker feedback on competitive positioning.
- **All four ↔ Project Tramuntana:** Each persona is affected by the digital transformation program, but their priorities and expectations differ significantly.
