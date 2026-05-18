---
session_id: 2026-05-18_dashboard-api-servers-start-path-augment
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

dashboard 가 launchd 기본 PATH 로 떠 있으면 /api/servers/start 가 자식에 빈약한 PATH 그대로 전달해 pnpm/npm 못 찾는 마찰. _augmented_path_env() 로 homebrew/local/bun/pnpm/nvm 보강 + shutil.which 사전 해석으로 차단. 비대화형 진입점(.app/.command) 환경의존성 일반 패턴.
