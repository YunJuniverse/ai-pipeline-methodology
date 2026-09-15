---
id: P-008
title: "한 달치 결정을 하나의 문법으로 총정리하는 절차 — Explore 3갈래 병렬 + 사람이 걷는 순서로 집필"
domain: planning
status: pending
source_observations:
  - icons__2026-09-11_monthly-grammar-synthesis-fanout (capsule)
signature: "월간.*총정리|문법.*종합|SUPERSEDED.*판정|연대표.*어휘"
created: 2026-09-15
last_seen: 2026-09-11
promotion_rule: "Promote to active Catalog after N>=2 observations or explicit human approval."
---

## 패턴 (Pattern)

한 달치 결정(ADR·설계서·계약·관찰 로그·TODO Done·HANDOFF)을 하나의 문법으로 총정리하는 절차.

1. **Explore 3갈래 병렬**(지침 08): ① 결정 기록에서 규칙과 SUPERSEDED 판정 ② 화면·컴포넌트 계약에서 현행 값 ③ 관찰·Done·prompting-report 에서 PM 발언 연대표·반복 원칙·기각·어휘 대조.
2. **본문은 사람이 걷는 순서로 직접 집필**(문제 → 왜 → 도출 → 적용). 팬아웃 결과를 이어 붙이지 않는다.
3. 부록: 연대표 · 반복 원칙 · 어휘. 문서 간 불일치는 말미에 기록. 뷰어 등록.

## 근거 (Evidence)

소스 30+ 문서·관찰 236건 → 본문 10절 + 부록 3 을 하루에(icons).

## 승급 조건

타 프로젝트에서 같은 종합 절차가 필요해 재현(N≥2)되면 active 등재 후 `skeleton/planning` bake 검토. Pending 은 bake-in 대상이 아니다.
