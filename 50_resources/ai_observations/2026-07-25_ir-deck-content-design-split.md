---
session_id: 2026-07-25_ir-deck-content-design-split
authored_by:
  agent: "gpt-5"
  tool: "codex-desktop"
  host_os: "darwin-26.4.1-arm64"
domain: meta
task_type: docs
stack_used:
  - "python3"
  - "methodology@v4.0"
flow_used: ad-hoc
friction:
  - id: F-001
    where: "python-pptx 헬퍼가 토큰을 기본인자로 조기바인딩하면 apply_theme 후에도 옛 색 유지 — 테마 전환 무력. 기본인자 None 센티넬+함수 본문 late-bind로 해결"
    cost_minutes: 15
    resolution: "헬퍼 시그니처 None화·본문에서 활성 테마 전역 해석"
    repeat_of: null
prompt_patterns:
  - intent: "l1 observation capture"
    success: true
    rounds: 1
---

지침 22 정련 — 사용자 피드백(텍스트 md 덱=SSOT·콘텐츠 먼저·디자인 여러 후보)을 반영해 콘텐츠·디자인 분리 모델로 재작성. §2 6단계(P0 데이터·P1 스토리라인·P2 슬라이드 텍스트 구조화·P3 디자인 후보 탐색·P4 빌드검증·P5 파생), contract.py THEMES 후보 레지스트리+apply_theme() late-bind, build.py --theme/--candidates 비교 렌더.
