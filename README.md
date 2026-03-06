# OpenAI Codex Workshop - Training Materials

Practical training for consultancy teams on using OpenAI Codex to build solutions without writing code.

## Who Is This For?

Non-technical insurance professionals who want to use AI coding agents to accelerate their work: data analysis, process prototyping, reporting automation, and rapid application building.

## Fictional Company: Mediterranean Insurance Group (MIG)

All materials use a consistent fictional context: **Mediterranean Insurance Group** -- a mid-size European insurer headquartered in Barcelona, operating across Spain, Portugal, Italy, and Southern France.

See [`company-context/`](company-context/) for the full company profile, product lines, personas, and market landscape.

## Documentation Website

Browse the training materials as a website:

```bash
cd website
npm install
npm run dev
# Open http://localhost:3000
```

To build and preview the static site:

```bash
cd website
npm run build
npm run preview
```

## Repository Structure

```text
codex-workshop/
├── AGENTS.md                           # Project context for OpenAI Codex
├── company-context/                    # Fictional company documentation
│   ├── COMPANY.md                      # MIG overview, financials, strategy
│   ├── PRODUCTS.md                     # Insurance product lines and metrics
│   ├── PERSONAS.md                     # 4 personas (Claims, Underwriting, Strategy, Actuarial)
│   └── MARKET.md                       # Southern European insurance market
│
├── course-materials/                   # Training modules
│   ├── 0-getting-started/              # Installation and first run
│   ├── 1-fundamentals/                 # Core OpenAI Codex skills
│   │   ├── 1.1-first-steps/           #   Natural language instructions, file ops
│   │   └── 1.2-project-memory/        #   AGENTS.md for persistent context
│   ├── 2-insurance-workflows/          # Insurance-specific workflows
│   │   ├── 2.1-underwriting-brief/    #   Commercial property underwriting
│   │   ├── 2.2-loss-ratio-analysis/   #   Motor portfolio loss ratio analysis
│   │   └── 2.3-market-assessment/     #   Portugal market entry assessment
│   ├── 3-vibe-coding/                 # Building a Claims Dashboard app
│   ├── 4-wrap-up/                     # Course wrap-up and next steps
│   └── 5-advanced-tips/               # Cost, security, diffs, context window
│
├── exercises/                          # Hands-on exercises with data
│   ├── exercise-0-executive-onramp/    # Zero-to-one executive onboarding
│   ├── exercise-1-data-insight-tool/   # Market white space analysis
│   │   └── data/                       #   4 CSVs: penetration, demographics, accidents, products
│   ├── exercise-2-claims-triage/       # Claims classification & routing prototype
│   │   └── data/                       #   220 claims, business rules JSON, 160 historical outcomes
│   └── exercise-3-automated-reporting/ # Quarterly claims report automation
│       └── data/                       #   4 quarters of claims data + report template
│
└── website/                            # Nextra documentation site
    ├── pages/                          #   MDX content pages
    ├── theme.config.tsx                #   Nextra theme configuration
    └── package.json                    #   Next.js 14 + Nextra 3
```

## Suggested Training Flow

| Order | Module | Duration | Description |
|-------|--------|----------|-------------|
| 1 | [Module 0 - Getting Started](course-materials/0-getting-started/) | 10 min | Install OpenAI Codex, authenticate, first session |
| 2 | [Module 1.1 - First Steps](course-materials/1-fundamentals/1.1-first-steps/) | 30 min | Natural language instructions, file operations, 3 scenarios |
| 3 | [Module 1.2 - Project Memory](course-materials/1-fundamentals/1.2-project-memory/) | 15 min | AGENTS.md for consistent insurance context |
| 4 | [Module 2.1 - Underwriting Brief](course-materials/2-insurance-workflows/2.1-underwriting-brief/) | 30 min | Commercial property underwriting workflow |
| 5 | [Module 2.2 - Loss Ratio Analysis](course-materials/2-insurance-workflows/2.2-loss-ratio-analysis/) | 30 min | Motor portfolio analysis with visualizations |
| 6 | [Module 2.3 - Market Assessment](course-materials/2-insurance-workflows/2.3-market-assessment/) | 30 min | Portugal market entry via web research |
| 7 | [Module 3 - Vibe Coding](course-materials/3-vibe-coding/) | 45 min | Build a Claims Dashboard app |
| -- | [Advanced Tips](course-materials/5-advanced-tips/) | Reference | Cost management, data security, reading diffs, context window |

**Total guided time: ~3 hours** (modules can be done independently; Advanced Tips are standalone reference material)

## Hands-On Exercises

These are standalone exercises designed for the live session. Each includes step-by-step prompts, expected outputs, and rich fake data.

| Exercise | Persona                   | Duration | What You Build |
|----------|---------------------------|----------|----------------|
| [0 - Executive Onramp (Zero to One)](exercises/exercise-0-executive-onramp/) | Executives | 90 min | Executive prompting fundamentals with progressive challenge |
| [1 - Data Insight Tool](exercises/exercise-1-data-insight-tool/) | Isabel Santos (Strategy)  | 40 min | Market white space analysis with interactive charts |
| [2 - Claims Triage](exercises/exercise-2-claims-triage/) | Ana Martinez (Claims)     | 45 min | Claims classification, prioritization & routing prototype |
| [3 - Automated Reporting](exercises/exercise-3-automated-reporting/) | Pierre Dupont (Actuarial) | 55 min | Quarterly claims report with auto-update capability |

## Prerequisites

- A ChatGPT account for `codex login` or an OpenAI API key (`OPENAI_API_KEY`)
- A terminal (macOS Terminal, Windows PowerShell, or WSL)
- No programming knowledge required

## Quick Start

```bash
# 1. Install OpenAI Codex
npm install -g @openai/codex

# 2. Authenticate
codex login

# 3. Navigate to an exercise
cd exercises/exercise-0-executive-onramp

# 4. Start OpenAI Codex
codex

# 5. Follow the prompts in the README
```
