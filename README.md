# OpenAI Codex Workshop - Training Materials

Practical training for non-technical professionals on using OpenAI Codex to build solutions without writing code.

> Scope note: this training is CLI-first. Core modules and exercises are designed for `codex` in a terminal. Codex App-specific material is isolated to the Codex App appendix.

## Who Is This For?

Non-technical professionals who want to use AI coding agents to accelerate their work: data analysis, process prototyping, reporting automation, and rapid application building.

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
│   ├── 1-getting-started/              # Installation and first run
│   │   ├── 1.1-what-is-codex/         #   What Codex is and where it fits
│   │   └── 1.2-install-codex/         #   Install, authenticate, first session
│   ├── 2-fundamentals/                 # Core OpenAI Codex skills
│   │   ├── 2.1-first-steps/           #   Natural language instructions, file ops
│   │   └── 2.2-project-memory/        #   AGENTS.md for persistent context
│   ├── 3-insurance-workflows/          # Insurance-specific workflows
│   │   ├── 3.1-underwriting-brief/    #   Commercial property underwriting
│   │   ├── 3.2-loss-ratio-analysis/   #   Motor portfolio loss ratio analysis
│   │   └── 3.3-market-assessment/     #   Portugal market entry assessment
│   ├── 4-vibe-coding/                 # Building a Claims Dashboard app
│   ├── 5-wrap-up/                     # Course wrap-up and next steps
│   └── 6-advanced-tips/               # Cost, security, diffs, context window
│
├── exercises/                          # Hands-on exercises with data
│   ├── exercise-1-executive-onramp/    # Zero-to-one executive onboarding
│   ├── exercise-2-data-insight-tool/   # Market white space analysis
│   │   └── data/                       #   4 CSVs: penetration, demographics, accidents, products
│   ├── exercise-3-claims-triage/       # Claims classification & routing prototype
│   │   └── data/                       #   220 claims, business rules JSON, 160 historical outcomes
│   └── exercise-4-automated-reporting/ # Quarterly claims report automation
│       └── data/                       #   4 quarters of claims data + report template
│
└── website/                            # Nextra documentation site
    ├── pages/                          #   MDX content pages
    ├── theme.config.tsx                #   Nextra theme configuration
    └── package.json                    #   Next.js 14 + Nextra 3
