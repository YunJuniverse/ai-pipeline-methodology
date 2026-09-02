---
id: icons__2026-08-27_embedded-preview-canvas-pitfalls
origin_repo: icons
type: tool-change
target: "catalog"
refs:
  - "50_apps/plan-viewer/public/prototypes/aouad-broadcast-graybox.html"
friction_ref: 2026-08-26_broadcast-pilot-g0-g1
created: 2026-08-27T01:00:37Z
---

## 제안
임베디드 브라우저 팬에서 캔버스·게임 검증 시 함정 2개와 대응: ① 백그라운드 탭 로드 시 window.innerWidth가 0 — 뷰포트 기반 크기 계산이면 0×0으로 부팅해 검은 화면(대응: 고정 논리 해상도 + FIT 스케일, 뷰포트로 초기 크기 계산 금지) ② rAF 스로틀로 실시간 재생 검증 불가(대응: 씬 핸들을 노출해 update를 수동 스텝 구동하거나, 로직을 헤드리스 실행). 검은 화면·느린 봇은 게임 버그가 아니라 팬 환경일 수 있다 — 원인 판별부터.

## 근거
- 동일 씬 클래스가 프로브 div에선 정상 부팅 — 원인은 코드가 아니라 로드 시점 뷰포트 0

