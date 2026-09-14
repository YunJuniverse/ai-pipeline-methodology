---
id: cafe24-renewal__2026-09-14_css-override-find-winner-first
origin_repo: cafe24-renewal
type: pattern
target: "catalog"
refs:
  - "50af7b8"
  - "CLAUDE.md"
friction_ref: 2026-09-01_header-icon-black-tabbar-noline
created: 2026-09-14T07:06:45Z
---

## 제안
레거시 CSS 위에 수정할 때 override 를 얹기 전에 CDP getMatchedStylesForNode 등으로 현재 이기는 규칙을 먼저 찾아 그 출처를 고치는 절차 제안 — 더 강한 셀렉터·!important 추가는 군비경쟁만 키운다. 로컬 금지 규칙이 있어도 월 7건 ~160분 재발해 '측정 먼저' 절차화가 필요

## 근거
- override 3연패(:not()×4·id 4개 규칙) — 그중 하나는 같은 파일 주석에 이미 경고돼 있었음(45분)
- 단일 클래스 규칙이 기존 2클래스 조합에 밀리는 같은 유형이 하루 3회

