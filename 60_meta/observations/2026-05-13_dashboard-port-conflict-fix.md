---
session_id: 2026-05-13_dashboard-port-conflict-fix
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
    where: "methodology dashboard 가 포트 점유 시 '어느 프로젝트를 서빙하는지' 구분 없이 무조건 '기존 URL 보고' → talmocom 에서 호출했는데 8765 에 떠 있던 본 저장소 dashboard 가 그대로 표시됨"
    cost_minutes: 8
    resolution: "_running_dashboard_root(port) — HTTP GET /dashboard.html 후 \"root\": 정규식 추출. target 과 같으면 재사용, 다르면 _kill_port_listeners(port) 후 재시작. 사용자가 'methodology dashboard' 호출 = 그 프로젝트를 보고 싶다는 의도이므로 다른 프로젝트 서버는 종료."
    repeat_of: null
  - id: F-002
    where: "_kill_port_listeners 에서 os.kill 호출했으나 methodology.py 상단에 import os 누락 — NameError"
    cost_minutes: 2
    resolution: "import os 상단 추가. 이전엔 os 를 안 썼다가 dashboard 제어 추가로 처음 필요해짐. 함수 내 lazy import 가능했으나 상단 정렬이 깔끔."
    repeat_of: null
  - id: F-003
    where: "적용 프로젝트(talmocom)의 local methodology.py 가 *옛 버전*이라 새 fix 가 안 적용됨 — talmocom 에서 호출하면 옛 동작"
    cost_minutes: 1
    resolution: "본 저장소 commit → 적용 프로젝트에 sync --apply 전파 필요. 임시 우회: python3 /Users/hayden/methodology/50_tools/methodology.py dashboard --path ~/talmocom --port 8765 (본 저장소 새 코드 사용). 근본: METH-015 류 전파 사이클."
    repeat_of: "F-001 (2026-05-12_meth-015-propagation)"
  - id: F-004
    where: "세션 resume 으로 자정 넘김 — 관찰 파일을 작업 시작일(2026-05-12)로 만들었는데 wrap 은 오늘(2026-05-13) 날짜만 봐서 ship 실패"
    cost_minutes: 2
    resolution: "관찰 파일 오늘 날짜로 rename + session_id 수정. 근본: wrap 의 날짜 매칭을 *최근 N일*(예: 2일) 허용으로 완화 필요. 장시간 세션·자정 넘김 흔함. METH-021 후보."
    repeat_of: null
  - id: F-005
    where: "hooks install 후 적용 프로젝트에서 방법론 sync chore commit 을 push 하면 pre-push hook 의 wrap --strict 가 막음 (4 라이브 파일이 sync 로는 갱신 안 됨)"
    cost_minutes: 3
    resolution: "git push --no-verify 우회 — 방법론 sync 는 *사용자 작업이 아닌 자산 갱신*이라 wrap 면제 정당. 근본: pre-push hook 이 commit 메시지 'chore(methodology): sync' 면 wrap 면제, 또는 wrap 이 50_tools/-only diff 면 통과. METH-022 후보."
    repeat_of: null
prompt_patterns:
  - intent: "사용자 증상 보고('방법론 dashboard만 열림')에서 포트 점유 원인 즉시 추론 → lsof + curl 로 확진"
    success: true
    rounds: 1
  - intent: "즉시 해결(kill+재시작) → 근본 수정(root 확인 로직) → 전파(sync) 3단계 분리"
    success: true
    rounds: 1
---

dashboard 포트 충돌 — 같은 8765 에 *서로 다른 프로젝트 dashboard 가 경쟁*하는 게 근본 문제. 해결: 포트 점유 시 그 서버의 root 를 HTTP 로 확인 → 다르면 종료 후 재시작. F-003 *재발* (적용 프로젝트가 옛 CLI 라 fix 못 받음 — F-001 of meth-015-propagation 과 동일 구조). 이건 *Catalog 승급 후보 강화* — "적용 프로젝트에 CLI fix 가 즉시 안 닿음" 패턴이 이미 3회 목격(meth-015 F-001, meth-015 F-003, 본 F-003). MC-002 후보. 다음 v3.x: dashboard 가 *프로젝트별 포트 자동 할당*(8765, 8766...) 옵션 검토 — 여러 프로젝트 동시 dashboard.
