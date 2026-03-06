# OpenAI Codex Workshop - Training Repository

## What This Is

Training materials for consultancy teams on using OpenAI Codex for insurance workflows. All content uses a fictional company context: **Mediterranean Insurance Group (MIG)**, a mid-size European insurer headquartered in Barcelona.

## Company Context: Mediterranean Insurance Group (MIG)

- Founded 1987, ~2,500 employees, EUR 1.8B gross written premium (GWP)
- Operates in Spain (52%), Italy (22%), Portugal (14%), Southern France (12%)
- Five business lines: Motor (45%), Home (20%), Health (15%), Commercial Property (12%), Life (8%)
- Combined ratio: 96.2%, Solvency II ratio: 178%
- Recently acquired LusoProtect (Portugal) in 2024
- Digital transformation program "Project Tramuntana" (2022-2027, EUR 95M budget)

## Repository Structure

- `course-materials/` -- Training modules (0-Getting Started through 4-Vibe Coding)
- `exercises/` -- Three hands-on exercises with CSV/JSON data files
- `company-context/` -- Detailed MIG company docs (COMPANY.md, PRODUCTS.md, PERSONAS.md, MARKET.md)
- `website/` -- Nextra-based documentation site (Next.js 14 + nextra-theme-docs)

## Insurance Terminology Conventions

- Use "gross written premium" (GWP), not "gross premiums written"
- Use "incurred claims" not "losses" when referring to claims costs
- Use "combined ratio" not "combined operating ratio"
- Use "cedant" not "ceding company" in reinsurance context
- First mention: "Solvency Capital Requirement (SCR)", then "SCR"
- First mention: "Own Risk and Solvency Assessment (ORSA)", then "ORSA"
- Product lines: Motor, Home/Property, Health, Commercial Property, Life

## Output Formatting

- Currency: EUR (not USD unless explicitly comparing markets)
- Number format: European style (1.000.000,00) in client-facing documents
- Dates: DD/MM/YYYY
- Tables preferred over long paragraphs for data presentation
- Executive summaries: under 250 words
- Always include "Key Takeaways" in analytical documents

## Key Rules

- Always cite data sources for market statistics
- Flag estimates vs. confirmed figures
- Show formulas and inputs when calculating ratios
- Include caveats and limitations in analytical work
- Do not invent specific regulatory article numbers
- Southern European focus: Spain (DGSFP), Italy (IVASS), Portugal (ASF), France (ACPR)

## Website Development

The `website/` directory uses Next.js 14.2.5 + Nextra 3.2.3 with static export. Run `cd website && npm run dev` for local development, `npm run build` for static export to `out/`.
