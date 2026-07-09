# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-090 **`.claude/skills` 레거시 3종 삭제** — ai-planning·ai-relay·vibe-coding(3/26 작성, 구모델: 스프린트·기획서6종/개발명세8종·`docs/` dead 경로). 기능은 guide 01(오케)/08(서브에이전트)/19(클린코드)+prompts가 정본이라 stale 중복이고, 호출 시 v4와 반대로 안내 → 삭제. 다운스트림 sync 대상 아님(로컬만). 잔여 참조는 90_archive 히스토리뿐(보존). 이번 세션 SSOT/anti-중복 철학과 일치. Class A. PR 대기.
- **Current mode**: fullstack
- **Next TODO**: ① **점검·정합·구조·전파·정비 사이클 완료** — 079~089(…·SPRINTS붕괴·다운스트림 sync 6곳·번호 remediation). 남은 후보: agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs), 메타/dev 지침(02~09·19~20), ai-icons 92_LOCAL↔상류05 환류(각 repo 세션). ② **graph.json 노드 완성**(guide 02~09·19~21 누락, 별건). ③ 학습 루프 후속: friction 축적→thinktank→catalog 승급→skeleton bake. **프로세스: branch-first 준수.**
- **Blockers**: none

## Active Links

- Current PR: METH-090 .claude/skills 삭제 (신규) · METH-089 guide 번호 remediation = #78 머지 완료 · 063~088 = #53~#77 머지 완료
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
| - | Some legacy/archive docs may still mention pre-`40_dev` or pre-`60_tools` paths | Low | Sweep only if those docs become live references again |
| - | ~~ai-icons·icons-invest guide 번호 충돌~~ | — | **Closed(METH-089)** — 커스텀 04/05/21→90/91/92 이관·doc_id·참조 갱신, origin/main 검증. 잔여: ai-icons 92_LOCAL(구 21)은 상류 05 정본과 149줄 차이=로컬 발전분 → 각 repo 세션에서 상류 05로 환류·재조정 검토 |
| - | ~~sync 홀드 3곳(dirty)~~ | — | **Closed(METH-088)** — ai-icons·cafe24·icons-invest dirty 해소 후 086 sync 완료. **관리 다운스트림 6곳 전부 086 반영** |
| - | `methodology-graph.json` 노드 불완전 — guide 02~09·19~21 누락(00·01·10~18만) | Low | 대시보드 시각화 그래프. METH-079에서 발견. 노드/엣지 보강은 별건(대시보드 렌더 영향 확인 후) |
| - | ~~`.claude/skills` 레거시 3종~~ | — | **Closed(METH-090)** — ai-planning·ai-relay·vibe-coding 삭제. 기능은 guide 01/08/19+prompts가 정본. 90_archive 히스토리는 보존 |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-09: **METH-090 `.claude/skills` 레거시 3종 삭제 (Class A, PR 대기)** — ai-planning·ai-relay·vibe-coding(2026-03 작성) 삭제. 3개 다 구모델(스프린트·기획서6종/개발명세8종·Phase1-10·`docs/planning|sprints|development/` dead 경로) 기준이라, 호출 시 v4와 반대로 안내하는 stale 중복. 기능은 이미 정본이 담당: 기획 오케→guide 01+`prompts/plan-routing`, 멀티AI 릴레이→guide 08(+checkpoint=handoff note), 구현 워크플로/4-레이어→guide 19+guide 00. 살릴 고유 콘텐츠 없음. 다운스트림 sync 대상 아님(shared_paths 밖, 로컬만). 잔여 참조는 90_archive/legacy-methodology 히스토리뿐(보존). 세션 관통 SSOT/anti-중복(AI-LOG·last_built·SPRINTS 제거와 동종).
- 2026-07-09: **METH-089 ai-icons·icons-invest guide 번호 충돌 remediation (Class A, PR #78 머지)** — guide 02 §7 예약범위(상류 00-89/커스텀 90-99) 준수: 예약범위 위반 레거시 커스텀 guide를 90+로 이관. **ai-icons**: 04_문서보관→90·05_회의록→91·21_산출물채널분리→92_LOCAL(doc_id guide-04/meeting-notes/21→guide-90/91/92). 21은 상류 05_산출물채널분리(정본)와 149줄 차이=로컬 발전분 → 삭제 않고 92로 보존+정본 플래그. **icons-invest**: 04→90·05_회의록→91. 기능적 참조(00_briefs/meetings/_README·HANDOFF 라이브 포인터) 갱신, 이력 기록(관찰로그·과거 ADR·checkpoint bullet)은 시점 기록 보존. git mv(rename+doc_id), --no-verify commit/push, origin/main 검증(충돌 해소·상류 정본 유지·라이브 참조 옛번호 0·데이터 손실 0). 잔여: ai-icons 92_LOCAL↔상류05 환류(각 repo 세션). friction: 한글경로 검증엔 core.quotepath=false.
- 2026-07-09: **METH-088 다운스트림 sync 홀드 3곳 완료 — 관리 6곳 전부 086 반영 (Class A, PR #77 머지)** — 사용자 dirty 해소 후 ai-icons·cafe24-renewal·icons-invest 를 086까지 sync(clean 검증→(feature면)main 전환→`sync --apply`→stale SPRINTS.md rm→--no-verify commit→push→복귀). origin/main 검증: SPRINTS 제거·WIP 린트·대시보드 정리 반영, **커스텀 guide 전부 보존(데이터 손실 0 — 검증 중 git 한글경로 octal-escape로 오탐 있었으나 UTF-8 재확인으로 보존 확정)**. gamblescan·icons·tshome(METH-087)+이번 3곳 = **관리 다운스트림 6곳 전부 완료**. 잔여: ai-icons(05×2·21×2)·icons-invest(05×2) guide 번호 충돌은 sync와 직교(각 repo 세션에서 커스텀→90+ 이관, Open Issue). ai-icons·icons-invest sibling worktree는 sync 기본 스킵(main만 반영).
- 2026-07-09: **METH-087 누적 다운스트림 sync (073~086) — clean 3곳 반영 (Class A, PR #76 머지)** — clean+관리 다운스트림 **gamblescan·icons·tshome**에 상류 누적분(072→086) 반영. repo당: main 전환→`sync --apply`(shared_paths: 지침·templates·prompts·catalog·skeleton·graph·대시보드·methodology.py·foundation)→**stale SPRINTS.md 수동 rm**(templates + 40_dev; sync는 상류 삭제분 자동 prune 안 함=opt-in)→--no-verify commit→push→원브랜치 복귀. **origin/main 검증 통과**: SPRINTS 제거·WIP 린트·대시보드 sprint 정리 반영, 고유 파일(gamblescan design-token-setup) 보존. 홀드(dirty): ai-icons·cafe24-renewal·icons-invest — clean 후 동일 절차. ver 없는 icons-ip·qmd·talmo·talmocom은 미적용이라 제외.
- 2026-07-09: **METH-086 SPRINTS 완전 붕괴(2층화) + TODO WIP 캡 — 웹리서치 (Class A, PR #75 머지)** — 사용자 지시. 리서치 2건: **TODO=베스트프랙티스 부합**(Backlog.md·에이전트 칸반 독립 재현), **SPRINTS=잉여 중간층+명칭 모순**(기간 고정 안 하는 sprint, velocity baggage가 METH-076 flow 메트릭과 충돌; solo+AI에선 팀 동기화·이해관계자 체크포인트 둘 다 불요/페이즈게이트가 이미 담당). **3층→2층**(페이즈→TODO): cadence=flow 메트릭, 배치 그룹핑=TODO `milestone:` 태그, 게이트=페이즈. 변경 다중: guide 02(§3 스프린트 삭제·재번호·v3), guide 18(§14.5 재작성·§10.2 velocity→throughput·v6), _CATALOG(3곳), TODO 템플릿(sprint→milestone+WIP 주석), **graph.json**(sprints 노드·엣지 제거), **대시보드**(Timeline 탭·gantt·sprint 모달·hero sprint→phase 카드·WIP 타일), mention 스윕(README·WHITEPAPER·HOW_TO_APPLY·40_dev·50_resources/_README·user-story·guide11·12). **SPRINTS.md 2개 삭제**. **wrap InProgress WIP≤3 린트 추가**. 대시보드 렌더+compile 검증 통과. `.claude/skills` 레거시는 Open Issue.
