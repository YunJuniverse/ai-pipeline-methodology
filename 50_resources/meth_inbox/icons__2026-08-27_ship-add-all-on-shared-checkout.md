---
id: icons__2026-08-27_ship-add-all-on-shared-checkout
origin_repo: icons
type: tool-change
target: "tool/ship"
refs:
  - "https://github.com/icons-hq/icons/pull/437"
friction_ref: null
created: 2026-08-27T00:58:29Z
---

## 제안
동시 세션이 체크아웃을 공유할 때 ship 앞에 git add -A 를 붙이면 남의 미완성 작업이 함께 커밋된다. 실제로 미정의 참조가 섞여 프로덕션이 깨졌다. ship 이 --no-add-all 을 받았는데도 인덱스에 사용자가 스테이징한 외부 변경이 있으면 경고하거나 거부하도록 제안한다.

## 근거
- CLAUDE.md 는 별도 git add 금지·ship 만인데, ship --no-add-all 앞에 git add -A 를 붙이면 규칙이 무력화된다
- 다른 세션의 미완성 MD 6종이 커밋되고 그중 미정의 구매권 참조가 매점 크래시를 일으켰다

