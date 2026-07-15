---
session_id: 2026-07-15_sync-all-helper
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: feature
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

METH-107 sync-all: root(기본 ~/) 아래 .methodology-version 보유 프로젝트 자동 발견→사전 스캔 표(버전·브랜치·dirty·behind)→각 cmd_sync 위임→요약. --apply 가드로 dirty·비-main skip(오늘 교훈 박제), --include-dirty/--allow-nonmain override. 의존성 없는 테스트 9개 추가.
