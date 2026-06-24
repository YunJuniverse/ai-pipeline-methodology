# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

### METH-045
- **title**: 방법론 백서 겸 가이드 문서 — 레포 md + Notion(In-spire) 업로드
- **notes**: 작업 완료, **PR 대기**(브랜치 `claude/meth-045-whitepaper-guide`, main 기준). Class A. 사용자 요청. 기존 `WHITEPAPER.md`(메타-시스템 헌법)는 이번 세션 추가분(기획 craft·25 템플릿·6모드)이 빠져 있어, 철학+거버넌스+기획 craft+템플릿/모드+워크플로를 아우르는 **공유용 백서 겸 가이드** 신설. ① 레포: `10_foundation/방법론_백서_가이드.md`(11개 섹션). ② Notion: **In-spire 페이지 아래 하위 페이지 생성** (https://app.notion.com/p/3891a2ebe06a812aa1f8cd6b79e2ae20). 레포 상대링크는 Notion용으로 inline code 처리. 머지 후 다운스트림 sync 대상(50_resources 아님·10_foundation은 shared 아니라 미전파 — 백서는 업스트림 전용).

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-044
- **notes**: Completed 2026-06-24. **PR #33 머지 완료**(main `6d3d4e8`). Class A. 모드별 템플릿 선택 체계 — `_CATALOG.md`(25종 카테고리 카탈로그 + 6모드 planning/dev/fullstack/agency/lean/ops × 템플릿 매트릭스) + CLAUDE.md·AGENTS.md Mode 확장 + 지침 00 §11.8. 폴더 재구성 없이 flat 경로 유지. **다운스트림 sync 완료**(2026-06-24): icons·gamblescan·ai-icons 3곳 main에 METH-039~044 전파(cafe24 제외). ai-icons는 고유 자산(guide 04·CLAUDE 커스텀) 보존하며 부분 sync.

### METH-043
- **notes**: Completed 2026-06-24. **PR #32 머지 완료**(main `ca6fc57`). Class A. icons-ip(방법론 미적용 lean) PRD 작성 craft 중 순수 doc craft 7종 채택. 신규 템플릿 3종(`prd`·`architecture`·`context-glossary`) + `ADR-template` 강화 + `requirements-spec`(M/S+Pn) + 지침 00 §11.5~11.7.

### METH-042
- **notes**: Completed 2026-06-24. **PR #32 머지 완료**(원래 PR #31 묶음이었으나 #31이 040까지만 머지돼 #32로 재통합). Class A. ICONS 학습 *원본*(다운로드 510종) 직접 정독 → 정제본이 흘린 craft 회수. **신규 템플릿 12종**(제안·검수·운영·수익관리) + 지침 10/11/13/15 §19 대량 보강 + 16 §15 신설.

<!-- Archived: METH-001~041 (2026-05~06). 특히 METH-039(PR #30)·040(PR #31 부분머지·#32 보완)·041(PR #32)는 머지 완료. 상세는 git log --grep="METH-" 및 PR #5~#33, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~3건만. -->
