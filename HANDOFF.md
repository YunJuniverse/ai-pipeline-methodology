# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **METH-131 캡슐 트리아지 반영**(2026-08-07) — 15건 전량 종결(유효 13·이미 반영 1·만료 0). 도구 3건 + 지침 23 v2·19 v3·07·24 v2 반영, `_inbox` 비움(원장 16건 유지). branch `feat/capsule-triage-reflect`, PR 대기. 직전: METH-136 전파 12/12.
- **Current mode**: fullstack
- **Next TODO**: METH-131 캡슐 14건 트리아지(우선 invest-ops `tool/ship`·`tool/hooks` 2건 — land 와 한 세트였음 → CROSS-REPO 3묶음 → catalog 재발 건). METH-135 **첫 실주행 검증**(사이클 45~90분 환산 실측 → 지침 29 v2 환류) · 무인 권한 allowlist. 다른 repo(별도 세션): ai-icons 92 환류·비대 라이브파일 트리밍·grooman sync(타 호스트). **프로세스: branch-first · 스택-PR 지양(main 직행) · 세션 종료 = ship → land.** 상세는 checkpoint.
- **Blockers**: none — METH-131 판정이 사람 확정으로 해소됨.

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

- 2026-08-07: **METH-131 캡슐 트리아지 반영 — 15건 전량 종결 (Class A)** — 유효 13·이미 반영 1·만료 0. 도구 3건(pre-push 참조전용 면제·build-guard 프로젝트 스코프+`tsc --noEmit` 폴백·ship Done 주장 경고) + **지침 23 v2**(대리 신호 금지·성능 다회 중앙값·픽스처 특이값·§4 판정기 신뢰도 신설) · **19 v3**(§8b 원시함수 단일화·일괄 편집) · **07**(부작용 범위 봉쇄) · **24 v2**(§3b 이식 요청 입력 실측). `_inbox` 비움(원장 16건 유지).
- 2026-08-07: **METH-136 운영 모드 키워드 트리거 — 전파 12/12 (Class A)** — 지침 28·29 를 만들었지만 *키워드로 불러오는 경로*가 없던 갭을 닫음. 지침 01 §5.11 운영 모드 라우팅 표(실험/자율주행/07/land + 경계 판정 3항) 신설, CLAUDE.md·AGENTS.md §2 를 서술→**동작 지시**로 전환("본문 먼저 로드 후 착수, 요약만 보고 시작 금지"). 안전장치: 속도 요구만으로 실험 모드가 켜지지 않고 **샌드박스 4조건 확인이 선행**.
- 2026-08-07: **METH-133/134/135 전파 종결 12/12 (Class A, ADR-004)** — `land`(Class A+CI green fail-closed 자동 착지)·지침 28 실험 모드·지침 29 자율주행이 전 repo 반영. sync-all: main 7곳 직접·비-main/dirty 4곳 worktree, 전부 origin 대조(icons-vault 는 icons 워크트리라 자동 커버 — 실 repo 는 11개). **PR #140 을 land 가 스스로 머지**해 end-to-end 증명(maincheck 747e9457 ✓).
- 2026-08-07: **METH-133/134/135 자율 범위 확장 (Class A, 근거 ADR-004)** — ① `land` 신설: PR 식별→Class 판정→CI green→squash 머지→기본브랜치 동기화→maincheck, 전 단계 fail-closed(판정 불가 시 진행 금지). 수거 캡슐 `land-command-post-merge` 설계 채택. ② 지침 28 실험 모드: 샌드박스 4조건 안에서 Class B/C 유예, 경계 넘을 때 졸업 게이트 7항 일괄 정산. ③ 지침 29 자율주행: 시간→사이클 환산, 개발·검토·QA·신규작업 루프, ground-truth 판정, 기획 소진 시 시간 남아도 종료.
- 2026-08-07: **METH-132 CI `validate` 복구 (Class A)** — observation lint `repeat_of` 자유서술 6건(5월 레거시 5 + 07-24 1)을 허용 스키마로 정규화, 서술은 `resolution` 보존. **CI가 #136~#138 세 번 연속 main red였고 아무도 못 봄** — 자동 머지 설계(METH-133)의 전제를 먼저 복구. 교훈: 스키마를 좁힐 때 기존 자산 전수 재검증.