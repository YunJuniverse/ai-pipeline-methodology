# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

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
