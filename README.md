# Harness-Driven Agile Methodology

**AI 코딩 툴을 활용한 바이브코딩을, 인간 승인 체계와 휴먼리더블 산출물 위에 올려놓기 위한 방법론**

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
실무자 리뷰와 경영자 승인 흐름을 문서와 체크포인트로 유지한다.

---

## 핵심 원리

### 문서 = 다음 단계 입력
리서치 문서는 기획의 입력이고, 기획 문서는 개발명세의 입력이며, 개발명세는 구현과 테스트의 입력이다.

### 스프린트 종료 시 반드시 문서가 남아야 한다
매 스프린트는 코드만 끝나면 안 된다.
반드시 빌드 결과, 리뷰 결과, 환류 결과, 다음 버전 문서가 남아야 한다.

### 하네스는 4개 층으로 구성된다

1. **문서 하네스**
리서치, 기획서, 개발명세서, 보고서, ADR

2. **코드 하네스**
컨벤션, 린터, 커밋훅, 테스트, 레이어 경계

3. **평가 하네스**
QA, UI 점검, 피어리뷰, 레퍼런스 괴리 점검, 추적성 검토

4. **승인 하네스**
실무 승인, 스프린트 종료 승인, 다음 스프린트 승인, 릴리스 승인

### Human-in-the-loop는 기본값이다
AI는 초안과 제안을 만든다.
전략 변경, 범위 변경, 아키텍처 변경, 스프린트 종료, 릴리스 결정은 인간이 승인한다.

### 문서 기본값은 항상 Markdown이다
이 저장소에서 문서 산출물은 기본적으로 모두 `.md`를 사용한다.

---

## 전체 파이프라인

```text
Phase 0  Project Init
   ↓
Phase 1  Discovery Research
   ↓
Phase 2  Planning Documents
   ↓
Phase 3  Development Spec
   ↓
Phase 4  MVP Build
   ↓
Phase 5  Sprint Review
   ↓
Phase 6  Feedback Revision
   ↓
Phase 7  Next Sprint Update
   ↓
Repeat until approval / release readiness
```

핵심은 선형 완료가 아니라, `Build -> Review -> Feedback -> Update`를 계속 반복하는 것이다.

---

## 필수 산출물 체계

### 1. 리서치
- `docs/research/research-v0.1.md`

### 2. 기획 문서 세트
- `service-overview`
- `requirements`
- `user-stories`
- `information-architecture`
- `user-flow`
- `wireframes`
- `functional-spec`
- `data-model`
- `operations-policy` (권장)

### 3. 개발명세
- `docs/development/development-spec-v0.1.md`

### 4. 구현 산출물
- `src/...`
- `tests/...`
- `docs/adr/...`

### 5. 스프린트 보고 체계
- `sprint-XX-completion-report.md`
- `sprint-XX-feedback-report.md`
- `executive-decision-brief.md`

### 6. 거버넌스 / 추적 / 승인 문서
- `approval-log.md`
- `definition-of-ready-done.md`
- `requirements-traceability-matrix.md`
- `human-readable-code-guide.md`

상세 맵은 [docs/agile-deliverables-map.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-deliverables-map.md) 참고.

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
- 각 스프린트는 close decision을 가진다
- 계획 변경은 approval log에 기록한다
- 릴리스 전에는 readiness 관점으로 다시 본다

---

## 이 저장소의 핵심 파일

### 운영 앵커
- [AGENTS.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/AGENTS.md)
- [CLAUDE.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/CLAUDE.md)

### 시작 프롬프트
- [KICKOFF_PROMPT.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/KICKOFF_PROMPT.md)

### 애자일 산출물 맵
- [docs/agile-deliverables-map.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-deliverables-map.md)

### 애자일 템플릿 세트
- [docs/agile-templates/README.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/README.md)

### 기존 계획 지침
- `docs/planning-guides/`

### 릴레이 템플릿
- `docs/relay-templates/`

### 구현 가이드 템플릿
- `docs/vibe-templates/`

---

## 권장 사용 흐름

### 1. 새 프로젝트 시작

```bash
./init-project.sh my-project --type fullstack
cd my-project
claude
```

### 2. 프로젝트 앵커 작성
- 프로젝트명
- 목적
- 스택
- 현재 버전
- 현재 스프린트
- 현재 페이즈

### 3. 첫 세션 요청

```text
CLAUDE.md를 읽고 프로젝트를 세팅해줘.

오늘은 Discovery Research와 Planning Docs v0.1을 시작하고 싶어.
레퍼런스와 목표를 반영해서 service-overview부터 작성해줘.
```

### 4. 스프린트 진행
- 리서치
- 기획 문서 작성/업데이트
- 개발명세 작성/업데이트
- 구현
- 스프린트 완료 보고
- 스프린트 환류 보고
- 다음 버전 문서 업데이트

### 5. 세션 종료 시

```text
오늘 작업 기준으로 AGENTS.md 현재 상태와 버전 테이블을 업데이트해줘.
```

---

## 현재 포함된 템플릿

### 계획 / 설계
- [service-overview-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/planning/service-overview-template.md)
- [requirements-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/planning/requirements-template.md)
- [user-stories-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/planning/user-stories-template.md)
- [information-architecture-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/planning/information-architecture-template.md)
- [user-flow-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/planning/user-flow-template.md)
- [wireframes-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/planning/wireframes-template.md)
- [functional-spec-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/planning/functional-spec-template.md)
- [data-model-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/planning/data-model-template.md)
- [operations-policy-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/planning/operations-policy-template.md)
- [development-spec-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/development/development-spec-template.md)

### 리뷰 / 환류 / 승인
- [sprint-completion-report-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/sprints/sprint-completion-report-template.md)
- [sprint-feedback-report-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/sprints/sprint-feedback-report-template.md)
- [executive-decision-brief-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/governance/executive-decision-brief-template.md)
- [approval-log-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/governance/approval-log-template.md)
- [definition-of-ready-done-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/governance/definition-of-ready-done-template.md)
- [requirements-traceability-matrix-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/governance/requirements-traceability-matrix-template.md)
- [human-readable-code-guide-template.md](/Users/hayden/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/methodology/docs/agile-templates/governance/human-readable-code-guide-template.md)

---

## 요약

이 방법론의 목표는 단순하다.

**AI 코딩 툴을 써도, 결과물이 매번 흔들리지 않게 만들고, 인간이 검토하고 승인할 수 있는 형태로 남기는 것.**

즉, 이 저장소는
`바이브코딩을 하되 멱등성과 지속 유지 가능성을 잃지 않기 위한 하네스 기반 애자일 운영체계`
를 제공한다.
