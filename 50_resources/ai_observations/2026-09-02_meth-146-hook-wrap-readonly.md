---
session_id: 2026-09-02_meth-146-hook-wrap-readonly
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
prompt_patterns: []
prompting:
  rounds_total: 1
---

pre-push 훅의 wrap 을 --read-only 로 — 리포트 재생성·wrap-state 부트스트랩이 repo 를 dirty 로 만들어 sync-all 이 skip 하던 부작용 제거. 대조군/실험군·실 push·단위 3테스트, 91/91.
