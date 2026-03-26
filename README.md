# Harness-Driven Agile Methodology

**AI 기획 + 바이브코딩 + 멀티 AI 릴레이를 인간 승인 체계와 휴먼리더블 산출물 위에 올려놓기 위한 통합 방법론**

---

## 이 방법론이 해결하는 문제

### 문제 1: AI는 빠르지만 결과물이 매번 달라진다
같은 요구를 주어도 모델, 세션, 컨텍스트에 따라 문서 구조와 코드 스타일이 흔들린다.

### 문제 2: 기획과 개발은 빨라졌지만 승인 체계는 그대로다
실무자 검토, 경영자 컨펌, 보고 문서, 변경 승인 같은 기존 의사결정 구조는 여전히 필요하다.

### 문제 3: 바이브코딩 결과가 유지보수 가능한 자산으로 남지 않는다
"일단 되는 코드"는 빨리 나오지만, 휴먼리더블 코드 컨벤션과 변경 이력이 없으면 팀 자산이 되지 못한다.

### 문제 4: 애자일을 한다고 해도 환류 문서 체계가 없으면 반복 개선이 남지 않는다
스프린트가 끝나도 이슈, QA, 피어리뷰, 레퍼런스 괴리, 개선 포인트가 구조적으로 누적되지 않는다.

---

## 핵심 관점

이 저장소는 단순한 프롬프트 모음이 아니다.

이 방법론은 아래 3가지를 결합한다.

1. **애자일 방법론**
스프린트 단위로 계획, 구현, 리뷰, 환류를 반복한다.

2. **하네스 엔지니어링**
문서, 코드 규칙, 평가 체계를 통해 AI 출력이 가능한 한 같은 Normal Form으로 수렴하게 만든다.

3. **인간 승인 체계**
매 Phase 전환마다 인간이 산출물을 받고, 검토하고, 다음 작업을 지시한다.

---

## 핵심 원리

### 문서 = 다음 단계 입력
리서치는 기획서의 입력이고, 기획서는 개발명세서의 입력이며, 개발명세서는 구현과 테스트의 입력이다.

### 스프린트 종료 시 반드시 문서가 남아야 한다
매 스프린트는 코드만 끝나면 안 된다.
반드시 완료 보고서, 환류 보고서, 추가 리서치, 다음 스크럼 계획 보고서, 개발명세서 업데이트가 남아야 한다.

### 하네스는 4개 층으로 구성된다

1. **문서 하네스**
리서치, 기획서 6종, 개발명세서 8종, 스프린트 보고서, ADR

2. **코드 하네스**
컨벤션, 린터, 커밋훅, 테스트, 레이어 경계

3. **평가 하네스**
QA, UI 점검, 피어리뷰, 레퍼런스 괴리 점검, 추적성 검토

4. **승인 하네스**
매 Phase 전환마다 인간이 검토하고 다음 작업을 지시

### Human-in-the-loop는 기본값이다
AI는 초안과 제안을 만든다.
인간은 매 게이트에서 산출물을 검토하고, 승인하고, 다음 Phase를 지시한다.
AI는 인간의 지시 없이 다음 Phase로 넘어가지 않는다.

### 문서 기본값은 항상 Markdown이다
이 저장소에서 문서 산출물은 기본적으로 모두 `.md`를 사용한다.

---

## 전체 파이프라인

```text
Phase 0   Project Init
   ↓
Phase 1   Discovery Research
   ↓      ← Gate 1: 인간 리서치 검토 → "기획서 작성 시작해"
Phase 2   기획서 작성 (6종)
   ↓      ← Gate 2: 인간 기획서 승인 → "개발명세서 작성해"
Phase 3   개발명세서 작성 (8종)
   ↓      ← Gate 3: 인간 개발명세서 승인 → "MVP 개발 시작해"
Phase 4   MVP Build
   ↓
Phase 5   Sprint Completion Report
   ↓      ← Gate 4: 인간 빌드 확인 → "환류 작업 진행해"
Phase 6   Sprint Feedback Report
   ↓
Phase 7   Feedback-Driven Research
   ↓
Phase 8   Sprint Plan Report
   ↓      ← Gate 5: 인간 다음 스크럼 승인 → "개발명세서 업데이트하고 개발해"
Phase 9   Development Spec Update
   ↓
   └──→ Phase 4로 반복 (컨펌까지)

           ← Gate 6: 인간 "개발 완료" 선언
Phase 10  Final Planning Update (기획서 6종 최종 업데이트)
```

