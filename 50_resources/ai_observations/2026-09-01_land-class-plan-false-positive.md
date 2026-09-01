---
session_id: 2026-09-01_land-class-plan-false-positive
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
    where: "60_tools/methodology.py:1604"
    cost_minutes: 25
    resolution: "앱 디렉터리 전체가 영구 Class B 라 자동 머지 불가. 테스트 선행으로 오탐 재현 후 plan 만 분리해 경계 축소. 감수한 미탐(복합어)도 테스트로 박제"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 2
---

land Class 스캐너 과금 트리거의 plan 대안이 plan-viewer 를 오판. 경계를 [./_-]→[./] 로 축소하고 회귀 테스트 6케이스 신설. 실사고 diff 재판정 Class A 확인.
