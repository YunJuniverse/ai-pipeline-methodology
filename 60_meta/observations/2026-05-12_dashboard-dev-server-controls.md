---
session_id: 2026-05-12_dashboard-dev-server-controls
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: feature
stack_used:
  - python3
  - http.server
  - javascript
flow_used: ad-hoc
friction:
  - id: F-001
    where: "dashboard 정적 HTML 한계 — 브라우저에서 OS 명령(pnpm dev, kill) 직접 실행 불가"
    cost_minutes: 0
    resolution: "기존 generate-dashboard.py --serve 의 SimpleHTTPRequestHandler 를 BaseHTTPRequestHandler 기반 커스텀 핸들러로 교체. 정적 파일 서빙은 super().do_GET() 유지, /api/servers/* 엔드포인트 4개(GET list, POST start, POST {pid}/stop, POST kill-range) 추가."
    repeat_of: null
  - id: F-002
    where: "포트 자동 할당 — 3000 점유 시 3001..3099 fallback"
    cost_minutes: 1
    resolution: "_find_free_port(start=3000, end=3099) — socket.bind 로 점검. listen 등록 직전 release 하지만 race 가능성 작음 (사용자 환경 1인). Next.js 등은 PORT env 로 받음."
    repeat_of: null
  - id: F-003
    where: "현재 추적 서버 vs 추적 외 서버 구분 — Stop 은 추적 PID만, Kill all 은 포트 범위 전체"
    cost_minutes: 2
    resolution: "_servers dict 로 spawn 된 PID 추적. Stop 은 등록된 PID 만 SIGTERM. Kill-range 는 lsof -ti :PORT -sTCP:LISTEN 으로 점유 PID 발견 후 모두 종료 (추적 외 포함)."
    repeat_of: null
  - id: F-004
    where: "spawn 한 자식 프로세스가 부모(서버) 종료 시 좀비 또는 고아"
    cost_minutes: 1
    resolution: "start_new_session=True 로 새 세션 그룹 생성. 부모 종료해도 자식 유지. Stop 시 os.killpg(getpgid(pid), SIGTERM) 로 세션 전체 종료 — pnpm/node child 프로세스도 함께 정리."
    repeat_of: null
  - id: F-005
    where: "JS UI 와 서버 API 통신 안전성 — 외부 origin 에서 호출 가능성"
    cost_minutes: 1
    resolution: "서버 bind 를 ('', port) 에서 ('127.0.0.1', port) 로 변경 — localhost 외 접근 차단. CORS 헤더 미설정으로 cross-origin fetch 도 차단."
    repeat_of: null
prompt_patterns:
  - intent: "정적 dashboard 한계를 작은 API 서버 추가로 돌파 — 외부 의존성 0"
    success: true
    rounds: 1
  - intent: "Kill all vs Stop 의 의미 분리 (추적 외 vs 추적 PID)"
    success: true
    rounds: 1
  - intent: "포트 자동 할당 + 환경 변수(PORT) 주입으로 Next.js·기타 dev server 호환"
    success: true
    rounds: 1
---

dashboard 의 본질이 *정적 + 인터랙티브*로 진화 — Python http.server 만으로 작은 control plane 구성. 외부 패키지 0개, 보안: localhost-only bind. setInterval 5초 자동 갱신 + 죽은 PID 자동 정리. Kill-range 는 *추적 외 프로세스도* 종료(편의 우선, 위험은 사용자가 confirm). 다음 v3.x 후보: WebSocket 또는 SSE 로 실시간 로그 스트리밍 (현재는 stdout=DEVNULL 로 무시). MP-NNN 후보: F-005(localhost-only bind)는 다른 서버 추가 시 반복될 안전 패턴.
