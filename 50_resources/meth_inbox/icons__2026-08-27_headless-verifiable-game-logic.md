---
id: icons__2026-08-27_headless-verifiable-game-logic
origin_repo: icons
type: pattern
target: "catalog"
refs:
  - "50_apps/plan-viewer/public/prototypes/aouad-broadcast-graybox.html"
  - "https://github.com/icons-hq/icons/pull/460"
friction_ref: null
created: 2026-08-27T01:00:21Z
---

## 제안
AI에게 시뮬레이션·게임 코드를 시킬 때 「수치/규칙/연출 3분리 + 씨앗 결정론」을 명세로 강제하면, 규칙만 헤드리스로 수천 판 돌려 렌더러 없이 밸런스를 기계 검증할 수 있다. 실사례: 초판 수치가 설계 목표(50~75초)의 1/4인 13초임을 화면 실행 전에 봇으로 발견, 후보 A/B 비교로 64.7초 안착. 같은 씨앗 2회 실행 결과 동일성 검증이 결정론의 합격 기준.

## 근거
- 화면으로 봤으면 「빠른가?」 하고 넘어갔을 것을 수치로 잡았다

