---
session_id: 2026-05-15_methodology-integrity-3-fixes
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
  - intent: "v3.2/v4.0 구조 차이 중앙화"
    success: true
    rounds: 2
---

구조 탐지 헬퍼·sync worktree·observe CLI 강제 — 같은 root cause 3개를 한 PR 로 묶음. tshome 사고에서 발견된 정합성 누수 차단.
