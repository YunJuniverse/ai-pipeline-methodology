# CLAUDE.md

> This file is auto-loaded by Claude Code at the start of each session.
> Fill the placeholders before project work begins.

---

## 0. Project Overview

- **Project Name**: [PROJECT_NAME]
- **Objective**: [one-line business or product goal]
- **Type**: [fullstack / planning-only / research / coding-only]
- **Stack**: [confirmed stack]
- **Started On**: [YYYY-MM-DD]
- **Current Version**: [v0.1]
- **Current Sprint**: [Sprint 01]
- **Current Phase**: [Phase 0~10]

---

## 1. Core Operating Principles

### Documents drive the next action
Every document is both an output and the input for the next task.
Research -> 기획서 -> 개발명세서 -> MVP Build -> Sprint Review -> Feedback Revision.

### Agile loop over one-pass delivery
This methodology does not stop after initial planning.
Every sprint must produce a build, a completion report, a feedback report, a sprint plan report, and updated documentation for the next sprint.

### Single source of truth per topic
Each fact should have one canonical home.
Other documents should summarize or reference it instead of duplicating it.

### Structure before prose
Start with sections, tables, decisions, and priorities before polishing language.

### No vague adjectives
Do not use words like "innovative" or "user-friendly" without concrete evidence, behavior, or criteria.

### Human approval at every gate
AI drafts, compares options, and recommends.
Humans review deliverables, approve, and instruct the next task at every gate.

### Version everything that changes meaning
기획서, 개발명세서, review reports, and MVP builds all carry versions.
If a document meaningfully changes, bump its version and record why.

### Traceability over speed
Each sprint should preserve a readable chain:
research -> 기획서 -> 개발명세서 -> build -> completion report -> feedback report -> research -> sprint plan report -> 개발명세서 update -> next build.

---

## 2. Agile Pipeline

### Phase 0: Project Init
- Fill project overview in CLAUDE.md / AGENTS.md
- Confirm stack, constraints, and first sprint goal
- Prepare folder structure and template set

### Phase 1: Discovery Research
- Problem research, market/reference scan, constraints and risk discovery
- output: `docs/research/research.md`
- **Gate 1**: 인간이 리서치 결과 검토 → "기획서 작성 시작해" 지시

### Phase 2: 기획서 작성 (6종)
Create and maintain business planning documents under `docs/planning/`:
1. `business-plan.md` (사업기획서)
2. `service-plan.md` (서비스기획서)
3. `operations-plan.md` (운영기획서)
4. `marketing-plan.md` (마케팅기획서)
5. `brand-plan.md` (브랜드기획서)
6. `project-management.md` (프로젝트관리기획서)
- **Gate 2**: 인간이 기획서 6종 검토/승인 → "개발명세서 작성해" 지시

### Phase 3: 개발명세서 작성 (8종)
Create and maintain development specification documents under `docs/development/`:
1. `service-overview.md` (서비스 개요서)
2. `requirements.md` (요구사항 정의서)
3. `user-stories.md` (사용자 스토리)
4. `information-architecture.md` (정보구조도)
5. `user-flow.md` (사용자 플로우차트)
6. `wireframes.md` (화면 설계서)
7. `functional-spec.md` (기능 정의서)
8. `data-model.md` (데이터 모델 정의서)
- **Gate 3**: 인간이 개발명세서 8종 검토/승인 → "MVP 개발 시작해" 지시

### Phase 4: MVP Build
- Build the scoped increment for the sprint
- output: working code, tests, and updated ADRs

### Phase 5: Sprint Completion Report
- Evaluate build result against plan, references, QA, and code conventions
- output: `docs/sprints/sprint-XX-completion-report.md`
- **Gate 4**: 인간이 빌드 결과 확인 → "환류 작업 진행해" 지시

### Phase 6: Sprint Feedback Report
- UI testing, QA, peer review, reference gap analysis
- Human-readable code convention compliance check
- Issue categorization and root cause hypothesis
- output: `docs/sprints/sprint-XX-feedback-report.md`

### Phase 7: Feedback-Driven Research
- Research to resolve issues from the feedback report
- Update existing research docs or create new ones
- output: `docs/research/research.md` (updated, version bumped internally)

