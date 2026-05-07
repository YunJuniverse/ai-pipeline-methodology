# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

### METH-007
- **title**: L1 관찰 로그 생성·검증 흐름 구현
- **mode**: fullstack
- **change-class**: A
- **owner**: Human + AI
- **sprint**: S-001
- **acceptance criteria**:
  - [ ] `methodology observe` 명령의 최소 입출력을 정의한다
  - [ ] `40_resources/ai_observations/`에 규칙 준수 로그 1건을 생성할 수 있다
  - [ ] 관찰 로그 필수 필드와 UTC/상대경로 규칙을 검증한다
- **notes**: See `30_dev/snapshots/implementation-plan-2026-05-07.md` P2.

### METH-002
- **title**: local tool metadata 정리 (`.claude/worktrees/`, `.codex/`) 정책 확정
- **mode**: fullstack
- **change-class**: A
- **owner**: Human + AI
- **sprint**: S-001
- **acceptance criteria**:
  - [ ] 로컬 전용 경로의 버전관리 여부를 결정한다
  - [ ] 필요 시 `.gitignore` 또는 운영 문서에 정책을 반영한다
- **notes**: 현재 `git status`에 untracked로 노출됨

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
