# 50_resources — 재사용 자원 (Reusable Resources)

## 구성

- `templates/` — 풀 템플릿 (`methodology.py init`이 새 프로젝트로 복사하는 원본)
  - `MASTER_PLAN.md` — 18번 풀 템플릿 (40_dev/MASTER_PLAN.md는 v0 스켈레톤)
  - `SPRINTS.md` — 풀 템플릿
  - `TODO.md` — 5섹션 칸반 헤더 포함
  - `HANDOFF.md` — 라이브 상태 템플릿
  - `ADR-template.md`
- `prompts/` — 스냅샷 생성 프롬프트
  - `business-plan.md`, `service-spec.md`, `architecture.md`, `api-spec.md`, `data-model.md`
- `onboarding/` — 사람이 바로 읽는 시작 자료
  - `HOW_TO_APPLY.md` — 적용 절차
  - `KICKOFF_PROMPT.md` — 첫 세션 시작 프롬프트
  - `DIAGRAM.md` — 핵심 워크플로 다이어그램

## 사용

새 스냅샷이 필요할 때 `50_resources/prompts/<type>.md`의 지시문을 AI에 전달한다.
산출물은 `40_dev/snapshots/<type>-YYYY-MM-DD.md`에 떨어진다.
