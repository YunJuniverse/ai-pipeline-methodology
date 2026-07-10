# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-105 — 브리프 **자동 분류·정리 체계**. 유형 폴더(meetings/research/reference/ideas + standing) + "브리프 던지면 AI가 유형 판별해 배치" 규칙 + boot이 유형별 그룹 노출. Class A(7 repo). PR base=main 대기. 상세는 checkpoint.
- **Current mode**: fullstack
- **Next TODO**: 079~105 점검·정비 + 부팅/브리프 개선(101~105) 사이클 종료. 다른 repo(별도 세션): ai-icons 92 환류·비대 라이브파일 트리밍·업무기술서 SOP 박제, talmo-com. **프로세스: branch-first · 스택-PR 지양(main 직행) · 세션 시작 = `methodology boot`.** 상세는 checkpoint.
- **Blockers**: none

## Active Links

- Current PR: METH-105 브리프 자동분류 (신규, base=main) · 095~104 = #84·#89·#91·#92·#93 머지 완료 · 063~094 = #53~#83 머지
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

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-10: **METH-105 브리프 자동 분류·정리 체계 (Class A, PR base=main 대기)** — 사용자가 브리프를 던지면 AI가 유형 판별해 폴더 배치. 유형 폴더 신설(`research/`·`reference/`·`ideas/`; 기존 meetings/·standing/) + `_README §자동 분류` 규칙표(회의→meetings/조사→research/외부원본→reference/방향→ideas/반복절차→standing; 애매하면 확인) + CLAUDE/AGENTS §2 "브리프 자동 분류" 규칙 + boot이 유형별 그룹으로 노출(standing ★ 최상단). MANIFEST init_paths 반영. 검증: py_compile·boot 그룹 스캔·manifest·managed sync.
- 2026-07-10: **METH-104 SOP 트리거에 "인식 신호" 항목 추가 (Class A, PR #93 머지)** — 반복작업 매칭이 문자열 아닌 LLM 의미추론이라, SOP 트리거에 "어떤 요청/말이 이 작업을 의미하는가"(인식 신호) 앵커를 명시하면 매칭 신뢰도↑. `SOP_template.md` 트리거 = 인식신호 + 주기/이벤트로 분리, `_README §standing` 반영.
- 2026-07-10: **METH-103 상시 SOP 쓰기 트리거 규칙 (Class A, PR #92 머지)** — 102가 standing SOP의 *읽기*(boot 노출)만 완비하고 *쓰기* 반사신경이 없던 구멍을 메움. CLAUDE/AGENTS managed block에 "반복 작업 기억 (요청 시)" 규칙: 사용자가 "기억해줘/반복작업이야" → `standing/SOP_<topic>.md` 박제 + 절차 변경 시 갱신 제안 + 작업SOP(repo) vs 개인메모리(도구) 구분. _README §5도 반영. managed sync 확인.
- 2026-07-10: **METH-102 라이브파일 경계 재분리 + 상시 브리프 (Class A, PR #91 머지)** — HANDOFF=상태보드/checkpoint=서사 경계를 §4·§2·템플릿·에 못박아 중복 제거(checkpoint의 "미해결 결정사항"=HANDOFF Open Issues 중복 제거). `00_briefs/standing/`(반복작업 SOP·아카이브 안 됨) 신설, boot이 ★로 항상 최상단 노출. 반복 작업이 새 세션에 안 잊히게. #90(boot) 포함 base=main.
- 2026-07-10: **METH-101 부팅 강제 + 비대화 린트 (Class A, PR #90 OPEN)** — `methodology.py boot` 신설 + wrap 사이즈 린트(`live_file_size_warnings`). ai-icons 부팅 스킵 사고 상류 대응.
