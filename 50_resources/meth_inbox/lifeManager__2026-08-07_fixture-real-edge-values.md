---
id: lifeManager__2026-08-07_fixture-real-edge-values
origin_repo: lifeManager
type: guide-update
target: "guide-23"
refs:
  - "src/lib/analytics.ts"
  - "supabase/migrations/0041_analytics_views.sql"
friction_ref: 2026-08-06_category-mix-label
created: 2026-08-07T00:32:05Z
---

## 제안
테스트 픽스처에 **실데이터·스키마가 실제로 만들어내는 특이값**을 반영한다는 규범 제안. 이번 세션에서 DB 뷰가 null 을 '기타'로 매핑한다는 걸 알면서도 픽스처에 '기타' 분류를 넣지 않아, 집계 함수의 접기 바구니 이름이 실제 분류와 충돌하는 버그를 놓쳤다. 테스트 20건이 전부 통과한 채 머지됐고 실화면에서야 범례 중복·React key 중복으로 드러났다. 값 매핑(null→기본값)이 있는 필드는 그 기본값을 픽스처에 반드시 포함한다.

## 근거
- (refs 참조 — 원문 정본은 이 repo)

