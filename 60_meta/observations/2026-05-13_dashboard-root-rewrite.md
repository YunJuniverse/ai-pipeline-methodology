---
session_id: 2026-05-13_dashboard-root-rewrite
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
    where: "http://localhost:8765/ 가 'Directory listing for /' 페이지로 랜딩 — SimpleHTTPRequestHandler 기본 동작 (index.html 미존재 시 listing 노출). 사용자 의도(dashboard.html 직접 표시) 미충족."
    cost_minutes: 0
    resolution: "do_GET 시작에서 self.path == '/' 면 '/dashboard.html' 로 rewrite. urllib.parse 가 쿼리스트링 분리하므로 self.path 직접 비교(parsed 변환 전)."
    repeat_of: null
  - id: F-002
    where: "초기 시도에서 self.path = f'/{out.name}' (closure 캡처) → HTTP 000 (서버 응답 없음). 원인은 closure 가 아니라 *옛 background server 가 새 코드 반영 안 됨*인데 진단 헷갈림."
    cost_minutes: 6
    resolution: "(1) 명시 하드코딩 '/dashboard.html' 로 단순화 (closure 의심 회피), (2) 서버 강제 kill -9 후 재시작. methodology dashboard 가 daemon 으로 떠 있어 일반 stop 후에도 코드 reload 안 됨 — *서버 재시작 시 항상 새 process spawn 됨* 이라 정상 동작인데, 빌드 산출물 캐시가 의심돼 진단 지연."
    repeat_of: null
  - id: F-003
    where: "사용자 진입점 표기 'http://localhost:8765' 가 *루트* 라 directory listing — `/dashboard.html` 명시 안 함"
    cost_minutes: 0
    resolution: "rewrite 로 *둘 다 동일 결과* 보장. methodology dashboard 출력 메시지의 URL 도 그대로 'http://localhost:8765' 유지 OK."
    repeat_of: null
prompt_patterns:
  - intent: "사용자 증상 → 원인(SimpleHTTPRequestHandler 기본 동작) 즉시 추론"
    success: true
    rounds: 1
  - intent: "디버깅 중 닫힌 가설(closure 캡처) → 진짜 원인(서버 재시작 누락) 발견"
    success: false
    rounds: 2
---

do_GET 첫 줄 rewrite 로 사용자 경험 통일 — / 또는 /dashboard.html 둘 다 동일. F-002 의 *서버 재시작 시점 혼동* 은 *AI 가 백그라운드 process 의 코드 버전 가시성 부족* — 디버그 시 항상 새 process spawn 확인 권장. MP-NNN 후보: "코드 수정 후 background daemon 재시작 누락 패턴". 일반화하면 *hot reload 가 없는 background process 의 디버그 비용*.
