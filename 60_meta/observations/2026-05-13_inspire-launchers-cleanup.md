---
session_id: 2026-05-13_inspire-launchers-cleanup
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: refactor
stack_used:
  - python3
  - pillow
flow_used: ad-hoc
friction:
  - id: F-001
    where: "사용자 명시 표기 (mac)(windows)(linux) — 공백+괄호 파일명 — Linux .desktop Exec 필드에 공백 처리 우려"
    cost_minutes: 1
    resolution: "sed 치환 시 '|' 구분자 사용해 슬래시·공백 안전. .desktop 의 Exec 자체는 공백 포함 경로 quote 없이 허용 (modern desktop entry spec). setup-linux.sh 에서 EXEC_PATH=\"$HERE/in-spire (linux).sh\" 큰따옴표로 안전."
    repeat_of: null
  - id: F-002
    where: "_start/ 옛 구조 (in-spire.app, in-spire.bat, icons/ 평면) 와 새 구조 (괄호명 + assets/ 하위 정리) 가 혼재할 위험 — clean rebuild 누락 시 옛 파일 잔존"
    cost_minutes: 0
    resolution: "build-launchers.py 에 clean_legacy() 추가 — 빌드 전 옛 파일 목록(in-spire.app, in-spire.bat, ..., icons/) 자동 삭제. 멱등 보장."
    repeat_of: null
  - id: F-003
    where: "루트의 사용자 추가 PNG 4장 (app-icon source + in-spire-{mac,win,linux}) 이 build-launchers 입력 후에도 루트에 잔존 — visual clutter + 동기화 혼동"
    cost_minutes: 1
    resolution: "find_source_pngs() 가 _start/assets/icons 우선·루트 fallback. 첫 빌드 후 사용자가 루트의 PNG 를 assets 로 이동(또는 삭제). 원본 AI 생성 PNG 는 assets/icons/app-icon-source.png 로 rename 보존."
    repeat_of: null
prompt_patterns:
  - intent: "사용자 명시 파일명 (괄호 포함) + 시각적 정리 + 루트 클러터 제거"
    success: true
    rounds: 1
  - intent: "clean rebuild — 옛 구조 자동 정리 + 새 구조 결정적 생성 (멱등)"
    success: true
    rounds: 1
---

_start/ 1차 빌드 후 사용자 요구로 구조 재편 — (mac)(windows)(linux) 파일명 + assets/ 하위 정리 + 루트 4 PNG 정리. clean_legacy() 가 옛 자산을 자동 제거해 멱등 빌드 보장. 격리 검증 통과 (적용 프로젝트 init 시 새 구조·실행권한·60_meta 격리 모두 ✅). F-003 (사용자 작업 산출물의 루트 클러터 정리) 는 *작업물 누적 패턴* 의 일반화 후보 — 향후 .png/.tmp 등 빌드 산출물 자동 정리 hook 검토 가능.
