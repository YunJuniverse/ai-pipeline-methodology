---
id: icons__2026-09-11_ci-absent-local-replication-gate
origin_repo: icons
type: guide-update
target: "guide-land"
refs:
  - "00_briefs/standing/SOP_plan-viewer-merge-deploy.md"
  - "https://github.com/icons-hq/icons/pull/921"
friction_ref: null
created: 2026-09-11T03:22:59Z
---

## 제안
CI 가 결제·인프라 사유로 아예 안 돌 때(잡 스텝 0개, annotations 에 billing) CI green 자동 머지 규칙을 그대로 두면 모든 PR 이 멈춘다. 절차: 잡 annotations 로 원인 확인 → PM 명시 판정을 TODO Blocked 에 박제 → CI 단계를 로컬에서 그대로 재현(manifest-check, observe validate 전수, dashboard build)과 앱 게이트(lint, 검증, build-guard) 통과 시에만 land no-ci-check → PR 본문에 CI 없이 머지·로컬 재현 통과 한 줄 → 결제 복구 시 원복. land 에 local-ci 옵션으로 재현 자동화 제안.

## 근거
- PM 2026-08-20 결제 안 하고 알아서 배포, 2026-09-09 재확인 결제 안 풀거야 CI 없이 진행

