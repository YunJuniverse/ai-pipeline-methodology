---
id: cafe24-renewal__2026-09-14_sequential-id-reservation
origin_repo: cafe24-renewal
type: tool-change
target: "tool/todo"
refs:
  - "40_dev/decisions/2026-08-16_todo-id-collision-registry.md"
  - "20_guides/30_동시_세션_git_격리.md"
friction_ref: 2026-08-31_brand-color-system-section
created: 2026-09-14T07:06:45Z
---

## 제안
병렬 세션이 TODO ID·HANDOFF 차수를 선점해 번호 충돌·커밋 혼입이 반복 — 원자적 ID 예약 명령(예: 즉시 커밋·push 로 번호를 확보하는 reserve) 또는 세션 접미사 ID 발급을 제안(지침 02·30 인접). 현재는 로컬 충돌 대장과 수동 재부여로 사후 처리 중

## 근거
- 병렬 세션 번호 선점 월 3건 이상 — 한 세션에서만 3번째, checkpoint 통째 덮어쓰기 동반
- 타 세션 ship 이 내 미커밋 변경까지 함께 커밋해 커밋 메시지와 내용 불일치

