# Checkpoint — 2026-07-15 (METH-111 지식그래프 대시보드 통합)

> ✅ 대시보드 '관계 그래프' 탭을 우리 dagre graph-viz iframe 임베드로 교체(자체 d3 force 대체). feat/dashboard-graph-embed, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `feat/dashboard-graph-embed` (updated main 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
사용자 "이 문서 파이프라인 & 역할 지식그래프를 아티팩트 말고 대시보드에 통합".
- **발견**: `generate-dashboard.py`에 이미 그래프 탭(03 관계 그래프)이 있었으나, 우리 graph-viz와 **별개인 손수 짠 d3 force 시뮬**(원 노드 720×540, 밀집시 라벨 숨김). d3 CDN은 로드만 하고 실사용 0(force는 순수 JS).
- **통합 방식**(사용자 의도=대시보드 안에): 그 탭 본문(`#graph-svg`+detail aside)을 **우리 dagre graph-viz iframe**으로 교체. `generate-graph-viz.py` 산출물 `methodology-graph-viz.html`(METH-109 co-build로 dashboard.html과 같은 폴더 생성)을 탭 첫 진입 시 lazy-load(`initGraph`가 iframe.src 설정). → 그래프 렌더러 하나로 통일(DRY).
- **죽은 코드 제거**: d3 CDN `<script>`, force `initGraph` 140줄(1303~1442) → 5줄 lazy 로더, `.graph-grid/.graph-canvas/.graph-detail`(+responsive) CSS. `.graph-frame`(82vh) 추가. 대시보드 외부 CDN=폰트만(완전 오프라인).
- **검증**: `tests/test_graph_viz.py`에 대시보드 임베드 테스트 추가(빌드 HTML에 graph-frame·graph-viz 참조 있고 d3js.org 없음) → **7/7**. 브라우저: 대시보드 서빙→탭03 클릭→iframe.src 설정·페이지 활성·contentDocument에 dagre 정의·42노드/53엣지 로드. 스크린샷: 다크 테마와 자연스럽게 blend.

## 다음 사람에게
1. **METH-111 PR(base=main) 머지** — feat/dashboard-graph-embed. 변경 파일: `60_tools/generate-dashboard.py`(iframe 임베드·죽은코드 제거), `tests/test_graph_viz.py`.
2. 머지 후 다음 sync 때 다운스트림 10곳 전파(60_tools shared).
3. (알려진 소소): 대시보드에 런타임 테마 토글이 있다면 iframe엔 data-theme 전파 안 됨(iframe은 prefers-color-scheme=OS 따름). 필요 시 postMessage로 테마 동기화 가능. 현재 OS 테마 따라 자연 blend라 보류.
4. 그래프 자체 개선은 `generate-graph-viz.py` 한 곳만 고치면 아티팩트·대시보드 양쪽 반영(단일 소스).

## 환경 메모
- 브랜치: `feat/dashboard-graph-embed` (updated main). branch-first.
- 그래프 작업 계보: 생성기(#98)→autobuild(#99)→dagre(#100)→대시보드 통합(이번). 단일 소스 = `generate-graph-viz.py`.
- 누적 상태(오픈이슈·PR)는 **HANDOFF 참조**.
