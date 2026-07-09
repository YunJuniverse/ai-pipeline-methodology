---
session_id: 2026-07-09_meth-099-graph-nodes
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
    where: "stacked-PR을 순차 머지했으나 GitHub 재타깃 미작동으로 #85/#86/#87이 main 아닌 중간 브랜치에 머지돼 096~098이 main 미반영"
    cost_minutes: 15
    resolution: "095-098 온전 보존된 최상위 스택 브랜치 기준으로 신작업 브랜치를 잡아 base=main 단일 PR로 한 번에 복구"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

methodology-graph.json 노드 29→42 보강(guide 02·03·05·06·07·08·09·19·20·21 + 학습루프 observations/catalog/skeletons + checkpoint), stale ai-log 제거, 엣지 39→53, tier6·learning kind, v3.2. dashboard 렌더 검증. 스택-PR 함정으로 main 미반영이던 096~098도 단일 base=main PR로 복구.
