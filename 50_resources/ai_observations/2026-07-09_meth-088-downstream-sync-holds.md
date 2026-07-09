---
session_id: 2026-07-09_meth-088-downstream-sync-holds
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
    where: "sync 결과 검증 시 git ls-tree가 한글 파일경로를 octal-escape → grep이 커스텀 guide 못 찾아 '데이터 손실' 오탐 발생"
    cost_minutes: 8
    resolution: "git -c core.quotepath=false 로 UTF-8 출력 강제 후 재확인; 한글 경로 검증엔 항상 quotepath=false"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

다운스트림 sync 홀드 3곳 완료. 사용자 dirty 해소 확인 후 ai-icons·cafe24-renewal·icons-invest 086까지 sync. (feature면)main 전환→sync --apply→stale SPRINTS.md rm→--no-verify commit→push→복귀. origin/main 검증: SPRINTS 제거·WIP 린트·대시보드 정리 반영, 커스텀 guide 전부 보존(데이터 손실 0). METH-087+이번=관리 다운스트림 6곳 전부 086. 잔여: ai-icons/icons-invest guide 번호 충돌(sync와 직교, 각 repo remediation).
