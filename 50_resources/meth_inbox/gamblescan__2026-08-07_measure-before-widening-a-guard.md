---
id: gamblescan__2026-08-07_measure-before-widening-a-guard
origin_repo: gamblescan
type: friction-escalation
target: "guide-23"
refs:
  - "https://github.com/YunJuniverse/gamblescan/pull/294"
  - "00_briefs/standing/SOP_dead-domain-cleanup.md"
  - "docs/snapshots/2026-08-06_dead-domain-cleanup.md"
friction_ref: 2026-08-06_dead-casino-cleanup-post-pilot
created: 2026-08-07T00:12:25Z
---

## 제안
판정기·지문을 넓히기 전에 그 규칙이 새로 잡을 대상을 표본 실측한다. 그럴듯한 지문 하나를 근거 없이 넓혔다가 운영 중인 대상 12곳을 비활성화할 뻔했고, 적용 직전 재측정으로 막았다. 검증 규범에 '탐지 규칙 확장은 적용 전 신규 적중분 전수 재측정'을 게이트로 넣을 것을 제안한다.

## 근거
- GoDaddy pdns##.domaincontrol.com 을 주차 네임서버로 오독 — 15곳이 새로 잡혔으나 A·MX 재측정 결과 12곳이 살아있는 MX + 실호스트였다(pdns 는 Premium DNS)
- 해당 SOP 가 '살아있는 대상을 내리는 오판이 죽은 걸 놓치는 것보다 나쁘다'를 최우선 원칙으로 두고 있었고, 그 원칙이 실제로 작동한 사례

