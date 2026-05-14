---
session_id: 2026-05-12_ship-and-hooks-and-automerge
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: feature
stack_used:
  - python3
  - git
  - github-actions
flow_used: ad-hoc
friction:
  - id: F-001
    where: "사용자가 매 작업 종료 시 git add/commit/push 3단계를 수동 입력 — TODO 미갱신 통증과 결합되면 4 파일 갱신·검증까지 7단계"
    cost_minutes: 0
    resolution: "methodology ship -m '...' 단일 명령으로 wrap+manifest-check+sensitive+(test/build)+add+commit+push 7단계 통합. 실패 시 명확한 단계 표시로 즉시 진단 가능."
    repeat_of: null
  - id: F-002
    where: "git add -A 가 무관 파일·sensitive 파일을 우연히 commit에 끌어들일 위험 (.env, credentials, *.pem)"
    cost_minutes: 1
    resolution: "ship 의 step 3/7 sensitive 검사 — _SENSITIVE_PATTERNS 매칭 시 차단, --allow-sensitive 옵션으로 의식적 우회. .sample/.example 확장자는 통과."
    repeat_of: null
  - id: F-003
    where: "ship CLI를 의식적으로 호출하지 않으면 우회됨 — AI가 git push 직접 호출하면 검증 0"
    cost_minutes: 2
    resolution: "methodology hooks install — .git/hooks/pre-push 에 manifest-check + wrap --strict 자동 등록. git push 어디서든 검증 통과 못 하면 차단. 우회는 --no-verify 명시 (의식적 비상 탈출)."
    repeat_of: null
  - id: F-004
    where: "worktree 환경에서 .git 이 파일(gitlink)이라 hooks 경로 직접 계산 어려움"
    cost_minutes: 2
    resolution: "git rev-parse --git-path hooks 로 정확한 hooks 디렉터리 얻기. 절대/상대 모두 처리. worktree에서도 정상 동작."
    repeat_of: null
  - id: F-005
    where: "PR 모델 전환 시 사용자가 매 PR 머지 버튼 클릭 — auto-merge 라벨로 자동화 가능"
    cost_minutes: 0
    resolution: "methodology-auto-merge.yml — 'auto-merge' 라벨 + 모든 check 통과 시 gh pr merge --auto --squash. 외부 action 의존 없음. 본 저장소 + 적용 프로젝트 모두 shared_paths로 전파."
    repeat_of: null
prompt_patterns:
  - intent: "사용자 워크플로의 7단계 통증을 1단계 명령으로 압축"
    success: true
    rounds: 1
  - intent: "안전망 이중화 — ship 안의 검증 + pre-push hook (의식적 호출 + 자동 강제)"
    success: true
    rounds: 1
  - intent: "외부 GitHub Action 의존 없이 gh CLI로 auto-merge 워크플로 구성"
    success: true
    rounds: 1
---

ship+hooks+auto-merge 3축 동시 도입. ship은 *의식적 호출*, hooks는 *우회 차단*, auto-merge는 *PR 모델 전환 시 머지 부담 0*. 세 가지가 결합되면 사용자의 작업 종료 명령은 `methodology ship -m "..."` 한 줄로 압축. MP-NNN 후보: F-003(검증 우회 가능성)은 다음 v3.x 마이그레이션에서 *새 검증 추가 시* 재발할 패턴 — hook에 누락되면 우회. 다음 부팅 시 ship 첫 시연이 본 commit 자체.
