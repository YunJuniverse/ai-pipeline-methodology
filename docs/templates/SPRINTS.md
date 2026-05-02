# SPRINTS.md

> 스프린트 타임라인의 단일 출처. 대시보드(`generate-dashboard.py`)가 이 파일을 파싱해 주/월/연 뷰를 렌더링한다.
> 각 스프린트는 `### S-NNN` 헤더로 시작하고, 아래 메타 필드를 그대로 유지한다.
> 완료된 스프린트는 지우지 말고 `status: done`으로 두면 연간 뷰에서 회고 자료가 된다.

---

## 연간 목표 (선택)

- **2026 H1**: [예: AI 기능 정식 출시, eval 인프라 표준화]
- **2026 H2**: [예: 다국어 지원, 운영 자동화]

---

## Sprints

### S-001
- **title**: [짧은 제목]
- **start**: 2026-05-04
- **end**: 2026-05-17
- **cadence**: weekly | biweekly | monthly
- **status**: planned | active | done | cancelled
- **owner**: Human / AI / Human + AI
- **goals**:
  - [ ] [목표 1]
  - [ ] [목표 2]
- **todo-ids**: [TODO.md의 ID 나열, 예: PROJ-001, PROJ-002]
- **gate**: [해당 스프린트 종료 시 통과해야 하는 휴먼 게이트, 예: "Dev Spec → Build"]
- **notes**: [선택 - 회고 또는 컨텍스트]

### S-002
- **title**: [짧은 제목]
- **start**: 2026-05-18
- **end**: 2026-05-31
- **cadence**: biweekly
- **status**: planned
- **owner**: AI
- **goals**:
  - [ ] [목표 1]
- **todo-ids**: []
- **gate**: —
- **notes**:

---

## 변경 이력

- 2026-05-03: 초기 템플릿 생성
