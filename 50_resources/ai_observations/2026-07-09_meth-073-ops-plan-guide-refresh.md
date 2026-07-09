---
session_id: 2026-07-09_meth-073-ops-plan-guide-refresh
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
friction: []
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

운영기획서 지침(guide 12) 심화 — 기획서 지침군 첫 대상. 웹리서치(Google SRE·PagerDuty/incident.io·ITIL 4·L1/L2/L3·OWASP LLM·LLM 운영) → §6 신규 8항목: §6.15 SLO/Error Budget(소진 시 기능 프리즈), §6.16 형식 인시던트(SEV1-4·IC·MTTD/MTTA/MTTR), §6.17 on-call/에스컬레이션/블레임리스 포스트모템, §6.18 SLO 기반 알림(multi-burn-rate·알림피로), §6.19 계층 지원 L1/L2/L3(SLA·CSAT/CES/FCR), §6.20 변경/릴리스 운영(ITIL·feature flag·롤백), §6.21 Toil 예산, §6.22 AI 프로덕션 운영(프로덕션 eval·가드레일=인시던트·provider failover·HITL·토큰 FinOps). §8·§16·§19.6·README 갱신. branch-first 준수.
