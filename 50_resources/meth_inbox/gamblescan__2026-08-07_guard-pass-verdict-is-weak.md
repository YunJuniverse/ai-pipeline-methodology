---
id: gamblescan__2026-08-07_guard-pass-verdict-is-weak
origin_repo: gamblescan
type: friction-escalation
target: "guide-23"
refs:
  - "https://github.com/YunJuniverse/gamblescan/pull/291"
  - "https://github.com/YunJuniverse/gamblescan/pull/297"
  - "docs/snapshots/2026-08-06_sportsbook-logos.md"
friction_ref: 2026-08-06_screenshot-guard-gaps
created: 2026-08-07T00:12:02Z
---

## 제안
자동 판정기의 '거부'와 '통과'는 신뢰도가 다르다. 실측에서 거부 86건은 전부 타당했는데 통과 10건 중 5건이 가짜였다. 검증 규범에 '통과 판정은 독립 확인 없이 최종으로 쓰지 않는다'와 '적재·발행 직전 육안 단계를 파이프라인에 남긴다'를 명문화할 것을 제안한다.

## 근거
- 파일럿 100곳: 거부 86(전부 타당) · 통과 10 중 5가 가짜 — 주차 도메인·타 브랜드 사이트·카지노 아님·지오블록 문구 미매칭·모달 백드롭
- 같은 세션에서 3회 반복: 로고(빈 이미지 4곳+스크린샷 1) · 스냅샷(쿠키바 잔존) · 캡처 자세(스크롤된 화면) — 전부 가드는 통과시키고 눈으로만 잡혔다

