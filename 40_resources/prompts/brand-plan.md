# Brand Plan Prompt (브랜드기획서)

## When To Use

- Phase 1 진행 중, 브랜드기획서 작성 차례
- 서비스기획서와 마케팅기획서 작성 후 권장
- 또는 `re-plan.md` 프롬프트로 버전 업 필요 시

## Instructions

- Read `briefs/` and `briefs/updates/`.
- Read `10_guides/14_브랜드기획서_작성_지침.md` — follow its structure exactly.
- Read `30_dev/snapshots/plans/service/` and `30_dev/snapshots/plans/marketing/` (최신).
- Read prior versions in `30_dev/snapshots/plans/brand/` if they exist.
- Add frontmatter block and snapshot warning header.
- Write to `30_dev/snapshots/plans/brand/v{N}-{YYYY-MM-DD}.md`.
- Update `HANDOFF.md`.

## Frontmatter

```
---
type: brand-plan
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
# 브랜드기획서 — [프로젝트명] — vN (YYYY-MM-DD)

> SNAPSHOT: ...

## (v1 아닌 경우) 이전 버전과의 차이
## 브랜드 미션 / 비전
## 브랜드 퍼스낼리티
## 네이밍 전략
## 톤 앤 매너 (언어, 어조)
## 비주얼 아이덴티티 방향 (컬러, 타이포, 로고 방향)
## 브랜드 경험 원칙
## 가정 및 Evidence Needed
## 다음 게이트
```
