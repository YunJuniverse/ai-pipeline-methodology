# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

### METH-013
- **title**: 메타-방법론 격리(`60_meta/`)의 ADR 후속화 — RFC-001 → ADR-002
- **mode**: planning-only
- **change-class**: B (구조 결정)
- **owner**: Human + AI
- **acceptance criteria**:
  - [ ] `60_meta/rfc/RFC-001_meta-folder-introduction.md` 작성 (Context/Proposal/Alternatives/Risks/Rollout 5섹션)
  - [ ] `30_dev/adr/ADR-002_meta-folder-isolation.md` 작성 (RFC-001 머지 후)
  - [ ] 백서 §13 / §부록 C·A 정합성 확인
- **notes**: 본 격리는 2026-05-12에 *코드·구조 차원에서 적용 완료*. 결정 기록만 후속.

### METH-014
- **title**: 메타-카탈로그 첫 시드 (MC-001~003 후보 탐색)
- **mode**: planning-only
- **change-class**: A
- **owner**: AI
- **acceptance criteria**:
  - [ ] 본 저장소 운영 이력에서 N≥2 목격된 메타 마찰 3건 식별
  - [ ] 각 후보를 `60_meta/catalog/_pending/MP-NNN_*.md`로 시드 (또는 N≥2이면 직접 `MC-NNN_*.md`)
  - [ ] 분류 실수 (도메인↔메타) 점검 통과

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

