---
id: icons__2026-09-01_repo-name-from-git-common-dir
origin_repo: icons
type: tool-change
target: "tool/capsule"
refs:
  - "60_tools/methodology.py:1208"
  - "https://github.com/icons-hq/icons/pull/667"
friction_ref: null
created: 2026-09-01T08:58:55Z
---

## 제안
_repo_name 이 디렉터리명을 그대로 써서 워크트리에서 발행한 캡슐이 워크트리명을 origin_repo·id 로 갖는다. 캡슐 id 는 _collect_plan 의 중복 수거 방지 키라 같은 제안이 워크트리마다 다른 id 로 갈라져 중복 적재된다. git --git-common-dir 로 주 체크아웃 이름을 쓰도록 교정.

## 근거
- 상류 원장 실사례 — 'gamblescan-p0-pr__2026-08-13_...' 2건이 repo=gamblescan 인데 id 접두는 워크트리명. 원장 21건 중 이미 오염
- icons outbox 실측 — 17건 중 3건이 워크트리명 키(priceless-perlman-c80820 ×2 · icons-wt-hub ×1). 그중 2건은 같은 제안의 중복 캡슐이었다(수거 전 통합·id 교정 완료)
- 증상 2 — capsule --validate 가 타 워크트리 발행 캡슐을 'id는 <origin_repo>__<stem> 이어야' 로 오검증. 교정 후 icons 전 캡슐 15건 검증 통과
- 교정 = git rev-parse --git-common-dir 의 위치를 repo 이름으로. 실측 8종 통과 — 주 체크아웃·중첩 워크트리(.claude/worktrees/*)·형제 워크트리·일반 repo·그 워크트리·bare(.git 접미사 제거)·bare 워크트리·非git 폴백

