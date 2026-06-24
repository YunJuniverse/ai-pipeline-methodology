# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

### METH-047
- **title**: 클린아키텍처·클린코드 개발 규칙 — 지침 19 신설 (GambleScan REFACTOR-CLEAN 역주입)
- **notes**: 작업 완료, **PR 대기**(브랜치 `claude/meth-047-clean-architecture-guide`, main 기준). Class A. 적용 프로젝트 GambleScan이 Robert C. Martin Clean Code/Architecture를 실용 적용한 REFACTOR-CLEAN(R0~R4, ~50 PR)의 회고+신설 가이드를 방법론으로 역환류. 핵심 통찰: 백서/지침 17 §4.2 **Guardrails-by-Construction**(원래 AI 안전용)이 *코드 품질*에도 유효 — "첫날부터 4 가드레일이 error였다면 부채가 안 쌓인다". ① `20_guides/19_클린아키텍처_클린코드_개발규칙.md` 신설(일반 craft만·도메인 특화 제외·출처 명시): 4-레이어 의존성 규칙·**4 코드 가드레일(레이어경계·no-explicit-any·no-console·max-lines=400)**·래칫 원리(warn→0→error)·god파일 분할 패턴·day-1 체크리스트·`any`는 버그은폐 교훈. ② README 카탈로그/현황/변경이력(v4) 등재. ③ CLAUDE.md·AGENTS.md §7에 guide 19 포인터. fullstack/dev 트랙용(planning-only 비적용). 머지 후 다운스트림 sync → 전 프로젝트가 day-1부터 적용.

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-045
- **notes**: Completed 2026-06-24. **PR #34 머지 완료**(main `7ed86f1`). Class A. 방법론 백서 겸 가이드 — 레포 `10_foundation/방법론_백서_가이드.md`(11섹션) + Notion In-spire 하위 페이지 업로드. 기존 WHITEPAPER.md(메타 헌법)와 상보, 콘텐츠(craft·템플릿·모드)까지 포함한 현행 종합본.

### METH-044
- **notes**: Completed 2026-06-24. **PR #33 머지 완료**(main `6d3d4e8`). Class A. 모드별 템플릿 선택 체계 — `_CATALOG.md`(25종 + 6모드 매트릭스) + CLAUDE/AGENTS Mode 확장 + 지침 00 §11.8. **다운스트림 sync 완료**(icons·gamblescan·ai-icons, cafe24 제외).

### METH-046
- **notes**: Completed 2026-06-24. **PR #35 머지 완료**(main `626b48a`). Class A. sync mirror-delete 버그 픽스 — `copy_path` prune_report 추가 + `cmd_sync` prune을 `--prune` opt-in으로(기본 보존+경고). 다운스트림 고유 파일(ai-icons guide 04)이 조용히 삭제되던 데이터손실 차단.

<!-- Archived: METH-001~044 (2026-05~06). 상세는 git log --grep="METH-" 및 PR #5~#35, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~3건만. -->
