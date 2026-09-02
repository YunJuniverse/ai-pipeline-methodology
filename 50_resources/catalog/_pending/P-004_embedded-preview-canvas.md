---
id: P-004
title: "임베디드 브라우저 팬에서 캔버스·자동화 검증 시 환경 함정 — 검은 화면·스로틀·측정 위장"
domain: browser-automation
status: pending
source_observations:
  - icons__2026-08-27_embedded-preview-canvas-pitfalls (capsule)
  - cafe24-renewal__2026-09-02_verification-measurement-pitfalls (capsule, 기법 2건)
signature: "innerWidth.*0|검은 화면|rAF.*throttl|백그라운드 탭|addInitScript|route.*가로채기"
created: 2026-09-02
last_seen: 2026-09-02
promotion_rule: "Promote to active Catalog after N>=2 observations or explicit human approval."
---

## 증상 (Symptom)

- 임베디드 프리뷰 팬에서 캔버스 앱이 **검은 화면**으로 뜬다. 같은 씬 클래스가 프로브 `div` 에서는 정상 부팅한다.
- 실시간 재생이 비정상적으로 느려 밸런스·애니메이션 검증이 불가능하다.

## 근본 원인 (Root Cause)

- **백그라운드 탭 로드 시 `window.innerWidth` 가 0** — 뷰포트 기반으로 초기 크기를 계산하면 0×0 으로 부팅한다. 코드 버그가 아니라 **로드 시점 환경**이다.
- **백그라운드 탭은 `requestAnimationFrame` 이 스로틀된다** — 실시간 재생 속도로 판정할 수 없다.

## 솔루션 (Solution)

- **고정 논리 해상도 + FIT 스케일.** 뷰포트로 초기 크기를 계산하지 않는다.
- **씬 핸들을 노출해 `update` 를 수동 스텝 구동**하거나 로직을 헤드리스로 실행한다(→ `P-003`).
- 검은 화면·느린 봇을 만나면 **게임 버그가 아니라 팬 환경일 수 있다** — 원인 판별을 먼저 한다(프로브 div 대조).

### 측정 기법 (cafe24-renewal 합류분)

- **캐시·환경 시나리오 재현은 `route` 로 페이지만 위장하고, 판정 조회는 실서버를 통과시킨다** — 전부 목으로 덮으면 판정 대상이 사라진다.
- **깜빡임(FOUC·재렌더)은 `addInitScript` 16ms 샘플링으로 정량화**한다. "깜빡이는 것 같다"는 판정이 아니다.

## 안티패턴 (Anti-Pattern)

- 검은 화면을 보고 렌더 코드부터 고친다(원인은 로드 시점 뷰포트).
- 백그라운드 탭의 체감 속도를 성능 수치로 기록한다.

## 관련 자료

- 지침 23 §2-3(내용·가시성) · §1-4(대리 신호) — 이 문서는 그 원칙의 *임베디드 환경* 인스턴스.

## 승급 조건

타 프로젝트의 임베디드 프리뷰·자동화 검증에서 같은 함정이 재현되면 active `C-NNN` 등재.
