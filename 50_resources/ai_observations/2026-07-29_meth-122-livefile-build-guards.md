---
session_id: 2026-07-29_meth-122-livefile-build-guards
authored_by:
  agent: "claude-fable-5"
  tool: "claude-code-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: feature
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction: []
prompt_patterns: []
---

METH-122 구현 — rotate 명령(라이브 파일 기계 회전·아카이브 이관), wrap 경성 한도 fail-closed(규정 2배·rotate 탈출구), boot 신선도 경고(HANDOFF·wrap 7일 stale), ship build dev 서버 차단+build-guard.sh(shared). tests 6종+회귀 44종 통과, E2E(rotate no-op·가드 차단 시뮬) 확인.
