---
session_id: 2026-08-22_guide-22-v4-propagation
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
    where: "sync-all 상태표의 branch/dirty 는 스캔 시점 스냅샷인데 커밋·푸시까지 시차가 있어, 활성 세션이 있는 repo 는 그 사이 브랜치가 바뀐다 — icons 에서 sync 커밋이 피처 브랜치로 유입돼 무관 PR squash 에 섞임(METH-137 의 착수 전 상태 재확인 교훈 재발)"
    cost_minutes: 20
    resolution: "repo 별 push 직전 rev-parse --abbrev-ref HEAD 재확인 후 push origin main(HEAD 금지). 활성 세션 repo 는 임시 worktree 로 main 만 조작(METH-115 패턴)"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 3
---

지침 22 v4 + README 정합을 다운스트림 8곳에 sync-all 전파 — 처리 7·skip 1(cafe24-renewal 진행중 작업 7건 보호). origin 실내용 대조(블롭 grep) 6/6 통과. icons 에서 사고 1건: sync-all 상태표는 main 으로 찍혔으나 커밋·푸시 시점에 다른 세션이 피처 브랜치로 전환한 뒤였고, push origin HEAD 가 sync 커밋을 그 브랜치에 올림. 이후 그 세션이 브랜치 위에 작업을 쌓아 PR #386 squash 로 머지 — 내용은 icons main 에 정상 도착했으나 전용 sync 커밋이 아니라 무관한 문서 PR 에 딸려 들어간 이력 오염. 사용자 판단으로 그대로 둠. ai-icons 는 원격이 icons-hq 로 이전돼 리다이렉트로 push 성공(URL 갱신 필요).
