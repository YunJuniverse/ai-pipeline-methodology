---
id: icons__2026-09-11_hidden-pane-frozen-animations-headless-measure
origin_repo: icons
type: guide-update
target: "guide-verification"
refs:
  - "https://github.com/icons-hq/icons/pull/926"
  - "https://github.com/icons-hq/icons/pull/942"
friction_ref: null
created: 2026-09-11T03:22:59Z
---

## 제안
숨은 브라우저 패널이나 백그라운드 탭은 rAF·CSS 애니메이션·스크롤 구동 타임라인이 얼어 연출 실측이 거짓값을 낸다(정지점 opacity 가 1 로 읽혔으나 실제 0). 연출·정지 위치 검증은 보이는 헤드리스 브라우저(Playwright)에서 rAF 대기 후 getAnimations 의 computed timing progress 로 잰다. 지침에 애니메이션 실측은 visible 컨텍스트 필수 한 줄과 계측 스니펫 추가 제안.

## 근거
- 2026-09-09 hidden 팬: 6개 정지점 전부 progress 1(동결) vs Playwright: 60→0.95, 114→0.01, 130→114 복귀

