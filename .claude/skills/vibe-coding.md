---
name: vibe-coding
description: 하네스 기반 구현 워크플로우. 개발명세, readability, 테스트, 린터, 스프린트 보고 체계까지 포함한다.
---

# Vibe Coding Implementation Guide

## 전제 조건

구현 전에 아래를 우선 확인한다.

- `docs/development/` 아래 개발명세서 8종이 존재하는가
  (service-overview, requirements, user-stories, information-architecture,
   user-flow, wireframes, functional-spec, data-model)
- 현재 작업이 Definition of Ready를 만족하는가
- 현재 스프린트 목표와 범위가 명확한가
- 기획서 6종(`docs/planning/`)이 승인되어 있는가 (참조용)

개발명세서 없이 바로 구현을 시작하지 않는다.

---

## 구현 루프

각 기능 구현은 아래 루프를 따른다.

```text
1. 개발명세서 8종 확인 (특히 requirements, functional-spec, data-model)
2. requirements traceability 확인
3. 테스트 케이스 먼저 작성
4. 구현
5. lint / typecheck / test 확인
6. human-readable review 관점으로 점검
7. 필요한 ADR 기록
8. sprint artifact에 결과 반영
```

핵심은 "동작하는 코드"가 아니라 "다음 스프린트에도 읽히는 코드"다.

---

## 하네스 우선순위

### 1. 문서 하네스
- 구현 전 관련 문서를 확인한다
- 요구사항을 추측하지 않는다
- 범위 밖 요청은 out-of-scope로 분리한다

### 2. 코드 하네스
- 린터와 구조 규칙으로 출력을 강제한다
- 레이어 경계를 유지한다
- 중복 파일/함수 생성을 피한다

### 3. 평가 하네스
- 테스트, QA, UI, 피어리뷰에서 다시 읽히는 결과를 만든다

### 4. 승인 하네스
- 구조적 변경, 아키텍처 변경, 범위 확장은 인간 승인 후 진행한다

---

## 4-레이어 기본 구조

```text
/src
  /domain
  /application
  /infrastructure
  /interface
  /shared
```

### 레이어 의존성

```text
interface -> application -> domain
                    ^
             infrastructure
```

| 레이어 | 가능한 import | 금지된 import |
|--------|-------------|---------------|
| `domain` | `shared` | 나머지 |
| `application` | `domain`, `shared` | `infrastructure`, `interface` |
| `infrastructure` | `domain`, `application/ports`, `shared` | `interface` |
| `interface` | `application`, `shared` | `domain`, `infrastructure` |

---

## 휴먼리더블 코드 규칙

- 이름은 축약보다 의미를 우선한다
- 함수는 한 책임만 가진다
- 깊은 중첩보다 early return을 선호한다
- 에러 흐름은 숨기지 않는다
- 주석은 왜를 설명하고, 코드가 이미 말하는 what은 반복하지 않는다

관련 기준은 `human-readable-code-guide`와 함께 본다.

---

## 멱등성 체크리스트

```text
[ ] 기존 파일과 역할이 중복되지 않는가
[ ] 기존 함수/컴포넌트와 책임이 중복되지 않는가
[ ] 동일 입력에서 예측 가능한 결과를 만드는가
[ ] 에러 처리와 재실행 가능성을 고려했는가
[ ] 스프린트 산출물에 반영 가능한 형태인가
```

---

## 테스트 및 검증

- 단위 테스트: 도메인/유스케이스 계약 검증
- 통합 테스트: 인프라와 경계 검증
- UI 또는 E2E 테스트: 핵심 흐름 검증
- 수동 QA: 스프린트 리뷰 관점 검증

테스트 통과는 필요조건이고,
가독성과 추적성은 별도 점검 대상이다.

---

## Git 훅 / 린터 원칙

- pre-commit: lint, typecheck, obvious logging checks
- pre-push: test suite
- commit-msg: commit type convention

린터 실패 시 통과할 때까지 수정하는 루프를 통해 Normal Form 수렴을 유도한다.

---

## 스프린트 연동 규칙

기능을 구현했으면 아래 문서 반영 필요를 같이 판단한다.

- `sprint-completion-report`
- `sprint-feedback-report`
- `approval-log`
- `requirements-traceability-matrix`
- `docs/adr/*`

구현은 코드만 바꾸고 끝나지 않는다.

---

## 리팩토링 세션 규칙

- 기능 추가 세션과 리팩토링 세션을 분리한다
- 먼저 분석 보고를 만든 뒤 수정한다
- 대규모 리팩토링은 approval 대상인지 확인한다

추천 프롬프트:

```text
수정하지 말고 먼저 분석만 해줘.
중복, 50줄 초과 함수, 경계 위반, 가독성 문제를 리스트업해줘.
```
