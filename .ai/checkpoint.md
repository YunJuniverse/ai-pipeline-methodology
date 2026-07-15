# Checkpoint — 2026-07-15 (METH-109 graph-viz를 dashboard/boot에 통합)

> ✅ cmd_dashboard가 대시보드 빌드 직후 graph-viz를 동반 빌드. boot 경유로 매 세션 자동 최신화. feat/graph-viz-autobuild, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `feat/graph-viz-autobuild` (updated main 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
METH-108(graph-viz 생성기) 후속 — 사용자 요청으로 **dashboard/boot에 통합**해 자동 최신화.
- **통합 지점**: `cmd_boot` → `cmd_dashboard`(기존 호출) → `generate-dashboard.py`. 여기 `cmd_dashboard`의 대시보드 빌드 subprocess **직후**에 `_build_graph_viz(build_root, out_path.parent)` 추가.
- **`_build_graph_viz`**: `<build_root>/60_tools/generate-graph-viz.py`(없으면 METHODOLOGY_ROOT fallback)를 `--standalone --out <cache>/methodology-graph-viz.html`로 subprocess 실행. 생성기 미존재(미sync 다운스트림)·실패해도 대시보드 빌드 **안 막음**(warn만, 부수 산출물). 성공 시 `ok("graph-viz built: ...")`.
- 결과: boot·`dashboard` 양쪽이 매번 graph-viz를 정본 JSON에서 재생성 → 수동 실행 불필요.
- **테스트**: `tests/test_graph_viz.py`에 통합 테스트 1개 추가(`_build_graph_viz`가 실제 파일 생성·`<svg` 포함) → **9/9**. sync-all 9/9 회귀 없음.
- **실측**: `dashboard --no-serve` → "graph-viz built" + 파일 생성, 주입 상수 NCOUNT=42·ECOUNT=53·VERSION=v3.2-2026-07 확인.

## 다음 사람에게
1. **METH-109 PR(base=main) 머지** — feat/graph-viz-autobuild.
2. 머지 후 다음 sync 때 이 통합(methodology.py)이 다운스트림 10곳에 전파 → 각 repo boot도 자동 graph-viz 생성.
3. (선택) graph-viz를 서빙 URL로 노출하고 싶으면 dashboard 서버가 cache 디렉터리를 서빙하므로 `…/methodology-graph-viz.html` 경로로 접근 가능(현재는 파일만 생성).

## 환경 메모
- 브랜치: `feat/graph-viz-autobuild` (updated main). branch-first.
- 오늘 세션 = 4번째 PR(다운스트림 처리 → sync-all #97 → graph-viz #98 → autobuild).
- 누적 상태(오픈이슈·PR)는 **HANDOFF 참조**.
