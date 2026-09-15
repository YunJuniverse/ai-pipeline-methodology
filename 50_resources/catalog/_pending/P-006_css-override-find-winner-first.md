---
id: P-006
title: "레거시 CSS 위에 override 를 얹기 전에 «현재 이기는 규칙»을 먼저 찾는다"
domain: frontend-css
status: pending
source_observations:
  - cafe24-renewal__2026-09-14_css-override-find-winner-first (capsule)
signature: "!important|specificity|:not\\(|override.*밀림|getMatchedStylesForNode"
created: 2026-09-15
last_seen: 2026-09-14
promotion_rule: "Promote to active Catalog after N>=2 observations or explicit human approval."
---

## 패턴 (Pattern)

레거시 CSS 위에 수정할 때 **더 강한 셀렉터·`!important` 를 얹는 것은 군비경쟁만 키운다.** CDP `CSS.getMatchedStylesForNode`(또는 DevTools Computed) 로 **지금 이기는 규칙과 그 출처**를 먼저 찾고, 그 출처를 고친다.

## 근거 (Evidence)

cafe24-renewal 월 7건 ~160분. override 3연패(`:not()`×4·id 4개 규칙) — 그중 하나는 같은 파일 주석에 이미 경고돼 있었다(45분). 단일 클래스 규칙이 기존 2클래스 조합에 밀리는 같은 유형이 하루 3회. 로컬 금지 규칙이 있어도 재발 → «측정 먼저» 절차화가 필요.

## 안티패턴 (Anti-Pattern)

- 안 먹으면 `!important` 추가 · 셀렉터를 길게 늘이기.
- 출처를 모른 채 같은 속성을 다른 파일에 한 번 더 선언.

## 승급 조건

타 프로젝트 레거시 CSS 작업에서 재현(N≥2)되면 active `C-NNN` 등재. 지침 20 §4 가드레일과 인접.
