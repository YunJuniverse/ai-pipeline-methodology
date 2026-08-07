---
id: gamblescan__2026-07-31_orphaned-pr-branch-commits
origin_repo: gamblescan
type: friction-escalation
target: "guide-07"
refs:
  - "https://github.com/YunJuniverse/gamblescan/pull/243"
  - "https://github.com/YunJuniverse/gamblescan/pull/247"
  - "https://github.com/YunJuniverse/gamblescan/pull/249"
  - "50_resources/ai_observations/2026-07-30_migration-094-drift.md"
friction_ref: 2026-07-30_migration-094-drift
created: 2026-07-31T03:16:04Z
---

## 제안
METH-120(스택-PR 금지)의 미포착 실패모드: 열린/머지된 PR 브랜치에 커밋을 계속 쌓으면, PR이 중간 커밋에서 머지될 때 이후 커밋이 고아가 돼 프로덕션·main 미도달. 한 세션에 4회 재발(094드리프트·terms세션2·세션4·죽은도메인3차), 매번 cherry-pick 복구 비용. 규칙 승급 제안: 'PR을 연 브랜치엔 더 커밋하지 않는다 — 추가 작업은 머지 확인 후 main에서 새 분기. 1작업=1커밋=1PR, 다단계는 이전 PR 머지 후 시작.' maincheck를 Done뿐 아니라 후속작업 착수 전에도 강제.

## 근거
- 094 드리프트 자체가 동일 사고의 원조(PR#206 머지 후 같은 브랜치 추가 푸시→고아), 그걸 고치는 세션에서 같은 실수 3회 더