핵심은 선형 완료가 아니라, `Build → Review → Feedback → Research → Plan → Spec Update → Build`를 인간 승인 하에 계속 반복하는 것이다.

---

## 필수 산출물 체계

### 1. 리서치
- `docs/research/research.md`

### 2. 기획서 6종
- `docs/planning/business-plan.md` (사업기획서)
- `docs/planning/service-plan.md` (서비스기획서)
- `docs/planning/operations-plan.md` (운영기획서)
- `docs/planning/marketing-plan.md` (마케팅기획서)
- `docs/planning/brand-plan.md` (브랜드기획서)
- `docs/planning/project-management.md` (프로젝트관리기획서)

### 3. 개발명세서 8종
- `docs/development/service-overview.md` (서비스 개요서)
- `docs/development/requirements.md` (요구사항 정의서)
- `docs/development/user-stories.md` (사용자 스토리)
- `docs/development/information-architecture.md` (정보구조도)
- `docs/development/user-flow.md` (사용자 플로우차트)
- `docs/development/wireframes.md` (화면 설계서)
- `docs/development/functional-spec.md` (기능 정의서)
- `docs/development/data-model.md` (데이터 모델 정의서)

### 4. 구현 산출물
- `src/...`
- `tests/...`
- `docs/adr/...`

### 5. 스프린트 보고 체계
- `sprint-XX-completion-report.md` (완료 보고서)
- `sprint-XX-feedback-report.md` (환류 보고서)
- `sprint-XX-plan-report.md` (계획 보고서)
- `executive-decision-brief.md` (의사결정 요약)

### 6. 거버넌스 / 추적 / 승인 문서
- `approval-log.md`
- `definition-of-ready-done.md`
- `requirements-traceability-matrix.md`
- `human-readable-code-guide.md`

상세 맵은 [docs/agile-deliverables-map.md](docs/agile-deliverables-map.md) 참고.

---

## 인간 승인 게이트 요약

| Gate | 시점 | 인간이 하는 일 | 다음 지시 |
|------|------|----------------|-----------|
| 1 | 리서치 후 | 리서치 결과 검토 | "기획서 작성 시작해" |
| 2 | 기획서 후 | 기획서 6종 검토/승인 | "개발명세서 작성해" |
| 3 | 개발명세서 후 | 개발명세서 8종 검토/승인 | "MVP 개발 시작해" |
| 4 | 완료 보고서 후 | 빌드 결과 확인 | "환류 작업 진행해" |
| 5 | 계획 보고서 후 | 다음 스크럼 범위 승인 | "개발명세서 업데이트하고 개발해" |
| 6 | 최종 컨펌 | "개발 완료" 선언 | "기획서 최종 업데이트해" |

---

## 왜 보고 문서가 필요한가

애자일은 문서를 버리라는 뜻이 아니다.
현실의 IT 프로젝트는 여전히 아래를 요구한다.

- 현업자와의 합의
- 경영진의 승인
- 변경 이력 추적
- QA 결과 공유
- 위험과 가정 관리
- 릴리스 전 최종 판단

그래서 이 방법론은 "문서는 최소화"가 아니라, **판단과 승인에 필요한 문서는 구조화해서 유지**하는 쪽을 택한다.

---

## 하네스 엔지니어링 관점에서의 운영 방식

### 문서 하네스
- 모든 중요한 판단은 문서로 남긴다
- 각 문서는 버전과 변경 이유를 가진다
- 문서마다 단일 원본을 유지한다

### 코드 하네스
- 코드 컨벤션은 사람이 읽기 좋은 방향을 우선한다
- AI가 생성한 코드도 린터와 테스트를 통과해야 한다
- 레이어 경계와 네이밍 규칙으로 구조를 강제한다

### 평가 하네스
- 매 스프린트마다 QA, UI, 피어리뷰, 레퍼런스 괴리를 평가한다
- "무엇이 잘못되었는가"뿐 아니라 "왜 그랬는가"를 남긴다

### 승인 하네스
- 매 Phase 전환마다 인간이 산출물을 받고 검토하고 다음 작업을 지시한다
- 계획 변경은 approval log에 기록한다
- 릴리스 전에는 readiness 관점으로 다시 본다

---

## 이 저장소의 핵심 파일

### 운영 앵커
- [AGENTS.md](AGENTS.md) — Codex용
- [CLAUDE.md](CLAUDE.md) — Claude Code용

### 시작 프롬프트
- [KICKOFF_PROMPT.md](KICKOFF_PROMPT.md)

### 애자일 산출물 맵
- [docs/agile-deliverables-map.md](docs/agile-deliverables-map.md)

