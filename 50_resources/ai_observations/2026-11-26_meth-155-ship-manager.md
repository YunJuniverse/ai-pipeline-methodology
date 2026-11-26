---
session_id: 2026-11-26_meth-155-ship-manager
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: bugfix
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction:
  - id: F-001
    where: "ship --no-test --no-build 가 tsc 단계에서 NameError"
    cost_minutes: 10
    resolution: "매니저 판정을 단계 밖 헬퍼로 이동, 회귀 테스트 추가"
    repeat_of: null
    phase: fix
prompt_patterns:
  - intent: "버그 신고 → 상류 수정"
    success: true
    rounds: 2
prompting:
  rounds_total: 7
---

PR #191 머지와 머지된 브랜치 정리 뒤, 다운스트림 세션이 신고한 ship 버그를 상류에서 고쳤다. manager 변수를 test·build 블록 안에서만 정해 두 단계를 모두 건너뛰면 tsc 최소 검증이 NameError 로 죽었다. 매니저 판정을 헬퍼로 빼고 npm exec 의 -- 누락도 함께 고쳤다.
