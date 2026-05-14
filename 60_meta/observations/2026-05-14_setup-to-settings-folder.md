---
session_id: 2026-05-14_setup-to-settings-folder
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: refactor
stack_used:
  - python3
flow_used: ad-hoc
friction:
  - id: F-001
    where: "_start/ 루트에 setup-*.{ps1,sh} 두 파일이 *진입점 3개와 같은 레벨* 노출 — 사용자가 *진입점*과 *1회 setup*을 시각적으로 구분 어려움"
    cost_minutes: 0
    resolution: "settings/ 하위 폴더 신설 — _start/{진입점 3개 + README + assets/ + settings/ + .cache/} 6항목 트리. 진입점·setup 명확 분리."
    repeat_of: null
  - id: F-002
    where: "setup 스크립트 내부 경로 — settings/ 로 이동 후 *$here 한 단계 위* 필요 (.bat, .desktop, icons 모두 부모/형제 디렉터리)"
    cost_minutes: 1
    resolution: "PowerShell: `$root = Split-Path -Parent $here` 후 `Join-Path $root '...'`. bash: `ROOT=\"$(dirname \"$HERE\")\"` 후 `\"$ROOT/...\"`. .lnk 도 _start/ 루트 (사용자 진입점) 에 생성."
    repeat_of: null
  - id: F-003
    where: "build-launchers.py 의 clean_legacy() 가 *옛 위치 setup-*.{ps1,sh}* 까지 정리해야 멱등 보장"
    cost_minutes: 0
    resolution: "legacy_items 에 'setup-windows.ps1', 'setup-linux.sh' 추가. 기존 _start/ 가 옛 구조였어도 새 빌드 시 자동 정리."
    repeat_of: null
prompt_patterns:
  - intent: "진입점·자산·1회setup 시각적 분리 (settings/ 폴더 + assets/ + .cache/)"
    success: true
    rounds: 1
---

_start/ 안 시각적 위계 명확화 — 진입점(3) + README + 3 폴더(assets/settings/.cache). 사용자가 *어느 파일을 더블클릭*해야 하는지 한눈에. settings/ 안 두 setup 은 *처음 한 번* 만 보면 됨. 다음 v3.x 후보: .lnk 가 _start/ 에 생성되는지 .lnk 도 settings 옆에 두는 게 좋은지 — 사용자 실사용 후 결정.
