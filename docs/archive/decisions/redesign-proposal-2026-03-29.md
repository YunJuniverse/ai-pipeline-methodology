# Methodology Redesign Proposal v2

**Date**: 2026-03-29  
**Status**: accepted working direction

---

## What This Redesign Fixes

이 재설계는 세 가지 실패를 직접 겨냥한다.

1. 문서가 코드보다 커지는 문제
2. 텍스트 게이트가 실제 승인처럼 보이는 문제
3. 스프린트 보고서가 환류보다 의례가 되는 문제

---

## Accepted Decisions

### 1. Active operating docs are minimal

프로젝트 런타임에서 유지되는 핵심 파일은 아래다.

- `CLAUDE.md`
- `AGENTS.md`
- `HANDOFF.md`
- `TODO.md`
- `.github/PULL_REQUEST_TEMPLATE.md`

### 2. Change Class replaces uniform gates

- `Class A`: 기본 구현 변경
- `Class B`: 기술 리스크가 큰 변경
- `Class C`: 비기술 또는 대외 영향이 큰 변경

### 3. Snapshots replace always-on planning docs

기획서 6종과 개발명세서 8종은 상시 유지하지 않는다.
필요할 때만 `docs/snapshots/`에 날짜가 찍힌 문서로 만든다.

### 4. Approval must leave evidence

승인은 아래 둘 중 하나로만 인정한다.

- merged PR
- linked issue/ADR approval evidence

### 5. Legacy materials are archived, not treated as active system

이전 템플릿 세트와 파이프라인 자료는 `docs/archive/` 아래에 남긴다.

---

## Rejected Directions

아래 방향은 이번 버전에서 채택하지 않았다.

- `PROJECT.md` 추가
- 별도 `docs/approvals/` 운영
- 다중 운영 모드(`governed-team`) 공식 지원
- 4-Plane 개념을 사용자 운영 용어로 강제
- 보고서 3종을 축약한 새 보고서 의례

이유는 단순하다. 구조를 설명하려고 또 다른 구조를 만들 가능성이 컸기 때문이다.

---

## Final Architecture

### Runtime

- 부트 컨텍스트: `CLAUDE/AGENTS + HANDOFF`
- 작업 컨텍스트: 필요한 TODO, 코드, 테스트, ADR만 추가
- 상태 동기화: `HANDOFF.md`
- 승인 evidence: PR 또는 issue/ADR 링크

### Documents

- live operating docs: `HANDOFF.md`, `TODO.md`
- stable rules: `CLAUDE.md`, `AGENTS.md`
- rationale: `docs/adr/`
- snapshots: `docs/snapshots/`

---

## Behavior-Based Success Criteria

- 새 프로젝트를 만들면 즉시 작업 가능한 backlog가 생긴다.
- AI는 세션 시작 시 두 파일만 읽고 출발할 수 있다.
- `Class B/C` 변경에는 승인 근거 링크가 남는다.
- `HANDOFF.md`가 짧게 유지된다.
- snapshot 문서는 live source처럼 사용되지 않는다.
- 비즈니스 로직 변경 PR에는 테스트 증거가 포함된다.
