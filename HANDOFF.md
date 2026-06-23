# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-043(icons-ip 경량 문서 craft) + **PR #31 누락분 METH-041/042 재통합**. ⚠️ PR #31은 METH-040까지만 머지됨 → 041/042를 gamblescan 브랜치에서 **PR #32로 병합**. 이제 PR #32 = 041+042+043. 브랜치 `claude/inject-lean-doc-craft-from-icons-ip`, **PR #32 대기**.
- **Current mode**: fullstack
- **Next TODO**: ① **PR #32 머지**(→ 040~043 전부 main 안착) → ② **다운스트림 sync**(METH-039~043 합산: icons·ai-icons·gamblescan `sync --apply`, cafe24 경로 미확인) → ③ **METH-044**(모드별 템플릿 카탈로그 capstone — TODO Backlog에 설계 확정).
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
| - | PR #31이 METH-040까지만 머지(041/042 누락) | Med | PR #32로 041/042 재통합 완료 → PR #32 머지 시 해소 |
| - | Some legacy/archive docs may still mention pre-`40_dev` or pre-`60_tools` paths | Low | Sweep only if those docs become live references again |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-06-23: **PR #31 부분머지 복구 — METH-041/042를 PR #32로 재통합** — PR #31이 METH-040(commit `450045a`)까지만 머지되고 METH-041(`b3a48f7`)·042(`18d3784`)가 main에 누락된 것을 PR #32 충돌 해소 중 발견. gamblescan 브랜치(살아있던 18d3784)를 PR #32 브랜치에 병합 → PR #32가 041+042+043 전부 운반. 라이브 파일은 정확한 현실(039·040 머지 / 041~043 PR #32 대기)로 해소.
- 2026-06-23: **METH-043 icons-ip 경량 문서 craft 역주입 (PR #32)** — icons-ip(lean 코드베이스) PRD craft 중 순수 doc craft 7종 채택. 신규 템플릿 3종(`prd`·`architecture`·`context-glossary`) + `ADR-template` 강화(결정문장·Considered Options·되돌리기 비용) + `requirements-spec`(M/S+Pn) + 지침 00 §11.5~11.7. GitHub-Issues 트래커는 제외(file-based 설계 충돌).
- 2026-06-23: **METH-042 원본 기획 학습 코퍼스 직접 정독 (PR #32 대기)** — ICONS 학습 *원본*(다운로드 510종) 직접 정독 → 정제본이 흘린 craft 회수. **신규 템플릿 12종**(제안·검수·운영·수익관리) + 지침 10/11/13/15 §19 대량 보강 + 16 §15 신설.
- 2026-06-23: **METH-041 ICONS §19 압축 누락 보충 (PR #32 대기)** — METH-039 압축 시 "이름만 남고 본문 증발"한 체크리스트 6건 복원(지침 10/11/15).
- 2026-06-23: **METH-040 GambleScan 기획 craft 역주입 — PR #31 머지 완료** — 실전 풀 기획 코퍼스 6 영역 병렬 학습. **§19 없던 지침 12·14 §19 신설 + 18 §18 신설** + 10/11/13/15 §19 보강 + 개발명세 템플릿 4종. (같은 PR #31의 041/042는 미머지 → PR #32 운반.)
