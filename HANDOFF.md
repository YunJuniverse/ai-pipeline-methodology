# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **METH-146 훅 wrap 읽기 전용**(branch `fix/hook-wrap-readonly`) — 구현·증명 완료, land 후 전파+훅 재설치 남음. 직전 완결: METH-145(훅 한글 경로) · 144(후속 2건) · 143(wrap 구조 검증) · 142(캡슐 4회차) — 전부 전파 11/11·origin 대조 ✓. 직전 완결: METH-143 · METH-142 캡슐 루프 4회차 — 수거 24건→판정→반영→전파 2회를 한 세션에 완주(#155·#157·#158·#159·#160·#161, maincheck 전건 ✓).
- **Current mode**: fullstack
- **Next TODO**: **METH-135 첫 실주행 검증**(사이클 45~90분 환산 실측 → 지침 29 v2 환류) · 무인 권한 allowlist(settings.json) · METH-134 실험 모드 첫 실전 적용. 다음 캡슐 수거는 다운스트림 축적 후(주기 약 1주). 후속 후보: capsule 발신 시점 id 검증(워크트리 접두어 경고 — METH-140 이전 발행분이 이번 수거에도 1건) · 월간 전수조사 2회차(8월 말). **프로세스: branch-first · 세션 종료 = ship → land.** 상세는 checkpoint.
- **Blockers**: none.

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
- 2026-09-02 — **METH-146 훅 wrap 읽기 전용**: pre-push 의 wrap 이 리포트 재생성·wrap-state 부트스트랩으로 repo 를 dirty 로 만들어 sync-all 이 skip 하던 부작용 제거(`wrap --read-only`). 대조군/실험군 + 실 push 증명, 91/91.
- 2026-09-02 — **METH-144·145 전파 종결 11/11**: 훅 재설치 직후 ai-icons·lifeManager 의 막혔던 커밋이 통과 — 한글 경로 수정의 e2e 증명. origin 대조 3항목 × 11 ✓. icons 워크트리가 계속 늘어(wt-admin·wt-cast 신규) sync-all 대상 18 — 전부 icons origin 공유라 실 repo 는 11.
- 2026-09-02 — **METH-145 훅 한글 경로 함정**: METH-142 훅 경로 판정이 `core.quotePath` 기본값 때문에 한글 지침 경로를 못 알아봐 2 repo push 차단. `-c core.quotePath=false` 로 수정, **한글 파일명 픽스처로 재증명**(ASCII 픽스처가 놓친 구멍 — 지침 23 §2-5). METH-144 전파는 9/11(잔여 2 는 훅 재설치 후).
- 2026-09-02 — **METH-144 후속 2건**: 지침 30 v2(워크트리 push 는 로컬 main 을 안 따라온다 — invest-ops 충돌 실사고) · 그래프 **지침 22~30 노드 9·엣지 18 백필**(42→51·53→71, lifecycle L2/L5/L6 배치). 첫 시도의 `json.dumps` 전면 재작성(1055줄 diff)을 되돌리고 행 단위 삽입으로 49줄 — §8b.3 자기적용.
- 2026-09-02 — **METH-143 전파 11/11 종결**: main 직접 8·격리 워크트리 3, origin 대조 ✓, 훅 3 repo 재설치. 전파 후 다운스트림 실측 **error 0 · warn 11** — 착수 전 예측과 일치(오탐 0).
- 2026-09-02 — **METH-143 wrap 라이브 파일 구조 검증**: Working-on·섹션·칸반 **중복을 error**(모호성 = 파서가 조용히 하나를 고름), 부재는 warn. 착수 전 12 repo 전수 실측으로 경계 확정(**error 0건** — 오탐 없이 사고만 잡는다). 87/87 green.
