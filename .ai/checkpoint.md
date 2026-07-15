# Checkpoint — 2026-07-15 (METH-110 graph-viz dagre 레이아웃)

> ✅ 지식그래프 레이아웃을 손 배치 격자 → dagre 계층 DAG로 교체(교차↓). feat/graph-viz-dagre, PR 대기. 아티팩트 갱신.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `feat/graph-viz-dagre` (updated main 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
사용자 "그래프가 좀 지저분" + "쓸 수 있는 스킬·커넥터·플러그인 조사해서 디벨롭".
- **진단**: 손 배치 격자(category=열)라 42노드/53엣지에서 엣지 교차(스파게티)가 근본 원인 — 색 아니라 **레이아웃 알고리즘** 문제.
- **수단 조사**: dataviz 스킬(✅ 시각 정돈)·Mermaid 네이티브 렌더(✅ 자동 레이아웃)·그래프 레이아웃 lib 인라인(✅ CSP가 인라인 JS 허용)·frontend-design/web-design-guidelines(보조)·Figma/Canva(인증·부적합). → 사용자가 **dagre 인라인** 선택.
- **구현**: `npm pack @dagrejs/dagre`로 `dagre.min.js`(40KB) 확보 → `60_tools/vendor/`에 벤더링(MIT LEGAL 동봉). 생성기 재작성:
  - 파이썬은 좌표 안 만들고 **노드/엣지 데이터만 주입**(`js_nodes`에서 x/y 제거). dagre 번들을 `<script>`로 인라인(`dagre_source()`가 sourceMappingURL 주석 제거).
  - 브라우저에서 `new dagre.graphlib.Graph()` → rankdir=LR, primary 엣지 weight=4(흐름축 곧게) → `dagre.layout()` → 노드 좌표·엣지 `points`로 SVG 렌더(엣지는 smoothPath 곡선).
  - **클릭→상세·라이프사이클·테마 recolor·dim 하이라이트 전부 유지**. dataviz 반영(recessive 엣지·라벨 2차인코딩·다크 설계 팔레트 소폭 정돈).
- **검증**: `tests/test_graph_viz.py` 6개(데이터 주입·번들 인라인·sourceMappingURL 제거·치환·통합) 6/6. 브라우저 DOM: dagre 정의됨·42노드 9개 rank(x 18~1794)·53엣지 다중점 곡선·클릭 시 상세("CLAUDE.md")+38노드 dim·콘솔 오류0. 스크린샷 육안: 곡선 라우팅·팬아웃 깔끔.
- **아티팩트**(e3d2f0cc) dagre 출력으로 갱신(같은 URL).

## 다음 사람에게
1. **METH-110 PR(base=main) 머지** — feat/graph-viz-dagre. 벤더 `60_tools/vendor/dagre.min.js`(+LEGAL) 신규 포함.
2. 머지 후 다음 sync 때 벤더 dagre + 새 생성기가 다운스트림 10곳 전파(60_tools shared).
3. (선택) dagre `ranksep`/`nodesep` 튜닝으로 밀도 조정 가능. 현재 rankdir=LR, ranksep=64.

## 환경 메모
- 브랜치: `feat/graph-viz-dagre` (updated main). branch-first.
- 오늘 세션 = 다운스트림 처리 → sync-all #97 → graph-viz #98 → autobuild #99 → dagre(대기).
- 누적 상태(오픈이슈·PR)는 **HANDOFF 참조**.
