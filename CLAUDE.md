# CLAUDE.md

> This file is auto-loaded by Claude Code at the start of each session.
> Fill the project settings before active work begins.

---

## 1. Project Settings

- **Project Name**: [PROJECT_NAME]
- **Objective**: [one-line goal]
- **Mode**: [fullstack / planning-only]
- **Stack**: [confirmed stack]
- **Primary Approver**: [name or role]
- **Started On**: [YYYY-MM-DD]
- **Release Policy**: [private / staged / public]

---

## 2. Operating Rules

- Code is the source of truth for implementation details.
- ADR is the source of truth for decisions that code cannot explain.
- `HANDOFF.md` is the only live state file. Keep it under 150 lines.
- `TODO.md` is the active backlog. Use stable IDs and acceptance criteria.
- `docs/snapshots/` contains dated artifacts. Snapshots are never live source.
- Human approval is only real when evidenced by a merged PR or a linked issue/ADR approval.
- Default boot context is `CLAUDE.md` + `HANDOFF.md`.
- Load `TODO.md`, related code/tests, and related ADRs only when needed.
- `AI-LOG.md` is optional. Use it only for short collaboration notes not yet captured in `HANDOFF.md`, `TODO.md`, a PR, or an ADR.
- Do not keep sprint summaries, deliverable tables, or open-issue lists in this file.

---

## 3. Change Class Triggers

### Class A

- Default class.
- Applies to normal feature work, UI copy/style changes, internal refactors, and bug fixes that do not change schema, auth, or external contracts.
- Gate: merged PR.

### Class B

Automatic `Class B` triggers:

- DB migration or schema change
- New external API or changed integration contract
- Authentication or authorization change
- Destructive data change
- Background job, scheduler, or queue introduction

Required evidence in the PR:

- decision rationale
- impact scope
- rollback plan
- data/auth/external-contract risk

### Class C

Automatic `Class C` candidates:

- pricing or billing policy
- legal, compliance, or policy change
- brand or public messaging change
- public release or launch decision
- scope commitment made to outside stakeholders

Process:

- pause implementation
- create or update an ADR or linked issue discussion
- wait for explicit human approval evidence
- implement only after that approval exists

Additional rule:

- AI may escalate work upward from `A` to `B/C`.
- AI must not silently downgrade an automatic `B/C` trigger.

---

## 4. File Roles

| File | Contains | Must NOT contain |
|------|----------|-----------------|
| `CLAUDE.md` | Project settings, change-class rules, workflow rules, file-role definitions, code/test conventions | Current sprint summaries, deliverable version tables, open-issue inventories, evolving implementation status |
| `AGENTS.md` | Codex-facing mirror of `CLAUDE.md` | Same restrictions as `CLAUDE.md` |
| `HANDOFF.md` | Current focus, latest verified checks, latest local or merged work, open issues, next best actions, active links | Long project history, full sprint archives, methodology essays, duplicated ADR reasoning |
| `TODO.md` | Active backlog items with stable IDs, mode, change class, owner, acceptance criteria | Full completion archives — move historical detail to git, PRs, or dated snapshots |
| `AI-LOG.md` | Optional short collaboration notes not yet in a durable home | Duplicates of `HANDOFF.md`, `TODO.md`, PR descriptions, or ADR decisions |
| `docs/adr/` | Durable decisions that code cannot explain | Implementation detail that belongs in code |
| `docs/snapshots/` | Dated outputs, reviews, plans, runbooks | Live operating state — never promote a snapshot to a live document |

---

## 5. Human Approval Gates

Phase gates require explicit human instruction before the AI proceeds to the next phase.

Rules:
- AI does not cross a phase gate without a human review and an explicit next instruction.
- A phase gate is only passed when the human provides a named trigger phrase or links durable approval evidence (merged PR, ADR, or issue).
- AI may surface a gate recommendation ("ready for Phase N review") but must not self-advance.

Typical gate points:

| Gate | When | What the human provides |
|------|------|-------------------------|
| Research → Planning | After research deliverable | Instruction to begin planning document |
| Planning → Dev Spec | After planning review | Instruction to write development spec |
| Dev Spec → Build | After spec review | Instruction to start implementation |
| Build → Feedback | After build review | Instruction to begin feedback/hardening pass |
| Feedback → Next Sprint | After feedback integration | Instruction to update spec and start next sprint |
| Final | Work declared complete | Explicit completion declaration |

> Customize gate labels and trigger phrases for your project in `HANDOFF.md` or a project-specific ADR. Keep this section as the structural rule only.

---

## 6. Workflow

### Fullstack

1. Human adds or confirms a backlog item in `TODO.md`.
2. AI reads `CLAUDE.md` and `HANDOFF.md`.
3. AI loads only the relevant TODO, code, tests, and ADRs.
4. AI determines the change class.
5. AI implements the change and opens a PR.
6. Human reviews and merges.
7. AI updates `HANDOFF.md` and `TODO.md`.

### Planning-Only

1. Human adds or confirms a planning item in `TODO.md`.
2. AI reads `CLAUDE.md` and `HANDOFF.md`.
3. AI performs research and writes a dated snapshot under `docs/snapshots/`.
4. Human reviews through a PR or issue thread.
5. AI updates `HANDOFF.md` and `TODO.md`.

Restrictions:

- no direct push to `main`
- no approval claims without linked evidence
- no snapshot may be treated as a live operating document

---

## 7. Code And Review Rules

### Naming

- files: plural nouns where appropriate (`users.ts`, `orders.ts`)
- banned suffixes: `Manager`, `Helper`, `Util`, `Thing`
- components/classes: PascalCase
- functions/variables: camelCase
- constants/env vars: UPPER_SNAKE_CASE
- types: PascalCase, no `I` prefix

### Structural Rules

- split functions that exceed 50 lines
- avoid nesting deeper than 3 levels
- no `any`; use `unknown` plus type guards
- no production `console.log`
- update barrel exports intentionally, not blindly

### Testing And Errors

- business logic changes require tests
- start from tests by default; if you cannot write tests first, explain why in the PR
- lint and type checks must pass before review
- do not swallow errors; normalize boundary errors intentionally
- auth, data, and external API changes must call out risk explicitly in the PR

### Decision Records

- architecture and product decisions go to `docs/adr/`
- use ADRs only when code cannot explain the reason

### Commit Types

- `feat`, `fix`, `refactor`, `docs`, `test`, `chore`
