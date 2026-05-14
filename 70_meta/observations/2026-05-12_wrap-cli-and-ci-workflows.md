---
session_id: 2026-05-12_wrap-cli-and-ci-workflows
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: feature
stack_used:
  - python3
  - github-actions
flow_used: ad-hoc
friction:
  - id: F-001
    where: "CLAUDE.md/AGENTS.md의 'After every task' 규칙이 강제력 부족 — AI가 자주 깜빡함"
    cost_minutes: 0
    resolution: "wrap CLI + managed 마커 안 규칙 보강. (α) AI 자동 작성 → wrap 검증 패턴 채택."
    repeat_of: null
  - id: F-002
    where: "본 저장소 전용 CI와 적용 프로젝트 주입 CI를 같은 .github/workflows/ 디렉터리에 두면 sync가 둘 다 복사할 위험"
    cost_minutes: 2
    resolution: "shared_paths에 `.github/workflows/methodology-applied-ci.yml` *단일 파일* 명시. source-ci는 디렉터리 안에 있지만 MANIFEST에 없어 격리. 실측으로 검증."
    repeat_of: null
  - id: F-003
    where: "wrap CLI를 사용자 호출 시 *AI가 갱신을 자동 수행*하는 (α) 패턴이 wrap 자체에 들어갈 수 없음 — wrap은 *검증*만"
    cost_minutes: 3
    resolution: "역할 분리 — wrap=검증, AI 갱신=CLAUDE.md/AGENTS.md 규칙. wrap은 4/4 ✓이면 통과, ✗이면 AI가 재시도. 검증 비용 작아 hook으로도 사용 가능."
    repeat_of: null
prompt_patterns:
  - intent: "두 요청을 같은 답변에서 처리하되 메커니즘 분리 (로컬 hook vs CI)"
    success: true
    rounds: 1
  - intent: "managed 마커 안 규칙 보강 → sync로 모든 적용 프로젝트 자동 전파"
    success: true
    rounds: 1
  - intent: "워크플로 디렉터리 격리 (shared_paths 단일 파일 명시)"
    success: true
    rounds: 1
---

wrap CLI의 핵심 통찰: *AI 자동 갱신 vs 검증 도구*를 분리해야 (α) 패턴이 성립. CLAUDE.md/AGENTS.md 규칙으로 갱신 강제, wrap으로 검증. CI 워크플로는 source/applied 분리 — shared_paths 단일 파일 명시로 격리 보증. 다음 v3.x 마이그레이션 후보: wrap 결과를 다음 세션 컨텍스트에 자동 주입하는 메커니즘(현재 사용자가 보고 다음 turn에 반영). MP-NNN 추가 후보 F-002(워크플로 디렉터리 격리 패턴) — 다음 .github/ 자산 추가 시 같은 함정에 빠질 가능성.
