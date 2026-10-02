# Google Colab CLI Setup Implementation Plan

> **For agentic workers:** Execute this plan task-by-task in the current session. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Install Google's Colab CLI on this Apple Silicon Mac and add accurate Chinese setup, TODO, and agent usage notes to this repository.

**Architecture:** Install `uv` with Homebrew if it is absent, then install `google-colab-cli` as an isolated uv tool. Verify local commands before attempting account authentication or a short CPU runtime. Record only successful steps and clearly label any account-dependent action that could not be completed.

**Tech Stack:** macOS arm64, Homebrew, uv, Google `google-colab-cli`, Markdown.

---

### Task 1: Install and verify the local CLI

**Files:**
- No repository files. Install `uv` and the Colab CLI into user-level tool locations.

- [x] **Step 1: Install uv if missing**

Run `brew install uv` only if `command -v uv` returns no path.

- [x] **Step 2: Install the official CLI**

Run `uv tool install google-colab-cli`.

- [x] **Step 3: Verify the executable**

Run `colab version` and `colab --help`. The installed CLI reports version 0.7.4; help lists session and execution commands. The supported version command is `colab version`.

### Task 2: Check authentication and perform a bounded cloud verification

**Files:**
- No repository files. Authentication state remains in the user's home directory.

- [x] **Step 1: Check available authentication tooling**

Run `command -v gcloud` and inspect `colab --help` for the installed release's authentication options. Do not print credential files or token contents. On this Mac, `gcloud` is absent and `colab --help` reports `oauth2` as the default. No `gcloud` installation is needed for the OAuth2 route.

- [ ] **Step 2: Authenticate only with supported official flow**

For this installed release, start the first-use browser consent flow with `colab --auth=oauth2 sessions`. The user selects an account, grants consent, and pastes the returned code into the terminal. This command can authenticate and list sessions without creating a VM. The bundled upstream skill text describes ADC as its default, which differs from this installed CLI's help; pass `--auth=oauth2` explicitly. If an existing Google Cloud setup uses ADC instead, use the official Colab CLI instructions and required scopes. Do not place credentials in repository files.

- [ ] **Step 3: Run a short CPU smoke test only if authenticated**

Create a named CPU session with `colab --auth=oauth2 new -s useful-commands-smoke`, run `printf 'print(1 + 1)\n' | colab --auth=oauth2 exec -s useful-commands-smoke`, inspect it with `colab --auth=oauth2 status -s useful-commands-smoke`, then run `colab --auth=oauth2 stop -s useful-commands-smoke`. Confirm output `2` and confirm the session is stopped. If account authentication or allocation is unavailable, record the exact prerequisite and leave the runtime smoke test incomplete.

### Task 3: Add installation and agent guidance

**Files:**
- Create: `Colab/README.md` — overview, links, quick start, and document index.
- Create: `Colab/installation.md` — actual Mac environment, successful install commands, version check, authentication route, validation outcome, upgrade and uninstall.
- Create: `Colab/agent-usage.md` — shell-based Claude Code/Codex examples, task prompt, identity and permission boundaries, resource and runtime limits, file transfer and interactive-auth details.

- [x] **Step 1: Record verified install and auth steps**

Write `Colab/installation.md` from the actual outputs and actions in Tasks 1–2. Distinguish local installation verification from cloud runtime verification.

- [x] **Step 2: Document agent invocation and constraints**

Write `Colab/agent-usage.md` with examples using `colab new`, `colab exec -f`, `colab download`, and `colab stop`. State that agents need local terminal permission and a pre-authenticated local Google identity; include the rule to stop sessions and avoid submitting secrets or untrusted scripts.

- [x] **Step 3: Add the overview**

Write `Colab/README.md` with links to the other three files and a minimal CPU job example whose cleanup command is explicit.

### Task 4: Add and review the follow-up list

**Files:**
- Create: `Colab/TODO.md` — completed setup tasks and only remaining user decisions or follow-up work.

- [x] **Step 1: Write status-based TODO items**

Mark successful local installation and checks complete. Mark account login, cloud smoke test, or GPU entitlement checks complete only when observed; otherwise describe the exact user action that remains.

- [x] **Step 2: Review documentation consistency**

Run `git diff --check`; inspect the four files for consistent command names, accurate completion states, absent secrets, working relative links, and no discarded error history.

- [x] **Step 3: Report the result**

Summarize the CLI version, whether a cloud session was verified and stopped, created files, and any remaining account-dependent TODO.
