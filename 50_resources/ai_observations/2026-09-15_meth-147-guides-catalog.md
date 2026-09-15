---
session_id: 2026-09-15_meth-147-guides-catalog
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
    where: "README 변경이력 삽입"
    cost_minutes: 5
    resolution: "정규식 first-match 가 표 첫 행(v4.1) 앞에 끼워 v4.2 로 오기입 — 마지막 행 기준으로 재삽입. 표 구조 검증은 열 수만 봐서 못 잡는다(순서 오류)"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 1
---

METH-147 지침·catalog — 05 v5·19 v5·23 v5·24 v4·30 v3, CLAUDE Blocked 중복 grep·reserve, C-002 승급(교차 N≥2)·P-006~008. README 변경이력 정규식 first-match 함정 발견·수정.