```

## Suggested Training Flows

Choose the path that fits the time you have:

### Express (1 to 1.5 hours)

- [Module 1 - Getting Started](course-materials/1-getting-started/)
- [Module 2.1 - First Steps](course-materials/2-fundamentals/2.1-first-steps/)
- [Exercise 1 - Executive Onramp](exercises/exercise-1-executive-onramp/)

Best for: a short live introduction where learners need one concrete win quickly.

### Intermediate (2 to 3 hours)

- [Module 1 - Getting Started](course-materials/1-getting-started/)
- [Module 2.1 - First Steps](course-materials/2-fundamentals/2.1-first-steps/)
- [Module 2.2 - Project Memory](course-materials/2-fundamentals/2.2-project-memory/)
- [Module 3 - Guided Workflows](course-materials/3-insurance-workflows/)
- One exercise from Module 4 in the [`exercises/`](exercises/) folder

Best for: a workshop where learners should move from guided use into one independent task.

### Full (4 to 5 hours)

- [Module 1 - Getting Started](course-materials/1-getting-started/)
- [Module 2.1 - First Steps](course-materials/2-fundamentals/2.1-first-steps/)
- [Module 2.2 - Project Memory](course-materials/2-fundamentals/2.2-project-memory/)
- [Module 3 - Guided Workflows](course-materials/3-insurance-workflows/)
- Module 4 in the [`exercises/`](exercises/) folder
- [Module 5 - Vibe Coding](course-materials/4-vibe-coding/)
- [Course Wrap-Up](course-materials/5-wrap-up/)

Best for: the complete learning journey from first use through independent work and tool building.

## Complete Course Map

| Order | Module | Duration | Description |
|-------|--------|----------|-------------|
| 1 | [Module 1 - Getting Started](course-materials/1-getting-started/) | 10 min | Install OpenAI Codex, authenticate, first session |
| 2 | [Module 2.1 - First Steps](course-materials/2-fundamentals/2.1-first-steps/) | 30 min | Natural language instructions, file operations, 3 scenarios |
| 3 | [Module 2.2 - Project Memory](course-materials/2-fundamentals/2.2-project-memory/) | 15 min | AGENTS.md for consistent insurance context |
| 4 | [Module 3.1 - Underwriting Brief](course-materials/3-insurance-workflows/3.1-underwriting-brief/) | 30 min | Commercial property underwriting workflow |
| 5 | [Module 3.2 - Loss Ratio Analysis](course-materials/3-insurance-workflows/3.2-loss-ratio-analysis/) | 30 min | Motor portfolio analysis with visualizations |
| 6 | [Module 3.3 - Market Assessment](course-materials/3-insurance-workflows/3.3-market-assessment/) | 30 min | Portugal market entry via web research |
| 7 | Module 4 - Practice Exercises | 40-90 min | Apply the workflows independently with realistic business problems |
| 8 | [Module 5 - Vibe Coding](course-materials/4-vibe-coding/) | 45 min | Build a Claims Dashboard app |
| -- | [Advanced Tips](course-materials/6-advanced-tips/) | Reference | Cost management, data security, reading diffs, context window |

**Full path time: ~4 to 5 hours depending on which practice exercise you choose** (Advanced Tips are standalone reference material)

## How This Course Works

The course moves from guided use to independent use, then to tool building:

- **Module 1:** Get set up and understand what OpenAI Codex is.
- **Modules 2 and 3 (Guided):** Learn how to work with OpenAI Codex, then apply it in step-by-step insurance workflows.
- **Module 4 (Independent):** You get the business problem, the files, and the goal. You decide how to solve it.
- **Module 5 (Creator):** You move beyond using workflows and start building lightweight tools and applications yourself.

## Module 4: Practice Exercises

These are standalone exercises designed for the live session. Each includes step-by-step prompts, realistic context, and practical deliverables.

| Exercise | Duration | What You Build |
|----------|----------|----------------|
| [1 - Executive Onramp](exercises/exercise-1-executive-onramp/) | 90 min | Executive prompting fundamentals with progressive challenge |
| [2 - Data Insight Tool](exercises/exercise-2-data-insight-tool/) | 40 min | Market white space analysis with interactive charts |
| [3 - Claims Triage](exercises/exercise-3-claims-triage/) | 45 min | Claims classification, prioritization & routing prototype |
| [4 - Automated Reporting](exercises/exercise-4-automated-reporting/) | 55 min | Quarterly claims report with auto-update capability |

## Reference Material

Use these alongside the course when you need background, datasets, or deeper guidance:

- [`company-context/`](company-context/) -- Shared company, market, product, and persona background used across Modules 3 to 5
- [`website/public/data/`](website/public/data/) -- Website download files for the exercise datasets used in Exercises 1 to 4
- [`course-materials/6-advanced-tips/`](course-materials/6-advanced-tips/) -- Practical guidance on cost, data security, diffs, and context-window management
- [`course-materials/appendix-a-codex-app/`](course-materials/appendix-a-codex-app/) -- Optional deeper dives into the Codex App and related reference topics

## Prerequisites

- A ChatGPT account for `codex login` or an OpenAI API key (`OPENAI_API_KEY`)
- A terminal (macOS Terminal, Windows PowerShell, or WSL)
- No programming knowledge required

## Quick Start

```bash
# 1. Install OpenAI Codex
npm install -g @openai/codex

# 2. Open the training repository
cd codex-workshop

# 3. Authenticate
codex login

# 4. Start OpenAI Codex
codex

# 5. Open the exercise or module you want to follow
```
