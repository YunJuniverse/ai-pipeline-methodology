---
session_id: 2026-07-09_meth-087-downstream-sync-086
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
    where: "sync가 상류에서 삭제된 파일을 다운스트림에서 auto-prune 안 함(--prune은 고유 파일도 삭제해 부적합) — 티어/파일 폐지 전파 시 repo마다 수동 git rm 필요"
    cost_minutes: 10
    resolution: "repo별 stale 파일(SPRINTS.md 등) 목록화 후 수동 git rm; 향후 sync에 상류-삭제분 선별 prune 옵션 검토"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

누적 다운스트림 sync 073~086. clean+관리(.methodology-version 보유) 다운스트림 gamblescan·icons·tshome에 상류 누적분(072→086) 전파. repo당 main 전환→sync --apply(shared_paths)→stale SPRINTS.md 수동 rm→--no-verify commit→push→원브랜치 복귀. origin/main 트리 검증 통과(SPRINTS 제거·WIP 린트·대시보드 sprint 정리, 고유 파일 보존). 홀드 dirty 3곳(ai-icons·cafe24·icons-invest)은 clean 후. ver 없는 4곳 제외.
