---
session_id: 2026-09-21_adr-citation-cross-repo-false-warn
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
    where: "wrap ADR 인용 검사"
    cost_minutes: 10
    resolution: "공유 지침이 하류 사고 사례로 icons ADR 번호를 인용해 전 repo 에서 없는 ADR 로 경고될 구조 — repo 한정 표기 규칙+regex 예외"
    repeat_of: null
    phase: verify
prompt_patterns: []
prompting:
  rounds_total: 3
---

METH-147 ADR 인용 검사가 공유 지침의 타 repo ADR 사례 인용을 오경고 — <repo>:ADR-NNNN 표기 규칙과 검사기 예외로 해소. 공유 문서라 11 repo 전부에 뜰 오경고였다.
