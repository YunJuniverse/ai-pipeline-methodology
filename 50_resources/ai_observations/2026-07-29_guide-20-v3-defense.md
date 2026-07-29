---
session_id: 2026-07-29_guide-20-v3-defense
authored_by:
  agent: "claude-fable-5"
  tool: "claude-code-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: docs
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction: []
prompt_patterns: []
prompting:
  rounds_total: 3
  exchanges:
    - intent: "반복 디자인 실수 방지책 질의"
      rounds: 2
      vague: "다크모드 배경인데 까만 텍스트·패딩 마진값을 안 줘서 붙어보임"
      correction: "증상 나열이 정확해 1라운드에 진단 가능했음 — 좋은 프롬프트 사례. 더 빠르게는 '구조적으로 못 하게 만들어줘'처럼 원하는 개입 수준(규칙/도구/자동차단)을 함께 지정"
      terms:
        - "가드레일"
        - "fail-closed"
        - "프리미티브"
      situation: design-defect-prevention
---

지침 20 v3 — 사용자 반복 실수(다크 대비·간격 붙음) 3층 방어(절대색 차단·프리미티브 내장 간격·axe/간격 린트) + METH-130(UI repo 6곳 실설치) 등록. #135 cherry-pick 통합(스택-PR 회피).
