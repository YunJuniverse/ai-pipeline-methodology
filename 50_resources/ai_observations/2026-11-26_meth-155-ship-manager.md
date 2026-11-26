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
  - id: F-002
    where: "휴면 repo 2곳 CI 가 옛 관찰 로그 repeat_of 형식 위반으로 9월부터 실패"
    cost_minutes: 20
    resolution: "값을 null 로, 원문은 resolution 으로 이동"
    repeat_of: null
    phase: deploy
  - id: F-003
    where: "다운스트림 목록이 디스크 스캔이라 원격 없는 repo 를 뺄 수단이 없음"
    cost_minutes: 15
    resolution: "버전 파일 retired 표시 도입"
    repeat_of: null
    phase: fix
prompt_patterns:
  - intent: "버그 신고 → 상류 수정"
    success: true
    rounds: 2
  - intent: "휴면 전파·퇴역 처리"
    success: true
    rounds: 3
prompting:
  rounds_total: 11
---

PR #191 머지와 브랜치 정리 뒤, 다운스트림이 신고한 ship 버그(manager 미정의)를 고쳐 활동 7곳과 원격 있는 휴면 5곳에 전파했다. 휴면 2곳은 옛 관찰 로그 형식 위반으로 CI 가 계속 실패하고 있어 로그를 고쳤고, 원격이 사라진 2곳은 버전 파일 retired 표시로 목록에서 뺐다.
