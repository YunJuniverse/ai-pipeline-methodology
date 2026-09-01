---
session_id: 2026-09-01_class-trigger-asset-exclusion
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
    where: "60_tools/methodology.py"
    cost_minutes: 20
    resolution: "하류 병렬 패치 3건이 전부 sync 대상 파일에 있어 상류 미반영 시 되돌아갈 상태였다 — 전수 확인 후 일괄 역주입"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 5
---

Class B/C 경로 트리거에서 표현용 자산 제외를 상류 역주입. 문서 확장자는 의도적 유지(법무·과금 미탐 방지). icons 인증 적중 25→9건.
