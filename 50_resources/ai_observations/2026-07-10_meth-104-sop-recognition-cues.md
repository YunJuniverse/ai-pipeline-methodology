---
session_id: 2026-07-10_meth-104-sop-recognition-cues
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
friction: []
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

SOP 템플릿 트리거에 '인식 신호'(어떤 요청/말이 이 작업을 의미하는가) 항목 추가 — 반복작업 매칭이 LLM 의미추론이라 이 앵커로 신뢰도↑. SOP_template 트리거=인식신호+주기/이벤트 분리, _README §standing 반영.
