# Ops Plan Prompt (운영기획서)

## When To Use

- Phase 1 진행 중, 운영기획서 작성 차례
- 서비스기획서 작성 후 권장
- 또는 `re-plan.md` 프롬프트로 버전 업 필요 시

## Instructions

- Read `briefs/` and `briefs/updates/`.
- Read `docs/guides/planning/12_운영기획서_작성_지침.md` — follow its structure exactly.
- Read `docs/snapshots/plans/service/` (최신) — 서비스 흐름과 정합성 유지.
- Read prior versions in `docs/snapshots/plans/ops/` if they exist.
- Add frontmatter block and snapshot warning header.
- Write to `docs/snapshots/plans/ops/v{N}-{YYYY-MM-DD}.md`.
- Update `HANDOFF.md`.

## Frontmatter

```
---
type: ops-plan
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
# 운영기획서 — [프로젝트명] — vN (YYYY-MM-DD)

> SNAPSHOT: ...

## (v1 아닌 경우) 이전 버전과의 차이
## 운영 목표
## 운영 조직 및 역할
## 고객 지원 정책 (CS 플로우, SLA)
## 데이터 운영 정책 (개인정보, 보존, 삭제)
## 장애 대응 프로세스
## 모니터링 지표
## 운영 비용 구조
## 가정 및 Evidence Needed
## 다음 게이트
```
