---
id: gamblescan__2026-07-31_verify-source-not-proxy
origin_repo: gamblescan
type: pattern
target: "catalog"
refs:
  - "https://github.com/YunJuniverse/gamblescan/pull/238"
  - "https://github.com/YunJuniverse/gamblescan/pull/243"
  - "https://github.com/YunJuniverse/gamblescan/pull/254"
  - "50_resources/ai_observations/2026-07-31_game-provider-card.md"
friction_ref: 2026-07-31_game-provider-card
created: 2026-07-31T03:16:31Z
---

## 제안
'대리 신호'(요약도구·컬럼명·빌드성공)를 사실 근거로 삼아 오판·오배포한 3실사례 → 검증 패턴 승급: ① WebFetch 요약이 'CGF는 이름만'이라 했으나 원문 HTML엔 도메인 15개(요약만 믿으면 근거 틀린 기각) ② 컬럼명 published_withdrawal_min을 '최소출금액'으로 단정해 3개 문서·후보G 계획에 전파했으나 실값은 처리시간(분)(DATA-041에서 정정) ③ 게임제공사 카드가 빌드는 통과했으나 렌더 링크가 /providers/138로 404(curl 렌더검증서만 포착). 규칙: 사실로 기록/배포하기 전 원문·실값·렌더를 직접 확인한다. 틀린 기록은 후속 계획으로 전파된다.

## 근거
- provider 카드: 빌드 통과했으나 game_providers(610) slug와 providers(10) 페이지 불일치로 링크 전부 404, 렌더 curl로만 발견

