---
id: cafe24-renewal__2026-09-14_absence-verdict-observation-conditions
origin_repo: cafe24-renewal
type: guide-update
target: "guide-23"
refs:
  - "0436a17"
  - "40_dev/snapshots/2026-09-11_final-meeting-prep.md"
  - "20_guides/24_착수_게이트.md"
friction_ref: 2026-09-11_alpha-lazyload-misdiagnosis
created: 2026-09-14T07:06:45Z
---

## 제안
'없다·비었다' 판정은 관측 조건 검증 후에만 — 지침 24 §2 '부재≠미포착'을 UI 검증 절차로 구체화: 지연로딩은 실제 스크롤 입력 후 측정, 백그라운드 탭·UA·세션·표본 범위를 판정문에 명시, 부재 판정 전 스크린샷 육안 대조 필수. 수치 0·1px 만으로 부재 단정 금지

## 근거
- 지연로딩 위젯을 scrollIntoView 로 재 1px 자리표시를 '빈 위젯'으로 오판 → 발주처 회신문안·최종 미팅 안건까지 오염(90분, 4일 방치)
- 같은 유형 월 9건 ~320분: lazy 이미지 높이0·백그라운드 탭 rAF 정지·데스크톱UA에서 앱 미주입·내 세션 1페이지 vs 발주처 3페이지·표본 6파일로 '1개뿐'

