---
id: P-003
title: "시뮬레이션·게임 로직은 수치/규칙/연출 3분리 + 씨앗 결정론으로 헤드리스 검증한다"
domain: game-simulation
status: pending
source_observations:
  - icons__2026-08-27_headless-verifiable-game-logic (capsule)
signature: "게임|시뮬레이션.*밸런스|헤드리스|seed.*결정론|rAF|렌더러 없이"
created: 2026-09-02
last_seen: 2026-08-27
promotion_rule: "Promote to active Catalog after N>=2 observations or explicit human approval."
---

## 패턴 (Pattern)

AI에게 시뮬레이션·게임 코드를 시킬 때 **명세 단계에서** 세 가지를 강제하면, 규칙만 헤드리스로 수천 판 돌려 렌더러 없이 밸런스를 기계 검증할 수 있다.

1. **수치/규칙/연출 3분리** — 밸런스 수치는 데이터로, 규칙은 순수 함수로, 연출(렌더·사운드·트윈)은 그 바깥으로. 규칙이 렌더러를 참조하면 헤드리스 실행이 불가능해진다.
2. **씨앗 결정론** — 난수는 씨앗을 받는다. **같은 씨앗 2회 실행 결과가 동일한가**가 결정론의 합격 기준이다.
3. **봇 구동 진입점** — 규칙만 N판 돌려 분포를 뽑는 실행 경로를 처음부터 만든다.

## 근거 (Evidence)

초판 수치가 설계 목표(50~75초)의 **1/4인 13초**임을 화면 실행 전에 봇으로 발견했고, 후보 A/B 비교로 64.7초에 안착했다(icons, PR #460). 화면으로 봤으면 "좀 빠른가?" 하고 넘어갔을 값이다 — **눈은 분포를 못 본다.**

## 안티패턴 (Anti-Pattern)

- 밸런스를 화면 플레이로 판정 — 표본 1회, 관찰자 편향, 재현 불가.
- 규칙 함수가 렌더 객체·DOM·`performance.now()` 를 직접 참조 — 헤드리스 실행이 막힌다.
- 난수에 씨앗이 없어 "방금 그 판"을 재현하지 못함.

## 관련 자료

- 지침 23 §2-3(존재가 아니라 내용으로) · §4(판정기 신뢰도)의 시뮬레이션 인스턴스.
- 지침 25 §5 게이트 ②(저비용 대리물) — 회색 상자 단계에서 이 검증이 판정 근거가 된다.
- 원문 정본: icons `50_apps/plan-viewer/public/prototypes/aouad-broadcast-graybox.html`.

## 승급 조건

타 프로젝트(시뮬레이션·게임·확률 산출물)에서 같은 3분리 필요가 재현되면 active `C-NNN` 등재.
