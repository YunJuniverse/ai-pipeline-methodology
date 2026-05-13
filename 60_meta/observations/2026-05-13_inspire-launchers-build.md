---
session_id: 2026-05-13_inspire-launchers-build
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: feature
stack_used:
  - python3
  - pillow
  - iconutil
flow_used: ad-hoc
friction:
  - id: F-001
    where: "3개 OS 별로 *동일 디자인 + 배경색만 swap* 을 AI 이미지 생성에 의존하면 일관성 깨질 위험"
    cost_minutes: 0
    resolution: "Pillow 픽셀 단위 스왑 — 흰색 임계값(220+ 모든 채널)으로 stroke·외부 배경 자동 보호. 그라데이션 영역만 위치 좌표 (x+y)/(w+h) 기반 새 색상 보간. 결과: 형태 100% 동일, 배경만 정확히 새 그라데이션. 833,858 swap / 214,718 preserved / 1,048,576 total."
    repeat_of: null
  - id: F-002
    where: ".bat 단독으로는 아이콘 부여 불가 — Windows 한계"
    cost_minutes: 1
    resolution: "setup-windows.ps1 (사용자 1회 실행) 로 .lnk 바로가기 자동 생성 — WScript.Shell COM 객체 + IconLocation 필드. .lnk 가 진짜 더블클릭 진입점. .bat 직접 실행도 가능하나 아이콘 없음."
    repeat_of: null
  - id: F-003
    where: ".desktop 파일은 Exec/Icon 절대경로 필요 — 배포 시 사용자 환경마다 다름"
    cost_minutes: 1
    resolution: "__EXEC__ / __ICON__ 토큰 템플릿 + setup-linux.sh 로 sed 치환. 사용자 1회 실행으로 현재 절대경로 자동 설정. ~/.local/share/applications/ 에 복사하면 시스템 메뉴 등록."
    repeat_of: null
  - id: F-004
    where: "macOS .icns 생성에 8 크기 PNG 필요 + iconutil 호출 — iconset 디렉터리 임시 생성·정리"
    cost_minutes: 0
    resolution: "ICONSET_SIZES_MAC 정의 (16/32/64/128/256/512/1024) → Pillow LANCZOS resize → iconutil -c icns → iconset 디렉터리 정리. 외부 의존 0 (Pillow + macOS 내장 iconutil)."
    repeat_of: null
prompt_patterns:
  - intent: "1장 원본 → Pillow 픽셀 swap → 3개 OS 변형 (AI 비결정성 회피)"
    success: true
    rounds: 1
  - intent: "각 OS 표준 패키지 (.app/.bat+.lnk/.sh+.desktop) 자동 생성 — 외부 도구 0"
    success: true
    rounds: 1
  - intent: "사용자 1회 setup (Windows .lnk, Linux .desktop) 으로 배포 자동화 한계 우회"
    success: true
    rounds: 1
---

in-spire 브랜드 첫 시각 자산 완성 — 3 OS 더블클릭 진입점. 핵심 통찰: AI 이미지 생성으로 *디자인 일관성* 보장 어려움 → 1장만 AI 생성 + Pillow 픽셀 swap 으로 *결정적 변형*. `.app` 더블클릭 실측 통과 (dashboard 빌드 + 포트 8765 + 브라우저 자동). MANIFEST shared 로 적용 프로젝트 자동 전파, 격리 안전망 통과, .app 실행권한(shutil.copy2 mode 보존) 유지. 다음 v3.x 후보: Windows .lnk 의 setup.ps1 자동 호출 — 사용자가 .ps1 직접 실행 필요한 단계 회피.
