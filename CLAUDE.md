# CLAUDE.md

> This file is auto-loaded by Claude Code at the start of each session.
> Fill the project settings before active work begins.

---

## 1. Project Settings

- **Project Name**: [PROJECT_NAME]
- **Objective**: [one-line goal]
- **Mode**: [planning / dev / fullstack / agency / lean / ops]  <!-- 모드별 권장 템플릿 세트는 50_resources/templates/_CATALOG.md 참조 — 필요한 템플릿만 로드 -->
- **Stack**: [confirmed stack]
- **Primary Approver**: [name or role]
- **Started On**: [YYYY-MM-DD]
- **Release Policy**: [private / staged / public]

---

<!-- methodology:managed:start id=operating-rules -->
## 2. Operating Rules

- Code is the source of truth for implementation details.
- ADR is the source of truth for decisions that code cannot explain.
- `HANDOFF.md` is the only live state file. Keep it under 150 lines.
- `TODO.md` is the active backlog. Use stable IDs and acceptance criteria.
- **세션·작업 종료 절차 (의무, 모든 AI 모델 공통)**: 자연스러운 작업 단위가 끝나면 다음 4개 라이브 파일을 *AI가 자동으로* 갱신한 뒤 `python3 60_tools/methodology.py wrap` 으로 검증 → 결과를 사용자에게 보고. 사용자는 다음 turn에서 결과를 보고 수정 요청 가능.
  1. `TODO.md` — 완료 항목 Done 이동, 새 항목 추가
  2. `HANDOFF.md` — Current Focus + Recent Changes 갱신 (최근 5건 유지)
  3. `.ai/checkpoint.md` — 다음 사람·다른 AI를 위한 인계서 갱신 (백서 §2-2 형식)
  4. **관찰 로그 작성 — 반드시 CLI 사용 (직접 `cat >` 금지)**:
     ```
     python3 60_tools/methodology.py observe \
       --slug "<kebab-case-slug>" \
       --task-type <bootstrap|feature|bugfix|refactor|research|docs> \
       --summary "<50~150자 자유서술>"
     ```
     CLI 가 frontmatter·enum·길이 검증을 atomic 하게 처리. `cat > .md` 직접 작성은 형식 오류로 wrap·CI 실패 유발.
  wrap 출력이 `4/4 ✓` 일 때만 종료. `✗` 가 있으면 누락 갱신 후 다시 호출. wrap v4.1+ 는 sha256 콘텐츠 해시 비교 — *실제 내용 갱신* 만 통과 (`touch`/동일 내용 재저장 차단).
- **컨텍스트 컴팩션 경계 (의무, 긴 세션)**: 컨텍스트가 한계에 근접하거나 하네스가 요약(compaction)을 예고하면, *요약 전에* 라이브 파일(특히 `.ai/checkpoint.md`의 방금 한 것·다음 사람에게·미해결 결정)을 먼저 갱신한다. compaction 은 "세션 중간 인계" — 파일에 상태가 있으면 요약이 잃어도 복원된다. 보존/폐기 규칙·pre-compaction 체크리스트는 `20_guides/06_컨텍스트_컴팩션_프로토콜.md`. 핵심: *"compaction 후의 내가 이걸 잃으면 사용자에게 다시 물어야 하나?"* → 그렇다면 보존, 파일 재로드로 되는 것은 경로만 남기고 폐기.
- **commit/push 자동화 (권장)**: 위 4 파일 갱신 후 `python3 60_tools/methodology.py ship -m "<conventional commit message>"` 한 명령으로 wrap+manifest-check+sensitive 검사+(test/build)+commit+push 일괄 처리. 별도로 `git add`/`git commit`/`git push` 호출 금지 — *ship*만 사용.
- **외주 인계 (코드만 추출)**: `python3 60_tools/methodology.py export --path <project> --dry-run` 으로 포함·제외 미리보기 후, `--dry-run` 빼고 재호출. `<project>-handover/` 폴더에 *방법론·메타·브리프 모두 제외*된 코드만 추출. sensitive 파일(.env/credentials/keys)은 *기본 차단* — 의도 확인 후 `--allow-sensitive`. `--zip` 으로 tar.gz 압축. 결과 검증: *방법론 흔적 잔존 0* 자동 보장.
- **로컬 안전망 (1회 설치)**: `python3 60_tools/methodology.py hooks install` — `.git/hooks/pre-push`에 manifest-check + wrap --strict 자동 등록. push 직전 검증 실패 시 push 자체 차단. 우회는 `git push --no-verify` (의식적 비상 탈출).
- Identifier and versioning rules (phase M0/M1, sprint S-NNN, TODO ID, ADR, doc version, AI feature ID) are defined in `20_guides/02_식별자_및_버전_관리_규칙.md`. Follow that file before creating any new identifier.
- `40_dev/snapshots/` contains dated artifacts. Snapshots are never live source.
- Human approval is only real when evidenced by a merged PR or a linked issue/ADR approval.
- Default boot context is `CLAUDE.md` + `HANDOFF.md`.
- Load `TODO.md`, related code/tests, and related ADRs only when needed.
- **세션 부팅 시 브리프 자동 로드 (의무)**: `00_briefs/current/*.md` 의 모든 .md 파일을 *날짜 순* 으로 읽음. 인간이 던진 raw 입력(아이디어·리서치·회의록)을 *기획서·개발 산출물에 어떻게 반영* 했는지 작업 보고에 명시. *옛 브리프와 충돌* 발견 시 자동 결정 금지 — 사용자에게 확인. 자세히는 `00_briefs/_README.md`.
- **세션 부팅 마지막 단계 (의무, 모든 AI 모델 공통)**: `must_read` 로드 + checkpoint 확인 후, **반드시** 다음을 호출하고 결과 URL을 사용자에게 첫 보고 메시지에 포함:
  ```
  python3 60_tools/methodology.py dashboard
  ```
  - 출력: `http://localhost:8765 (branch: <name>, commit: <sha>)`. 사용자가 ⌘+클릭으로 즉시 열어 *현재 브랜치 상태*를 확인.
  - 이미 떠 있으면 중복 시작하지 않고 기존 URL 보고.
  - dashboard는 *현재 작업 디렉터리·현재 브랜치*를 반영. main 고정 아님 — 브랜치 전환 후 다시 호출하면 그 브랜치 상태로 재빌드.
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
2. AI reads `CLAUDE.md` and `HANDOFF.md`.
3. AI loads only the relevant TODO, code, tests, and ADRs.
4. AI determines the change class.
5. AI implements the change and opens a PR.
6. Human reviews and merges.
7. AI updates `HANDOFF.md` and `TODO.md`.

### Planning-Only

1. Human adds or confirms a planning item in `TODO.md`.
2. AI reads `CLAUDE.md` and `HANDOFF.md`.
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
