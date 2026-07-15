# Checkpoint — 2026-07-15 (METH-112 대시보드 슬림화)

> ✅ 대시보드 5탭→3탭(상태/문서/관계그래프), 운영 콘솔·중복·죽은데이터 제거. planning 리서치 스냅샷 후 구현. feat/dashboard-slim, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `feat/dashboard-slim` (updated main=09c86b0 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
사용자 "대시보드 너무 난잡, 필요한 것만 남긴 실용적 대시보드로 디벨롭하는 기획 리서치".
- **리서치(planning)**: `40_dev/snapshots/dashboard-slim-research-2026-07-15.md` — 현행 감사(5탭·데이터 카탈로그) → 진단(한 화면이 상태/레퍼런스/운영콘솔/파일브라우징 **4가지 일 겸함**). 사용자 결정: 용도=**모니터링·공유**, **3탭 유지**, **파일뷰어만 유지**, **스택 헤더축약**.
- **구현(METH-112, `generate-dashboard.py`)**: JS 섹션이 `// ── 헤더`로 구분돼 있어 컷 블록을 **헤더→다음헤더 범위 regex**로 안전 제거. HTML은 앵커 regex로 재구성.
  - **5탭→3탭**: 상태(page-status)·문서(page-docs)·관계그래프(page-graph).
  - **상태탭** = hero + stat-row(WIP/TODO/ADR/Snapshots/Guides) + 진행현황%카드 + 칸반(이동, `#kanban-board` id 유지→renderKanban 무손상).
  - **문서탭** = 파일 전문 뷰어(CLAUDE/HANDOFF/TODO/MASTER_PLAN/AGENTS).
  - **컷**: 통합뷰(01 중복)·dev서버 start/kill·대시보드/worktree spawn·로컬대시보드 테이블·커맨드팔레트·스택 bento(+openStackModal)·가이드백서 + 대응 JS IIFE 전부 + `assemble.node_contents`(그래프 iframe화로 죽은 데이터, payload 대폭↓).
  - `generate-dashboard.py` 1981→1587줄. dashboard.html 765줄.
- **검증**: dangling 참조 0(grep). 브라우저 서빙→3탭: hero·stat5·진행현황·칸반5열·파일탭5·graph iframe(src set)·콘솔 오류 0. `tests/test_graph_viz.py`에 슬림 구조 단언(3페이지·컷대상 부재·핵심 존재·node_contents 부재) 추가 → **7/7**.

## 다음 사람에게
1. **METH-112 PR(base=main) 머지** — feat/dashboard-slim. 리서치 스냅샷 + generate-dashboard.py + tests 포함.
2. 머지 후 다음 sync 때 다운스트림 10곳 전파(60_tools shared). **주의**: 다운스트림은 dev서버/spawn 운영 기능을 잃음(의도된 슬림 — 필요 repo는 CLI `methodology dashboard list/stop` 사용).
3. 잔여(스냅샷 §5): 서버측 `/api/*` 엔드포인트는 코드에 남아있음(UI만 제거) — 원하면 후속으로 서버 핸들러도 정리 가능.

## 환경 메모
- 브랜치: `feat/dashboard-slim` (updated main). branch-first.
- 세션 계보: 다운스트림 처리 → sync-all #97 → graph-viz #98 → autobuild #99 → dagre #100 → 대시보드 통합 #101 → 슬림화(이번).
- 누적 상태(오픈이슈·PR)는 **HANDOFF 참조**.
