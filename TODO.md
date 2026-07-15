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

### METH-111 · 지식그래프 대시보드 통합
- **notes**: 2026-07-15. Class A. PR base=main 대기(feat/dashboard-graph-embed). "아티팩트 말고 대시보드에 통합". 대시보드 '관계 그래프' 탭(기존 자체 d3 force 시뮬)을 우리 dagre graph-viz iframe 임베드로 교체(탭 첫 진입 lazy-load, sibling `methodology-graph-viz.html`). 죽은 d3 CDN·force 140줄·graph CSS 제거→단일 렌더러. `.graph-frame` 82vh. `tests/test_graph_viz.py` 대시보드 임베드 테스트 추가 7/7 + 브라우저 검증(탭→iframe 42/53 로드). branch-first.

### METH-110 · graph-viz 레이아웃 dagre 교체
- **notes**: 2026-07-15. Class A. PR base=main 대기(feat/graph-viz-dagre). 사용자 "지저분" 지적 → 손 배치 격자 엣지 교차가 원인. 수단 조사(dataviz 스킬·mermaid·그래프 레이아웃 lib) 후 dagre 채택. `60_tools/vendor/dagre.min.js`(40KB, MIT) 벤더링·인라인 → 브라우저 rankdir=LR 계층 레이아웃·엣지 라우팅. 파이썬은 데이터만 주입, 클릭→상세·라이프사이클·테마 유지. dataviz 정돈. `tests/test_graph_viz.py` 6개 + 브라우저 DOM 검증(42노드 9랭크·교차↓·클릭 동작·오류0). 아티팩트 갱신. branch-first.

### METH-109 · graph-viz를 dashboard/boot에 통합
- **notes**: 2026-07-15. Class A. PR base=main 대기(feat/graph-viz-autobuild). `cmd_dashboard`에 `_build_graph_viz` 추가 — 대시보드 빌드 직후 `generate-graph-viz.py --standalone` 동반 실행. boot→cmd_dashboard 경로라 매 세션 부팅 시 그래프 뷰 자동 최신화(수동 불필요). 생성기 미존재·실패해도 대시보드 안 막음(경고만). `tests/test_graph_viz.py` 통합 테스트 1개 추가 → 9/9. 실측: dashboard --no-serve에서 동반 빌드 확인. branch-first.

### METH-108 · 지식그래프 시각화 생성기
- **notes**: 2026-07-15. Class A. PR base=main 대기(feat/graph-viz-generator). `60_tools/generate-graph-viz.py`: 정본 `methodology-graph.json`(42/53)을 문서역할 지식그래프 HTML로 자동 렌더 → 하드코딩 아티팩트(v3.1 30/41) 드리프트 해결. 노드 좌표=category열/guides tier분할 결정적 배치, 엣지 primary/보조 분류, 라이프사이클+상세패널 상호작용 포팅. 기본 출력 body-content(Artifact용), --standalone 완전문서. `tests/test_graph_viz.py` 8/8 + 브라우저 DOM 검증. 사용자 아티팩트(e3d2f0cc) 갱신. branch-first.

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
