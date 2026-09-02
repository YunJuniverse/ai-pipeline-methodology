---
id: icons-wt-hub__2026-09-01_land-classbc-plan-viewer-false-positive
origin_repo: icons-wt-hub
type: guide-update
target: "methodology.py"
refs:
  - "https://github.com/icons-hq/icons/pull/658"
friction_ref: null
created: 2026-09-01T07:37:43Z
---

## 제안
land 의 Class B/C 판정 정규식 `(^|/)(billing|payment|pricing|checkout|invoice|subscription|plan)s?[./_-]` 가 경로 세그먼트 `plan-viewer` 에 걸린다(`/plan-` 매칭). icons 레포의 시연 앱 전체 경로가 `50_apps/plan-viewer/` 라 **그 아래 모든 파일이 「과금·결제·가격」 트리거로 자동 머지 거부**된다 — 정적 HTML 회색 상자 하나에도 걸린다. 오탐이 싼 건 맞지만 이 오탐은 상시라 land 자체가 무력해지고, 결국 사람이 매번 판정을 우회하게 되어 **가드가 훈련시키는 습관이 반대가 된다**. 제안 = `plan` 을 `plans?` 단독 세그먼트로 좁히거나(`(^|/)plans?[./]`) `subscription-plan`·`pricing-plan` 처럼 과금 문맥이 있는 형태만 매칭. 다른 항목(`session` 이 `session-storage` 에, `job` 이 `job-board` 에)도 같은 계열 오탐 여지가 있다.

## 근거
- (refs 참조 — 원문 정본은 이 repo)

