---
session_id: 2026-05-18_meth-018-hooks-stale-reinstall
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
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

METH-018 점검 중 발견: 4 프로젝트 pre-push hook 이 활성이나 구버전(v3.x) 템플릿 — 50_tools 만 검사해 v4.0 에선 항상 검증 skip = 안전망 무력화. hooks install --force 로 4개 재설치 → 3-tier 경로탐지+ship-skip+METH-022 sync면제 반영, 4개 검증 통과. git 공용 .git/hooks 라 repo당 1회면 worktree 커버. TODO 의 미설치 프레이밍 정정.
