---
session_id: 2026-07-29_sync-propagate-meth-116
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
    where: "다운스트림 pre-push wrap 훅이 상류 sync push 차단"
    cost_minutes: 8
    resolution: "상류 sync 커밋엔 세션 라이브파일 갱신이 없어 wrap --strict fail — 확립 절차대로 --no-verify FF push(merge-base로 원격=조상 확인 후). 근본 해법 후보: 훅이 방법론 경로만 변경된 sync 커밋을 인지해 면제"
    repeat_of: 2026-07-15_ai-icons-talmo-sync
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

지침 22 sync-all 전파 종결 11/11 — main 6곳 직접, 비-main 5곳 임시 worktree(origin/main만 조작), 전부 타깃 스테이징·ls-remote 대조. 스켈레톤은 init 경로라 비전파(설계 정상).
