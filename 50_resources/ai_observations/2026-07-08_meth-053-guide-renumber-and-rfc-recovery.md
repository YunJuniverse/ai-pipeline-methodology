---
session_id: 2026-07-08_meth-053-guide-renumber-and-rfc-recovery
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
friction: []
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

상류 산출물 채널 분리 지침 04→05 리넘버(다운스트림 커스텀 04 doc_id 충돌 회피) + guide 02 §8 지침번호 예약범위 신설(상류 00-89/다운스트림 90-99). 스택 PR 함정으로 main 미도달·고아화된 RFC-002(METH-052) 복구. 교훈: 스택 PR은 base 먼저 머지 시 stale 브랜치로 머지돼 고아화.
