---
id: priceless-perlman-c80820__2026-08-31_land-class-regex-plan-viewer-false-positive
origin_repo: priceless-perlman-c80820
type: guide-update
target: "land"
refs:
  - "https://github.com/icons-hq/icons/pull/603"
friction_ref: null
created: 2026-08-31T04:57:11Z
---

## 제안
land 의 Class B/C 경로 트리거 정규식 (^|/)(billing|payment|pricing|checkout|invoice|subscription|plan)s?[./_-] 가 'plan' 토큰 때문에 50_apps/plan-viewer/ 하위 전 파일을 「과금·결제·가격」으로 오판 — 이 레포 주 앱 디렉토리라 plan-viewer 를 만지는 모든 PR 에서 자동 머지가 거부된다(2026-08-31 PR #603 실사례). 제안: plan 토큰을 pricing-plan 맥락으로 좁히거나(디렉토리 한정 (^|/)plans?/) 레포별 allowlist.

## 근거
- (refs 참조 — 원문 정본은 이 repo)

