---
session_id: 2026-05-13_multi-dashboard-and-branches
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: feature
stack_used:
  - python3
  - git-worktree
flow_used: ad-hoc
friction:
  - id: F-001
    where: "여러 dashboard 동시 운영 불가 — 8765 고정 + 다른 프로젝트면 종료 후 재시작"
    cost_minutes: 0
    resolution: "포트 자동 할당 (8765-8799 빈 포트 탐색), ~/.methodology-dashboards.json 레지스트리에 (port, root, branch, pid, started_at) 기록. 같은 (root, branch) 재호출은 재사용. _registry_cleanup 으로 죽은 항목 자동 제거. methodology dashboard list/stop 서브커맨드 추가."
    repeat_of: null
  - id: F-002
    where: "다른 브랜치 dashboard 를 보고 싶지만 working tree 전환 위험 (미커밋 변경 충돌)"
    cost_minutes: 0
    resolution: "methodology dashboard --branch <name> 옵션 — git worktree add --detach 로 ~/.methodology-cache/<project>/<branch-slug>/ 에 격리 추출 → 거기서 빌드 → 별도 포트 서빙. 정리는 methodology dashboard stop --port <N> 호출 시 worktree remove --force 자동. working tree 절대 안 건드림."
    repeat_of: null
  - id: F-003
    where: "Edit 도구가 def _port_in_use 함수 body 를 날려버림 — old_string=한 줄 함수 시그니처, new_string=새 블록 + 함수 시그니처. 결과적으로 빈 stub 생성, 원본 body 어디로 사라짐"
    cost_minutes: 5
    resolution: "grep -n 으로 중복 정의 탐지 → 빈 stub 제거. 교훈: Edit 의 old_string 이 함수 시그니처 한 줄이면 body 까지 포함해서 매칭해야. 단일 식별자성 라인을 분기점으로 쓰면 위험."
    repeat_of: null
  - id: F-004
    where: "git branch -a 출력의 '+' prefix (다른 worktree 에서 체크아웃된 브랜치 표시) 가 브랜치 이름에 섞임 — '+ claude/lucid-...'"
    cost_minutes: 1
    resolution: "정규식 re.sub(r'^[*+-]\\s+', '', s) 로 모든 prefix 마커 제거. '*' (현재), '+' (다른 worktree), '-' (없을지 모름) 모두 처리. 사전에 시뮬레이션 어려운 worktree 환경 특유 출력."
    repeat_of: null
  - id: F-005
    where: "spawn 시 적용 프로젝트의 local methodology.py 가 옛 버전이면 --branch 옵션 모름 → spawn 실패"
    cost_minutes: 0
    resolution: "spawn 동작 자체는 본 저장소(generate-dashboard.py 가 호출됨 → 본 저장소 자기 root 의 60_tools/methodology.py)에서 OK. 단 적용 프로젝트는 sync 전까지 옛 동작. 알려진 한계 (F-001 of 2026-05-12_meth-015-propagation 와 동일 패턴 — N=4 째 목격, MC-002 승급 더 명백해짐)."
    repeat_of: 2026-05-12_meth-015-propagation
prompt_patterns:
  - intent: "여러 dashboard 동시 + 브랜치 라디오 — 별도 포트 spawn 방식 (A)"
    success: true
    rounds: 1
  - intent: "git worktree add --detach 로 working tree 격리 → 빌드 → stop 시 정리"
    success: true
    rounds: 1
  - intent: "registry JSON (~/ 홈 디렉터리) + _registry_cleanup 으로 죽은 항목 자동 제거"
    success: true
    rounds: 1
---

여러 dashboard 동시 + 브랜치별 spawn 완성. 핵심: 포트 자동 할당 + worktree 격리 + 레지스트리 자동 정리. UI 측 Local Dashboards 카드 + Branches 라디오 → /api/dashboard/spawn POST → 별도 포트에 spawn → window.open. F-003 (Edit 도구 함수 body 손실) 은 *방법론 외* 도구 마찰이라 catalog 후보 아님. F-005 = METH-020 MC-002 승급 후보 N=4 도달 — 매 CLI 변경 시 적용 프로젝트가 옛 동작. *근본 해결*은 적용 프로젝트가 본 저장소 CLI 를 symlink 또는 PATH 로 참조하는 메커니즘. 다음 v3.x 후보.
