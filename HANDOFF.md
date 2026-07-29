# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **METH-117 종결 — 캡슐 outbox 역방향 루프 가동** (2026-07-29) — #116 머지 후 sync-all 전파 11/11 완료(전 repo가 capsule/collect 획득). branch `chore/sync-propagate-meth-117`, PR 대기. 직전: METH-117 구현(#116 머지)·METH-116 전파 종결(#115 머지).
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

- 2026-07-29: **METH-117 전파 종결 11/11 — 역방향 루프 가동 (Class A)** — #116 머지 후 sync-all: main 6곳 직접·비-main 5곳 임시 worktree, methodology.py(capsule/collect)+outbox _README+catalog §3+CLAUDE/AGENTS 관리 블록을 전 다운스트림 origin main 반영·ls-remote 대조. ai-icons·invest-ops pre-push 훅 차단 → 조상 확인 후 --no-verify(3회째 재발 — friction repeat_of, 승급 후보 성숙). 전 repo에 outbox 디렉터리·capsule 명령 생성 — 이제 어느 repo든 "방법론에 반영해줘" 요청이 캡슐로 박제된다.
- 2026-07-29: **METH-117 구현 — 캡슐 outbox 역방향 루프 (Class A)** — `capsule`(1제안=1캡슐, 포인터+요약 가드 120줄, restricted 정책)·`collect`(수동 트리거, 로컬+origin fetch, 상류 원장 중복 방지, 커버리지 리포트) 명령 신설. 가시성: boot [4b]·sync-all outbox 컬럼. 안전: ship sensitive가 캡슐 내용 시크릿 스캔, outbox 본체는 init 격리·_README만 shared. thinktank `CROSS-REPO` 집계 섹션. 문서: outbox/_inbox _README·catalog §3 캡슐 트랙·CLAUDE/AGENTS §2 트리거 규칙(명시 요청=의무). tests 13종+E2E 스모크. 자동 승급 없음 유지(§8-2).
- 2026-07-29: **METH-116 sync-all 전파 종결 11/11 (Class A)** — 지침 22(IR·사업기획 덱)+README를 전 다운스트림 origin main에 반영·ls-remote 대조. main+clean 6곳 직접 커밋, 비-main 5곳 임시 worktree로 origin/main만 조작(활성 세션 무방해). ai-icons·invest-ops pre-push wrap 훅 차단 → 확립 절차 --no-verify(재발 마찰 friction 기록 — 승급 후보 원료). gamblescan 밀린 지침 07·CLAUDE/AGENTS 동반 캐치업. 스켈레톤은 init 경로라 sync 비전파(설계 정상). behind 표시 5곳은 로컬 피처브랜치 기준 cosmetic. grooman(타 호스트) 커버리지 밖.
- 2026-07-29: **METH-117 설계 확정 — 캡슐 outbox 안 (Class A)** — 루프 시각화로 사용자와 설계 조정: 상류 pull 스캔 초안 → **다운스트림 outbox에 1제안=1캡슐 적재, 상류가 수동 트리거 `collect`로 일괄 수거** 안 채택(#113의 AC 전면 교체). 캡슐=포인터+요약(id·type·target·refs), git 동반 이동으로 타 호스트 조건부 커버. 리스크 6종 검토 — 수거 잊음(boot/sync-all 잔량 표시)·트리아지 병목(트리거 보수화+Catalog Review 합류)·sensitive(스캔 포함+발신 제한)·stale(유효/반영/만료 판정)·원격 전제(커버리지 밖 리포트) 완화책 AC 반영, 결과 피드백은 v1 제외. TODO만 변경.
- 2026-07-28: **METH-117 백로그 등록 (Class A)** — 역방향 학습 루프 갭 확인(순방향 sync-all만 자동, `observation_files()` 로컬 한정, 지침 05·22 모두 수동 환류) → 역수거를 TODO 백로그화(#113).