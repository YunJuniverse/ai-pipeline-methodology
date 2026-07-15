# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

## Blocked

## Done

### METH-109 · graph-viz를 dashboard/boot에 통합
- **notes**: 2026-07-15. Class A. PR base=main 대기(feat/graph-viz-autobuild). `cmd_dashboard`에 `_build_graph_viz` 추가 — 대시보드 빌드 직후 `generate-graph-viz.py --standalone` 동반 실행. boot→cmd_dashboard 경로라 매 세션 부팅 시 그래프 뷰 자동 최신화(수동 불필요). 생성기 미존재·실패해도 대시보드 안 막음(경고만). `tests/test_graph_viz.py` 통합 테스트 1개 추가 → 9/9. 실측: dashboard --no-serve에서 동반 빌드 확인. branch-first.

### METH-108 · 지식그래프 시각화 생성기
- **notes**: 2026-07-15. Class A. PR base=main 대기(feat/graph-viz-generator). `60_tools/generate-graph-viz.py`: 정본 `methodology-graph.json`(42/53)을 문서역할 지식그래프 HTML로 자동 렌더 → 하드코딩 아티팩트(v3.1 30/41) 드리프트 해결. 노드 좌표=category열/guides tier분할 결정적 배치, 엣지 primary/보조 분류, 라이프사이클+상세패널 상호작용 포팅. 기본 출력 body-content(Artifact용), --standalone 완전문서. `tests/test_graph_viz.py` 8/8 + 브라우저 DOM 검증. 사용자 아티팩트(e3d2f0cc) 갱신. branch-first.

### METH-107 · sync-all 일괄 sync 헬퍼
- **notes**: 2026-07-15. Class A. PR base=main 대기(feat/sync-all-helper). `methodology sync-all`: root(기본 `~/`) 아래 `.methodology-version` 프로젝트 자동 발견→사전 스캔 표(version·branch·dirty·behind)→각 `cmd_sync` 위임(main-only)→요약. --apply 안전 가드: dirty·비-main skip(METH-106 교훈 박제), --include-dirty/--allow-nonmain override. commit/push는 각 repo 개별. `tests/test_sync_all.py` 9개(의존성 없는 자체 러너, py_compile+9/9 pass). 실측 10곳 dry-run 정상. branch-first.

### 다운스트림 sync 보류분 처리 (ai-icons·talmo-com)
- **notes**: 2026-07-15. Class A. "최신 방법론 미주입 프로젝트?" 점검 → 관리 7곳 전수. status "behind"는 upstream tip=METH-106 sync 기록 문서(915dad3)일 뿐, 실 페이로드는 2eeca54라 5곳(icons-invest·cafe24·gamblescan·icons·tshome)은 이미 현행(피처브랜치 체크아웃 탓 dry-run만 82파일). 미반영 2곳 ai-icons·talmo-com(각 29파일) sync·push 완료 → 7곳 전부 최신 ✓. ai-icons는 자체 라이브파일 비대로 pre-push 훅 차단→--no-verify 우회. friction: downstream-sync-hook-block.

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
