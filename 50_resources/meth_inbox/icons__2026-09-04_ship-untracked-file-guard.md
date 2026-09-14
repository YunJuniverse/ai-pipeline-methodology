---
id: icons__2026-09-04_ship-untracked-file-guard
origin_repo: icons
type: guide-update
target: "methodology"
refs:
  - "PR icons-hq/icons#738"
  - "PR icons-hq/icons#740"
  - "METH-142 · 20_guides/30_동시_세션_git_격리.md"
friction_ref: null
created: 2026-09-04T06:49:02Z
---

## 제안
ship 의 git add -A 가 공유 워크트리에서 다른 세션의 미커밋 파일을 담아 main 에 올린 사고가 2건(2026-09-01 화장실 회색상자 · 2026-09-04 소화전 호스 회색상자). 한 번 격리해도 «다음 ship» 이 다시 담는다 — 사람 규율이 아니라 ship 자체가 커밋 직전 미추적/미커밋 파일을 열거해 확인을 요구하거나(--allow-foreign 없으면 거부) 브랜치 범위 밖 파일을 빼도록 제안

## 근거
- (refs 참조 — 원문 정본은 이 repo)

