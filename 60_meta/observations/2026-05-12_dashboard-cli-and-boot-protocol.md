---
session_id: 2026-05-12_dashboard-cli-and-boot-protocol
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: feature
stack_used:
  - python3
flow_used: ad-hoc
friction:
  - id: F-001
    where: "사용자가 dashboard.html을 *파일 시스템에서 직접* 열면 brunch 표시 부재로 '메인 고정'으로 오해"
    cost_minutes: 1
    resolution: "generate-dashboard.py 빌드 시 git branch/commit을 자동 호출해 HTML 헤더 meta span 에 표시. dashboard는 실제로는 *현재 디렉터리·현재 브랜치* 반영이지만 시각적 단서가 없어 '고정'으로 오인됨."
    repeat_of: null
  - id: F-002
    where: "세션 시작 시 dashboard URL 표시가 비의무 — AI가 깜빡 가능, 사용자가 매번 빌드 명령 검색"
    cost_minutes: 2
    resolution: "CLAUDE.md/AGENTS.md (managed 마커 안) 부팅 절차 마지막 단계로 `methodology dashboard` 호출 의무화. AI가 첫 보고 메시지에 URL을 자동 포함."
    repeat_of: null
  - id: F-003
    where: "포트 충돌·중복 시작 위험 — 사용자가 매 세션마다 새 서버 띄우면 8765 점유 충돌"
    cost_minutes: 1
    resolution: "cmd_dashboard 에 _port_in_use socket 점검. 이미 떠 있으면 새로 시작하지 않고 기존 URL 보고. background 시작 시 start_new_session=True 로 부모 종료에도 서버 유지."
    repeat_of: null
prompt_patterns:
  - intent: "사용자 오해(브랜치 고정)를 진단 → 진짜 통증(stale + visibility) 도출"
    success: true
    rounds: 1
  - intent: "(α) 패턴 정합 — AI 자동 빌드 + URL 보고, 사용자는 클릭만"
    success: true
    rounds: 1
---

dashboard CLI는 *그 자체로* 큰 가치는 없지만 *부팅 절차 의무 호출*과 결합되어야 통증 해소. (α) 패턴: AI가 호출 → 사용자는 URL 클릭만. branch/commit 표시는 file:// 직접 열기 시 *어느 상태를 보고 있는지* 즉시 알게 함. F-002 는 다음 v3.x 마이그레이션 시 같은 *부팅 절차에 새 의무 추가*에서 재발 가능 — MP-NNN 후보. 백서 §0 제0원칙(이식성) 측면에서 dashboard URL은 *어떤 PC/AI에서도 동일 형태*라 적합.
