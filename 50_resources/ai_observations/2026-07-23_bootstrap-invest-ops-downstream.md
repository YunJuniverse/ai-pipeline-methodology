---
session_id: 2026-07-23_bootstrap-invest-ops-downstream
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: bootstrap
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction:
  - id: F-001
    where: "init 스캐폴드 HANDOFF"
    cost_minutes: 5
    resolution: "'- Working on:' 비볼드가 boot 파서 기대와 불일치 → invest-ops 볼드 수정 + Open Issue + 태스크 칩"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

invest-ops(민법상 투자조합 운영 repo)를 12번째 관리 다운스트림으로 신규 부트스트랩 — planning-only 주입, 딜 분석 SOP·deal-memo 템플릿·ADR-0001(스코프·Class C), 소스 HANDOFF 11→12곳 정합화
