# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

### METH-044
- **title**: 모드별 템플릿 선택 체계 — `_CATALOG.md` + CLAUDE.md/AGENTS.md Mode 확장 + 지침 00 §11.8
- **notes**: 작업 완료, **PR 대기**(브랜치 `claude/meth-044-template-mode-catalog`, main 기준). Class A. 템플릿이 25종+로 늘어 "작업 용도에 따라 필요한 템플릿만" 선택하는 체계 신설(사용자 제안). ① `50_resources/templates/_CATALOG.md` 신설 — 25종 카테고리별 카탈로그 + **6모드(planning/dev/fullstack/agency/lean/ops) × 템플릿 매트릭스** + 모드별 권장 세트. ② CLAUDE.md·AGENTS.md `Mode` 필드 확장(`fullstack/planning-only` → 6모드). ③ 지침 00 §11.8(작업 모드별 템플릿 선택, 카탈로그 정본). **폴더 재구성 안 함**(flat 경로 유지 — 기존 참조 보존). (선택·후속) CLI `methodology templates --mode <mode>`는 별도. 머지 후 다운스트림 sync(METH-039~044 합산).

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-043
- **notes**: Completed 2026-06-24. **PR #32 머지 완료**(main `ca6fc57`). Class A. icons-ip(방법론 미적용 lean) PRD 작성 craft 중 순수 doc craft 7종 채택. 신규 템플릿 3종(`prd`·`architecture`·`context-glossary`) + `ADR-template` 강화(결정문장·Considered Options·되돌리기 비용) + `requirements-spec`(M/S+Pn) + 지침 00 §11.5~11.7. GitHub-Issues 트래커는 제외(file-based 설계 충돌).

### METH-042
- **notes**: Completed 2026-06-24. **PR #32 머지 완료**(원래 PR #31 묶음이었으나 #31이 040까지만 머지돼 #32로 재통합). Class A. ICONS 학습 *원본*(다운로드 510종) 직접 정독 → 정제본이 흘린 craft 회수. **신규 템플릿 12종**(제안·검수·운영·수익관리) + 지침 10/11/13/15 §19 대량 보강 + 16 §15 신설.

### METH-041
- **notes**: Completed 2026-06-24. **PR #32 머지 완료**(원래 PR #31 묶음, #32로 재통합). Class A. METH-039 압축 시 "이름만 남고 본문 증발"한 체크리스트 6건 복원(지침 10/11/15: 협업·커뮤니케이션·Exec Summary 8칸·서비스정의 3종·UIUX 7루브릭·WBS 3계층·제안서 3 Style·품질검토 8항목).

<!-- Archived: METH-001~040 (2026-05~06-23). 특히 METH-039(PR #30)·040(PR #31 부분머지)는 머지 완료. 상세는 git log --grep="METH-" 및 PR #5~#32, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~3건만. -->
