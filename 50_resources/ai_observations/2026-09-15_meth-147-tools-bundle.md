---
session_id: 2026-09-15_meth-147-tools-bundle
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
    where: "ship --land Namespace"
    cost_minutes: 5
    resolution: "land 에 --local-ci 를 추가하며 ship 이 만드는 Namespace 에 local_ci 가 빠져 AttributeError 위험 — grep 'a|b' 식 세로줄 포함 검증도 겸함"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 2
---

METH-147 도구 묶음 — wrap baseline HEAD 재계산(생성물 커밋 중단)·ship 공유 체크아웃 가드·reserve 원자 예약·land DIRTY/스텝0/local-ci·observe 세로줄·boot preflight·ADR 인용 검사. 단위 9 + e2e 3, 96/96.
