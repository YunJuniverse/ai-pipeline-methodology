---
session_id: 2026-07-09_meth-070-architecture-refresh
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

아키텍처 문서 심화(문서별 8번, 개발명세 계열 시작). 웹리서치(arc42·C4/Simon Brown·Richards&Ford·ThoughtWorks fitness functions·OWASP·LLM 게이트웨이) → architecture.md 강화(현행 14섹션을 arc42 매핑해 gap 도출). 추가: §2 품질속성 top3(least-worst·측정시나리오), §16 적합성 함수(CI 가드레일, 지침19 연결), §4 C4(Context+Container Mermaid), §6 런타임 뷰, §11 신뢰경계·위협(STRIDE-lite), §14 배포 뷰, §15 AI 아키텍처(게이트웨이·폴백·RAG·가드레일/eval 배치·예산, 조건부), §20 리스크/기술부채 register. risk-driven just-enough + docs-as-AI-context. _CATALOG 갱신. branch-first 준수.
