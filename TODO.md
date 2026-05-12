# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

### METH-015
- **title**: 적용 프로젝트 3개에 applied-ci 워크플로 자동 주입 검증
- **mode**: fullstack
- **change-class**: A
- **owner**: AI
- **acceptance criteria**:
  - [ ] icons/gamblescan/talmocom에 `sync --apply` 호출 — `.github/workflows/methodology-applied-ci.yml` 신규 생성 확인
  - [ ] GitHub에서 첫 push 시 워크플로 실행 결과 확인 (60_meta 미주입, manifest-check, observation lint 통과)
  - [ ] 실패 시 워크플로 또는 검증 로직 조정

### METH-018
- **title**: 사용자 환경에 hooks 설치 + ship 첫 일상 사용 검증
- **mode**: fullstack
- **change-class**: A
- **owner**: Human + AI
- **acceptance criteria**:
  - [ ] 사용자가 본 저장소·icons·gamblescan·talmocom 각각에서 `methodology hooks install` 1회 실행
  - [ ] 다음 작업 종료 시 `methodology ship -m "..."` 사용 — git add/commit/push 직접 호출 없이 통과
  - [ ] sensitive 파일 차단·테스트 실패 차단 동작 1회씩 우연히 시연되면 학습 신호 누적
- **notes**: hooks는 worktree마다 별도 설치 필요 (git의 hooks는 추적되지 않음). 적용 프로젝트는 다음 sync로 ship CLI를 받지만 hooks는 *그 다음 단계*에서 사용자가 1회 실행.

### METH-016
- **title**: SessionEnd hook 활성화 — Claude Code 환경에서 wrap 자동 호출
- **mode**: fullstack
- **change-class**: A
- **owner**: Human (settings.json 사용자 결정 영역)
- **acceptance criteria**:
  - [ ] 사용자 `.claude/settings.json` 또는 `.claude/settings.local.json`에 `SessionEnd` hook 등록
  - [ ] 다음 세션 종료 시 wrap 자동 호출 확인
- **notes**: 가이드 위치 `.ai/adapters/claude.md`. 본 항목은 *사용자 설정 변경*이라 AI가 직접 적용하지 않음.

### METH-013
- **title**: 메타-방법론 격리(`60_meta/`)의 ADR 후속화 — RFC-001 → ADR-002
- **mode**: planning-only
- **change-class**: B (구조 결정)
- **owner**: Human + AI
- **notes**: RFC-001은 status 개선용으로 *재사용됨* (2026-05-12 accepted). 격리 결정의 별도 RFC/ADR은 추후 *변경 발생 시점*에 작성. 본 TODO는 *대기*.

### METH-014
- **title**: 메타-카탈로그 첫 시드 — MP-001/MP-002 완료
- **mode**: planning-only
- **change-class**: A
- **owner**: AI
- **notes**: 2026-05-12 MP-001(status 버전 문자열만 비교) + MP-002(sync init_files 누락) 시드 완료. N≥2 목격 시 active(MC) 승급. 본 TODO는 *지속 모니터링* 상태로 남음.

## InProgress

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `30_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-012
- **title**: 인계 시뮬레이션과 온보딩 검증
- **notes**: Completed 2026-05-08. Added `30_dev/snapshots/transfer-drill-2026-05-08.md` and verified portable state inputs for current v0 scope.

### METH-011
- **title**: Dashboard L0~L4 패널 통합
- **notes**: Completed 2026-05-08. Dashboard data now includes L0 adapters, observations, Catalog counts, Skeleton counts, and Thinktank reports.

### METH-010
- **title**: Thinktank v0 마이닝 리포트 구현
- **notes**: Completed 2026-05-08. Added `methodology thinktank` and generated `30_dev/snapshots/insights/2026-W19_thinktank.md`.

<!-- Archived: METH-001 ~ METH-009 (2026-05-07 ~ 2026-05-08). See git history. -->

