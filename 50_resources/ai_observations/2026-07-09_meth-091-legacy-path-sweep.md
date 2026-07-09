---
session_id: 2026-07-09_meth-091-legacy-path-sweep
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

legacy 경로 sweep — 라이브 문서의 pre-v4 경로 참조 점검(90_archive·migrations·시점기록 제외). 실제 stale 3건 발견·수정: 10_foundation/{KICKOFF_PROMPT,DIAGRAM,HOW_TO_APPLY}.md의 docs/snapshots/→40_dev/snapshots/(신규 사용자 오도 제거). 나머지 docs/ 참조는 정당(guide19 gamblescan 인용=실제 위치·api-contract=예시). 부수 발견: v3.2 backward-compat 코드 폴백(40_resources/60_meta/docs)은 7 repo 전부 v4.0이라 dead지만 별건. docs sweep Open Issue Closed.
