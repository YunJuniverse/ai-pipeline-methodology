# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-045 방법론 백서 겸 가이드 — 레포 `10_foundation/방법론_백서_가이드.md` + Notion(In-spire 하위 페이지) 업로드. 브랜치 `claude/meth-045-whitepaper-guide`(main 기준), **PR 대기**.
- **Current mode**: fullstack
- **Next TODO**: METH-045 PR 머지. (METH-039~044 전부 main 안착 + 다운스트림 sync 완료. 이번 세션 역주입 작업 일단락.) 후속: sync mirror-delete 수정(chip `task_b0c3337e`), `methodology templates --mode` CLI(선택).
- **Blockers**: none

## Active Links

- Current PR: #32 (METH-041/042/043 통합)
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
| - | ~~PR #31이 METH-040까지만 머지(041/042 누락)~~ | — | **Closed** — PR #32로 041/042 재통합·머지(main `ca6fc57`). 041~043 전부 안착 검증 |
| - | Some legacy/archive docs may still mention pre-`40_dev` or pre-`60_tools` paths | Low | Sweep only if those docs become live references again |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-06-24: **METH-045 방법론 백서 겸 가이드** — 철학+거버넌스+기획 craft+25 템플릿/6모드+워크플로를 아우르는 공유용 백서 겸 가이드 신설. 레포 `10_foundation/방법론_백서_가이드.md`(11섹션) + **Notion In-spire 하위 페이지 업로드**(app.notion.com/p/3891a2ebe06a812aa1f8cd6b79e2ae20). 기존 WHITEPAPER.md(메타 시스템 헌법)와 상보 — 이건 콘텐츠(craft·템플릿·모드)까지 포함한 현행 종합본. Class A. PR 대기.
- 2026-06-24: **METH-039~044 다운스트림 sync 완료** — icons(`b1c60db`)·gamblescan(`561c0f5`)·ai-icons(`7ef2be7`) 3곳 main에 25종 템플릿+지침 전파(cafe24 제외=사용자 지시). icons/gamblescan은 feature 브랜치라 main 전환→sync→복귀. **ai-icons는 sync가 고유 지침 guide 04를 mirror-delete하려 해 복원**(+CLAUDE/AGENTS 커스텀 룰 보존), 새 자산만 반영. sync mirror-delete 버그는 후속 chip(`task_b0c3337e`).
- 2026-06-24: **METH-044 모드별 템플릿 선택 체계 — PR #33 머지** — `_CATALOG.md`(25종 + 6모드 매트릭스) + CLAUDE/AGENTS Mode 확장 + 지침 00 §11.8. flat 경로 유지. Class A.
- 2026-06-24: **PR #31 부분머지 복구 — METH-041/042를 PR #32로 재통합·머지** — PR #31이 METH-040(`450045a`)까지만 머지되고 041(`b3a48f7`)·042(`18d3784`)가 main 누락된 것을 #32 충돌 해소 중 발견. gamblescan 브랜치(살아있던 18d3784)를 PR #32에 병합 → #32가 041+042+043 운반. **PR #32 머지(main `ca6fc57`)로 040~043 전부 안착·검증 완료**(25종 템플릿 전수).
- 2026-06-23: **METH-043 icons-ip 경량 문서 craft 역주입 (PR #32)** — icons-ip(lean 코드베이스) PRD craft 중 순수 doc craft 7종 채택. 신규 템플릿 3종(`prd`·`architecture`·`context-glossary`) + `ADR-template` 강화(결정문장·Considered Options·되돌리기 비용) + `requirements-spec`(M/S+Pn) + 지침 00 §11.5~11.7. GitHub-Issues 트래커는 제외(file-based 설계 충돌).
