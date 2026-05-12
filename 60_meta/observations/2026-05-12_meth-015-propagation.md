---
session_id: 2026-05-12_meth-015-propagation
authored_by:
  agent: claude-sonnet-4-6
  tool: claude-code-cli
  host_os: darwin-25.4
domain: meta-methodology
task_type: refactor
stack_used:
  - python3
  - git
flow_used: ad-hoc
friction:
  - id: F-001
    where: "적용 프로젝트의 local methodology.py 가 status 호출 시 자기 자신의 commit을 upstream으로 봄 — sync 직후 'behind upstream' 잘못 표시"
    cost_minutes: 1
    resolution: "RFC-001의 *알려진 한계* — upstream_commit() = git rev-parse HEAD (호출된 methodology.py 의 저장소). 진짜 upstream 비교는 *본 저장소 methodology.py*로 호출해야 함. 사용자가 본 저장소 CLI 절대 경로로 호출하는 패턴이 표준. MP-NNN 후보: 다음 RFC로 upstream URL/path 명시 옵션 추가."
    repeat_of: null
  - id: F-002
    where: "방법론 sync 결과를 ship 으로 commit/push 시도 시 wrap fail — 4 라이브 파일(HANDOFF/TODO/checkpoint/observation) 갱신 안 됨"
    cost_minutes: 0
    resolution: "방법론 sync 는 *사용자 작업*이 아닌 *자산 갱신* — manual git add + commit + push 가 자연스러움. ship 은 *프로젝트 안 사용자 작업 종료*용. 역할 분리 명확."
    repeat_of: null
  - id: F-003
    where: "talmocom 의 untracked 이미지 2건 (talmocom-home-images.png, talmocom-products-images.png) 가 git add -A 시 마이그레이션 commit에 혼입 위험"
    cost_minutes: 1
    resolution: "명시 add: 'git add -u' (modified/deleted) + 'git add .github/workflows/' (신규 워크플로). 이미지 의도적 untracked 유지. 이전 v3.1→v3.2 sync에서 채택한 동일 패턴 재사용."
    repeat_of: "F-004 (2026-05-12_v3.1-to-v3.2-migration)"
prompt_patterns:
  - intent: "3개 프로젝트 동시 pre-check → 안전 확인 후 순차 sync"
    success: true
    rounds: 1
  - intent: "sync는 manual commit, ship은 사용자 작업 종료 — 두 흐름 역할 분리"
    success: true
    rounds: 1
  - intent: "프로젝트별 동일 commit 메시지 템플릿으로 일관성 유지"
    success: true
    rounds: 1
---

3개 적용 프로젝트(icons/gamblescan/talmocom) 동시 sync 통과. 각각 7 파일 변경 + applied-ci/auto-merge 신규 주입. 60_meta 격리 3/3 ✅. F-003 *재발* — 이전 v3.1→v3.2 마이그레이션에서 한 번 학습했던 패턴 (talmocom 이미지 제외). 이건 *Catalog 승급 후보* — N≥2 목격으로 MC-NNN 승급 자격. 다음 sync 시 동일 마찰이면 적극 승급 권고. F-001 의 RFC-001 한계는 다음 RFC 후보. 자가발전 루프의 진짜 첫 회전 — 동일 마찰 재발이 *시스템에 학습된 결과*로 이어지는 사이클 시작.
