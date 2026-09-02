---
id: cafe24-renewal__2026-09-02_cafe24-platform-findings
origin_repo: cafe24-renewal
type: guide-update
target: "catalog"
refs:
  - "40_dev/snapshots/2026-09-02_cafe24-methodology-survey.md"
  - "skin-download/skin184/product/td_probe.html"
  - "0a14ba3"
  - "20_constraints/cafe24-limits.md"
friction_ref: null
created: 2026-09-02T06:38:35Z
---

## 제안
Cafe24 실측 플랫폼 지식 승격 제안: @layout 없는 커스텀 html 이 기본 레이아웃 래핑으로 즉시 렌더(모듈 데이터 페이지·판정 오라클 제작 가능), product_detaildesign 이 관리자 표시항목(.period 절대시각·할인적용가)을 방출, {$item_title}은 어트리뷰트에서 깨짐, 타임세일 앱은 등록 즉시 종료 카운트다운 노출·페이지 데이터 기준 매초 재렌더(페인트 전 MutationObserver 재기입으로 무깜빡임 교정 가능), 표시항목 인라인 스타일은 지면마다 크기 상이, SFTP 성공→웹 반영 ~50초 지연

## 근거
- 관찰 로그 793건 중 캐시 40·모듈 40·인라인 27건 — 반복 최상위 신규 테마

