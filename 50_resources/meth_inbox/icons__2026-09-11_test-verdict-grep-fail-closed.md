---
id: icons__2026-09-11_test-verdict-grep-fail-closed
origin_repo: icons
type: tool-change
target: "tool/ship"
refs:
  - "https://github.com/icons-hq/icons/pull/926"
  - "https://github.com/icons-hq/icons/pull/931"
friction_ref: null
created: 2026-09-11T03:21:56Z
---

## 제안
ship/land 체인에서 테스트 결과를 grep 통과·실패 로 판정하면 실패 문자열도 매치돼 빨간 테스트가 통과로 넘어간다(실사고: 버튼 등록부 미분류 상태로 머지). 판정은 성공 토큰만(^통과) 보고 실패 시 체인 정지. ship 이 test 스크립트 exit code 를 직접 읽게 하면 근본 해결.

## 근거
- 2026-09-09 test:button-grammar 실패 상태로 #926 머지 → #931 로 복구

