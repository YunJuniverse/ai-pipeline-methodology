---
session_id: 2026-09-15_readme-changelog-order-repair
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
    where: "20_guides/README.md 변경이력 순서"
    cost_minutes: 10
    resolution: "행 앞 끼워넣기 편집이 세 번 누적돼 역순 — 표 전체 재정렬. 순서가 의미인 표는 정렬 검증 필요"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 1
---

README 변경이력 표가 3세션 누적 «행 앞 끼워넣기» 편집으로 v4.7·4.6·4.5·4.4 역순 오염 — 오름차순 복구 + v4.8. 열 수 검증은 순서 오류를 못 잡는다.
