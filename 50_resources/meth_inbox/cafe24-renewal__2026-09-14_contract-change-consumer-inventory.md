---
id: cafe24-renewal__2026-09-14_contract-change-consumer-inventory
origin_repo: cafe24-renewal
type: friction-escalation
target: "guide-23"
refs:
  - "0dae70d"
  - "20_guides/23_검증_규범.md"
friction_ref: 2026-09-04_event-card-member-dealprice
created: 2026-09-14T07:06:45Z
---

## 제안
규칙·데이터 계약·셀렉터를 바꿀 때 그 계약의 소비처 인벤토리(grep 전수)를 먼저 만들고 전부 반영하는 절차의 승급 제안 — 지침 23 '키로 조회하는 전 지점 목록화'를 계약 일반으로 확장. 한 소비처만 고치는 반쪽 반영이 월 11건 ~240분 재발

## 근거
- 같은 데이터를 읽는 파서 2곳 중 한 곳에만 마크업 규칙 반영 → 3일 뒤 발주처 실사고 제보(40분)
- 셀렉터 그룹 14곳 수동 복제 누락·목록형 설정 누락·높이 상수 30여 곳 산재·요소 타입 교체 후 그 타입을 노리던 규칙 무음 무효화

