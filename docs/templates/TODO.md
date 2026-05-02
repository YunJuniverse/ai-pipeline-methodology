# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

### [ID]-010
- **title**: [짧은 제목]
- **mode**: fullstack / planning-only
- **change-class**: A / B / C
- **owner**: Human / AI / Human + AI
- **acceptance criteria**:
  - [ ] [criterion 1]
- **notes**: 아직 Ready로 끌어올리기 전의 아이디어

## Ready

### [ID]-001
- **title**: [짧은 제목]
- **mode**: fullstack / planning-only
- **change-class**: A / B / C
- **owner**: Human / AI / Human + AI
- **sprint**: S-001
- **acceptance criteria**:
  - [ ] [criterion 1]
  - [ ] [criterion 2]
- **notes**: [optional short context]

## InProgress

### [ID]-003
- **title**: [짧은 제목]
- **mode**: fullstack
- **change-class**: B
- **owner**: AI
- **sprint**: S-001
- **acceptance criteria**:
  - [x] [done criterion]
  - [ ] [pending criterion]
- **notes**: 현재 작업 중

## Blocked

### [ID]-002
- **title**: [짧은 제목]
- **mode**: planning-only
- **change-class**: C
- **owner**: Human
- **acceptance criteria**:
  - [ ] [criterion 1]
- **notes**: Blocked by [reason].

## Done

### [ID]-000
- **title**: [짧은 제목]
- **notes**: Completed [YYYY-MM-DD]. See [PR / snapshot link].
