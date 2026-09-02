---
id: icons__2026-09-01_asset-exts-excluded-from-class-triggers
origin_repo: icons
type: tool-change
target: "tool/land"
refs:
  - "60_tools/methodology.py:1642"
  - "https://github.com/icons-hq/icons/pull/670"
friction_ref: null
created: 2026-09-01T09:05:54Z
---

## 제안
Class B/C 경로 트리거에서 표현용 바이너리 자산(이미지·영상·폰트)을 제외한다. 트리거는 경로 단어로 위험을 추정하는데 자산은 그 경로에 있어도 로직을 바꿀 수 없다. 문서 확장자(.pdf·.md·.json·.docx)는 정책·약관·가격을 담으므로 일부러 제외하지 않는다.

## 근거
- icons 실측 — 인증·인가 트리거 적중 25건 중 16건이 public/gallery/auth-*.jpg 갤러리 스크린샷. 갤러리 재촬영 PR 마다 Class B 로 자동 머지 거부
- 실사례 커밋 3bf0fe79(인증 화면 32컷 촬영) — 구 동작 Class B(jpg 16건) → 신 동작 Class A. 다른 6개 트리거 적중 수는 불변
- 경계 = 문서는 자산이 아니다. legal/terms-2026.pdf · docs/policy-changes.md · config/pricing.json · privacy/notice.docx 는 계속 트리거된다(테스트로 고정)
- 조용한 축소 금지 — land 2/6 이 제외한 자산 건수와 예시 경로를 출력한다

