# Service Plan Prompt (서비스기획서)

## When To Use

- Phase 1 진행 중, 서비스기획서 작성 차례
- 사업기획서가 먼저 작성된 후 작성 권장
- 또는 `re-plan.md` 프롬프트로 버전 업 필요 시

## Instructions

- Read `briefs/` and `briefs/updates/`.
- Read `20_guides/11_서비스기획서_작성_지침.md` — follow its structure exactly.
- Read `40_dev/snapshots/plans/business/` (최신 버전) — 사업기획서와 정합성 유지.
- Read prior versions in `40_dev/snapshots/plans/service/` if they exist.
- Add frontmatter block and snapshot warning header.
- Write to `40_dev/snapshots/plans/service/v{N}-{YYYY-MM-DD}.md`.
- Update `HANDOFF.md`.

## Frontmatter

```
---
type: service-plan
version: N
date: YYYY-MM-DD
supersedes: (이전 버전 파일명, 없으면 null)
trigger: (변경 트리거 또는 initial)
adr: null
status: draft
---
```

## Output Structure (지침서 준수)

```
# 서비스기획서 — [프로젝트명] — vN (YYYY-MM-DD)

> SNAPSHOT: ...

## (v1 아닌 경우) 이전 버전과의 차이
## 서비스 개요
## 사용자 정의 및 페르소나
## 핵심 사용자 시나리오 (User Journey)
## 기능 목록 (Must / Should / Could)
## 화면 목록 및 흐름
## 비기능 요건 (성능, 보안, 접근성)
## 제외 범위 (Out of Scope)
## 가정 및 Evidence Needed
## 다음 게이트
```
