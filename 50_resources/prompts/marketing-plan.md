# Marketing Plan Prompt (마케팅기획서)

## When To Use

- Phase 1 진행 중, 마케팅기획서 작성 차례
- 사업기획서와 서비스기획서 작성 후 권장
- 또는 `re-plan.md` 프롬프트로 버전 업 필요 시

## Instructions

- Read `briefs/` and `briefs/updates/`.
- Read `20_guides/13_마케팅기획서_작성_지침.md` — follow its structure exactly.
- Read `40_dev/snapshots/plans/business/` (최신) — 수익 모델, 타겟 고객과 정합성 유지.
- Read prior versions in `40_dev/snapshots/plans/marketing/` if they exist.
- Add frontmatter block and snapshot warning header.
- Write to `40_dev/snapshots/plans/marketing/v{N}-{YYYY-MM-DD}.md`.
- Update `HANDOFF.md`.

## Frontmatter

```
---
type: marketing-plan
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
# 마케팅기획서 — [프로젝트명] — vN (YYYY-MM-DD)

> SNAPSHOT: ...

## (v1 아닌 경우) 이전 버전과의 차이
## 마케팅 목표
## 타겟 세그먼트
## 포지셔닝 전략
## 채널 전략 (획득 채널)
## GTM (Go-To-Market) 플랜
## 콘텐츠 전략
## 예산 개요
## 성과 지표 (CAC, LTV, 전환율 등)
## 가정 및 Evidence Needed
## 다음 게이트
```
