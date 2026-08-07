# Thinktank v0 — 2026-W32

> **수동 승급이 정식.** 이 리포트는 지표 집계 + 승급 *후보* 마킹만 한다 — 자동 승급 없음.
> 승급은 사람이 PR로(백서 §8-2). 분기 회고 §1 지표의 소스 — 회고 직전 실행.
> Generated at: 2026-08-07T03:14:18Z

## 지표 (Metrics)

- 관찰 로그: **136건** (충족)
- 기간: 2026-05-07 ~ 2026-07-29 (83일)
- 케이던스: 주당 약 11.5건
- task_type 분포: docs 71, feature 23, refactor 19, bugfix 16, research 6, bootstrap 1
- 마찰 총계: 22건 · Catalog 재적중(repeat_of): 7건 · 승급 후보(≥2회): 2건

## Repeated Friction Candidates

- `PROMOTE-CANDIDATE` x2: TODO 섹션 이동 스크립트의 문자열 index() 오매칭
- `PROMOTE-CANDIDATE` x2: 다운스트림 pre-push wrap 훅이 상류 sync push 차단
- `watch` x1: .git write lock
- `watch` x1: HANDOFF.md Working-on 단일 불릿을 부분 문장만 교체하면 이전 task 텍스트가 잔존
- `watch` x1: ai-icons push
- `watch` x1: browser preview
- `watch` x1: init 스캐폴드 HANDOFF
- `watch` x1: ship push step
- `watch` x1: stacked-PR을 순차 머지했으나 GitHub 재타깃 미작동으로 #85/#86/#87이 main 아닌 중간 브랜치에 머지돼 096~098이 main 미반영
- `watch` x1: sync 결과 검증 시 git ls-tree가 한글 파일경로를 octal-escape → grep이 커스텀 guide 못 찾아 '데이터 손실' 오탐 발생
- `watch` x1: sync 커밋 스테이징
- `watch` x1: sync-all 비-main repo 체크아웃
- `watch` x1: sync가 상류에서 삭제된 파일을 다운스트림에서 auto-prune 안 함(--prune은 고유 파일도 삭제해 부적합) — 티어/파일 폐지 전파 시 repo마다 수동 git rm 필요
- `watch` x1: worktree push 직전 origin 전진
- `watch` x1: 그래프 레이아웃
- `watch` x1: 다운스트림 sync 커밋 시 git add -A 가 icons-invest 미커밋 프로젝트 WIP(30_planning 사업기획서 3줄)를 methodology-sync 커밋에 쓸어담음 — 초기 dirty=0였으나 sync 시점엔 WIP 존재
- `watch` x1: 다운스트림(icons-invest)에 축적된 대량 도메인 작업을 상류 방법론으로 역환류할 때 원료가 스냅샷·빌드스크립트·관찰로그 3곳에 흩어져 통독 비용 큼
- `watch` x1: 대시보드(generate-dashboard.py) sprint 결합이 15+ JS 사이트에 산재 — 티어 제거 시 데이터+UI+호출부 모두 추적 필요
- `watch` x1: 새 세션이 부팅 계약(브리프 로드·dashboard)을 건너뛰고 IR 질문에 바로 뛰어들어 기존 프로세스 모른 채 오답 — 부팅 강제장치 없음 + HANDOFF 81KB 비대화로 부팅 프라이머 무력
- `watch` x1: 한글 파일명·본문 편집을 perl/sed+hex로 하니 개행 삭제·인코딩 mojibake 발생(doc_id·title 병합)

## Observations

