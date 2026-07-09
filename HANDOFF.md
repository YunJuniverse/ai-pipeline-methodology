# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: 메타/dev 지침 심화 배치(사용자 "전부"). **METH-092 완료분**: guide 03(관찰 로그) 심화 — §5 수동요청→`observe` CLI 정본화(cat 금지·헌법 §2④), `--friction` positional 형식·캡처 규칙, §6 학습루프 파이프라인(observe→thinktank→pending→catalog→skeleton)+"마찰 안 남기면 굶는다", v2 이력. **다음(리서치 완료)**: 093=06 컴팩션·07 자율·08 서브에이전트(웹리서치 3건 반영), 094=05·09+02/19/20 경량. Class A(guide 03=Class B). PR 대기.
- **Current mode**: fullstack
- **Next TODO**: ① **점검·정합·구조·전파·정비 사이클 완료** — 079~091(…·SPRINTS붕괴·다운스트림 sync 6곳·번호 remediation·skills 삭제·경로 sweep). 남은 후보(전부 Low·선택): agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs), 메타/dev 지침(02~09·19~20), graph.json 노드(02~09·19~21), v3.2 backward-compat 코드 정리(별건). 다른 repo(별도 세션): ai-icons 92_LOCAL↔상류05 환류, talmo-com 실작업. ② 학습 루프 후속: friction 축적→thinktank→catalog 승급→skeleton bake. **프로세스: branch-first 준수.**
- **Blockers**: none

## Active Links

