# HARNESS_TEMPLATE.md

# ⬡ 바이브코딩 멱등성 템플릿

> AI 코딩툴로 일관성 있는 프로젝트를 만드는 하네스 엔지니어링 방법론
> 

포함 항목: `CLAUDE.md` · `CPS/PRD` · 린터 설정 · 폴더 아키텍처

---

## 목차

1. [방법론 개요](#1-방법론-개요)
2. [CLAUDE.md](http://CLAUDE.md) [— 컨텍스트 앵커](#2-claudemd--컨텍스트-앵커)
3. [CPS 문서 템플릿](#3-cps-문서-템플릿)
4. [PRD 템플릿](#4-prd-템플릿)
5. [린터 + 커밋훅 설정](#5-린터--커밋훅-설정)
6. [폴더 구조 & 아키텍처](#6-폴더-구조--아키텍처)
7. [빠른 시작 가이드](#7-빠른-시작-가이드)
8. [ADR-001 문서 기본값 결정](#adr-001-문서-기본값-결정)

---

## 1. 방법론 개요

> "어떤 AI 모델을 써도 동일한 고품질 결과물이 나오도록 강제하는 엔지니어링 방법론"
> 

**핵심 원리: 멱등성(Idempotency)** — 같은 입력 → 항상 같은 구조로 수렴

하네스 엔지니어링은 세 계층으로 AI 출력을 강제합니다.

| 계층 | 구성 요소 | 역할 |
| --- | --- | --- |
| 문서 계층 | [CLAUDE.md](http://CLAUDE.md) / CPS / PRD / ADR | AI의 컨텍스트와 원칙 고정 |
| 코드 계층 | ESLint / 커밋훅 / 타입체크 | 출력 Normal Form 강제 |
| 평가 계층 | 테스트 / 모니터링 | 멱등성 지속 검증 |

### 5단계 워크플로

```
0단계  CLAUDE.md에 Grand Principles 선언
  ↓
1단계  CPS → PRD 문서로 기능 "왜"를 고정
  ↓
2단계  아키텍처 합의 (레이어, 네이밍 규칙)
  ↓
3단계  TDG 루프 — 테스트 → 구현 → 린터 → 커밋
  ↓
4단계  주기적 리팩토링 세션 (기능 세션과 분리)
```

---

## 2. [CLAUDE.md](http://CLAUDE.md) — 컨텍스트 앵커

> 프로젝트 루트에 위치. Claude Code가 매 세션 시작 시 자동으로 읽습니다.
> 

### 세션 시작 표준 프롬프트

```
CLAUDE.md를 읽고 현재 프로젝트 구조를 파악해줘.
오늘 작업할 내용: [TODAY'S TASK]
작업 전 멱등성 체크리스트 확인해줘.
```

### 주요 규칙 요약

- 파일명: 복수 명사 강제 (`users.ts`, `products.ts`)
- `List`, `Detail`, `Manager`, `Helper` 접미사 금지
- 함수 길이 50줄 초과 시 즉시 분리
- 중첩 깊이 3단계 초과 금지 → early return 패턴
- `any` 타입 절대 사용 금지
- `domain` 레이어는 다른 레이어 import 금지

> 상세 내용은 [CLAUDE.md](http://CLAUDE.md) 페이지 참고
> 

---

## 3. CPS 문서 템플릿

> Context / Problem / Solution — 발산적 미팅을 수렴적 문서로 변환합니다.
> 

CPS는 코드 작성 전, 기능의 "왜"를 고정하는 계약서입니다.

| 섹션 | 질문 | 결과물 |
| --- | --- | --- |
| Context | 현재 상황은 무엇인가? | 팀과 AI의 멘탈 모델 정렬 |
| Problem | 무엇이 문제인가? | 측정 가능한 성공 기준 |
| Solution | 어떻게 해결하나? | AI 프롬프트 시퀀스 |

### AI 활용 패턴

```
이 기능을 구현하기 전에 CPS 문서를 작성해줘.
Context: [현재 상황]
Problem: [해결할 문제]
Solution: [구현 방향]
코드는 아직 쓰지 마.
```

> 상세 템플릿은 CPS_[TEMPLATE.md](http://TEMPLATE.md) 페이지 참고
> 

---

## 4. PRD 템플릿

> Product Requirements Document — 기술 요구사항과 AI 구현 가이드를 포함합니다.
> 

| 섹션 | 내용 |
| --- | --- |
| 1. 개요 | 기능명, 우선순위, 담당자, 완료일 |
| 2. 사용자 스토리 | As a / I want / So that 형식 |
| 3. 기능 요구사항 | Must/Should/Could/Won't Have 분류 |
| 4. 기술 요구사항 | API 명세, 데이터 모델, 성능/보안 |
| 5. AI 구현 가이드 | 구현 순서, 참고 코드, 주의사항 |
| 6. 테스트 계획 | 단위/통합/E2E 테스트 범위 |

### AI 구현 가이드 섹션의 중요성

```
구현 순서 예시:
1. 도메인 타입/인터페이스 정의 (/domain)
2. 유스케이스 테스트 작성 (/application)
3. 유스케이스 구현 (/application)
4. 인프라 구현 (/infrastructure)
5. 인터페이스 구현 (/interface)
```

> 상세 템플릿은 PRD_[TEMPLATE.md](http://TEMPLATE.md) 페이지 참고
> 

---

## 5. 린터 + 커밋훅 설정

> 코드 레이어 하네스 — AI 출력을 Normal Form으로 강제합니다.
> 

### ESLint 핵심 규칙

| 규칙 | 설정 | 목적 |
| --- | --- | --- |
| `@typescript-eslint/no-explicit-any` | error | any 타입 금지 |
| `@typescript-eslint/naming-convention` | error | 네이밍 컨벤션 강제 |
| `import/order` | error | import 순서 고정 |
| `import/no-cycle` | error | 순환 참조 금지 |
| `max-depth` | error (3) | 중첩 깊이 제한 |
| `no-console` | warn | console.log 경고 |
| `import/no-restricted-paths` | error | 레이어 경계 강제 |

### Git 훅 3단계

- **pre-commit**: 린터 → 타입체크 → console.log 검사
- **commit-msg**: `feat/fix/refactor/docs/test/chore` 형식 검사
- **pre-push**: 테스트 전체 실행

### 설치 방법

```bash
# 1. 의존성 설치
npm install -D eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
npm install -D eslint-plugin-import eslint-import-resolver-typescript

# 2. Git 훅 설치
node scripts/setup-hooks.js
```

> 커밋 시 린터 실패 → AI에게 "린터 에러 고쳐줘" → 재커밋
> 

> 이 루프가 Normal Form 수렴의 핵심 메커니즘입니다.
> 

---

## 6. 폴더 구조 & 아키텍처

> 4-레이어 아키텍처 — 레이어 경계가 멱등성의 물리적 보장입니다.
> 

### 레이어 의존성 규칙

```
interface ──→ application ──→ domain
                    ↑
             infrastructure
```

| 레이어 | 가능한 import | 금지된 import |
| --- | --- | --- |
| `domain` | `shared`만 | 나머지 모두 |
| `application` | `domain`, `shared` | `infrastructure`, `interface` |
| `infrastructure` | `domain`, `application/ports` | `interface` |
| `interface` | `application`, `shared` | `domain`, `infrastructure` |

### 파일 네이밍 규칙

| 파일 종류 | 패턴 | 예시 |
| --- | --- | --- |
| 도메인 엔티티 | `[name].ts` | `user.ts` |
| 유스케이스 | `[name].usecase.ts` | `create-user.usecase.ts` |
| 레포지토리 | `[name].repository.ts` | `user.repository.ts` |
| 라우터 | `[name].router.ts` | `users.router.ts` |
| 핸들러 | `[name].handler.ts` | `users.handler.ts` |
| 테스트 | `[name].test.ts` | `create-user.usecase.test.ts` |

**금지 패턴**: `userList.ts`, `userDetail.ts`, `userManager.ts`, `userHelper.ts`

> 상세 구조는 [ARCHITECTURE.md](http://ARCHITECTURE.md) 페이지 참고
> 

---

## 7. 빠른 시작 가이드

### 새 프로젝트 시작

```bash
# 1. 파일 복사
cp CLAUDE.md .eslintrc.json [새프로젝트]/
cp -r docs/ scripts/ [새프로젝트]/

# 2. Git 훅 설치
node scripts/setup-hooks.js

# 3. CLAUDE.md 채우기
# [PROJECT_NAME], 스택, 목적만 채우면 바로 사용 가능
```

### 기능 개발 체크리스트 (매번)

- [ ]  CPS 문서 먼저 작성 (코드 전)
- [ ]  PRD로 구체화
- [ ]  세션 시작 프롬프트로 Claude 로딩
- [ ]  테스트 케이스 작성 요청
- [ ]  구현 요청 (레이어 명시)
- [ ]  린터 통과 확인
- [ ]  커밋 (컨벤션 형식)

### 주기적 유지보수

- 기능 세션과 리팩토링 세션 분리 (같은 날 섯지 않기)
- 리팩토링 전 "분석만 해줘, 수정 금지" 프롬프트 사용
- 주요 결정은 ADR 문서로 기록
- `CLAUDE.md` ADR 로그 테이블 업데이트

> 핵심 원칙: AI는 빠른 손, 하네스는 그 손이 항상 같은 글씨를 쓰게 만드는 틀
> 

---

## ADR-001 문서 기본값 결정

| 항목 | 내용 |
| --- | --- |
| 날짜 | 2026-03-25 |
| 상태 | 승인 |
| 결정자 | 프로젝트 오너 |

**결정**: 이 프로젝트의 모든 문서는 `.md` (Markdown)을 기본값으로 사용한다.

**이유**:

- Git 버전 관리에 최적화 (diff, blame, PR 리뷰 가능)
- Claude Code가 직접 읽고 컨텍스트로 활용 가능
- 별도 뷰어 없이 GitHub/VSCode에서 즉시 렌더링
- `docx`, `pdf` 대비 용량 경량, 충돌 해결 용이

**영향 범위**: 모든 문서 (`docs/`, `CLAUDE.md`, `ADR`, `CPS`, `PRD`)

**금지**: `.docx`, `.pdf` 등 바이너리 포맷을 문서로 사용하는 것