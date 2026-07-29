# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **METH-125~127 종결 — 전파 11/11** (2026-07-29) — 전 repo가 스크래핑 SOP(standing)·CI 정합(지침 19 v2)·사실 주장 규칙(지침 05 v2) 획득. branch `chore/sync-propagate-meth-125-127`, PR 대기. **잔여 트리아지: METH-128 하나**(지침 22 보강 — _inbox 캡슐). 직전: METH-125~127 구현(#129 머지).
- **Current mode**: fullstack
- **Next TODO**: 후속 후보(백로그 미등록): graph.json에 outbox/collect 노드·invest-ops `capsule_policy: restricted` 부여(그 repo 세션·ADR-0001 근거)·pre-push 훅 vs sync push 충돌 3회 재발 → thinktank 승급 후보. 다른 repo(별도 세션): ai-icons 92 환류·비대 라이브파일 트리밍·grooman sync(타 호스트). **프로세스: branch-first · 스택-PR 지양(main 직행) · 세션 시작 = `methodology boot`.** 상세는 checkpoint.
- **Blockers**: none

## Active Links

- Current PR: METH-106 다운스트림 sync (신규, base=main) · 095~105 = #84~#94 머지 완료 · 063~094 = #53~#83 머지
- Current issue:
- Relevant ADRs:
- Relevant snapshots: `40_dev/snapshots/implementation-plan-2026-05-07.md`, `40_dev/snapshots/transfer-drill-2026-05-08.md`

## Open Decisions

| ID | Decision | Needed By | Status |
|----|----------|-----------|--------|
| - | `.claude/worktrees/` and `.codex/` are local tool metadata and should be gitignored | 2026-05-07 | Closed |

## Open Issues