- Current PR: METH-092 guide 03 심화 (신규) · METH-091 legacy sweep = #80 머지 완료 · 063~090 = #53~#79 머지 완료
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
| - | (참고, 별건) v3.2 backward-compat 코드 폴백 — `methodology.py _wrap_obs_dirs`·dashboard obs/templates 폴백(40_resources/60_meta/docs) | Low | 현존 repo 7곳 전부 v4.0이라 dead. 제거 시 v3 지원 포기 — 필요시 별도 판단(마이그레이션 스크립트는 유지) |
| - | ~~ai-icons·icons-invest guide 번호 충돌~~ | — | **Closed(METH-089)** — 커스텀 04/05/21→90/91/92 이관·doc_id·참조 갱신, origin/main 검증. 잔여: ai-icons 92_LOCAL(구 21)은 상류 05 정본과 149줄 차이=로컬 발전분 → 각 repo 세션에서 상류 05로 환류·재조정 검토 |
| - | ~~sync 홀드 3곳(dirty)~~ | — | **Closed(METH-088)** — ai-icons·cafe24·icons-invest dirty 해소 후 086 sync 완료. **관리 다운스트림 6곳 전부 086 반영** |
| - | `methodology-graph.json` 노드 불완전 — guide 02~09·19~21 누락(00·01·10~18만) | Low | 대시보드 시각화 그래프. METH-079에서 발견. 노드/엣지 보강은 별건(대시보드 렌더 영향 확인 후) |
| - | ~~`.claude/skills` 레거시 3종~~ | — | **Closed(METH-090)** — ai-planning·ai-relay·vibe-coding 삭제. 기능은 guide 01/08/19+prompts가 정본. 90_archive 히스토리는 보존 |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-09: **METH-092 guide 03(AI 관찰 로그) 심화 — CLI 정본화 + 학습루프 연결 (Class B, PR 대기)** — 메타/dev 지침 심화 배치의 1번(내부 정합, 리서치 불요). guide 03이 §5에서 아직 수동 `cat` 요청 방식을 안내(stale)하던 것을 **`observe` CLI 정본화**: 직접 `cat >` 금지(형식오류로 wrap fail)·헌법 §2④ 의무화 명시 + `--friction` **positional 형식**(where\|cost_minutes\|resolution\|repeat_of)·캡처 규칙(비자명·재발·막힘만, 노이즈 방지)·where=재발판정키. §6에 **학습 파이프라인**(observe→thinktank[≥2 승급후보]→pending→catalog→skeleton) + "마찰 안 남기면 루프 굶는다" + catalog/skeleton _README 교차링크. v2 변경이력 신설. METH-085(friction 규칙)·086(flow) 반영.
- 2026-07-09: **METH-091 legacy 경로 sweep — 라이브 문서 3건 수정 (Class A, PR #80 머지)** — 라이브 문서의 pre-v4 경로 참조 점검(90_archive·마이그레이션·시점기록 제외). **실제 stale 3건 발견·수정**: `10_foundation/{KICKOFF_PROMPT,DIAGRAM,HOW_TO_APPLY}.md`가 산출물 위치를 `docs/snapshots/`(구조 개편 前)로 안내 → `40_dev/snapshots/`(v4)로 교정(신규 사용자 오도 제거). 나머지 `docs/` 참조는 정당 확인: guide 19의 `gamblescan:docs/snapshots/...retrospective` = gamblescan 실제 파일 위치(자체 docs), api-contract `docs/openapi.yaml` = 프로젝트 예시. **부수 발견**: v3.2 backward-compat 코드 폴백(methodology.py·dashboard의 40_resources/60_meta/docs 폴백)은 현존 7 repo 전부 v4.0이라 dead지만 코드 backward-compat라 별건 Open Issue 등재(제거는 v3 지원 포기 결정 필요). Open Issue(docs sweep) Closed.
- 2026-07-09: **METH-090 `.claude/skills` 레거시 3종 삭제 (Class A, PR #79 머지)** — ai-planning·ai-relay·vibe-coding(2026-03 작성) 삭제. 3개 다 구모델(스프린트·기획서6종/개발명세8종·Phase1-10·`docs/planning|sprints|development/` dead 경로) 기준이라, 호출 시 v4와 반대로 안내하는 stale 중복. 기능은 이미 정본이 담당: 기획 오케→guide 01+`prompts/plan-routing`, 멀티AI 릴레이→guide 08(+checkpoint=handoff note), 구현 워크플로/4-레이어→guide 19+guide 00. 살릴 고유 콘텐츠 없음. 다운스트림 sync 대상 아님(shared_paths 밖, 로컬만). 잔여 참조는 90_archive/legacy-methodology 히스토리뿐(보존). 세션 관통 SSOT/anti-중복(AI-LOG·last_built·SPRINTS 제거와 동종).
- 2026-07-09: **METH-089 ai-icons·icons-invest guide 번호 충돌 remediation (Class A, PR #78 머지)** — guide 02 §7 예약범위(상류 00-89/커스텀 90-99) 준수: 예약범위 위반 레거시 커스텀 guide를 90+로 이관. **ai-icons**: 04_문서보관→90·05_회의록→91·21_산출물채널분리→92_LOCAL(doc_id guide-04/meeting-notes/21→guide-90/91/92). 21은 상류 05_산출물채널분리(정본)와 149줄 차이=로컬 발전분 → 삭제 않고 92로 보존+정본 플래그. **icons-invest**: 04→90·05_회의록→91. 기능적 참조(00_briefs/meetings/_README·HANDOFF 라이브 포인터) 갱신, 이력 기록(관찰로그·과거 ADR·checkpoint bullet)은 시점 기록 보존. git mv(rename+doc_id), --no-verify commit/push, origin/main 검증(충돌 해소·상류 정본 유지·라이브 참조 옛번호 0·데이터 손실 0). 잔여: ai-icons 92_LOCAL↔상류05 환류(각 repo 세션). friction: 한글경로 검증엔 core.quotepath=false.
- 2026-07-09: **METH-088 다운스트림 sync 홀드 3곳 완료 — 관리 6곳 전부 086 반영 (Class A, PR #77 머지)** — 사용자 dirty 해소 후 ai-icons·cafe24-renewal·icons-invest 를 086까지 sync(clean 검증→(feature면)main 전환→`sync --apply`→stale SPRINTS.md rm→--no-verify commit→push→복귀). origin/main 검증: SPRINTS 제거·WIP 린트·대시보드 정리 반영, **커스텀 guide 전부 보존(데이터 손실 0 — 검증 중 git 한글경로 octal-escape로 오탐 있었으나 UTF-8 재확인으로 보존 확정)**. gamblescan·icons·tshome(METH-087)+이번 3곳 = **관리 다운스트림 6곳 전부 완료**. 잔여: ai-icons(05×2·21×2)·icons-invest(05×2) guide 번호 충돌은 sync와 직교(각 repo 세션에서 커스텀→90+ 이관, Open Issue). ai-icons·icons-invest sibling worktree는 sync 기본 스킵(main만 반영).
