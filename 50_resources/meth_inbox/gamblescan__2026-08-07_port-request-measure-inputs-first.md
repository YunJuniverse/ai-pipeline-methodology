---
id: gamblescan__2026-08-07_port-request-measure-inputs-first
origin_repo: gamblescan
type: guide-update
target: "guide-24"
refs:
  - "https://github.com/YunJuniverse/gamblescan/pull/299"
  - "docs/adr/ADR-0017-sportsbook-trust-score-scope.md"
  - "src/domain/trust-score/boundary.ts"
friction_ref: 2026-08-06_sportsbook-trust-adr
created: 2026-08-07T00:12:51Z
---

## 제안
'A도 B에 맞춰줘' 형태의 이식 요청은 착수 전에 입력 가용성부터 측정한다. 겉보기엔 포팅이지만 입력이 없으면 그것은 새 정의를 만드는 일이고 등급이 달라진다. 착수 게이트에 '이식 요청 = 입력 축 실측 → 부재분이 크면 Class C 에스컬레이션'을 절차로 넣을 것을 제안한다.

## 근거
- 요청받은 점수 체계의 입력 5축을 대상에 대보니 가중치 60%에 데이터가 아예 없었다(분쟁 테이블이 다른 엔티티 전용·KYC·보너스 없음)
- 그대로 만들었다면 같은 UI 에 정의가 다른 점수가 떠 비교 가능한 척하는 값이 됐다. 코드가 이미 '스코어 정의 변경은 Class C' 를 명시하고 있었고, 선행 채점 실행조차 승인 대기였다

