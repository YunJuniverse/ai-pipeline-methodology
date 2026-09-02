---
id: cafe24-renewal__2026-09-02_verification-measurement-pitfalls
origin_repo: cafe24-renewal
type: pattern
target: "catalog"
refs:
  - "50_resources/ai_observations/2026-09-02_curl-variant-false-gone.md"
  - "50_resources/ai_observations/2026-09-01_probe-cache-mode-failclosed.md"
  - "40_dev/snapshots/2026-09-02_cafe24-methodology-survey.md"
friction_ref: 2026-09-02_curl-variant-false-gone
created: 2026-09-02T06:38:35Z
---

## 제안
웹 검증 측정 함정·기법 승급 제안: ①원본 진실 판정은 브라우저 fetch 다발로(같은 URL 이라도 curl 무쿠키 변형은 다른 사본 — '원복 실패' 오판 2회) ②textContent 는 숨긴 자식을 포함하므로 요소별 노출여부(display·offsetHeight) 포함 덤프로 판정 ③버전 게이트 폴링 후에만 측정(업로드 직후 측정 금지) ④캐시 시나리오 재현은 route 로 페이지만 위장하고 판정 조회는 실서버 통과 ⑤깜빡임은 addInitScript 16ms 샘플링으로 정량화

## 근거
- curl 6/6 '딜없음' vs 브라우저 2/2 신선 — 도구가 다르면 결과도 다르다(같은 날 2회 재발)

