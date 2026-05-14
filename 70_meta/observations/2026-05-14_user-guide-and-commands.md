---
session_id: 2026-05-14_user-guide-and-commands
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: docs
stack_used:
  - python3
  - javascript
flow_used: ad-hoc
friction:
  - id: F-001
    where: "WHITEPAPER 는 헌법(추상), ONBOARDING 은 AI 부팅, CLAUDE/AGENTS 는 AI 운영 규칙 — *인간 사용자가 매일 사용하는 명령·워크플로* 단일 매뉴얼 없음"
    cost_minutes: 0
    resolution: "10_foundation/USER_GUIDE.md 신설 — 11개 섹션 (시작·매일·brief·작업·종료·인계·명령·Class·문제해결·다이어그램·참조). 신규 진입점에서 *인간 측*만 한 곳에서 읽고 끝."
    repeat_of: null
  - id: F-002
    where: "자주 사용 명령을 *기억* 하거나 *USER_GUIDE 매번 검색* — UX 비용"
    cost_minutes: 0
    resolution: "60_tools/commands.json 데이터 파일 — 5 카테고리(boot/end/ops/observe/export) × 23 명령. dashboard 가 자동 로드해 Commands 카드로 표시. 클릭 → 클립보드 복사."
    repeat_of: null
  - id: F-003
    where: "USER_GUIDE 와 commands.json 이 *분리*되어 *부패 동기화 비용* — 명령 추가 시 두 파일 갱신"
    cost_minutes: 1
    resolution: "USER_GUIDE §7 Cheatsheet 와 commands.json 정합 유지를 *각 ship 시* 점검. 차후 자동 검증(commands.json 의 각 명령이 USER_GUIDE 에 언급되는지) 가능 — METH 후보."
    repeat_of: null
prompt_patterns:
  - intent: "인간 사용자 매뉴얼 + 머신 읽기 명령 데이터 + 대시보드 표시 — 3축 결합"
    success: true
    rounds: 1
  - intent: "Commands 카드 클릭 → 클립보드 복사 UX (toast 메시지 2.5s)"
    success: true
    rounds: 1
---

USER_GUIDE + commands.json + dashboard Commands 카드 — 인간 워크플로 단일 진입점. 백서 §3-G1 (G1: 누구나 쉽게 학습) 의 구체화. AI 측(CLAUDE/AGENTS), 메타 측(WHITEPAPER), 인간 측(USER_GUIDE) 3축 분리 완성. commands.json 은 카테고리·메타데이터 풍부 — 향후 *프로젝트별 커스텀 명령* 확장 가능 (예: 사용자 추가 alias).
