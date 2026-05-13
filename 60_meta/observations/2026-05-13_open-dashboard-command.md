---
session_id: 2026-05-13_open-dashboard-command
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: feature
stack_used:
  - python3
  - bash
flow_used: ad-hoc
friction:
  - id: F-001
    where: "사용자가 dashboard 를 열려면 매번 터미널에서 'methodology dashboard' 입력 필요 — 더블클릭 진입점 부재"
    cost_minutes: 0
    resolution: "open-dashboard.command 신설 (macOS .command 파일, +x). Finder 더블클릭 시 Terminal 에서 자동 실행. 내용은 단순 'cd $(dirname) && python3 50_tools/methodology.py dashboard --open'. cmd_dashboard 에 --open 옵션 추가 (macOS: subprocess.Popen(['open', url]) / 기타: webbrowser.open). 적용 프로젝트에도 MANIFEST shared_paths 로 자동 전파."
    repeat_of: null
  - id: F-002
    where: "shutil.copy2 가 mode 보존하니 sync 시 .command 의 +x 권한도 적용 프로젝트로 전달 — 다만 git core.fileMode 가 false 인 환경에선 commit 시 +x 가 빠질 수 있음"
    cost_minutes: 0
    resolution: "본 저장소에 .command 추가 시 chmod +x 후 git add — git index 에 +x 모드 저장. 다른 사용자가 clone 해도 +x 유지. macOS 기본 git core.fileMode=true."
    repeat_of: null
prompt_patterns:
  - intent: "사용자 '더블클릭 진입점' 요구 → macOS .command 파일 + --open 옵션 조합"
    success: true
    rounds: 1
---

더블클릭 진입점 — open-dashboard.command. 사용자 의도: 터미널 명령 외우지 않고 *폴더에서 더블클릭* 으로 dashboard 시작. .command 파일이 cd + methodology dashboard --open 호출. cross-platform 후속(Windows .bat, Linux .desktop) 은 사용자 환경 darwin 우선 후 추가. MANIFEST shared 전파 — 적용 프로젝트도 다음 sync 후 자동 획득.
