---
session_id: 2026-05-17_qa4-dashboard-layout-helper
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: refactor
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction: []
prompt_patterns:
  - intent: "layout 정합성 완성"
    success: true
    rounds: 2
---

generate-dashboard.py standalone 이라 methodology_layout import 불가. 자체 dash_layout + resolve_methodology_py 헬퍼로 12곳 NN_ 하드코딩 전환. v3.2/v4.0 양쪽 정확.
