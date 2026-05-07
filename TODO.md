# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

## Blocked

## Done

### METH-001
- **title**: 폴더 구조와 문서 경로를 현재 규칙에 맞게 정리
- **notes**: Completed 2026-05-07. Moved onboarding docs to `40_resources/onboarding/`, moved evaluation docs to `90_archive/evaluation/`, and aligned live docs to `30_dev/*` paths.

### METH-003
- **title**: `40_resources` L1/L2 자산 디렉터리 골격과 스키마 문서 신설
- **notes**: Completed 2026-05-07. Added `40_resources/catalog/`, `40_resources/skeletons/`, and `40_resources/ai_observations/` with `_README.md` schema documents.

### METH-004
- **title**: AI 관찰 로그 작성 규칙 가이드 신설
- **notes**: Completed 2026-05-07. Added `10_guides/03_AI_관찰_로그_작성_규칙.md` as the single-source writing rule for L1 observation logs.

### METH-005
- **title**: 백서를 실행 가능한 헌법으로 정리하고 구현 기획 작성
- **notes**: Completed 2026-05-07. Revised `00_foundation/WHITEPAPER.md` to v0.2.0 and added `30_dev/snapshots/implementation-plan-2026-05-07.md`.

### METH-006
- **title**: L0 이식성 코어 스키마와 체크포인트 템플릿 구현
- **notes**: Completed 2026-05-07. Updated `.ai/context.json`, `.ai/schema/context.schema.json`, `.ai/checkpoint.md`, and adapters; verified JSON parse, path existence, and checkpoint sections.

### METH-007
- **title**: L1 관찰 로그 생성·검증 흐름 구현
- **notes**: Completed 2026-05-07. Added `methodology observe`, generated `40_resources/ai_observations/2026-05-07_l1-observe-flow.md`, and validated required fields/path rules.

### METH-002
- **title**: local tool metadata 정리 (`.claude/worktrees/`, `.codex/`) 정책 확정
- **notes**: Completed 2026-05-07. Added `.claude/worktrees/` and `.codex/` to `.gitignore`; `.ai/` remains tracked as L0 portable state.

### METH-008
- **title**: Pending Lesson과 Catalog 승급 흐름 정리
- **notes**: Completed 2026-05-08. Added `catalog` CLI flow, `_pending/` and `archived/` dirs, `P-001` seed, README rules, and ADR-001.

### METH-009
- **title**: 첫 Skeleton domain build/apply v0 구현
- **notes**: Completed 2026-05-08. Added `skeleton init/build/apply`, created `40_resources/skeletons/meta/`, built lock/README, and verified apply to a temporary target.

### METH-010
- **title**: Thinktank v0 마이닝 리포트 구현
- **notes**: Completed 2026-05-08. Added `methodology thinktank` and generated `30_dev/snapshots/insights/2026-W19_thinktank.md`.

### METH-011
- **title**: Dashboard L0~L4 패널 통합
- **notes**: Completed 2026-05-08. Dashboard data now includes L0 adapters, observations, Catalog counts, Skeleton counts, and Thinktank reports.

### METH-012
- **title**: 인계 시뮬레이션과 온보딩 검증
- **notes**: Completed 2026-05-08. Added `30_dev/snapshots/transfer-drill-2026-05-08.md` and verified portable state inputs for current v0 scope.
