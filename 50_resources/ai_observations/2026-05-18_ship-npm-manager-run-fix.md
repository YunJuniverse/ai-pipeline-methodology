---
session_id: 2026-05-18_ship-npm-manager-run-fix
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

cmd_ship test/build 단계가 [manager,'<script>'] 호출 — pnpm/yarn 은 bare→run alias 하나 npm 내장 단축어는 test/start/stop/restart 뿐이라 npm build 실패(talmocom). 두 호출을 [manager,'run','<script>']로 통일. methodology.py 는 shared_paths 정본이라 upstream 수정→다운스트림 sync 수령. py_compile 통과, Class A.
