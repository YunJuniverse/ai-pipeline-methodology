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

### sync-all 보류분 처리 (ai-icons·cafe24)
- **notes**: 2026-07-15. Class A. PR base=main 대기(chore/sync-ai-icons-residual). ai-icons: WIP(tier2_ai_text.py=프로젝트 코드) 보존한 채 방법론만 sync·push(add -A→WIP reset로 안전 스테이징). main==origin 5a2547c. cafe24: 피처브랜치+skin184 활성 WIP 91건 → 사용자 결정으로 그 세션 위임(미처리). 관리 10곳 중 9 최신·1 보류. branch-first.

### sync-all 다운스트림 전파 (88b9382)
- **notes**: 2026-07-15. Class A. PR base=main 대기(chore/sync-all-propagate). 방법론 최신(graph-viz·dagre·대시보드 통합·슬림화)을 다운스트림 일괄 전파. `sync-all --apply`(가드 skip dirty·비-main) → main-clean 4곳 처리; clean 피처브랜치 4곳(gamblescan·icons·lifeManager·tshome)은 main 체크아웃→sync→push→복원. 8/10 반영(main==origin 0/0). 보류 2: ai-icons·cafe24(dirty WIP). friction: 타깃 스테이징이 루트 shared(ONBOARDING.md) 누락→추가 커밋. branch-first.

### METH-112 · 대시보드 슬림화
- **notes**: 2026-07-15. Class A. PR base=main 대기(feat/dashboard-slim). "대시보드 난잡, 필요한 것만" → planning 리서치 스냅샷(`40_dev/snapshots/dashboard-slim-research-2026-07-15.md`) 먼저, 사용자 결정(모니터링·공유/3탭/파일뷰어 유지/스택 헤더축약) 후 구현. 5탭→3탭(상태/문서/관계그래프). 컷: 통합뷰(중복)·dev서버·spawn·커맨드팔레트·스택bento·가이드백서·node_contents(죽은데이터). generate-dashboard.py 1981→1587줄. 브라우저 3탭 검증·오류0. `tests/test_graph_viz.py` 슬림 단언 7/7. branch-first.

### METH-111 · 지식그래프 대시보드 통합
- **notes**: 2026-07-15. Class A. PR base=main 대기(feat/dashboard-graph-embed). "아티팩트 말고 대시보드에 통합". 대시보드 '관계 그래프' 탭(기존 자체 d3 force 시뮬)을 우리 dagre graph-viz iframe 임베드로 교체(탭 첫 진입 lazy-load, sibling `methodology-graph-viz.html`). 죽은 d3 CDN·force 140줄·graph CSS 제거→단일 렌더러. `.graph-frame` 82vh. `tests/test_graph_viz.py` 대시보드 임베드 테스트 추가 7/7 + 브라우저 검증(탭→iframe 42/53 로드). branch-first.


> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
