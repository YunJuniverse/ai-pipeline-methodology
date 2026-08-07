---
id: lifeManager__2026-08-07_scoped-bulk-edit
origin_repo: lifeManager
type: guide-update
target: "guide-19"
refs:
  - "src/app/budget/page.tsx"
friction_ref: 2026-08-06_scenic-budget-habits
created: 2026-08-07T00:32:05Z
---

## 제안
일괄 치환(정규식·sed)은 **매칭 단위를 최소 범위로 좁히고 카나리로 검증**한다는 규칙 제안. 이번 세션에서 className 공백 정리용 re.sub(r'\\s+"','"') 를 파일 전체에 걸어 import 문까지 파괴했다(from "next" → from"next"). 타입체크는 통과해 조용히 넘어갈 뻔했다. 규칙: ① 치환 대상을 캡처 그룹 안쪽으로 한정 ② 치환 전후로 건드리면 안 되는 라인(import 등)을 카나리로 grep 검증.

## 근거
- (refs 참조 — 원문 정본은 이 repo)

