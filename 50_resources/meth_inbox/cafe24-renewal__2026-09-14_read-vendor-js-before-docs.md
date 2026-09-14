---
id: cafe24-renewal__2026-09-14_read-vendor-js-before-docs
origin_repo: cafe24-renewal
type: pattern
target: "catalog"
refs:
  - "2b6eefa"
  - "40_dev/decisions/2026-09-07_floating-review-alpha-api.md"
friction_ref: 2026-08-21_ytz-morenvy-product-tokens
created: 2026-09-14T07:06:46Z
---

## 제안
블랙박스 서드파티 위젯·앱의 동작·파라미터는 공개 문서나 추측보다 실제 로드되는 JS·CSS 원본을 직접 받아 읽어 확정하는 편이 빠르고 정확하다는 패턴 제안. 그 과정에서 비공식 API 를 쓰게 되면 실패 시 기존 경로로 떨어지는 폴백과 롤백 스위치를 필수로 둔다

## 근거
- 배너 앱의 토큰 치환 조건을 문서 추측으로 두 번 헛발 → 설치 스크립트를 받아 코드에서 확정(60분)
- 리뷰 앱 스크립트 문자열에서 API 경로군·필수 파라미터까지 확정 → 반나절 만에 데이터원 교체를 폴백 포함 배포

