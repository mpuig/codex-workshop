# Install OpenAI Codex

> **Time:** 5 minutes | **Prerequisites:** A laptop with terminal access and either a ChatGPT account or an OpenAI API key

## Step 1: Install OpenAI Codex

Open your terminal application and run one of the supported install commands:

**npm (all platforms, requires Node.js 18+):**

```bash
npm install -g @openai/codex
```

**macOS (Homebrew):**

```bash
brew install --cask codex
```

If you prefer, you can also install a platform-specific binary from the Codex GitHub releases page.

> **Tip for Mac users:** Open the Terminal app from Applications > Utilities, or search for "Terminal" in Spotlight (Cmd + Space).

## Step 2: Authenticate

Authenticate before your first session:

```bash
codex login
```

Alternative login options:

```bash
codex login --device-auth
printenv OPENAI_API_KEY | codex login --with-api-key
```

Then start OpenAI Codex:

```bash
codex
```

![OpenAI Codex session after startup](images/codex.jpg)

_Example of OpenAI Codex running in the terminal after login._

## Step 3: Orient Yourself

After authentication, you are in an OpenAI Codex session. This is where you will work. Here is what you need to know:

### Essential Commands

| Command | What It Does |
|---------|-------------|
| `codex login status` | Checks whether you are authenticated |
| `codex resume --last` | Reopens your last Codex session |
| `codex mcp list` | Lists configured MCP servers |
| **Ctrl+C** | Exits OpenAI Codex |

## Step 4: Try Your First Instruction

Type something simple to confirm everything works:

```text
What is the current Solvency II standard formula SCR calculation structure?
Give me a brief overview in plain language.
```

OpenAI Codex will respond directly in your terminal. You are ready to go.

---

## Quick Reference: Session Control

Codex behavior is controlled by CLI options and config:

| Setting | Example | Use Case |
|------|----------|-------------|
| Approval policy | `codex -c permissions.approval_policy=on-request` | Review potentially risky actions before execution |
| Sandbox mode | `codex -c permissions.sandbox_mode=workspace-write` | Limit file/system access during normal work |
| Full auto mode | `codex --full-auto` | Fast iterative work in a trusted project |

---

## Next Step

For non-technical executive users, start with [Exercise 0: Executive Onramp (Zero to One)](../../../exercises/exercise-0-executive-onramp/README.md).
Then proceed to [Module 1.1: First Steps with OpenAI Codex](../../1-fundamentals/1.1-first-steps/README.md) to learn how to give effective instructions and complete your first insurance tasks.
