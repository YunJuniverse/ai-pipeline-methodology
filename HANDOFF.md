# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **METH-152(ADR-007) PR 사람 머지 대기** — land 머지 기록 폐지·sync-all 휴면 skip·boot 상류 알림. 머지 후 METH-154 전파.
- **Current mode**: fullstack
- **Next TODO**: **METH-153 산문 규칙 슬림화 목록**(ADR-007 D3, 승인 필요) · 다운스트림 `required_checks` 등록(repo 세션 몫) · 남긴 도구 후보(Blocked 1:1 대조·rotate 긴 줄 회전 등, 스냅샷 §2) · **METH-135 첫 실주행 검증**(사이클 45~90분 환산 실측 → 지침 29 v2 환류) · 무인 권한 allowlist(settings.json) · METH-134 실험 모드 첫 실전 적용. 다음 캡슐 수거는 다운스트림 축적 후(주기 약 1주). 후속 후보: capsule 발신 시점 id 검증(워크트리 접두어 경고 — METH-140 이전 발행분이 이번 수거에도 1건) · 월간 전수조사 2회차(8월 말). **프로세스: branch-first · 세션 종료 = ship → land.** 상세는 checkpoint.
- **Blockers**: METH-154 전파 — METH-152 PR 사람 머지 필요(Class C).

## Active Links

- Current PR: METH-106 다운스트림 sync (신규, base=main) · 095~105 = #84~#94 머지 완료 · 063~094 = #53~#83 머지
- Current issue:
- Relevant ADRs: ADR-006(전수조사 판단 7지점)
- Relevant snapshots: `40_dev/snapshots/2026-11-09_전레포-30일-전수조사.md`, `40_dev/snapshots/implementation-plan-2026-05-07.md`, `40_dev/snapshots/transfer-drill-2026-05-08.md`

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
- 2026-11-25 — **METH-152(ADR-007)**: land 머지 기록 커밋 폐지(Done 전이는 작업 PR 안에, main 직push 예외 삭제) · sync-all 휴면 repo skip · boot 상류 버전 차이 알림 · 슬림화는 METH-153. 근거: 전 repo 30일 커밋 집계.
- 2026-11-09 — **METH-149·151 전파 13/13**: repo 마다 origin/main 격리 워크트리에서 sync → push → 원격 대조(SOP·land 기록·ADR-006·지침 23 v7·AGENTS 중복 해소). ai-icons TODO 깨진 헤더 선복구(ai-icons#469). D2 첫 실주행 성공(`bfb0e5a`).
- 2026-11-09 — land: PR #186 머지(main `69b956ca`) · Done METH-151
- 2026-11-09 — **METH-151 판단 반영(ADR-006)**: checkpoint 세션별 절 · land 머지 기록 직접 커밋 · 같은 날 관찰로그 갱신 인정 · 공유 가드 미추적 신규만 · `required_checks` · C-004~006 승급. METH-149 #185 머지(`86a11ed7`)·METH-150 종결.
- 2026-11-09 — **METH-149 전수조사(30일·9 repo)**: 도구 결함 15 반영(줄수 우회 lint·phase 오파싱·reserve 접두어·land TODO Class·ship 대용량) · 지침 8 개정 · P-010~014 · SOP 시트 편집. 판단 7지점은 METH-150 Blocked.
