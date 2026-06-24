---
session_id: 2026-06-24_meth-046-sync-no-mirror-delete
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
friction: []
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

sync가 shared 디렉터리를 mirror하며 상류에 없는 다운스트림 고유 파일(ai-icons 20_guides/04)을 조용히 삭제하던 데이터손실 버그 픽스. copy_path에 prune_report 추가(후보 보고만), cmd_sync prune을 --prune opt-in으로(기본 보존+경고, --prune시 삭제목록), sync --prune 플래그+worktree 전파. ai-icons dry-run 검증, init 무영향.
