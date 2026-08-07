---
session_id: 2026-08-07_mode-keyword-routing
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
    where: "새 지침을 만들었지만 로딩 트리거를 안 만듦"
    cost_minutes: 12
    resolution: "지침 28·29 신설 시 CLAUDE.md 요약과 guides README 등록은 했으나, 지침 01 라우팅 표에는 기획서(5.9)·작업모드(5.10) 축만 있고 운영 모드 축이 없어 키워드로 본문이 로드되지 않았다. 사용자 질문으로 발각 — 규칙 문서 신설 시 '어떤 입력에서 이 문서가 로드되는가'를 함께 정의해야 한다"
    repeat_of: null
prompt_patterns: []
prompting:
  rounds_total: 4
---

METH-136: 지침 28·29를 키워드로 불러오는 경로 연결. 지침 01 §5.11 운영 모드 라우팅 표 신설, CLAUDE/AGENTS §2를 서술에서 동작 지시로 전환. 속도 요구만으로 실험 모드가 켜지지 않도록 샌드박스 4조건 확인을 선행 조건화.
