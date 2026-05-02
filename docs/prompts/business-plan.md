# Business Plan Prompt (사업기획서)

## When To Use

- Phase 1 진행 중, 사업기획서 작성 차례
- 또는 `re-plan.md` 프롬프트로 버전 업이 필요할 때

## Instructions

- Read `briefs/` and `briefs/updates/` (if any).
- Read `docs/guides/planning/10_사업기획서_작성_지침.md` — follow its structure exactly.
- Read existing `docs/snapshots/plans/business/` to check prior versions.
- If this is v1: write fresh from briefs.
- If this is v(N+1): include a "v(N)과의 차이" section at the top and state the trigger.
- Add snapshot warning header.
- Write to `docs/snapshots/plans/business/v{N}-{YYYY-MM-DD}.md`.
- Add frontmatter block (see below).
- Update `HANDOFF.md`: note business plan written, link to file.

## Frontmatter

```
---
type: business-plan
version: N
date: YYYY-MM-DD
supersedes: (이전 버전 파일명, 없으면 null)
trigger: (변경 트리거 파일 또는 사유, v1이면 initial)
adr: (관련 ADR 번호, 없으면 null)
status: draft
---
```

## Output Structure (지침서 준수)

```
# 사업기획서 — [프로젝트명] — vN (YYYY-MM-DD)

> SNAPSHOT: ...

## (v1이 아닌 경우) 이전 버전과의 차이
## 사업 목적 및 배경
## 문제 정의
## 목표 시장 및 타겟 고객
## 비즈니스 모델 / 수익 구조
## 경쟁 환경
## 성공 지표 (KPI)
## 리스크
## 가정 및 Evidence Needed
## 다음 게이트
```
