---
session_id: 2026-09-01_capsule-repo-name-worktree
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
    where: "60_tools/methodology.py:_repo_name"
    cost_minutes: 20
    resolution: "하류가 먼저 고친 sync 대상 파일을 상류에 올리지 않으면 다음 sync 에 덮여 되돌아온다. 하류 수정 발견 시 상류 반영 동반 확인 필요"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 3
---

캡슐 origin_repo 가 워크트리명으로 갈라져 상류 중복 수거되던 것을 _repo_name 의 git-common-dir 환원으로 해소. 하류 icons#668 을 상류로 역주입.
