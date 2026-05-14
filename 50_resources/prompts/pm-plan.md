# PM Plan Prompt (프로젝트 관리 기획서)

## When To Use

- Phase 1 마지막, 나머지 5종 작성 후 권장
- 일정·리스크·리소스 전반을 종합하므로 가장 마지막에 작성
- 또는 `re-plan.md` 프롬프트로 버전 업 필요 시

## Instructions

- Read `briefs/` and `briefs/updates/`.
- Read `20_guides/15_프로젝트_관리_기획서_작성_지침.md` — follow its structure exactly.
- Read all other plan snapshots (business, service, ops, marketing, brand) — 최신 버전.
- Read prior versions in `40_dev/snapshots/plans/pm/` if they exist.
- Add frontmatter block and snapshot warning header.
- Write to `40_dev/snapshots/plans/pm/v{N}-{YYYY-MM-DD}.md`.
- Update `HANDOFF.md`: note all 6 plans complete, ready for Phase 1 review gate.

## Frontmatter

```
---
type: pm-plan
version: N
date: YYYY-MM-DD
supersedes: null
trigger: initial
adr: null
status: draft
---
```

## Output Structure (지침서 준수)

```
# 프로젝트 관리 기획서 — [프로젝트명] — vN (YYYY-MM-DD)

> SNAPSHOT: ...

## (v1 아닌 경우) 이전 버전과의 차이
## 프로젝트 목표 및 범위
## 이해관계자
## 일정 계획 (Milestone)
## 리소스 계획
## 리스크 관리
## 커뮤니케이션 계획
## 품질 기준
## 변경 관리 프로세스
## 가정 및 Evidence Needed
## 다음 게이트
```

## 작성 완료 후 할 일

PM 기획서까지 완료되면 HANDOFF.md를 아래와 같이 갱신:

```markdown
- Working on: Phase 1 완료 — 6종 기획서 검토 대기
- Next TODO: 사람이 6종 기획서를 검토하고 Phase 2 승인 필요
```
