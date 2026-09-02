---
id: icons__2026-08-22_land-classifier-cries-wolf
origin_repo: icons
type: tool-change
target: "tool/land"
refs:
  - "https://github.com/icons-hq/icons/pull/381"
  - "https://github.com/icons-hq/icons/pull/356"
  - "de432c9"
friction_ref: 2026-08-22_sync-data-bounded-internal-refs
created: 2026-08-22T13:21:56Z
---

## 제안
land의 Class B/C 스캐너가 «파일에 결제 단어가 있는가»를 보지만 기준은 «결제 정책을 바꾸는가»다. 생성물이 개행 0개 단일 라인 JSON이면 한 글자 변경에도 전 코퍼스가 추가된 줄로 잡혀 3회 연속 오탐했다. 반복 오탐이 운영자를 '또 오탐'으로 길들여, 진짜 결제 내용이 섞인 PR을 하마터면 통과시킬 뻔했다. 용어별 순증(added-removed) 기준 판정과 단일 라인 블롭 예외를 제안한다.

## 근거
- 3회 연속 오탐: PR #355·#356·#381 — 전부 sync-data 산출물(search-index.json = 개행 0개 블롭)
- 순증 측정 시 결제 364→364·과금 43→43·가격 78→78 — 실제 추가 0인데 트리거
- 위험: #381에서는 복원 문서에 실제 신규 가격(유상 럭키드로우 12,000원)이 있었고, 앞선 오탐 경험 때문에 '또 오탐'으로 넘길 뻔했다 — 파일별 재검증으로 발견

