# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-047 클린아키텍처·클린코드 개발 규칙 — 지침 19 신설(GambleScan REFACTOR-CLEAN 회고 역주입). 4 코드 가드레일·래칫·4-레이어·god파일 분할. 브랜치 `claude/meth-047-clean-architecture-guide`(main 기준), **PR 대기**.
- **Current mode**: fullstack
- **Next TODO**: METH-047 PR 머지 → 머지 후 다운스트림 sync(지침 19 전파, 전 프로젝트 day-1 가드레일). (METH-039~046 전부 main 안착 완료.)
- **Blockers**: none

## Active Links

- Current PR: #35 (METH-046 sync 픽스)
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

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-06-24: **METH-047 클린아키텍처·클린코드 개발 규칙 (지침 19 신설)** — 적용 프로젝트 GambleScan의 Clean Code/Architecture 리팩토링(REFACTOR-CLEAN, R0~R4 ~50 PR) 회고를 방법론으로 역주입. 핵심: 백서/지침 17 §4.2 Guardrails-by-Construction이 *코드 품질*에도 유효 → 첫날부터 4 코드 가드레일(레이어경계·no-explicit-any·no-console·max-lines=400)을 린트로 fail-closed 강제(래칫 warn→0→error). 4-레이어 의존성 규칙·god파일 분할 패턴·day-1 체크리스트. README 카탈로그/v4 + CLAUDE/AGENTS §7 포인터. fullstack/dev 트랙. Class A. PR 대기.
- 2026-06-24: **METH-046 sync mirror-delete 버그 픽스 (PR #35 머지)** — sync가 상류에 없는 다운스트림 고유 파일(ai-icons `20_guides/04`)을 조용히 삭제하던 데이터손실 차단. prune을 `--prune` opt-in으로(기본 보존+경고). Class A.
- 2026-06-24: **METH-045 방법론 백서 겸 가이드 (PR #34 머지)** — 철학+거버넌스+기획 craft+25 템플릿/6모드+워크플로 공유용 종합본. 레포 `10_foundation/방법론_백서_가이드.md`(11섹션) + Notion In-spire 하위 페이지(app.notion.com/p/3891a2ebe06a812aa1f8cd6b79e2ae20).
- 2026-06-24: **METH-039~044 다운스트림 sync 완료** — icons(`b1c60db`)·gamblescan(`561c0f5`)·ai-icons(`7ef2be7`) 3곳 main에 25종 템플릿+지침 전파(cafe24 제외). icons/gamblescan은 feature 브랜치라 main 전환→sync→복귀. ai-icons는 고유 자산(guide 04·CLAUDE 커스텀) 보존하며 부분 sync → 그 버그를 METH-046으로 픽스.
- 2026-06-24: **METH-044 모드별 템플릿 선택 체계 (PR #33 머지)** — `_CATALOG.md`(25종 + 6모드 매트릭스) + CLAUDE/AGENTS Mode 확장 + 지침 00 §11.8. flat 경로 유지.
