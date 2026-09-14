---
id: icons__2026-09-03_wrap-generated-files-pr-conflict-race
origin_repo: icons
type: guide-update
target: "methodology.py"
refs:
  - "https://github.com/icons-hq/icons/pull/687"
friction_ref: null
created: 2026-09-03T00:49:30Z
---

## 제안
ship 이 매 커밋마다 재생성하는 `.ai/wrap-state.json`·`50_resources/prompting-report.md`·(세션 바통) `.ai/checkpoint.md` 가 모든 PR 에 들어가서, 세션 셋이 몇 분 간격으로 머지하는 날엔 **모든 열린 PR 이 main 이 움직일 때마다 DIRTY** 가 된다. DIRTY 면 GitHub 가 merge ref 를 못 만들어 pull_request CI 가 아예 시작되지 않고, land 는 CI 미확인으로 거부(fail-closed) → rebase/merge 를 4번 반복해도 다음 머지에 다시 DIRTY(실측 2026-09-02 PR #687, 약 50분 소요). 제안 = ① wrap-state·prompting-report 를 PR 에서 제외(ship 이 커밋하지 않고 main 머지 후 CI/훅이 재생성하거나 .gitignore) ② checkpoint 는 세션별 파일(`.ai/checkpoint/<session>.md`)로 분리 ③ land 에 「DIRTY 면 origin/main 자동 머지→재푸시→재시도」 1회 내장. 오탐 아닌 구조 문제.

## 근거
- (refs 참조 — 원문 정본은 이 repo)

