---
session_id: 2026-05-17_sync-worktree-stale-guard
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
  - intent: "전파 안전성 가드"
    success: true
    rounds: 2
---

sync --include-worktrees 가 stale v3.1 worktree 8개에 풀 마이그레이션 churn 무차별 적용. dirty/마이그레이션 유발 worktree skip 가드 + force escape hatch 추가.
