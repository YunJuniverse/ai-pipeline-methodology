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
- `docs/snapshots/` contains dated artifacts. Snapshots are never live source.
- Human approval is only real when evidenced by a merged PR or a linked issue/ADR approval.
- Default boot context is `CLAUDE.md` + `HANDOFF.md`.
- Load `TODO.md`, related code/tests, and related ADRs only when needed.

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

## 4. Workflow

### Fullstack

1. Human adds a TODO item with acceptance criteria.
2. AI reads `CLAUDE.md` and `HANDOFF.md`.
3. AI loads only the relevant TODO, code, tests, and ADRs.
4. AI determines the change class.
5. AI implements the change and opens a PR.
6. Human reviews and merges.
7. AI updates `HANDOFF.md` and `TODO.md`.

### Planning-Only

1. Human adds a research or planning TODO with acceptance criteria.
2. AI reads `CLAUDE.md` and `HANDOFF.md`.
3. AI performs research and writes a dated snapshot under `docs/snapshots/`.
4. Human reviews through a PR or issue thread.
5. AI updates `HANDOFF.md` and `TODO.md`.

Restrictions:

- no direct push to `main`
- no approval claims without linked evidence
- no snapshot may be treated as a live operating document

---

## 5. Code And Review Rules

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
