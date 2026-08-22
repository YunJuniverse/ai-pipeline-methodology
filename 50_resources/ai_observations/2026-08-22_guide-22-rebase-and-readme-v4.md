---
session_id: 2026-08-22_guide-22-rebase-and-readme-v4
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: docs
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction:
  - id: F-001
    where: "20_guides/README.md 현황표·§3.6 요약이 지침 본문 버전 개정(v2·v3)을 따라가지 못해 3개 릴리스 연속 v1 로 방치"
    cost_minutes: 25
    resolution: "본문 v4 개정 시 README 3곳(§3.6 역할·현황표·변경이력) 동시 정정, 소급분 명시"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 6
---

정련 브랜치(1커밋)를 61커밋 앞선 main 위로 리베이스하며 지침 22 내용 충돌 해소. 브랜치가 v1 기준 §2 전면 재작성이라, 그 사이 main 에 들어온 v2(METH-128)·v3(METH-129)와 정면 충돌 — 한쪽 채택 시 불변규율 4·5 와 P3 리드백 게이트가 조용히 유실되는 구조였다. 6단계 모델은 브랜치 것을 채택하되 v2 규율을 승계해 규율 6개로 통합하고, 리드백 게이트를 신 P4 행으로 이관, 변경이력은 v1~v3 보존 + v4 추가. 라이브 상태 파일(checkpoint·wrap-state)은 나중 것(main)이 정본이라 되감지 않음. 후속으로 20_guides/README.md 현황표가 22 를 v1 로 표기(v2·v3 때도 누락)한 것을 v4 로 소급 정정.
