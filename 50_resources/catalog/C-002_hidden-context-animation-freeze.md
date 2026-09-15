---
id: C-002
title: "숨은 브라우저 패널·백그라운드 탭에서 캔버스·애니메이션 실측은 거짓값을 낸다"
domain: browser-automation
status: active
seen_in:
  - 2026-08-27
  - 2026-09-09
  - 2026-09-14
signature: "innerWidth.*0|검은 화면|rAF.*throttl|백그라운드 탭|getAnimations|progress.*1|addInitScript"
verified_with:
  - claude-opus-5
  - claude-fable-5-1
deps_implicated: []
created: 2026-09-15
last_hit: 2026-09-14
---

> **승급 (2026-09-15, METH-147)**: P-004(1 repo 1회) → active. 근거 = icons 2번째 케이스(숨은 패널에서
> `getAnimations()` progress 가 정지점 6개 전부 1 — Playwright visible 에서는 0.95·0.01·복귀) +
> **cafe24-renewal 의 부재 판정 캡슐 근거에 같은 원인(백그라운드 탭 rAF 정지)** — 서로 다른 repo N≥2.
> 지침 23 §2-7 이 규칙, 이 엔트리가 증상·원인·솔루션의 정본.

## 증상 (Symptom)

- 임베디드 프리뷰 팬에서 캔버스 앱이 **검은 화면**. 같은 씬 클래스가 프로브 `div` 에서는 정상.
- 숨은 패널·백그라운드 탭에서 **애니메이션 진행도가 전부 1(끝)** 또는 정지 — 정지점 opacity 가 1 로 읽혔으나 실제 0.
- 실시간 재생이 비정상적으로 느려 밸런스·연출 검증 불가. 지연로딩 위젯이 «빈 위젯»으로 보임.

## 근본 원인 (Root Cause)

- 백그라운드 탭 로드 시 `window.innerWidth` 가 0 — 뷰포트 기반 초기 크기 계산이 0×0 으로 부팅.
- 숨은 컨텍스트는 `requestAnimationFrame`·CSS 애니메이션·스크롤 구동 타임라인이 **동결/스로틀** — 실측이 환경 산물이다.

## 솔루션 (Solution)

- 고정 논리 해상도 + FIT 스케일. 뷰포트로 초기 크기를 계산하지 않는다.
- **애니메이션·연출·정지 위치 실측은 보이는 헤드리스 브라우저(Playwright)에서** rAF 대기 후 `getAnimations()` 의 computed timing progress 로 잰다(지침 23 §2-7).
- 씬 핸들을 노출해 `update` 를 수동 스텝 구동하거나 로직을 헤드리스로 실행(P-003).
- 부재·정지 판정문에는 **관측 조건(탭 가시성·UA·세션)을 명시**한다(지침 23 §2-6).
- 캐시·환경 재현은 `route` 로 페이지만 위장하고 판정 조회는 실서버 통과 · 깜빡임은 `addInitScript` 16ms 샘플링.

## 안티패턴 (Anti-Pattern)

- 검은 화면을 보고 렌더 코드부터 고친다.
- 숨은 패널의 progress·opacity 를 연출 검증 결과로 기록한다.
- 백그라운드 탭의 체감 속도를 성능 수치로 쓴다.

## 관련 자료

- 지침 23 §2-6·§2-7 · 지침 24 §2(부재≠미포착)
- 출처 캡슐: icons `embedded-preview-canvas-pitfalls`(08-27) · `hidden-pane-frozen-animations-headless-measure`(09-11) · cafe24 `absence-verdict-observation-conditions`·`verification-measurement-pitfalls`(09-14)
