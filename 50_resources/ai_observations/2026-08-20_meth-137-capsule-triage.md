---
session_id: 2026-08-20_meth-137-capsule-triage
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
    where: "capsule-id-worktree-prefix"
    cost_minutes: 5
    resolution: "gamblescan 캡슐 2건 id가 worktree명(gamblescan-p0-pr) 접두어로 생성돼 collect 형식 경고 — 발신 시점(capsule 명령) id 검증 부재, 후속 후보로 기록"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 3
---

캡슐 3회차 수거 5건 전량 유효 확정·반영 — 지침 05 v3(§9b 작성 규율)·23 v3(§4b 표면 매트릭스), 훅 timeout, land 머지/동기화 분리·squash SHA maincheck, P-002. negative case 증명(land A/B/C·훅 D1~D4).
