---
session_id: 2026-05-15_observation-lint-policy-realignment
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
  - intent: "정책-현실 정렬"
    success: true
    rounds: 2
---

validator 의 본문 1단락 ≤ 220자 정책이 실제 multi-section markdown 사용과 어긋남. body markdown 자유화 + 5개 진짜 위반 fix. 18→0.
