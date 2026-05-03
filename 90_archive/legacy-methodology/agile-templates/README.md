# Agile Deliverables Templates

This folder contains the default template set for the harness-driven agile methodology.

## Folder Map

- `research/` — 리서치 템플릿
- `planning/` — 기획서 6종 산출물 템플릿 + 운영정책 템플릿
- `development/` — 개발명세서 8종 산출물 템플릿
- `sprints/` — 스프린트 보고서 템플릿 (완료/환류/계획)
- `governance/` — 거버넌스, 승인, 추적 템플릿

## Template Inventory

### Planning (기획서 6종)
| Template | Purpose |
|----------|---------|
| `business-plan-template.md` | 사업기획서 |
| `service-plan-template.md` | 서비스기획서 |
| `operations-plan-template.md` | 운영기획서 |
| `marketing-plan-template.md` | 마케팅기획서 |
| `brand-plan-template.md` | 브랜드기획서 |
| `project-management-template.md` | 프로젝트관리기획서 |
| `operations-policy-template.md` | 운영정책 (개발명세 보조) |

### Development (개발명세서 8종)
| Template | Purpose |
|----------|---------|
| `service-overview-template.md` | 서비스 개요서 |
| `requirements-template.md` | 요구사항 정의서 |
| `user-stories-template.md` | 사용자 스토리 |
| `information-architecture-template.md` | 정보구조도 |
| `user-flow-template.md` | 사용자 플로우차트 |
| `wireframes-template.md` | 화면 설계서 |
| `functional-spec-template.md` | 기능 정의서 |
| `data-model-template.md` | 데이터 모델 정의서 |
| `development-spec-template.md` | 개발명세 통합본 (선택) |

### Sprints (스프린트 보고서)
| Template | Purpose |
|----------|---------|
| `sprint-completion-report-template.md` | 완료 보고서 |
| `sprint-feedback-report-template.md` | 환류 보고서 |
| `sprint-plan-report-template.md` | 계획 보고서 |

### Governance (거버넌스)
| Template | Purpose |
|----------|---------|
| `approval-log-template.md` | 승인 이력 |
| `definition-of-ready-done-template.md` | Ready/Done 기준 |
| `executive-decision-brief-template.md` | 의사결정 요약 |
| `requirements-traceability-matrix-template.md` | 추적성 매트릭스 |
| `human-readable-code-guide-template.md` | 코드 가독성 가이드 |

## Standard Rules

- Every document carries a version.
- Every sprint produces a completion report, a feedback report, and (for the next sprint) a plan report.
- 개발명세서 updates must reference the sprint that triggered the revision.
- 기획서 6종 are updated at Phase 10 (final) after human confirms completion.
- When a document changes meaningfully, record:
  - version
  - date
  - reason for change
  - affected downstream artifacts

## Recommended Workspace Structure

```text
docs/
  research/
  planning/          ← 기획서 6종
  development/       ← 개발명세서 8종
  sprints/
  governance/
  adr/
src/
tests/
```
