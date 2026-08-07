---
id: gamblescan__2026-08-07_single-source-primitive
origin_repo: gamblescan
type: pattern
target: "guide-19"
refs:
  - "https://github.com/YunJuniverse/gamblescan/pull/295"
  - "https://github.com/YunJuniverse/gamblescan/pull/288"
  - "src/domain/ingestion/source-provenance.ts"
friction_ref: 2026-08-06_sportsbook-hygiene
created: 2026-08-07T00:12:51Z
---

## 제안
같은 판단을 하는 원시함수는 저장소에 한 벌만 둔다. 도메인 동일성 판정이 두 벌로 갈려 있었고 그 함수가 가드 두 곳의 기준이라, 접미사 누락 하나가 서로 다른 사이트를 같다고 보게 만들 뻔했다. 클린코드 규칙에 '판정 원시함수 중복 금지 + 가드는 자기 원시함수를 테스트로 고정'을 넣을 것을 제안한다.

## 근거
- registrableDomain 이 legal-url-candidates·redirect-destination 두 곳에 따로 있었고, 다중 라벨 접미사 누락으로 betus.com.pa 가 com.pa 로 잘려 그 아래 모든 도메인이 동일 사이트로 판정될 수 있었다
- 그 함수는 캡처 가드(wrong_domain)와 수집 경로 cross-site 가드가 함께 딛고 선 기준이었다 — 원시함수 하나가 상위 가드 둘을 조용히 무력화한다

