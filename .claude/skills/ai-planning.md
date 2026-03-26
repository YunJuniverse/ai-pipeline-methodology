---
name: ai-planning
description: 하네스 기반 애자일 기획 오케스트레이션. 리서치, 기획서 6종, 개발명세서 8종, 스프린트 보고서, 승인 게이트까지 연결한다.
---

# AI Planning Orchestration

## 목적

이 스킬은 기획 요청을 단발성 문서 작성으로 끝내지 않고,
리서치 → 기획서 6종 → 개발명세서 8종 → MVP → 스프린트 환류 체계로 연결한다.

핵심은 아래 3가지다:

1. 문서 간 추적성 유지
2. 버전 관리
3. 인간 승인 게이트 반영 (매 Phase 전환마다 인간이 검토하고 다음을 지시)

---

## 실행 절차

### 1단계: 현재 상태 확인

먼저 아래를 확인한다.

- `CLAUDE.md` 또는 `AGENTS.md`의 현재 버전, 현재 스프린트, 현재 페이즈
- 이미 존재하는 문서
- 현재 요청이 신규 작성인지, 업데이트인지, 환류 반영인지

### 2단계: 요청 분류

| 요청 유형 | 기본 산출물 | Phase |
|-----------|-------------|-------|
| 시장, 레퍼런스, 문제 검증, 위험 탐색 | `docs/research/*.md` | 1 |
| 사업 방향, BM, 고객, 포지셔닝 | `docs/planning/business-plan.md` | 2 |
| 서비스 구조, 기능 범위, MVP 정의 | `docs/planning/service-plan.md` | 2 |
| 운영 기준, CS, 검수, 관리자 | `docs/planning/operations-plan.md` | 2 |
| 채널, 퍼널, KPI, 캠페인 | `docs/planning/marketing-plan.md` | 2 |
| 브랜드 정체성, 톤앤매너, 비주얼 | `docs/planning/brand-plan.md` | 2 |
| 일정, 범위, 역할, 리스크 관리 | `docs/planning/project-management.md` | 2 |
| 서비스 개요, 요구사항, 사용자 행동 | `docs/development/*.md` | 3 |
| 구현 범위, 테스트 전략, 기술 반영 | `docs/development/*.md` | 3 |
| 스프린트 완료 평가 | `docs/sprints/sprint-XX-completion-report.md` | 5 |
| QA, 피어리뷰, 괴리 분석, 개선점 | `docs/sprints/sprint-XX-feedback-report.md` | 6 |
| 다음 스크럼 범위, 목표, 계획 | `docs/sprints/sprint-XX-plan-report.md` | 8 |
| 승인, 추적, readiness, 보고 | `docs/governance/*.md` | any |

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

## 기획서 6종 규칙

기획서는 사업 전략과 방향을 담는 상위 문서다.
개발명세서의 입력이 되며, 개발 완료 후 Phase 10에서 최종 업데이트한다.

1. `business-plan` (사업기획서) — 시장, 고객, BM, 성장
2. `service-plan` (서비스기획서) — 사용자, 기능 구조, MVP
3. `operations-plan` (운영기획서) — 운영 기준, CS, 검수
4. `marketing-plan` (마케팅기획서) — 채널, 퍼널, KPI
5. `brand-plan` (브랜드기획서) — 정체성, 톤앤매너
6. `project-management` (프로젝트관리기획서) — 일정, 역할, 리스크

### 기획서 선택 가이드

| 요청 키워드 | 기본 문서 |
|------------|-----------|
| 시장 분석, BM, 수익 모델, 투자, 성장 | `business-plan` |
| 서비스 구조, 핵심 기능, MVP 범위, 시나리오 | `service-plan` |
| 운영 규칙, CS 정책, 검수, 관리자, 어뷰징 | `operations-plan` |
| 채널, 캠페인, 퍼널, 전환, 리텐션, 광고 | `marketing-plan` |
| 브랜드, 톤앤매너, 비주얼, 포지셔닝 | `brand-plan` |
| 일정, 범위, 역할, 리스크, 보고, 변경 관리 | `project-management` |

---

## 개발명세서 8종 규칙

개발명세서는 기획서를 구현 가능한 형태로 변환한 문서다.
매 스프린트마다 환류 결과를 반영하여 버전을 올린다.

1. `service-overview` (서비스 개요서)
2. `requirements` (요구사항 정의서)
3. `user-stories` (사용자 스토리)
4. `information-architecture` (정보구조도)
5. `user-flow` (사용자 플로우차트)
6. `wireframes` (화면 설계서)
7. `functional-spec` (기능 정의서)
8. `data-model` (데이터 모델 정의서)

### 개발명세서 선택 가이드

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
어느 기획서 또는 개발명세서가 업데이트되어야 하는지도 함께 적는다.

---

## 스프린트 환류 연결 규칙

스프린트 완료나 QA 결과가 들어오면,
아래 흐름으로 처리한다.

1. `sprint-XX-completion-report` (Phase 5)
2. `sprint-XX-feedback-report` (Phase 6)
3. feedback-driven research (Phase 7)
4. `sprint-XX-plan-report` (Phase 8)
5. 개발명세서 8종 version bump (Phase 9)

환류 없는 기획은 정적인 문서가 되므로 지양한다.

---

## 인간 승인 게이트 규칙

AI는 게이트 없이 다음 Phase로 넘어가지 않는다.

| Gate | After | Human Instruction |
|------|-------|-------------------|
| 1 | Phase 1 Research | "기획서 작성 시작해" |
| 2 | Phase 2 기획서 | "개발명세서 작성해" |
| 3 | Phase 3 개발명세서 | "MVP 개발 시작해" |
| 4 | Phase 5 완료 보고서 | "환류 작업 진행해" |
| 5 | Phase 8 계획 보고서 | "개발명세서 업데이트하고 개발해" |
| 6 | 최종 컨펌 | "기획서 최종 업데이트해" |

---

## 품질 체크리스트

- [ ] 문서 목적이 첫 부분에 드러나는가
- [ ] 독자와 승인자가 명시되는가
- [ ] 기획서와 개발명세서의 경계가 분명한가
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
