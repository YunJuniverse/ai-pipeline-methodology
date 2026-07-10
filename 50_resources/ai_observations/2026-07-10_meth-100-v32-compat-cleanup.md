---
session_id: 2026-07-10_meth-100-v32-compat-cleanup
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
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

v3.2 backward-compat 코드 제거 — methodology.py·generate-dashboard.py의 v3.2/v4.0 구조탐지(_LAYOUT_V32·methodology_layout·dash_layout)와 40_resources/60_meta/docs/legacy-root 폴백 삭제→v4.0 고정. migrations 스크립트·런처/훅 부트스트랩 탐지는 보존. py_compile·dashboard 재생성·wrap 검증.
