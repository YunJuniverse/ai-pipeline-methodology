# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-048 백서·온보딩에 코드 품질 가드레일 통합 — 지침 19를 방법론 표준 서사로. 백서_가이드 §5/§7 + WHITEPAPER §8-5(헌법, Class C·ADR-003) + HOW_TO_APPLY §5. 브랜치 `claude/meth-048-whitepaper-guide-codequality`(main 기준), **PR 대기**.
- **Current mode**: fullstack
- **Next TODO**: METH-048 PR 머지. (METH-039~047 전부 main 안착·지침 19 다운스트림 전파 완료. 백서/온보딩은 10_foundation이라 미전파=업스트림 전용.)
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

- 2026-06-24: **METH-048 백서·온보딩에 코드 품질 가드레일 통합** — 지침 19(METH-047)를 standalone에서 *방법론 표준 서사*로 통합(사용자 지시). `방법론_백서_가이드.md` §5 "코드 품질 craft(Guardrails by Construction)" + §7 워크플로 day-1 가드레일·lint 게이트 / **`WHITEPAPER.md`(헌법) §8-5 신규 운영 원칙**(AI 안전+코드 품질 횡단) + 부록A + v0.3.0 / `HOW_TO_APPLY.md` §5 Fullstack 게이트. 백서 변경이라 **Class C·ADR-003 신설**(사용자 지시=승인). PR 대기.
- 2026-06-24: **METH-047 클린아키텍처·클린코드 지침 19 신설 (PR #36 머지)** — GambleScan REFACTOR-CLEAN(~50 PR) 회고 역주입. 4 코드 가드레일(레이어경계·no-explicit-any·no-console·max-lines=400)·래칫·4-레이어·god파일 분할·day-1 체크리스트. 지침 17 §4.2의 코드 품질 인스턴스화. Class A.
- 2026-06-24: **METH-046 sync mirror-delete 버그 픽스 (PR #35 머지)** — sync가 상류에 없는 다운스트림 고유 파일(ai-icons `20_guides/04`)을 조용히 삭제하던 데이터손실 차단. prune을 `--prune` opt-in으로(기본 보존+경고). Class A.
- 2026-06-24: **METH-045 방법론 백서 겸 가이드 (PR #34 머지)** — 철학+거버넌스+기획 craft+25 템플릿/6모드+워크플로 공유용 종합본. 레포 `10_foundation/방법론_백서_가이드.md`(11섹션) + Notion In-spire 하위 페이지(app.notion.com/p/3891a2ebe06a812aa1f8cd6b79e2ae20).
- 2026-06-24: **METH-039~044 다운스트림 sync 완료** — icons(`b1c60db`)·gamblescan(`561c0f5`)·ai-icons(`7ef2be7`) 3곳 main에 25종 템플릿+지침 전파(cafe24 제외). icons/gamblescan은 feature 브랜치라 main 전환→sync→복귀. ai-icons는 고유 자산(guide 04·CLAUDE 커스텀) 보존하며 부분 sync → 그 버그를 METH-046으로 픽스.
