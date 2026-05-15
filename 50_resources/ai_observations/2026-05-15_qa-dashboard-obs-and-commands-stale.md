---
session_id: 2026-05-15_qa-dashboard-obs-and-commands-stale
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
friction: []
prompt_patterns:
  - intent: "정합성 회복"
    success: true
    rounds: 1
---

정합성 QA 18 카테고리 점검 후 우선순위 1·2 묶음 fix. dashboard 가 70_meta/observations 의 20건 누락하던 버그 + commands.json 의 v3.2 명명 잔재 정리.