### Phase 8: Sprint Plan Report
- Synthesize feedback report + additional research into next sprint plan
- Define next sprint goal, scope, risks, and approval needs
- output: `docs/sprints/sprint-XX-plan-report.md`
- **Gate 5**: 인간이 다음 스크럼 범위 승인 → "개발명세서 업데이트하고 N차 개발 시작해" 지시

### Phase 9: Development Spec Update
- Update 개발명세서 8종 based on the sprint plan report
- Bump versions of affected documents
- output: `docs/development/*.md` (updated, versions bumped internally)

> Phases 4 → 9 repeat until human confirms completion.

### Phase 10: Final Planning Update
- After human confirms "개발 완료"
- Update 기획서 6종 to final version reflecting actual implementation
- output: `docs/planning/*.md` (version bumped to vFinal internally)

---

## 3. Deliverables By Phase

| Phase | Required Outputs | Typical Versioning |
|------|------------------|--------------------|
| 0 | `CLAUDE.md` / `AGENTS.md` current state | project-level |
| 1 | research docs | `v0.1`, `v0.2` |
| 2 | 기획서 6종 | `v0.1`, `v0.2` |
| 3 | 개발명세서 8종 | `v0.1`, `v0.2` |
| 4 | MVP code + tests + ADR | `build-v0.1`, `build-v0.2` |
| 5 | sprint completion report | `sprint-01`, `sprint-02` |
| 6 | sprint feedback report | `sprint-01`, `sprint-02` |
| 7 | updated/new research docs | `v0.2`, `v0.3` |
| 8 | sprint plan report | `sprint-02-plan`, `sprint-03-plan` |
| 9 | updated 개발명세서 8종 | next version |
| 10 | final 기획서 6종 | `vFinal` |

---

## 4. Human Approval Gates

인간은 매 게이트에서 산출물을 받고, 검토하고, 다음 작업을 지시한다.
AI는 게이트 없이 다음 Phase로 넘어가지 않는다.

### Gate 1: Research Approval
After Phase 1 (Discovery Research):
- 인간이 리서치 결과를 검토
- 리서치 방향이 맞는지, 누락된 영역이 있는지 확인
- → "기획서 작성 시작해" 지시

### Gate 2: Planning Approval
After Phase 2 (기획서 6종):
- 인간이 기획서 6종을 검토/승인
- 사업 방향, 서비스 범위, 운영 정책, 마케팅 전략, 브랜드 방향, 프로젝트 일정이 맞는지 확인
- → "개발명세서 작성해" 지시

### Gate 3: Development Spec Approval
After Phase 3 (개발명세서 8종):
- 인간이 개발명세서를 검토/승인
- 기능 범위, IA, 플로우, 와이어프레임, 데이터 모델이 기획 의도와 맞는지 확인
- → "MVP 개발 시작해" 지시

### Gate 4: Build Review
After Phase 5 (Sprint Completion Report):
- 인간이 빌드 결과와 완료 보고서를 확인
- → "환류 작업 진행해" 지시

### Gate 5: Next Sprint Approval
After Phase 8 (Sprint Plan Report):
- 인간이 다음 스크럼 계획 보고서를 검토/승인
- 다음 스프린트 범위와 목표가 적절한지 확인
- → "개발명세서 업데이트하고 N차 개발 시작해" 지시

### Gate 6: Final Confirmation
When human declares "개발 완료":
- → "기획서 최종 업데이트해" 지시
- 기획서 6종을 실제 구현 결과에 맞춰 최종 버전으로 업데이트

---

## 5. Current State

### Last Work
- Date: [YYYY-MM-DD]
- Summary: [one-line summary]

### Current Deliverable Versions

| Deliverable | Current Version | Status | Notes |
|------------|-----------------|--------|-------|
| Research | [v0.1] | [draft / approved] | [notes] |
| 기획서 6종 | [v0.1] | [draft / approved] | [notes] |
| 개발명세서 8종 | [v0.1] | [draft / approved] | [notes] |
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
| [DATE] | 기획서 6종 and 개발명세서 8종 are versioned assets | repeated sprint updates require traceability | docs and build flow |
| [DATE] | Human approval gates at every phase transition | AI does not proceed without human review and instruction | whole project |

> Store detailed ADR files in `docs/adr/` with ordered filenames.
