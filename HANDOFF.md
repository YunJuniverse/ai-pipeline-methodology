# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-107 sync-all 헬퍼 (feat/sync-all-helper, PR 대기). 관리 다운스트림(현 10곳: +lifeManager·icons-marketing·insta-toon 신규 init) 전체 일괄 sync 명령. --apply 안전 가드로 dirty·비-main skip. 테스트 9개.
- **Current mode**: fullstack
- **Next TODO**: 079~105 점검·정비 + 부팅/브리프 개선(101~105) 사이클 종료. 다른 repo(별도 세션): ai-icons 92 환류·비대 라이브파일 트리밍·업무기술서 SOP 박제, talmo-com. **프로세스: branch-first · 스택-PR 지양(main 직행) · 세션 시작 = `methodology boot`.** 상세는 checkpoint.
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
| - | ~~ai-icons·talmo-com 다운스트림 sync 미적용~~ | — | **Closed(2026-07-15)** — 두 곳 clean 재확인 후 v4.0 sync·push(각 29파일). ai-icons push는 자체 라이브파일 비대로 pre-push 훅 차단→established 절차대로 --no-verify 우회. **잔여**: ai-icons 자체 checkpoint(547줄)·TODO Done(272건) 비대 트리밍은 그 repo 세션 몫 |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-15: **METH-107 sync-all 일괄 sync 헬퍼 (Class A, PR 대기)** — `methodology sync-all`: root(기본 방법론 상위 `~/`) 아래 `.methodology-version` 보유 프로젝트 자동 발견 → 사전 스캔 표(project·version·branch·dirty·vs-upstream) → 각 프로젝트 `cmd_sync` 위임(main-only) → 요약. **--apply 안전 가드**: dirty repo·비-main 브랜치는 skip(오늘 METH-106 교훈 박제 — 진행 중 작업/피처브랜치 오염 방지), `--include-dirty`·`--allow-nonmain`로 override. commit/push는 각 repo 개별(add -A 혼입 회피). `tests/test_sync_all.py` 9개(발견·가드·behind 판정, 의존성 없는 자체 러너). 실측: 10곳 발견·표·dry-run 정상. **주의**: methodology.py가 shared라 이 헬퍼는 다음 sync 때 다운스트림에 전파됨.
- 2026-07-15: **다운스트림 sync 보류분 처리 + 신규 3곳 init (Class A)** — 관리 7곳 현행 점검(status "behind"는 upstream tip이 METH-106 sync 기록 문서라서였고, 실측 5곳 이미 현행/2곳 ai-icons·talmo-com 미반영→sync·push 완료). 이후 신규 fullstack repo 3곳 init·비공개 origin 생성: lifeManager·icons-marketing·insta-toon. → 관리 다운스트림 10곳.
- 2026-07-10: **METH-106 다운스트림 sync 5곳 (Class A, PR #95 머지)** — 092~105 전파. icons-invest(main)·cafe24·gamblescan·icons·tshome(feature 브랜치→main 체크아웃 후 sync·원 브랜치 복원). 각 29파일 shared+managed 머지, 커스텀 guide --prune 없이 보존, main 직접 push. 혼입 1건(icons-invest add -A, 정당·유실 없음). 교훈: sync 커밋 타깃 스테이징.
- 2026-07-10: **METH-105 브리프 자동 분류·정리 체계 (Class A, PR #94 머지)** — 브리프 던지면 AI가 유형 판별해 폴더 배치. 유형 폴더 신설(research/reference/ideas) + `_README §자동 분류` 규칙표 + CLAUDE/AGENTS §2 규칙 + boot 유형별 그룹 노출. MANIFEST init_paths 반영.
- 2026-07-10: **METH-104 SOP 트리거에 "인식 신호" 항목 추가 (Class A, PR #93 머지)** — 반복작업 매칭이 LLM 의미추론이라, SOP 트리거에 "어떤 요청/말이 이 작업을 의미하는가"(인식 신호) 앵커 명시로 매칭 신뢰도↑. `SOP_template.md`·`_README §standing` 반영.
