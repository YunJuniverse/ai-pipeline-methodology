# AGENTS.md

> This file is auto-loaded by Codex at the start of each session.
> Fill the placeholders before project work begins.

---

## 0. Project Overview

- **Project Name**: [PROJECT_NAME]
- **Objective**: [one-line business or product goal]
- **Type**: [fullstack]
- **Stack**: [confirmed stack]
- **Started On**: [YYYY-MM-DD]
- **Current Version**: [v0.1]
- **Current Sprint**: [Sprint 01]
- **Current Phase**: [Discovery / Planning / Build / Review / Feedback]

---

## 1. Core Operating Principles

### Documents drive the next action
Every document is both an output and the input for the next task.
Research -> Planning Docs -> Development Spec -> MVP Build -> Sprint Review -> Feedback Revision.

### Agile loop over one-pass delivery
This methodology does not stop after initial planning.
Every sprint must produce a build, a review, a feedback report, and updated documentation for the next sprint.

### Single source of truth per topic
Each fact should have one canonical home.
Other documents should summarize or reference it instead of duplicating it.

### Structure before prose
Start with sections, tables, decisions, and priorities before polishing language.

### No vague adjectives
Do not use words like "innovative" or "user-friendly" without concrete evidence, behavior, or criteria.

### Human approval at decision gates
AI can draft, compare options, and recommend.
Humans approve strategy changes, scope changes, architecture changes, and sprint close decisions.

### Version everything that changes meaning
Planning docs, development specs, review reports, and MVP builds all carry versions.
If a document meaningfully changes, bump its version and record why.

### Traceability over speed
Each sprint should preserve a readable chain:
research -> planning update -> development spec update -> build -> review -> feedback -> next sprint.

---

## 2. Agile Pipeline

### Phase 0: Project Init
- Fill project overview
- Confirm stack, constraints, and first sprint goal
- Prepare folder structure and template set

### Phase 1: Discovery Research
- Problem research
- market/reference scan
- constraints and risk discovery
- outputs go into `docs/research/`

### Phase 2: Planning Documents
Create and maintain the planning set under `docs/planning/`:
1. `service-overview.md`
2. `requirements.md`
3. `user-stories.md`
4. `information-architecture.md`
5. `user-flow.md`
6. `wireframes.md`
7. `functional-spec.md`
8. `data-model.md`
9. `operations-policy.md` [optional but recommended]

### Phase 3: Development Spec
- Convert current planning version into implementation-ready scope
- output: `docs/development/development-spec.md`

### Phase 4: MVP Build
- Build the scoped increment for the sprint
- output: working code, tests, and updated ADRs

### Phase 5: Sprint Review
- Evaluate build result against plan, references, QA, and code conventions
- output: `docs/sprints/sprint-XX-completion-report.md`

### Phase 6: Feedback Revision
- Research current issues
- summarize gap analysis and corrective actions
- output: `docs/sprints/sprint-XX-feedback-report.md`

### Phase 7: Next Sprint Update
- Update planning docs to next version
- Update development spec to next version
- define next sprint scope and acceptance criteria

> Phases 4 -> 7 repeat until approval or release readiness.

---

## 3. Deliverables By Phase

| Phase | Required Outputs | Typical Versioning |
|------|------------------|--------------------|
| 0 | `AGENTS.md` current state | project-level |
| 1 | research docs | `v0.1`, `v0.2` |
| 2 | planning docs set | `v0.1`, `v0.2` |
| 3 | development spec | `v0.1`, `v0.2` |
| 4 | MVP code + tests + ADR | `build-v0.1`, `build-v0.2` |
| 5 | sprint completion report | `sprint-01`, `sprint-02` |
| 6 | sprint feedback report | `sprint-01`, `sprint-02` |
| 7 | updated planning + updated development spec | next version |

---

## 4. Definition Of Done Gates

### Planning Gate
Before build starts:
- planning docs are internally consistent
- out-of-scope is explicit
- MVP acceptance criteria exist
- human approved sprint scope

### Build Gate
Before sprint review:
- core scope implemented
- critical paths tested
- known issues listed
- ADR updated if architecture changed

### Review Gate
Before feedback closes:
- UI/UX issues captured
- QA defects categorized
- reference gaps identified
- human-readable code convention review complete
- peer review findings summarized

### Feedback Gate
Before next sprint starts:
- root causes identified
- research updated if needed
- planning docs updated to new version
- development spec updated to new version
- next sprint goal approved

---

## 5. Current State

### Last Work
- Date: [YYYY-MM-DD]
- Summary: [one-line summary]

### Current Deliverable Versions

| Deliverable | Current Version | Status | Notes |
|------------|-----------------|--------|-------|
| Research | [v0.1] | [draft / approved] | [notes] |
| Planning Docs | [v0.1] | [draft / approved] | [notes] |
| Development Spec | [v0.1] | [draft / approved] | [notes] |
| MVP Build | [v0.1] | [building / review / approved] | [notes] |

### Key Decisions
- [append important decisions]

### Open Issues

| # | Issue | Severity | Owner | Status | Notes |
|---|-------|----------|-------|--------|-------|
| - | - | - | - | - | - |

### Next Sprint Goal
- [what the next sprint must achieve]

### Immediate Next Task
- [the next concrete task for this session]

---

## 6. Code Conventions

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

### Quality Rules
- business logic requires tests
- architecture decisions go to `docs/adr/`
- layer boundary violations are not allowed
- code should remain readable to humans first, AI second

### Commit Types
- `feat`, `fix`, `refactor`, `docs`, `test`, `chore`

---

## 7. ADR Log

| Date | Decision | Reason | Impact |
|------|----------|--------|--------|
| [DATE] | Adopt agile feedback-driven methodology | planning-build-review loop is the main operating model | whole project |
| [DATE] | Planning docs are versioned assets | repeated sprint updates require traceability | docs and build flow |

> Store detailed ADR files in `docs/adr/` with ordered filenames.
