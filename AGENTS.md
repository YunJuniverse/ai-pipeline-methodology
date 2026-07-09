# AGENTS.md

> This file is auto-loaded by Codex at the start of each session.
> Fill the project settings before active work begins.

---

## 1. Project Settings

- **Project Name**: [PROJECT_NAME]
- **Objective**: [one-line goal]
- **Mode**: [planning / planning-handoff / dev / fullstack / agency / lean / ops]  <!-- 모드별 권장 템플릿 세트는 50_resources/templates/_CATALOG.md 참조 — 필요한 템플릿만 로드. planning-handoff(사람 개발자 인계)는 20_guides/09 재포맷 규칙 적용 -->
- **Stack**: [confirmed stack]
- **Primary Approver**: [name or role]
- **Started On**: [YYYY-MM-DD]
- **Release Policy**: [private / staged / public]

---

<!-- methodology:managed:start id=operating-rules -->
## 2. Operating Rules

<!-- 이 섹션은 원칙·load-bearing 규칙만 담는다(Anthropic 권장: <200줄, 준수율↑). 절차 상세는 지침이 정본 — 복제하지 않고 포인터. METH-083. -->

- Code is the source of truth for implementation; ADR for decisions code can't explain.
- `HANDOFF.md` is the only live state file (<150 lines). `TODO.md` is the active backlog (stable IDs + acceptance criteria).
- **세션·작업 종료 (의무)**: 작업 단위가 끝나면 4개 라이브 파일을 갱신하고 `python3 60_tools/methodology.py wrap`(→`4/4 ✓`)로 검증 후 보고. ① `TODO.md`(완료→Done·신규) ② `HANDOFF.md`(Working-on + Recent Changes 최근 5건) ③ `.ai/checkpoint.md`(인계서, 백서 §2-2) ④ 관찰 로그 — **반드시 CLI**: `methodology.py observe --slug <kebab> --task-type <bootstrap|feature|bugfix|refactor|research|docs> --summary "<50~150자>"` (직접 `cat >` 금지 — 형식오류로 wrap 실패). wrap v4.1+ = sha256 콘텐츠 비교(실내용 갱신만 통과).
- **commit/push (권장)**: 위 갱신 후 `methodology.py ship -m "<conventional>"` 하나로 wrap+manifest+sensitive+(test/build)+commit+push. 별도 `git add`/`commit`/`push` 금지 — *ship만*.
- **컨텍스트 컴팩션 (의무, 긴 세션)**: 요약 예고 시 *요약 전에* 라이브 파일(특히 `.ai/checkpoint.md`) 먼저 갱신 — 파일에 있으면 요약이 잃어도 복원. 규칙 `20_guides/06_컨텍스트_컴팩션_프로토콜.md`.
- **자율 진행 예산·정지 (권장)**: 다단계 자율 시 착수 전 예산(파일/PR/반복) 선언, no-progress 2회·예산 초과 시 멈춰 보고, 범위 축소 시 남긴 것 보고. `20_guides/07_자율진행_예산_및_정지조건.md` (멀티에이전트 팬아웃 `20_guides/08_서브에이전트_오케스트레이션.md`).
- **외주 인계·로컬 안전망**: 코드만 추출 `methodology.py export --path <p> --dry-run`(방법론·sensitive 기본 차단; `--allow-sensitive`/`--zip`); push 가드 `methodology.py hooks install`(pre-push manifest+wrap --strict).
- 식별자·버전 규칙은 `20_guides/02_식별자_및_버전_관리_규칙.md` 준수 후 새 ID 생성.
- `40_dev/snapshots/`는 날짜 산출물 — 라이브 아님. 사람 승인은 머지된 PR 또는 링크된 ADR·이슈로만 성립.
- Default boot context = `AGENTS.md` + `HANDOFF.md`; `TODO.md`·관련 코드·테스트·ADR은 필요 시 로드.
- **부팅 브리프 자동 로드 (의무)**: `00_briefs/current/*.md` 날짜순 전부 읽고 반영 내역 보고, 옛 브리프 충돌 시 자동 결정 금지·사용자 확인. `00_briefs/_README.md`.
- **부팅 마지막 (의무)**: `methodology.py dashboard` 호출 → 결과 URL을 첫 보고에 포함(이미 떠 있으면 기존 URL 재보고). 현재 브랜치 상태 반영.
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
| `AGENTS.md` | Project settings, change-class rules, workflow rules, file-role definitions, code/test conventions | Current sprint summaries, deliverable version tables, open-issue inventories, evolving implementation status |
| `CLAUDE.md` | Claude Code-facing mirror of `AGENTS.md` | Same restrictions as `AGENTS.md` |
| `HANDOFF.md` | Current focus, latest verified checks, latest local or merged work, open issues, next best actions, active links | Long project history, full sprint archives, methodology essays, duplicated ADR reasoning |
| `TODO.md` | Active backlog items with stable IDs, mode, change class, owner, acceptance criteria | Full completion archives — move historical detail to git, PRs, or dated snapshots |
| `40_dev/adr/` | Durable decisions that code cannot explain | Implementation detail that belongs in code |
| `40_dev/snapshots/` | Dated outputs, reviews, plans, runbooks | Live operating state — never promote a snapshot to a live document |
| Output channel (`30_planning/*` 기획서, 서비스/랜딩 페이지, 앱 UI, 브랜드 카피 — 맥락 없는 외부 독자와 공유되는 배포물) | 독자가 알아야 할 순수·무시간적 내용 | 작업 메타 — 워크플로우 기제·결정 서사·편집 라벨 (메시지 채널로 라우팅; `20_guides/05_산출물_채널_분리_규칙.md`) |

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
2. AI reads `AGENTS.md` and `HANDOFF.md`.
3. AI loads only the relevant TODO, code, tests, and ADRs.
4. AI determines the change class.
5. AI implements the change and opens a PR.
6. Human reviews and merges.
7. AI updates `HANDOFF.md` and `TODO.md`.

### Planning-Only

1. Human adds or confirms a planning item in `TODO.md`.
2. AI reads `AGENTS.md` and `HANDOFF.md`.
3. AI performs research and writes a dated snapshot under `40_dev/snapshots/`.
4. Human reviews through a PR or issue thread.
5. AI updates `HANDOFF.md` and `TODO.md`.

Restrictions:

- no direct push to `main`
- no approval claims without linked evidence
- no snapshot may be treated as a live operating document

---

## 7. Code And Review Rules

> fullstack/dev 트랙은 아래 규칙을 *린트 가드레일로 fail-closed 강제*한다 — 메커니즘·레이어 의존성 규칙·god파일 분할 패턴은 `20_guides/19_클린아키텍처_클린코드_개발규칙.md` 참조.

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

- architecture and product decisions go to `40_dev/adr/`
- use ADRs only when code cannot explain the reason

### Commit Types

- `feat`, `fix`, `refactor`, `docs`, `test`, `chore`

<!-- methodology:managed:end -->
