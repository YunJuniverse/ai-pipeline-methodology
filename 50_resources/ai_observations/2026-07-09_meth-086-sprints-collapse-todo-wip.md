---
session_id: 2026-07-09_meth-086-sprints-collapse-todo-wip
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
friction:
  - id: F-001
    where: "대시보드(generate-dashboard.py) sprint 결합이 15+ JS 사이트에 산재 — 티어 제거 시 데이터+UI+호출부 모두 추적 필요"
    cost_minutes: 25
    resolution: "Python 데이터부터 제거 후 grep로 잔여 UI 사이트 열거·호출부까지 제거·생성 HTML grep으로 런타임 참조 0 검증"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

SPRINTS 완전 붕괴(2층화)+TODO WIP 캡. 웹리서치 2건: TODO=베스트프랙티스 부합(무변경), SPRINTS=잉여 중간층+명칭 모순(기간 고정 안 함·velocity가 METH-076 flow와 충돌). 3층(페이즈→스프린트→TODO)→2층(페이즈→TODO): cadence=flow 메트릭, 그룹핑=TODO milestone 태그, 게이트=페이즈. guide02(§3 삭제·재번호)·guide18(§14.5·§10.2)·_CATALOG·TODO템플릿·graph.json(sprints 노드/엣지)·대시보드(Timeline탭·gantt·sprint모달 제거,hero→phase,WIP 타일)·mention 스윕·SPRINTS.md 2개 삭제·wrap WIP≤3 린트. 대시보드 렌더+compile 통과.
