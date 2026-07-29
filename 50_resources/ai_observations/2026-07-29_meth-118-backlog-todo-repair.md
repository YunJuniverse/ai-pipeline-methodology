---
session_id: 2026-07-29_meth-118-backlog-todo-repair
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
friction:
  - id: F-001
    where: "TODO 섹션 이동 스크립트의 문자열 index() 오매칭"
    cost_minutes: 15
    resolution: "index('## Blocked')가 6행 안내문 속 백틱 문자열에 먼저 걸려 섹션 중복+Done 헤딩 유실, #117로 머지됨. 정본 재작성 복구·칸반 5헤더 검증. 교훈: 라이브 파일 섹션 조작은 ^## 행 시작 앵커 정규식 필수"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

METH-118 프롬프팅 코칭 루프 백로그 등록(상시 자동 기록+prompt-report 자동 갱신, 토큰 v1 프록시·원문 저장 금지·교차-repo v1 제외) + #117 혼입 TODO 손상 정본 복구.
