---
id: icons__2026-08-27_isolated-worktree-for-concurrent-sessions
origin_repo: icons
type: guide-update
target: "guide-08"
refs:
  - "https://github.com/icons-hq/icons/pull/447"
friction_ref: null
created: 2026-08-27T00:58:48Z
---

## 제안
동시 세션이 한 체크아웃을 공유하면 브랜치 전환·커밋·배포가 서로를 덮는다. origin/main 기반 격리 워크트리에서 작업·커밋·PR·배포하는 절차를 지침화하자. 배포 시 .vercel/project.json 을 복사하지 않으면 엉뚱한 프로젝트가 새로 생기는 함정도 포함한다.

## 근거
- 브랜치 전환이 남의 미커밋 작업 때문에 거부되고, 그대로 배포하면 검토 안 된 변경이 프로덕션에 나간다
- 격리 워크트리에는 .vercel 링크가 없어 vercel deploy 가 새 프로젝트를 만들었다 — 링크 복사 후 재배포하고 잘못 생긴 프로젝트를 삭제했다

