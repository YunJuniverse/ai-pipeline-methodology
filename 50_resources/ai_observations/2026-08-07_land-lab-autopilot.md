---
session_id: 2026-08-07_land-lab-autopilot
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
prompt_patterns: []
prompting:
  rounds_total: 3
  exchanges:
    - intent: "자율 범위 확장 3건 동시 요청"
      rounds: 3
      vague: "'경영상의 제약이 프로토타입과 서비스를 자유롭게 개발하는데 제약이 걸리는경우가 많이 생겨. god모드 또는 자율 실험모드 같은 맥락을 주입해서 제약 없이 개발 가능하도록'"
      correction: "제약의 정체를 먼저 지목하면 설계가 바로 나온다 — '프로토타입에서 Class B/C 게이트(스키마·인증·가격)가 걸려 멈춘다. 실데이터·실사용자·실결제 없는 범위에서는 게이트를 유예하고 운영으로 올릴 때 정산하는 모드를 만들어줘'"
      terms:
        - "샌드박스 경계·졸업 게이트·Class 유예"
      situation: governance-change-request
---

자율 범위 확장 3종: land 명령(Class A+CI green fail-closed 6단계 자동 착지), 지침 28 실험 모드(샌드박스 4조건+졸업 게이트 7항), 지침 29 자율주행(시간→사이클 환산·4단계 루프·정지 7종). 근거 ADR-004.
