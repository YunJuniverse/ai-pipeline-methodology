---
session_id: 2026-07-15_graph-viz-generator
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
friction:
  - id: F-001
    where: "browser preview"
    cost_minutes: 10
    resolution: "Claude_Browser 스크린샷이 다크 배경+와이드 SVG에서 빈 화면 반복→javascript_tool로 DOM 직접 조회해 렌더 검증(노드수·좌표·fill·클릭)"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

METH-108 generate-graph-viz.py: methodology-graph.json(정본 42/53)을 문서역할 지식그래프 HTML로 자동 렌더. 하드코딩 아티팩트(v3.1 30/41)가 그래프 변경마다 드리프트하던 문제 해결. 노드 좌표=category열/guides tier분할 결정적 배치, 엣지 primary(실선)/보조(점선) 분류, 라이프사이클·상세패널 상호작용. 테스트 8개. 브라우저 DOM 검증(42/53·클릭 동작).
