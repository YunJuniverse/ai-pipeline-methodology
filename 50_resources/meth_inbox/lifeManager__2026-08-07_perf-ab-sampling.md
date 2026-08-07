---
id: lifeManager__2026-08-07_perf-ab-sampling
origin_repo: lifeManager
type: guide-update
target: "guide-23"
refs:
  - "src/lib/supabase/middleware.ts"
friction_ref: 2026-08-06_proxy-getclaims
created: 2026-08-07T00:32:05Z
---

## 제안
성능 A/B는 **워밍 후 다회 표본의 중앙값**으로 판단한다는 규범 제안. 이번 세션 미들웨어 최적화에서 첫 측정이 개선안을 오히려 느리게(111ms vs 88ms) 보고했다 — dev 서버 컴파일 노이즈였고, 워밍 8회+표본 20회로 다시 재니 53ms vs 82ms 로 뒤집혔다. 단회 측정이었다면 옳은 변경을 기각할 뻔했다. 분산(p25~p75)도 함께 보고해야 노이즈와 실제 개선을 구분할 수 있다.

## 근거
- (refs 참조 — 원문 정본은 이 repo)

