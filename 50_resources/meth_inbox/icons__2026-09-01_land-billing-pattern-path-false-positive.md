---
id: icons__2026-09-01_land-billing-pattern-path-false-positive
origin_repo: icons
type: tool-change
target: "methodology.py"
refs:
  - "https://github.com/icons-hq/icons/pull/664#issuecomment-5491333469"
  - "60_tools/methodology.py:1604"
  - "50_resources/ai_observations/2026-09-01_land-plan-viewer-false-positive.md"
  - "https://github.com/icons-hq/icons/pull/667"
  - "https://github.com/icons-hq/icons/pull/603"
friction_ref: null
created: 2026-09-01T08:42:56Z
---

## 제안
land 의 Class B 과금 패턴 (^|/)(billing|payment|pricing|checkout|invoice|subscription|plan)s?[./_-] 에서 plan 대안이 요금제가 아닌 경로 단어를 문다. icons 레포에서 /plan-viewer/ 가 매칭돼 해당 앱 전체 변경이 자동 머지 불가. 실측: re.search 가 '/plan-' 에 매칭. plan 대안을 세그먼트 전체 매칭으로 좁히거나, pricing·billing·subscription 이 실사례를 덮으므로 제거 검토.

## 확정 패턴 (icons 에서 검증·선반영 2026-09-01)
`plan` 단독 대안을 제거하고 과금 어휘와 결합한 형태만 남긴다.

    (^|/)(billing|payment|pricing|checkout|invoice|subscription)s?[./_-]|(^|/)plans?[._-](pricing|price|billing|tier|quota)

## 근거
- (refs 참조 — 원문 정본은 이 repo)
- 참양성 11종 전수 유지 — `src/billing/checkout.ts` · `lib/pricing.ts` · `api/invoice.pdf.ts` · `server/checkout-session.ts` · `billing/plans.ts` · `src/pricing_plans.ts` · `src/plan_pricing.ts` · `web/subscription-plans/page.tsx` 등
- 오탐 해소 — icons 전체 트리 기준 과금 트리거 적중 **823 → 2건**(잔여 2건 모두 실제 `checkout` 경로)
- `_classify_change` 실측 — plan-viewer 를 건드린 커밋 `428cd07f` 이 구 패턴에선 Class B, 신 패턴에선 Class A(빈 목록)
- 세그먼트+확장자로 좁히는 대안(`plans?\.`)은 불충분 — `50_resources/prompts/plan.md` 가 계속 오탐된다. 그래서 단독 대안 제거를 택했다

## 같은 계열의 오탐 — 별도 캡슐로 분리·해소 (2026-09-01)
경로 단어를 문자열로 무는 방식이라 다른 항목에도 같은 오탐이 남는다. icons 전체 트리 실측:
- **인증·인가 25건 중 16건이 `.jpg`** — `50_apps/plan-viewer/public/gallery/auth-*.jpg` 갤러리 스크린샷. 이미지는 인증 로직을 바꿀 수 없다. 갤러리를 재촬영하는 PR 마다 Class B 로 걸린다.
- 나머지 9건은 참양성(`apps/web/src/lib/auth/*` 등) — 패턴을 좁히면 이쪽이 뚫린다.
- 제안 방향(택일) = ① 자산 확장자(`.jpg|.png|.webp|.svg|.mp4` …)를 전 트리거에서 제외 ② 트리거별 확장자 화이트리스트(코드·설정 파일만). ①이 안전하다 — 바이너리 자산은 어느 Class 트리거의 대상도 아니다.
- **PM 지시로 착수·해소** — 인증 패턴을 좁히지 않고 **자산 확장자를 전 트리거에서 제외**하는 ①안을 택했다(패턴은 그대로 두므로 참양성 9건 유지). 별도 캡슐 = `2026-09-01_asset-exts-excluded-from-class-triggers`. 이 캡슐의 범위는 `plan` 대안 정련까지다.

## 통합 이력 (2026-09-01)
같은 제안의 캡슐 3건을 이 파일로 합쳤다(1제안=1캡슐) — `2026-08-31_land-class-regex-plan-viewer-false-positive`(PR #603 최초 관측) · `2026-09-01_land-classbc-plan-viewer-false-positive`(같은 계열 오탐 지적, 위 절로 흡수). 상류 미수거 상태에서 정리했으므로 원장 중복은 없다.
