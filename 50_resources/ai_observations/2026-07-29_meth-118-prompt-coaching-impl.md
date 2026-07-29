---
session_id: 2026-07-29_meth-118-prompt-coaching-impl
authored_by:
  agent: "claude-fable-5"
  tool: "claude-code-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: feature
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction: []
prompt_patterns: []
prompting:
  rounds_total: 22
  exchanges:
    - intent: "프롬프팅 코칭 요구사항 전달"
      rounds: 2
      vague: "뒷단에서 알아서 자동으로 판단한뒤 리포트를 업데이트"
      correction: "자동의 3요소를 지정하면 1라운드 확정 — 기록 시점(wrap)·판단 주체(세션 AI)·갱신 트리거(wrap 자동). 예: '매 세션 종료 때 자동 기록하고 리포트 갱신해줘'"
      terms:
        - "온디맨드"
        - "프록시"
      situation: automation-request
    - intent: "트리아지 용어 확인"
      rounds: 1
      terms:
        - "트리아지"
      situation: term-clarification
---

METH-118 구현 — observe prompting 블록(rounds-total 상시·교환별 발췌+교정안·200자 가드)·prompt-report(wrap 자동 재생성)·boot 헤드라인·ship sensitive 관찰로그 확장. tests 7종+회귀 51종.
