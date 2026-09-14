---
id: icons__2026-09-09_land-merge-ref-race
origin_repo: icons
type: tool-change
target: "tool/land"
refs:
  - "https://github.com/icons-hq/icons/pull/907"
  - "6b1dfae336c5d81aef5047205e49f20add49ce48"
  - "https://github.com/icons-hq/icons/pull/885"
  - "https://github.com/icons-hq/icons/pull/876"
friction_ref: null
created: 2026-09-09T02:58:33Z
---

## 제안
병렬 세션이 많아 main 이 1~2분마다 움직이면 PR 의 CI 잡이 '스텝 0개·로그 없음' 으로 실패한다 — 내용 오류가 아니라 러너가 잡을 집기 전에 PR 머지 참조(refs/pull/N/merge)가 사라진 경합이다. land 는 ① 잡 스텝 0개 실패를 '경합' 으로 분류해 내용 오류와 구분하고 ② 리베이스→푸시 뒤 재푸시 없이 CI 한 사이클(≥2분)을 기다리며 ③ 로컬 wrap --strict·lint·manifest 가 통과한 Class A 문서 PR 은 CI 완료를 기다리지 않고 즉시 머지하는 경로를 둔다. 재시도 루프의 푸시 간격이 CI 1회보다 짧으면 매 푸시가 앞 실행을 죽여 영원히 못 붙는다.

## 근거
- #907: 리베이스→푸시 6회, methodology-validate 잡 6회 모두 steps=0 실패, 로컬 validate 4단계 전부 통과 → 리베이스 직후 CI 미대기 머지로 착지(2026-09-09)
- #876·#885·#893: 착지마다 리베이스 2~3회 — 살아 있는 파일 4종 충돌(2026-09-08~09)

