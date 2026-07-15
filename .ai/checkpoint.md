# Checkpoint — 2026-07-15 (METH-108 지식그래프 시각화 생성기)

> ✅ `60_tools/generate-graph-viz.py` 구현·테스트 완료. feat/graph-viz-generator, PR 대기.
> 사용자가 공유한 문서역할 지식그래프 아티팩트가 하드코딩 스냅샷이라 정본에서 드리프트(v3.1 30/41 vs 현 42/53)한 걸 data-driven 생성기로 해결.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `feat/graph-viz-generator` (updated main 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
사용자가 문서역할 지식그래프 **아티팩트 URL**(e3d2f0cc)을 주며 "업데이트해야하지 않아?" 물음.
- **진단**: 그 아티팩트는 `methodology-graph.json` 데이터를 HTML에 **하드코딩한 스냅샷**(v3.1-2026-05·30노드/41엣지)이라, 정본(현 **v3.2-2026-07·42노드/53엣지**, METH-099에서 확장)에서 한 버전 드리프트. repo JSON은 최신이고 **아티팩트만** 낡음. sync-all과 같은 "하드코딩→드리프트" 문제.
- **해결(사용자 선택=생성기)**: `60_tools/generate-graph-viz.py` — JSON 읽어 지식그래프 HTML 자동 렌더.
  - 노드 좌표 **결정적 배치**: category=열, guides(21개)는 tier(3~6)별 하위 열로 분할. `build_columns`+`layout`(최장 열 기준 세로 중앙정렬).
  - 엣지 primary(실선, 생산·서열·라우팅)/보조(점선, 부팅·참조·템플릿) 분류(`PRIMARY_KINDS`).
  - 라이프사이클 파이프라인(L1~L9, 게이트·순환)·노드 클릭 상세패널 **상호작용은 원 아티팩트 JS 포팅**, 데이터만 `/*__KEY__*/` 자리표시자로 주입.
  - 기본 출력 = Artifact 게시용 **body-content**(doctype/html/head/body 없음), `--standalone`이면 완전 문서. 기본 경로 `_start/.cache/`(gitignore).
  - 헤더/각주 카운트·버전을 JSON에서 동적 표기 → "30노드·v3.1" 하드코딩 낡음 자동 소거.
- **테스트**: `tests/test_graph_viz.py` 8개(열이 전 노드 포함·guides tier분할·좌표유일·좌우순서·열내 비겹침·루프판정·자리표시자 완전치환) 8/8. `py_compile` OK.
- **브라우저 검증**: Claude_Browser 스크린샷이 다크+와이드 SVG에서 빈 화면 반복 → `javascript_tool`로 DOM 직접 조회: 42노드/53엣지 렌더·좌표·fill 정상·노드 클릭→상세("CLAUDE.md")·콘솔 오류 0 확인.
- **아티팩트 갱신**: 이 생성기 출력으로 사용자 아티팩트(e3d2f0cc) 업데이트 (같은 URL).

## 다음 사람에게
1. **METH-108 PR(base=main) 머지** — feat/graph-viz-generator.
2. (선택) 생성기를 `generate-dashboard.py`/boot 파이프라인에 엮으면 그래프 변경 시 뷰가 자동 최신화(현재는 수동 `python3 60_tools/generate-graph-viz.py`). 지금은 독립 명령.
3. 주의: `60_tools/*`는 shared라 이 생성기도 다음 sync 때 다운스트림 전파.
4. graph JSON version 필드가 `v3.2-2026-07`인데 방법론 자체는 v4.0 — 그래프 내부 버전 문자열은 별도 스킴(혼선 시 정리 검토).

## 환경 메모
- 브랜치: `feat/graph-viz-generator` (updated main). branch-first.
- 이번 세션 = 오늘 3번째 PR(다운스트림 처리 → sync-all(107) → graph-viz(108)).
- 누적 상태(오픈이슈·PR)는 **HANDOFF 참조**.
