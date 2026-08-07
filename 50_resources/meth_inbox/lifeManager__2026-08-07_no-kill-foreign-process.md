---
id: lifeManager__2026-08-07_no-kill-foreign-process
origin_repo: lifeManager
type: guide-update
target: "guide-07"
refs:
  - "40_dev/snapshots/2026-08-06_recurring-backlink-pending.md"
  - ".ai/checkpoint.md"
friction_ref: 2026-08-06_todo-ms-style
created: 2026-08-07T00:31:40Z
---

## 제안
AI가 만들지 않은 프로세스·포트를 죽이지 않는다는 규칙을 자율진행 정지조건에 추가 제안. 이번 세션에서 ship 전 '포트 정리'로 lsof -ti:3000 | xargs kill -9 를 실행해 **다른 프로젝트의 dev 서버를 중단**시켰다. 도구(preview_start)가 이미 빈 포트를 자동 배정하므로 정리 자체가 불필요했다. 자율 작업의 부작용은 작업 범위 밖으로 새면 안 된다.

## 근거
- (refs 참조 — 원문 정본은 이 repo)

