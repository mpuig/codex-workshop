#!/usr/bin/env bash
# Convert existing Markdown content to MDX pages with YAML frontmatter.
# Usage: cd website && bash convert-content.sh
#
# This script copies content from the source .md files in course-materials/,
# exercises/, and company-context/ into the website/pages/ directory as .mdx
# files with frontmatter added.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PAGES_DIR="$(cd "$(dirname "$0")" && pwd)/pages"

add_frontmatter_and_copy() {
  local src="$1"
  local dest="$2"
  local title="$3"
  local description="$4"

  if [ ! -f "$src" ]; then
    echo "SKIP: $src not found"
    return
  fi

  mkdir -p "$(dirname "$dest")"

  {
    echo "---"
    echo "title: \"$title\""
    echo "description: \"$description\""
    echo "---"
    echo ""
    cat "$src"
  } > "$dest"

  echo "OK: $dest"
}

echo "Converting course-materials and exercises to MDX pages..."
echo ""

# Module 0: Getting Started
add_frontmatter_and_copy \
  "$REPO_ROOT/course-materials/0-getting-started/README.md" \
  "$PAGES_DIR/getting-started/index.mdx" \
  "Getting Started with OpenAI Codex" \
  "Install OpenAI Codex, authenticate, and run your first session in 10 minutes."

# Module 1.1: First Steps
add_frontmatter_and_copy \
  "$REPO_ROOT/course-materials/1-fundamentals/1.1-first-steps/README.md" \
  "$PAGES_DIR/fundamentals/first-steps.mdx" \
  "Module 1.1: First Steps with OpenAI Codex" \
  "Learn how to give Codex instructions in natural language, reference files, and complete three insurance scenarios."

# Module 1.2: Project Memory
add_frontmatter_and_copy \
  "$REPO_ROOT/course-materials/1-fundamentals/1.2-project-memory/README.md" \
  "$PAGES_DIR/fundamentals/project-memory.mdx" \
  "Module 1.2: Project Memory with AGENTS.md" \
  "Learn how to use AGENTS.md to give Codex persistent context about your projects and preferences."

# Module 2.1: Underwriting Brief
add_frontmatter_and_copy \
  "$REPO_ROOT/course-materials/2-insurance-workflows/2.1-underwriting-brief/README.md" \
  "$PAGES_DIR/insurance-workflows/underwriting-brief.mdx" \
  "Module 2.1: Writing an Underwriting Brief" \
  "Use OpenAI Codex to analyze a commercial property portfolio and generate a professional underwriting brief."

# Module 2.2: Loss Ratio Analysis
add_frontmatter_and_copy \
  "$REPO_ROOT/course-materials/2-insurance-workflows/2.2-loss-ratio-analysis/README.md" \
  "$PAGES_DIR/insurance-workflows/loss-ratio-analysis.mdx" \
  "Module 2.2: Loss Ratio Analysis" \
  "Analyze motor portfolio loss ratios across Spanish regions with OpenAI Codex."

# Module 2.3: Market Assessment
add_frontmatter_and_copy \
  "$REPO_ROOT/course-materials/2-insurance-workflows/2.3-market-assessment/README.md" \
  "$PAGES_DIR/insurance-workflows/market-assessment.mdx" \
  "Module 2.3: Market Entry Assessment" \
  "Use OpenAI Codex web search to build a market entry assessment for Portugal expansion."

# Module 3: Vibe Coding
add_frontmatter_and_copy \
  "$REPO_ROOT/course-materials/3-vibe-coding/README.md" \
  "$PAGES_DIR/vibe-coding/index.mdx" \
  "Module 3: Building an Insurance App with Vibe Coding" \
  "Build a Claims Dashboard app using natural language -- no coding experience required."

# Exercise 1
add_frontmatter_and_copy \
  "$REPO_ROOT/exercises/exercise-0-executive-onramp/README.md" \
  "$PAGES_DIR/exercises/executive-onramp.mdx" \
  "Exercise 0: Executive Onramp (Zero to One)" \
  "Zero-to-one onboarding for executive users with copy/paste wins and progressive prompting challenge."

# Exercise 1
add_frontmatter_and_copy \
  "$REPO_ROOT/exercises/exercise-1-data-insight-tool/README.md" \
  "$PAGES_DIR/exercises/data-insight-tool.mdx" \
  "Exercise 1: Data-Driven Insight Tool" \
  "Build an end-to-end analytical workflow to identify white space expansion opportunities."

# Exercise 2
add_frontmatter_and_copy \
  "$REPO_ROOT/exercises/exercise-2-claims-triage/README.md" \
  "$PAGES_DIR/exercises/claims-triage.mdx" \
  "Exercise 2: Claims Triage Prototype" \
  "Build a claims triage system that classifies, prioritizes, and routes 220 incoming claims."

# Exercise 3
add_frontmatter_and_copy \
  "$REPO_ROOT/exercises/exercise-3-automated-reporting/README.md" \
  "$PAGES_DIR/exercises/automated-reporting.mdx" \
  "Exercise 3: Automated Reporting Solution" \
  "Automate quarterly claims report generation with data analysis and visualizations."

# Company Context
add_frontmatter_and_copy \
  "$REPO_ROOT/company-context/COMPANY.md" \
  "$PAGES_DIR/company-context/company.mdx" \
  "Mediterranean Insurance Group (MIG)" \
  "Company overview, financials, leadership, and strategic context for MIG."

add_frontmatter_and_copy \
  "$REPO_ROOT/company-context/PRODUCTS.md" \
  "$PAGES_DIR/company-context/products.mdx" \
  "MIG Product Lines" \
  "Detailed breakdown of MIG's five principal lines of business."

add_frontmatter_and_copy \
  "$REPO_ROOT/company-context/PERSONAS.md" \
  "$PAGES_DIR/company-context/personas.mdx" \
  "MIG Stakeholder Personas" \
  "Four key personas at Mediterranean Insurance Group."

add_frontmatter_and_copy \
  "$REPO_ROOT/company-context/MARKET.md" \
  "$PAGES_DIR/company-context/market.mdx" \
  "Southern European Insurance Market" \
  "Market overview, competitive landscape, and industry trends."

echo ""
echo "Done. ${#} files converted."
echo "Note: The MDX files may need manual review for:"
echo "  - Nested code blocks (triple backticks inside code fences)"
echo "  - Links that need updating to website paths"
echo "  - Any JSX-incompatible syntax (angle brackets in text)"
