---
session_id: 2026-07-10_meth-106-downstream-sync
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
    where: "다운스트림 sync 커밋 시 git add -A 가 icons-invest 미커밋 프로젝트 WIP(30_planning 사업기획서 3줄)를 methodology-sync 커밋에 쓸어담음 — 초기 dirty=0였으나 sync 시점엔 WIP 존재"
    cost_minutes: 10
    resolution: "sync 커밋은 add -A 대신 방법론 shared 경로만 타깃 스테이징하거나 sync 직전 clean 재확인"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

다운스트림 5곳(icons-invest·cafe24·gamblescan·icons·tshome) v4.0 sync — 092~105 전파(boot·standing SOP·브리프 자동분류·템플릿12/지침 심화·graph·v3.2). feature 브랜치 4곳은 main 체크아웃 후 sync·복원. ai-icons·talmo(더티·타세션) 제외. 다운스트림 커스텀 guide 90/91 등 --prune 없이 보존.
