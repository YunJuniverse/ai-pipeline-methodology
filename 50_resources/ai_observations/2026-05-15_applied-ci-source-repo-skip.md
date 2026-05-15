---
session_id: 2026-05-15_applied-ci-source-repo-skip
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
  - intent: "워크플로 적용 범위 명시"
    success: true
    rounds: 1
---

methodology-applied-ci 가 source 저장소에서 70_meta 누수로 항상 fail. job-level if 로 source repo skip. validate / freshness 두 job 모두.
