---
session_id: 2026-05-14_wrap-state-commit-pre-step
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: refactor
stack_used:
  - python3
  - methodology@v4.0
flow_used: ad-hoc
friction:
  - id: F-001
    where: "push 후 갱신하면 commit 의 wrap-state.json 이 옛 baseline 가리킴. 새 clone 이 false-positive 통과"
    cost_minutes: 8
    resolution: "commit_wrap_state 를 step 6 (commit) 직전으로 이동. git add -A 가 wrap-state 갱신을 함께 staging"
    repeat_of: null
prompt_patterns:
  - intent: "commit_wrap_state 호출을 push 직후에서 commit 직전으로 이동 — clone/pull 후 wrap 일관성 보장."
    success: true
    rounds: 2
---

# wrap-state-commit-pre-step

날짜: 2026-05-15

## 패턴

초안 PR 에서 `commit_wrap_state` 를 ship 의 push *직후* 호출.

문제: 그렇게 하면 push 된 commit 의 wrap-state.json 이 *이 commit 이 만들기
직전의 baseline* 을 가리킴. clone/pull 이 commit 을 받으면 (현재 sha) != (옛
stored sha) 가 되어 wrap 이 "변경됨"으로 false-positive.

## 해결

`commit_wrap_state` 호출을 step 5 → step 6 (commit) 직전으로 이동.
git add -A 가 wrap-state.json 갱신을 함께 staging → 같은 commit 에 패키징.
clone/pull 후의 wrap 검증은 sha 일치 → no-change → fail (올바른 동작).

## 일반화 lesson

"검증 메타데이터" 파일은 *검증 대상 파일과 같은 commit* 에 들어가야 한다.
push 후 갱신 패턴은 metadata 의 commit-내-일관성을 깨뜨린다.