| ID | Issue | Severity | Next Step |
|----|-------|----------|-----------|
| - | ~~sync가 다운스트림 고유 파일 mirror-delete~~ | — | **Closed** — METH-046(PR #35)로 prune을 --prune opt-in화(기본 보존) |
| - | ~~legacy/archive docs pre-v4 경로 언급~~ | — | **Closed(METH-091)** — 라이브 문서 sweep: `10_foundation/` 3건(`docs/snapshots/`→`40_dev/snapshots/`) 수정. 나머지는 정당(정확한 인용·예시)·90_archive는 히스토리 보존 |
| - | ~~v3.2 backward-compat 코드 폴백~~ | — | **Closed(METH-100)** — methodology.py·generate-dashboard.py의 v3.2 구조탐지·폴백(40_resources/60_meta/docs/legacy-root) 제거→v4.0 고정. `migrations/v3.2_to_v4.0.py`(이관)·런처/훅 부트스트랩 탐지는 보존. py_compile·dashboard 재생성·wrap 검증 |
| - | ~~ai-icons·icons-invest guide 번호 충돌~~ | — | **Closed(METH-089)** — 커스텀 04/05/21→90/91/92 이관·doc_id·참조 갱신, origin/main 검증. 잔여: ai-icons 92_LOCAL(구 21)은 상류 05 정본과 149줄 차이=로컬 발전분 → 각 repo 세션에서 상류 05로 환류·재조정 검토 |
| - | ~~sync 홀드 3곳(dirty)~~ | — | **Closed(METH-088)** — ai-icons·cafe24·icons-invest dirty 해소 후 086 sync 완료. **관리 다운스트림 6곳 전부 086 반영** |
| - | ~~`methodology-graph.json` 노드 불완전~~ | — | **Closed(METH-099)** — guide 10종(02·03·05·06·07·08·09·19·20·21) + 학습루프(observations·catalog·skeletons) + checkpoint 노드 추가, stale ai-log 제거. 노드 29→42·엣지 39→53. dashboard 렌더 검증(nodes=42)·JSON 정합 0 오류. (04는 미존재라 제외) |
| - | ⚠️ **스택-PR 재타깃 함정** — #85/#86/#87이 main 아닌 중간 브랜치로 머지됨(096/097/098 main 미반영) | — | **복구중(METH-099)** — 099 브랜치가 095-098 온전 보존 브랜치 기준 → base=main 단일 PR로 096+097+098+099 한 번에 복구. 교훈: 스택-PR은 순서·브랜치 삭제 타이밍 취약 → **main 직행 단일 PR 선호** |
| - | ~~`.claude/skills` 레거시 3종~~ | — | **Closed(METH-090)** — ai-planning·ai-relay·vibe-coding 삭제. 기능은 guide 01/08/19+prompts가 정본. 90_archive 히스토리는 보존 |
| - | icons-invest sync 커밋(f4e6605)에 `30_planning/10_사업기획서.md` 3줄 WIP 혼입 | Low | METH-106 sync 시 `git add -A`가 미커밋 WIP 쓸어담음. 내용 정당(미정 placeholder·Class C 미침범)·main 보존·유실 없음. 히스토리 재작성 안 함. **교훈: sync 커밋은 타깃 스테이징**(observe friction 기록) |
| - | **grooman이 이 머신 sync-all에서 미발견** — `/Users/hayden` 아래 `.methodology-version` 스캔에 없음(2026-07-23 확인). 등록 세션은 타 호스트(codex, darwin-26.4.1) 추정 | Low | grooman 작업 세션에서 실제 경로/호스트 확인 — 타 머신이면 sync-all 커버리지 한계로 HANDOFF에 명시, 이 머신이면 경로 복구 |
| - | ~~init 스캐폴드 HANDOFF `- Working on:` ↔ boot 파서 볼드 기대 불일치~~ | — | **Closed(METH-114)** — 파서 `_handoff_working_on` 헬퍼로 양쪽 허용 + 템플릿 볼드화 + 회귀 테스트(`tests/test_boot_handoff.py`). 둘 다 shared_paths라 다음 sync-all에서 전 다운스트림 자동 전파 |
| - | ~~ai-icons·talmo-com 다운스트림 sync 미적용~~ | — | **Closed(2026-07-15)** — 두 곳 clean 재확인 후 v4.0 sync·push(각 29파일). ai-icons push는 자체 라이브파일 비대로 pre-push 훅 차단→established 절차대로 --no-verify 우회. **잔여**: ai-icons 자체 checkpoint(547줄)·TODO Done(272건) 비대 트리밍은 그 repo 세션 몫 |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-29: **METH-125~127 전파 종결 11/11 (Class A)** — #129 머지 후 sync-all: main 6곳 직접·비-main/dirty 5곳 worktree, 전부 origin 대조. SOP_scraping-pace가 전 repo standing에 배포(boot 노출), 지침 05/19 v2 반영. 트리아지 채택 12건 중 **11건 종결** — 잔여 METH-128(지침 22 보강)뿐.
- 2026-07-29: **METH-125+126+127 구현 (Class A)** — ① 스크래핑 페이스 SOP 상류 승급(`00_briefs/standing/SOP_scraping-pace.md`, shared_paths 등록 — 페널티 누적 실측·프로브≠회복·IP 교체 무효·폴백 사다리·신규 소스 3축 평가) ② 지침 19 v2 §11 CI-로컬 정합(CI 매니저 검증·packageManager 핀·lockfile 가드·런북=실측) ③ 지침 05 v2 §9 사실 주장·샘플 규칙(출처 없는 주장 라이브 금지·[샘플] 마킹·근거 등급). 전수조사 P7·P8·P11 승급.
- 2026-07-29: **지침 23·24 전파 종결 11/11 (Class A)** — #127 머지 후 sync-all: main 5곳 직접·비-main/dirty 6곳 worktree, 전부 origin 대조. METH-123·124 Done(maincheck ✓). 트리아지 채택 12건 중 **10건 종결**(118~124) — 잔여 METH-125~128 + RFC-003 관찰.
- 2026-07-29: **지침 23·24 신설 (Class A, METH-123·124)** — 전수조사 잔여 P 패턴 승급: **23 검증 규범**(무음 실패 4규칙 — 0건=실패·검사불능≠깨끗함·가드 negative case·리드백 / 내용 기준 검증 3기준 / 검증불가 등록부+우회 사다리+비-포인터 대안), **24 착수 게이트**(정본 사용자 확인·조사 진단 코드 재검증·반증 대조군·해석 계약·사용자 경계 원문 검증 + 상황별 질문표). 각 규칙에 실사고 계보 명기. README §3.6·이력 v4.2.
- 2026-07-29: **METH-120+121 전파 종결 11/11 (Class A)** — #121 머지 후 sync-all: main+clean 5곳 직접, 비-main 3곳+dirty 3곳(icons·icons-invest·lifeManager — 활성 세션 무방해)은 임시 worktree로 origin/main만 반영, 전부 ls-remote 대조. 전 repo가 `maincheck`(Done 전이·배포 게이트)와 observe 스키마 강제(repeat_of enum·메타 자동 채움·domain 필수)를 획득 — 전수조사 P1·P2 결함이 전 다운스트림에서 구조적으로 차단됨. Done 이동은 maincheck 자가 검증(04535d0d ✓, dogfood). 훅 차단 2곳(ai-icons·invest-ops) --no-verify 확립 절차.