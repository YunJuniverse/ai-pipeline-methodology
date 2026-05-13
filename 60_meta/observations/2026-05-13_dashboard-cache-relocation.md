---
session_id: 2026-05-13_dashboard-cache-relocation
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: bugfix
stack_used:
  - python3
flow_used: ad-hoc
friction:
  - id: F-001
    where: "사용자가 프로젝트 루트의 dashboard.html 을 직접 더블클릭 → file:// 로 열림 → 정적·반쪽 작동 (fetch 차단). 휴먼에러 가능성 명백."
    cost_minutes: 0
    resolution: "cmd_dashboard 기본 out_path 를 target/dashboard.html 에서 _start/.cache/dashboard.html 로 변경. _start/ 미존재 환경은 fallback. .cache/ 는 Finder 기본 숨김(.접두) + .gitignore 등록 → 사용자가 *볼 가능성 자체 차단*. SimpleHTTPRequestHandler 의 path traversal 차단으로 .cache 밖 접근 불가."
    repeat_of: null
  - id: F-002
    where: "기존 적용 프로젝트(icons/gamblescan/talmocom)에 옛 루트 dashboard.html 잔존 가능성 — sync 만으로는 자동 제거 안 됨 (F-005 패턴)"
    cost_minutes: 0
    resolution: "cmd_dashboard 가 다음 호출 시 legacy.unlink() 자동 실행 — 첫 .app 더블클릭으로 자가 정리. 다만 *그 사이* 사용자가 옛 dashboard.html 더블클릭하면 정적 페이지 봄. 다음 dashboard 호출 시 깨끗."
    repeat_of: "F-005 (2026-05-13_dashboard-port-conflict-fix)"
prompt_patterns:
  - intent: "사용자 휴먼에러 우려 → 진입점 분리 (정적 file 노출 0)"
    success: true
    rounds: 1
---

dashboard.html 빌드 위치 _start/.cache/ 로 격리 — *사용자가 직접 더블클릭 가능한 정적 파일 0개* 달성. file:// 진입 불가능. F-002 재발("CLI fix 가 적용 프로젝트에 즉시 안 닿음") — 다만 cmd_dashboard 가 다음 호출 시 자가 정리하므로 부작용 미미. METH-020 MC-002 승급 *6회째 목격* — 패턴 확정.
