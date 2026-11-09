---
id: P-012
title: "브라우저 자동화 도구의 입력·관측 특이 동작은 재발견하지 말고 표로 확인한다"
domain: verification
status: pending
source_observations:
  - lifeManager__2026-10-21_n2n-admin-extend
  - lifeManager__2026-10-21_n2n-redesign-verify
  - lifeManager__2026-10-26_n2n-changes-screenshots
  - lifeManager__2026-11-04_music-lib
  - gamblescan (기기 폭 375 넘침 판정 — 에뮬레이션 innerWidth)
signature: "form_input|onChange|sr-only|window.confirm|스무스 스크롤|스크린샷.*파일|innerWidth|에뮬레이션.*넘침"
created: 2026-11-09
last_seen: 2026-11-04
promotion_rule: "lifeManager 10건(96분) + gamblescan 1 — 2번째 repo 에서 같은 표 항목이 재현되면 active."
---

## 패턴 (Pattern)

| 증상 | 원인 | 처리 |
|---|---|---|
| 값을 넣었는데 상태가 안 바뀜 | 값 직접 설정이 React `onChange` 를 안 일으킴 | 실제 키 입력(type) 또는 네이티브 setter + `input` 이벤트 |
| 클릭이 안 먹는 라디오·체크박스 | `sr-only` 로 숨긴 입력 | 라벨 클릭 또는 폼 입력 도구 |
| 확인 창 뒤 진행 안 됨 | `window.confirm` 자동 거부 | 테스트에서 `confirm` 대체 또는 대화상자 처리 |
| 애니메이션 값이 이상함 | 백그라운드 탭 정지 | C-002 |
| 스크롤 후 재현됐다 사라짐 | `scroll-behavior: smooth` 진행 중 측정 | `behavior: "instant"` 로 스크롤 후 측정 |
| 모바일 넘침 0 인데 실기기에선 넘침 | 에뮬레이션이 `innerWidth` 를 키움 | 기준 폭 명시 + `scrollWidth` 실측(지침 23 §2-9) |
| dev 서버 기동 뒤 셸 전체 exit 1 | 포그라운드 기동이 셸을 점유 | 백그라운드·프리뷰 도구로 기동 |
| 로그인 벽 | 매번 우회 | 로컬 전용 테스트 계정 시드(지침 23 §3-5) |

## 근거 (Evidence)

lifeManager 10건 96분 — 같은 날 서로 반대 방향(onChange 불발 vs sr-only 라디오는 폼 입력 필요)이 함께 나와 «한 도구가 늘 맞다»가 성립하지 않음을 보였다.
