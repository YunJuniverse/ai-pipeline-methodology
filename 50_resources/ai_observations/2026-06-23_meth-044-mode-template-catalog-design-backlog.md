---
session_id: 2026-06-23_meth-044-mode-template-catalog-design-backlog
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
friction: []
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

사용자 제안: 방법론을 외주/풀스택/기획전용/개발전용 등 작업 용도별로 필요한 템플릿만 쓰게 해야 함. 템플릿 25종으로 불었으나 모드 선택 체계 부재 확인. 6개 모드(planning/dev/fullstack/agency/lean/ops)→세트 매핑 + _CATALOG.md + CLAUDE.md Mode 확장 설계 확정. 폴더 재구성 대신 카탈로그(비파괴적). #31/#32 머지 후 capstone(METH-044)으로 착수 — TODO Backlog에 설계 등록.
