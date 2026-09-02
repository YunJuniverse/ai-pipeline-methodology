---
id: icons__2026-08-27_shared-checkout-path-add-not-safe
origin_repo: icons
type: guide-update
target: "guide"
refs:
  - "icons@d216eff5 (혼입) → d92ffd8c (분리)"
  - "https://github.com/icons-hq/icons/pull/463"
friction_ref: 2026-08-27_aouad-md-gallery-grid-goodsshop
created: 2026-08-27T01:31:12Z
---

## 제안
공유 체크아웃에서 '경로 지정 git add'는 안전장치가 아니다 — 동시 세션이 같은 파일의 다른 블록을 편집 중이면 파일 단위 스테이징이 남의 훅을 통째로 가져간다. 기존 규칙은 'add -A 금지'까지만 다루는데, 실사고는 add -A 없이 발생했다. 파일이 겹칠 가능성이 있으면 add -p로 훅을 고르거나 애초에 격리 워크트리에서 시작한다. 착수 전 git status로 '남의 미추적 파일'만 보는 것으로는 부족하다 — 이미 추적 중인 파일 안의 미커밋 편집이 진짜 함정이다.

## 근거
- (refs 참조 — 원문 정본은 이 repo)

