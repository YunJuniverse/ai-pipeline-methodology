---
id: icons__2026-08-22_rotate-assumes-sorted-done
origin_repo: icons
type: tool-change
target: "tool/rotate"
refs:
  - "b499e01"
  - "https://github.com/icons-hq/icons/pull/382"
  - "60_tools/methodology.py"
friction_ref: 2026-08-22_todo-done-rotation
created: 2026-08-22T13:21:35Z
---

## 제안
rotate의 _rotate_todo_done()이 items[:keep]로 «문서 상위 N건»을 남기며 최신-우선 정렬을 가정만 하고 검증하지 않는다. 실제 TODO Done이 미정렬이면 최신 항목이 조용히 아카이브된다. rotate가 날짜 기준 정렬을 스스로 수행하거나, 미정렬 감지 시 경고·중단하도록 제안한다.

## 근거
- items[:keep] 는 문서 순서 상위 N건 — docstring은 '최신 keep건'이라 주장하나 정렬 보장 없음
- icons TODO Done 실측: 문서 5번이 2026-08-18, 3·4번이 2026-08-14 — 그대로 실행 시 최신 항목이 아카이브 대상

