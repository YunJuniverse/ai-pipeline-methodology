# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-046 sync mirror-delete 버그 픽스 — `methodology.py`가 sync 시 다운스트림 고유 파일을 삭제하던 문제. prune을 `--prune` opt-in으로(기본 보존). 브랜치 `claude/meth-046-sync-no-mirror-delete`(main 기준), **PR #35 대기**(충돌 해소 완료).
- **Current mode**: fullstack
- **Next TODO**: **PR #35(METH-046) 머지** → 이번 세션(METH-039~046) 완전 종결. (PR #34 백서 머지됨 → main `7ed86f1`.)
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

- 2026-06-24: **METH-046 sync mirror-delete 버그 픽스 (PR #35)** — sync가 shared 디렉터리를 mirror하며 상류에 없는 다운스트림 고유 파일(ai-icons `20_guides/04`)을 조용히 삭제하던 데이터손실 문제. `copy_path`에 prune_report 추가(후보 보고만, 기본 삭제 안 함) + `cmd_sync` prune을 `--prune` opt-in으로(기본 보존+"보존" 경고; `--prune` 시 삭제 목록) + sync `--prune` 플래그. ai-icons dry-run 검증. init 무영향. Class A.
- 2026-06-24: **METH-045 방법론 백서 겸 가이드 (PR #34 머지)** — 철학+거버넌스+기획 craft+25 템플릿/6모드+워크플로 공유용 종합본. 레포 `10_foundation/방법론_백서_가이드.md`(11섹션) + Notion In-spire 하위 페이지(app.notion.com/p/3891a2ebe06a812aa1f8cd6b79e2ae20).
- 2026-06-24: **METH-039~044 다운스트림 sync 완료** — icons(`b1c60db`)·gamblescan(`561c0f5`)·ai-icons(`7ef2be7`) 3곳 main에 25종 템플릿+지침 전파(cafe24 제외). icons/gamblescan은 feature 브랜치라 main 전환→sync→복귀. ai-icons는 고유 자산(guide 04·CLAUDE 커스텀) 보존하며 부분 sync → 그 버그를 METH-046으로 픽스.
- 2026-06-24: **METH-044 모드별 템플릿 선택 체계 (PR #33 머지)** — `_CATALOG.md`(25종 + 6모드 매트릭스) + CLAUDE/AGENTS Mode 확장 + 지침 00 §11.8. flat 경로 유지.
- 2026-06-24: **PR #31 부분머지 복구 — METH-041/042를 PR #32로 재통합·머지** — PR #31이 METH-040까지만 머지되고 041/042가 main 누락된 것을 #32 충돌 해소 중 발견·복구. PR #32 머지로 040~043 전부 안착(25종 템플릿 전수).
