# 50_resources — 재사용 자원 (Reusable Resources)

## 구성

- `templates/` — 풀 템플릿 (`methodology.py init`이 새 프로젝트로 복사하는 원본)
  - `MASTER_PLAN.md` — 18번 풀 템플릿 (40_dev/MASTER_PLAN.md는 v0 스켈레톤)
  - `SPRINTS.md` — 풀 템플릿
  - `TODO.md` — 5섹션 칸반 헤더 포함
  - `HANDOFF.md` — 라이브 상태 템플릿
  - `ADR-template.md`
- `prompts/` — AI 실행 프롬프트 (기획서 생성 + 개발 전환 + 코드 기반 스냅샷). 인덱스: `prompts/_README.md`
  - 기획서(→`30_planning/` 라이브): `plan-routing`·`business-plan`·`service-plan`·`ops-plan`·`marketing-plan`·`brand-plan`·`pm-plan`·`ai-feature`·`eval-guardrail`·`re-plan`·`plan`
  - 개발·스냅샷: `dev-spec`·`architecture`·`data-model`·`api-spec`·`service-spec`
- `onboarding/` — 사람이 바로 읽는 시작 자료
  - `HOW_TO_APPLY.md` — 적용 절차
  - `KICKOFF_PROMPT.md` — 첫 세션 시작 프롬프트
  - `DIAGRAM.md` — 핵심 워크플로 다이어그램

## 사용

`50_resources/prompts/<type>.md`의 지시문을 AI에 전달한다.
- 기획서 생성 프롬프트 → 산출물은 `30_planning/NN_*.md`(라이브, in-place).
- 코드 기반 스냅샷 프롬프트 → 산출물은 `40_dev/snapshots/<type>-YYYY-MM-DD.md`(비-라이브).
- 어떤 프롬프트가 어느 지침·모드와 짝인지는 `prompts/_README.md` 참조.