- `2026-05-07_l1-observe-flow` — domain `meta`, task `docs`
- `2026-05-15_applied-ci-source-repo-skip` — domain `meta`, task `bugfix`
- `2026-05-15_methodology-integrity-3-fixes` — domain `meta`, task `refactor`
- `2026-05-15_observation-lint-policy-realignment` — domain `meta`, task `bugfix`
- `2026-05-15_qa-dashboard-obs-and-commands-stale` — domain `meta`, task `bugfix`
- `2026-05-15_stack-bento-card-overview` — domain `meta`, task `feature`
- `2026-05-15_stack-cleanup-from-design-handoff` — domain `meta`, task `refactor`
- `2026-05-17_kanban-live-refresh-and-meth016` — domain `meta`, task `feature`
- `2026-05-17_meth-019-020-013-catalog-adr` — domain `meta`, task `docs`
- `2026-05-17_meth-022-hook-sync-skip-and-backlog` — domain `meta`, task `feature`
- `2026-05-17_meth-034-tshome-migration-and-propagation` — domain `meta`, task `bugfix`
- `2026-05-17_pr22-23-four-project-sync-propagation` — domain `meta`, task `docs`
- `2026-05-17_qa3-commands-json-coverage` — domain `meta`, task `docs`
- `2026-05-17_qa4-dashboard-layout-helper` — domain `meta`, task `refactor`
- `2026-05-17_qa5-launcher-3tier-detection` — domain `meta`, task `bugfix`
- `2026-05-17_sync-worktree-stale-guard` — domain `meta`, task `bugfix`
- `2026-05-18_dashboard-api-servers-start-path-augment` — domain `meta`, task `bugfix`
- `2026-05-18_gitignore-propagation-and-cache-copy-exclusion` — domain `meta`, task `bugfix`
- `2026-05-18_meth-018-hooks-stale-reinstall` — domain `meta`, task `bugfix`
- `2026-05-18_meth-038-propagate-4-projects` — domain `meta`, task `refactor`
- `2026-05-18_session-closeout-meth-036-038-018` — domain `meta`, task `docs`
- `2026-05-18_ship-npm-manager-run-fix` — domain `meta`, task `bugfix`
- `2026-06-23_live-files-cleanup-meth-039-merged` — domain `meta`, task `docs`
- `2026-06-23_meth-039-planning-craft-injection` — domain `meta`, task `docs`
- `2026-06-23_meth-040-inject-planning-craft-from-gamblescan` — domain `meta`, task `docs`
- `2026-06-23_meth-041-icons-section19-compression-backfill` — domain `meta`, task `docs`
- `2026-06-23_meth-042-original-planning-corpus-direct-study` — domain `meta`, task `docs`
- `2026-06-23_meth-043-lean-doc-craft-from-icons-ip` — domain `meta`, task `docs`
- `2026-06-23_meth-044-mode-template-catalog-design-backlog` — domain `meta`, task `docs`
- `2026-06-24_meth-044-template-mode-catalog` — domain `meta`, task `docs`
- `2026-06-24_meth-045-whitepaper-guide-notion` — domain `meta`, task `docs`
- `2026-06-24_meth-046-sync-no-mirror-delete` — domain `meta`, task `bugfix`
- `2026-06-24_meth-047-clean-architecture-clean-code-guide` — domain `meta`, task `docs`
- `2026-06-24_meth-048-whitepaper-onboarding-codequality-integration` — domain `meta`, task `docs`
- `2026-06-29_frontend-design-token-foundation` — domain `meta`, task `docs`
- `2026-06-29_meth-049-downstream-propagation` — domain `meta`, task `docs`
- `2026-06-29_meth-049-gamblescan-validation` — domain `meta`, task `research`
- `2026-06-29_meth-050-promote-c001` — domain `meta`, task `docs`
- `2026-07-08_meth-051-output-channel-separation-guide` — domain `meta`, task `docs`
- `2026-07-08_meth-053-guide-renumber-and-rfc-recovery` — domain `meta`, task `refactor`
- `2026-07-08_meth-054-first-quarterly-retrospective` — domain `meta`, task `docs`
- `2026-07-08_meth-055-accept-rfc002` — domain `meta`, task `docs`
- `2026-07-08_meth-056-compaction-protocol` — domain `meta`, task `feature`
- `2026-07-08_meth-057-metrics-thinktank-reframe` — domain `meta`, task `feature`
- `2026-07-08_meth-058-onboarding-band-diet` — domain `meta`, task `refactor`
- `2026-07-08_meth-059-roadmap-closure-r3-r4` — domain `meta`, task `feature`
- `2026-07-08_meth-060-downstream-sync-propagation` — domain `meta`, task `docs`
- `2026-07-08_meth-061-planning-handoff-mode` — domain `meta`, task `feature`
- `2026-07-08_meth-062-api-contract-devspec-guide` — domain `meta`, task `feature`
- `2026-07-08_meth-062-recovery-pr51-timing` — domain `meta`, task `bugfix`
- `2026-07-08_meth-063-business-plan-revamp` — domain `meta`, task `docs`
- `2026-07-08_meth-064-service-plan-index-model` — domain `meta`, task `docs`
- `2026-07-08_meth-065-child-templates-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-066-requirements-spec-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-067-prd-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-068-kpi-tree-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-069-context-glossary-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-070-architecture-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-071-data-model-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-072-downstream-sync` — domain `meta`, task `docs`
- `2026-07-09_meth-073-ops-plan-guide-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-074-marketing-plan-guide-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-075-brand-plan-guide-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-076-pm-plan-guide-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-077-ai-feature-guide-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-078-eval-guardrail-guide-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-079-orchestration-guide-refresh` — domain `meta`, task `docs`
- `2026-07-09_meth-080-master-plan-ssot-refactor` — domain `meta`, task `refactor`
- `2026-07-09_meth-081-prompts-modernization` — domain `meta`, task `refactor`
- `2026-07-09_meth-082-operating-principles-review` — domain `meta`, task `refactor`
- `2026-07-09_meth-083-meta-files-modernization` — domain `meta`, task `research`
- `2026-07-09_meth-084-skeleton-activation` — domain `meta`, task `refactor`
- `2026-07-09_meth-085-friction-capture-rule` — domain `meta`, task `feature`
- `2026-07-09_meth-086-sprints-collapse-todo-wip` — domain `meta`, task `refactor`
- `2026-07-09_meth-087-downstream-sync-086` — domain `meta`, task `refactor`
- `2026-07-09_meth-088-downstream-sync-holds` — domain `meta`, task `refactor`
- `2026-07-09_meth-089-guide-number-remediation` — domain `meta`, task `refactor`
- `2026-07-09_meth-090-remove-legacy-skills` — domain `meta`, task `refactor`
- `2026-07-09_meth-091-legacy-path-sweep` — domain `meta`, task `refactor`
- `2026-07-09_meth-092-guide03-observation-deepen` — domain `meta`, task `docs`
- `2026-07-09_meth-093-agent-mechanics-deepen` — domain `meta`, task `research`
- `2026-07-09_meth-094-internal-guides-deepen` — domain `meta`, task `docs`
- `2026-07-09_meth-095-qa-templates-deepen` — domain `meta`, task `docs`
- `2026-07-09_meth-096-proposal-templates-deepen` — domain `meta`, task `docs`
- `2026-07-09_meth-097-ops-templates-deepen` — domain `meta`, task `docs`
- `2026-07-09_meth-098-glossary-template` — domain `meta`, task `docs`
- `2026-07-09_meth-099-graph-nodes` — domain `meta`, task `refactor`
- `2026-07-10_meth-100-v32-compat-cleanup` — domain `meta`, task `refactor`
- `2026-07-10_meth-101-boot-cmd-size-lint` — domain `meta`, task `feature`
- `2026-07-10_meth-102-livefile-boundary-standing-briefs` — domain `meta`, task `feature`
- `2026-07-10_meth-103-standing-write-trigger` — domain `meta`, task `feature`
- `2026-07-10_meth-104-sop-recognition-cues` — domain `meta`, task `feature`
- `2026-07-10_meth-105-brief-auto-filing` — domain `meta`, task `feature`
- `2026-07-10_meth-106-downstream-sync` — domain `meta`, task `docs`
- `2026-07-15_ai-icons-talmo-sync` — domain `meta`, task `docs`
- `2026-07-15_dashboard-graph-embed` — domain `meta`, task `feature`
- `2026-07-15_dashboard-slim` — domain `meta`, task `refactor`
- `2026-07-15_graph-viz-autobuild` — domain `meta`, task `feature`
- `2026-07-15_graph-viz-dagre` — domain `meta`, task `feature`
- `2026-07-15_graph-viz-generator` — domain `meta`, task `feature`
- `2026-07-15_sync-ai-icons-residual` — domain `meta`, task `docs`
- `2026-07-15_sync-all-helper` — domain `meta`, task `feature`
- `2026-07-15_sync-all-propagate` — domain `meta`, task `docs`
- `2026-07-15_sync-cafe24` — domain `meta`, task `docs`
- `2026-07-21_grooman-registered-11th-downstream` — domain `meta`, task `docs`
- `2026-07-23_boot-handoff-parser-template-align` — domain `meta`, task `bugfix`
- `2026-07-23_bootstrap-invest-ops-downstream` — domain `meta`, task `bootstrap`
- `2026-07-24_ship-push-verify` — domain `meta`, task `bugfix`
- `2026-07-24_sync-all-meth-115-remainder` — domain `meta`, task `bugfix`
- `2026-07-24_sync-all-meth-115` — domain `meta`, task `bugfix`
- `2026-07-25_ir-deck-methodology-guide-22` — domain `meta`, task `docs`
- `2026-07-28_meth-117-reverse-harvest-backlog` — domain `meta`, task `docs`
- `2026-07-29_ai-design-research` — domain `meta`, task `research`
- `2026-07-29_guide-20-v3-defense` — domain `meta`, task `docs`
- `2026-07-29_guides-23-24-verification-kickoff` — domain `meta`, task `docs`
- `2026-07-29_meth-117-capsule-outbox-design` — domain `meta`, task `research`
- `2026-07-29_meth-117-capsule-outbox-impl` — domain `meta`, task `feature`
- `2026-07-29_meth-118-backlog-todo-repair` — domain `meta`, task `docs`
- `2026-07-29_meth-118-prompt-coaching-impl` — domain `meta`, task `feature`
- `2026-07-29_meth-119-triage-register` — domain `meta`, task `docs`
- `2026-07-29_meth-120-121-guards-impl` — domain `meta`, task `feature`
- `2026-07-29_meth-122-livefile-build-guards` — domain `meta`, task `feature`
- `2026-07-29_meth-125-127-sop-ci-facts` — domain `meta`, task `docs`
- `2026-07-29_meth-128-guide-22-capsule` — domain `meta`, task `docs`
- `2026-07-29_meth-129-ai-design-guides` — domain `meta`, task `docs`
- `2026-07-29_monthly-audit-2026-07` — domain `meta`, task `research`
- `2026-07-29_sync-propagate-guide-20-v3` — domain `meta`, task `docs`
- `2026-07-29_sync-propagate-guides-23-24` — domain `meta`, task `docs`
- `2026-07-29_sync-propagate-meth-116` — domain `meta`, task `docs`
- `2026-07-29_sync-propagate-meth-117` — domain `meta`, task `docs`
- `2026-07-29_sync-propagate-meth-118` — domain `meta`, task `docs`
- `2026-07-29_sync-propagate-meth-120-121` — domain `meta`, task `docs`
- `2026-07-29_sync-propagate-meth-122` — domain `meta`, task `docs`
- `2026-07-29_sync-propagate-meth-125-127` — domain `meta`, task `docs`
- `2026-07-29_sync-propagate-meth-128-final` — domain `meta`, task `docs`
- `2026-07-29_sync-propagate-meth-129` — domain `meta`, task `docs`

## Collected Capsules (_inbox)

- `CROSS-REPO` x4: target `guide-23` — repo gamblescan, lifeManager
- `DUP-TARGET` x2: target `catalog` — repo gamblescan
- `CROSS-REPO` x2: target `guide-07` — repo gamblescan, lifeManager
- `CROSS-REPO` x2: target `guide-19` — repo gamblescan, lifeManager
- `single` x1: target `60_tools/ship-build-guard` — repo gamblescan
- `single` x1: target `guide-24` — repo gamblescan
- `single` x1: target `tool/hooks` — repo invest-ops
- `single` x1: target `tool/land` — repo invest-ops
- `single` x1: target `tool/ship` — repo invest-ops

> 트리아지 판정(유효/이미 반영/만료)·분배는 사람 — `50_resources/meth_inbox/_README.md`.
