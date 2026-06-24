# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-044 모드별 템플릿 선택 체계 — `_CATALOG.md`(25종 카탈로그 + 6모드 매트릭스) + CLAUDE.md/AGENTS.md Mode 확장 + 지침 00 §11.8. 브랜치 `claude/meth-044-template-mode-catalog`(main `ca6fc57` 기준), **PR 대기**. (PR #32 머지로 040~043 전부 main 안착 완료.)
- **Current mode**: fullstack
- **Next TODO**: ① **METH-044 PR 머지** → ② **다운스트림 sync**(METH-039~044 합산: icons·ai-icons·gamblescan `sync --apply`, cafe24 경로 미확인). 이번 세션 역주입 작업 일단락.
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

- 2026-06-24: **METH-044 모드별 템플릿 선택 체계** — 템플릿 25종+ → 작업 모드별 선택 체계 신설. `_CATALOG.md`(25종 카테고리 카탈로그 + 6모드(planning/dev/fullstack/agency/lean/ops) × 템플릿 매트릭스 + 모드별 권장 세트) + CLAUDE.md·AGENTS.md Mode 확장 + 지침 00 §11.8. 폴더 재구성 없이 flat 경로 유지(기존 참조 보존). Class A. PR 대기.
- 2026-06-24: **PR #31 부분머지 복구 — METH-041/042를 PR #32로 재통합·머지** — PR #31이 METH-040(`450045a`)까지만 머지되고 041(`b3a48f7`)·042(`18d3784`)가 main 누락된 것을 #32 충돌 해소 중 발견. gamblescan 브랜치(살아있던 18d3784)를 PR #32에 병합 → #32가 041+042+043 운반. **PR #32 머지(main `ca6fc57`)로 040~043 전부 안착·검증 완료**(25종 템플릿 전수).
- 2026-06-23: **METH-043 icons-ip 경량 문서 craft 역주입 (PR #32)** — icons-ip(lean 코드베이스) PRD craft 중 순수 doc craft 7종 채택. 신규 템플릿 3종(`prd`·`architecture`·`context-glossary`) + `ADR-template` 강화(결정문장·Considered Options·되돌리기 비용) + `requirements-spec`(M/S+Pn) + 지침 00 §11.5~11.7. GitHub-Issues 트래커는 제외(file-based 설계 충돌).
- 2026-06-24: **METH-042 원본 기획 학습 코퍼스 직접 정독 (PR #32 머지)** — ICONS 학습 *원본*(다운로드 510종) 직접 정독 → 정제본이 흘린 craft 회수. **신규 템플릿 12종**(제안·검수·운영·수익관리) + 지침 10/11/13/15 §19 대량 보강 + 16 §15 신설.
- 2026-06-24: **METH-041 ICONS §19 압축 누락 보충 (PR #32 머지)** — METH-039 압축 시 "이름만 남고 본문 증발"한 체크리스트 6건 복원(지침 10/11/15).
