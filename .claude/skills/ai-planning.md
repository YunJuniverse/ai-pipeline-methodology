---
name: ai-planning
description: 하네스 기반 애자일 기획 오케스트레이션. 리서치, 기획서 8종, 개발명세, 승인 문서, 스프린트 환류까지 연결한다.
---

# AI Planning Orchestration

## 목적

이 스킬은 기획 요청을 단발성 문서 작성으로 끝내지 않고,
리서치 → 기획 문서 세트 → 개발명세 → 스프린트 환류 체계로 연결한다.

핵심은 아래 3가지다:

1. 문서 간 추적성 유지
2. 버전 관리
3. 인간 승인 체계 반영

---

## 실행 절차

### 1단계: 현재 상태 확인

먼저 아래를 확인한다.

- `CLAUDE.md` 또는 `AGENTS.md`의 현재 버전, 현재 스프린트, 현재 페이즈
- 이미 존재하는 문서
- 현재 요청이 신규 작성인지, 업데이트인지, 환류 반영인지

### 2단계: 요청 분류

| 요청 유형 | 기본 산출물 |
|-----------|-------------|
| 시장, 레퍼런스, 문제 검증, 위험 탐색 | `docs/research/*.md` |
| 서비스 방향, 요구사항, 사용자 행동, 구조 설계 | `docs/planning/*.md` |
| 구현 범위, 테스트 전략, 기술 반영 | `docs/development/development-spec.md` |
| 스프린트 회고, QA, 괴리 분석, 개선점 | `docs/sprints/*.md` |
| 승인, 추적, readiness, 보고 | `docs/governance/*.md` |

### 3단계: 문서 우선순위 판단

기획 요청이 오면 아래 순서로 판단한다.

1. 이 요청의 직접 산출물은 무엇인가
2. 이 문서를 쓰기 전에 필요한 upstream 문서는 무엇인가
3. 이 문서가 downstream 어떤 문서에 영향을 주는가
4. 인간 승인 또는 버전 증가가 필요한가

### 4단계: 깊이 판단

- 명시 없으면 `초안`
- "구조만", "목차만" → 개요 또는 목차
- "실무용", "대표 보고용", "승인용" → 완성본 수준

---

## 기획 문서 세트 규칙

기획은 하나의 거대 문서보다 아래 세트를 우선한다.

1. `service-overview`
2. `requirements`
3. `user-stories`
4. `information-architecture`
5. `user-flow`
6. `wireframes`
7. `functional-spec`
8. `data-model`
9. `operations-policy` [권장]

### 문서 선택 가이드

| 요청 키워드 | 기본 문서 |
|------------|-----------|
| 서비스 개요, 가치제안, 문제정의 | `service-overview` |
| 요구사항, 우선순위, 제약 | `requirements` |
| 사용자 행동, acceptance 기준 | `user-stories` |
| 메뉴 구조, 정보 구조, 네비게이션 | `information-architecture` |
| 단계 흐름, 예외 흐름 | `user-flow` |
| 화면 구조, 상태 설계 | `wireframes` |
| 기능 정의, 정책, 예외 처리 | `functional-spec` |
| 엔티티, 관계, 필드 | `data-model` |
| 운영 규칙, CS, 검수, 관리자 | `operations-policy` |

---

## 리서치 문서 규칙

리서치는 배경 설명이 아니라 판단 근거다.

반드시 아래를 포함한다.

- 질문
- 출처
- 핵심 발견
- 제품/기획 영향
- 열린 질문
- 권고안

리서치 결과가 기획에 영향을 주면,
어느 planning 문서가 업데이트되어야 하는지도 함께 적는다.

---

## 개발명세 연결 규칙

기획 문서를 작성하거나 수정한 뒤,
구현에 영향이 있으면 아래를 판단한다.

- `development-spec` 업데이트 필요 여부
- `requirements-traceability-matrix` 업데이트 필요 여부
- `definition-of-ready-done` 재점검 필요 여부

기획 변경이 스프린트 범위를 바꾸면 approval log 후보로 본다.

---

## 스프린트 환류 연결 규칙

스프린트 완료나 QA 결과가 들어오면,
아래 흐름으로 처리한다.

1. `sprint-completion-report`
2. `sprint-feedback-report`
3. planning docs version bump
4. development spec version bump

환류 없는 기획은 정적인 문서가 되므로 지양한다.

---

## 품질 체크리스트

- [ ] 문서 목적이 첫 부분에 드러나는가
- [ ] 독자와 승인자가 명시되는가
- [ ] 다른 문서와 경계가 분명한가
- [ ] 추상어 대신 판단 기준이 있는가
- [ ] 버전과 변경 이유가 기록되는가
- [ ] downstream 영향이 보이는가
- [ ] 필요한 인간 승인 지점이 보이는가

---

## 원본 지침 사용

완성본 수준이 필요하면 기존 원본 지침을 참조한다.

- `docs/planning-guides/00_AI_기획_프로젝트_운영_원칙.md`
- `docs/planning-guides/10_사업기획서_작성_지침.md`
- `docs/planning-guides/11_서비스기획서_작성_지침.md`
- `docs/planning-guides/12_운영기획서_작성_지침.md`
- `docs/planning-guides/13_마케팅기획서_작성_지침.md`
- `docs/planning-guides/14_브랜드기획서_작성_지침.md`
- `docs/planning-guides/15_프로젝트_관리_기획서_작성_지침.md`
