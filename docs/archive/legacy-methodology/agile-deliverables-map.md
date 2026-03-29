# Agile Deliverables Map

This methodology uses a repeating sprint loop with human approval at every gate.

## Required Output Chain

1. Research output
2. 기획서 6종 (business planning documents)
3. 개발명세서 8종 (development specification documents)
4. MVP build
5. Sprint completion report
6. Sprint feedback report
7. Feedback-driven research
8. Sprint plan report
9. Updated 개발명세서 8종
10. Next MVP build (repeat 4~9)
11. Final 기획서 6종 update (after completion confirmation)

## 기획서 6종 (Planning Documents)

| # | Document | File Name | Description |
|---|----------|-----------|-------------|
| 1 | 사업기획서 | `business-plan.md` | 시장, 고객, BM, 성장 전략 |
| 2 | 서비스기획서 | `service-plan.md` | 사용자 경험, 기능 구조 |
| 3 | 운영기획서 | `operations-plan.md` | 운영 기준, 절차, CS |
| 4 | 마케팅기획서 | `marketing-plan.md` | 채널, 퍼널, KPI |
| 5 | 브랜드기획서 | `brand-plan.md` | 브랜드 정체성, 톤앤매너 |
| 6 | 프로젝트관리기획서 | `project-management.md` | 일정, 범위, 역할, 리스크 |

## 개발명세서 8종 (Development Specifications)

| # | Document | File Name | Description |
|---|----------|-----------|-------------|
| 1 | 서비스 개요서 | `service-overview.md` | 서비스 정의, 가치제안, 성공지표 |
| 2 | 요구사항 정의서 | `requirements.md` | 기능/비기능 요구사항, 제약 |
| 3 | 사용자 스토리 | `user-stories.md` | 사용자 관점 행동, 수용 기준 |
| 4 | 정보구조도 | `information-architecture.md` | 메뉴, 네비게이션, 콘텐츠 구조 |
| 5 | 사용자 플로우차트 | `user-flow.md` | 단계별 흐름, 분기, 예외 |
| 6 | 화면 설계서 | `wireframes.md` | 화면 구성, 컴포넌트, 상태 |
| 7 | 기능 정의서 | `functional-spec.md` | 기능 상세, 정책, 예외 처리 |
| 8 | 데이터 모델 정의서 | `data-model.md` | 엔티티, 관계, 필드, 무결성 |

## Sprint Report Set

| Document | File Name | When |
|----------|-----------|------|
| 완료 보고서 | `sprint-XX-completion-report.md` | Phase 5: 빌드 결과 평가 |
| 환류 보고서 | `sprint-XX-feedback-report.md` | Phase 6: QA, 피어리뷰, 이슈 |
| 계획 보고서 | `sprint-XX-plan-report.md` | Phase 8: 다음 스크럼 범위 |

## Versioning Example

| Sprint | 기획서 6종 | 개발명세서 8종 | Build | Reports |
|--------|-----------|--------------|-------|---------|
| 01 | v0.1 | v0.1 | v0.1 | sprint-01 |
| 02 | v0.1 | v0.2 | v0.2 | sprint-02 |
| 03 | v0.1 | v0.3 | v0.3 | sprint-03 |
| Final | vFinal | v0.3 | v0.3 | - |

> 기획서 6종은 스프린트 중에는 v0.1을 유지하고, 개발 완료 후 Phase 10에서 최종 업데이트한다.
> 개발명세서 8종은 매 스프린트마다 환류 결과를 반영하여 버전을 올린다.

## File Naming Policy

**파일명에 버전 번호를 넣지 않는다.** 파일은 항상 1개만 유지하고, 버전은 문서 내부 헤더와 Change Log에 기록한다. 버전 이력은 Git이 담당한다.

이유:
- 단일 원본 원칙: `business-plan.md`와 `business-plan-v0.1.md`가 공존하면 추적성이 깨진다
- 파일 폭발 방지: 9개 스프린트 x 14개 문서 = 126개 파일이 되는 것을 막는다
- Git과 역할 분리: 파일 시스템은 "현재 상태", Git은 "변경 이력"을 담당한다

규칙:
- 기획서/개발명세서/리서치: 파일명 고정, 내부 `Version: v0.X` 헤더로 버전 표기
- 스프린트 보고서: `sprint-XX-` 접두사로 스프린트 번호만 구분 (보고서는 스프린트마다 새 파일)
- 거버넌스 문서: 파일명 고정, 내용 누적

## Recommended Folder Structure

```text
docs/
  research/
    research.md                      ← 내부에 Version: v0.1
  planning/                          ← 기획서 6종
    business-plan.md
    service-plan.md
    operations-plan.md
    marketing-plan.md
    brand-plan.md
    project-management.md
  development/                       ← 개발명세서 8종
    service-overview.md
    requirements.md
    user-stories.md
    information-architecture.md
    user-flow.md
    wireframes.md
    functional-spec.md
    data-model.md
  sprints/                           ← 스프린트별 새 파일
    sprint-01-completion-report.md
    sprint-01-feedback-report.md
    sprint-02-plan-report.md
    sprint-02-completion-report.md
    sprint-02-feedback-report.md
  governance/                        ← 파일명 고정, 내용 누적
    approval-log.md
    definition-of-ready-done.md
    requirements-traceability-matrix.md
    human-readable-code-guide.md
    executive-decision-brief.md
  adr/
src/
tests/
```

## Human Approval Gates

| Gate | After Phase | Human Action | Next Instruction |
|------|------------|--------------|------------------|
| 1 | Phase 1 Research | 리서치 결과 검토 | "기획서 작성 시작해" |
| 2 | Phase 2 기획서 | 기획서 6종 검토/승인 | "개발명세서 작성해" |
| 3 | Phase 3 개발명세서 | 개발명세서 8종 검토/승인 | "MVP 개발 시작해" |
| 4 | Phase 5 완료 보고서 | 빌드 결과 확인 | "환류 작업 진행해" |
| 5 | Phase 8 계획 보고서 | 다음 스크럼 범위 승인 | "개발명세서 업데이트하고 개발해" |
| 6 | 최종 컨펌 | "개발 완료" 선언 | "기획서 최종 업데이트해" |