### 애자일 템플릿 세트
- [docs/agile-templates/README.md](docs/agile-templates/README.md)

### 기획서 작성 지침 (완성본 참조용)
- `docs/planning-guides/`

### 릴레이 템플릿
- `docs/relay-templates/`

### 구현 가이드 템플릿
- `docs/vibe-templates/`

---

## 권장 사용 흐름

### 1. 새 프로젝트 시작

```bash
# 새 프로젝트 골격 생성
./init-project.sh my-project --type fullstack
cd my-project
claude
```

### 2. 프로젝트 앵커 작성
- 프로젝트명, 목적, 스택, 현재 버전, 현재 스프린트, 현재 페이즈

### 3. 첫 세션 요청

```text
CLAUDE.md를 읽고 프로젝트를 세팅해줘.
오늘은 Discovery Research부터 시작하고 싶어.
```

### 4. 스프린트 진행 (인간 승인 하에 반복)

```text
Phase 1: 리서치
  → 인간 검토 → "기획서 작성 시작해"
Phase 2: 기획서 6종
  → 인간 검토 → "개발명세서 작성해"
Phase 3: 개발명세서 8종
  → 인간 검토 → "MVP 개발 시작해"
Phase 4: MVP 개발
Phase 5: 완료 보고서
  → 인간 검토 → "환류 작업 진행해"
Phase 6: 환류 보고서
Phase 7: 추가 리서치
Phase 8: 스크럼 계획 보고서
  → 인간 검토 → "개발명세서 업데이트하고 개발해"
Phase 9: 개발명세서 업데이트
  → Phase 4로 반복
...
Phase 10: 기획서 최종 업데이트
```

### 5. 세션 종료 시

```text
오늘 작업 기준으로 CLAUDE.md 현재 상태와 버전 테이블을 업데이트해줘.
```

---

## 현재 포함된 템플릿

### 기획서 (기획서 6종 산출물용)
- [business-plan-template.md](docs/agile-templates/planning/business-plan-template.md)
- [service-plan-template.md](docs/agile-templates/planning/service-plan-template.md)
- [operations-plan-template.md](docs/agile-templates/planning/operations-plan-template.md)
- [marketing-plan-template.md](docs/agile-templates/planning/marketing-plan-template.md)
- [brand-plan-template.md](docs/agile-templates/planning/brand-plan-template.md)
- [project-management-template.md](docs/agile-templates/planning/project-management-template.md)

### 개발명세서 (개발명세서 8종 산출물용)
- [service-overview-template.md](docs/agile-templates/development/service-overview-template.md)
- [requirements-template.md](docs/agile-templates/development/requirements-template.md)
- [user-stories-template.md](docs/agile-templates/development/user-stories-template.md)
- [information-architecture-template.md](docs/agile-templates/development/information-architecture-template.md)
- [user-flow-template.md](docs/agile-templates/development/user-flow-template.md)
- [wireframes-template.md](docs/agile-templates/development/wireframes-template.md)
- [functional-spec-template.md](docs/agile-templates/development/functional-spec-template.md)
- [data-model-template.md](docs/agile-templates/development/data-model-template.md)

### 스프린트 보고서
- [sprint-completion-report-template.md](docs/agile-templates/sprints/sprint-completion-report-template.md)
- [sprint-feedback-report-template.md](docs/agile-templates/sprints/sprint-feedback-report-template.md)
- [sprint-plan-report-template.md](docs/agile-templates/sprints/sprint-plan-report-template.md)

### 거버넌스 / 승인
- [executive-decision-brief-template.md](docs/agile-templates/governance/executive-decision-brief-template.md)
- [approval-log-template.md](docs/agile-templates/governance/approval-log-template.md)
- [definition-of-ready-done-template.md](docs/agile-templates/governance/definition-of-ready-done-template.md)
- [requirements-traceability-matrix-template.md](docs/agile-templates/governance/requirements-traceability-matrix-template.md)
- [human-readable-code-guide-template.md](docs/agile-templates/governance/human-readable-code-guide-template.md)

---

## 요약

이 방법론의 목표는 단순하다.

**AI 코딩 툴을 써도, 결과물이 매번 흔들리지 않게 만들고, 인간이 매 단계에서 검토하고 승인하며 다음을 지시할 수 있는 형태로 남기는 것.**

즉, 이 저장소는
`바이브코딩을 하되 멱등성과 지속 유지 가능성을 잃지 않기 위한, 인간 승인 기반 하네스 애자일 운영체계`
를 제공한다.
