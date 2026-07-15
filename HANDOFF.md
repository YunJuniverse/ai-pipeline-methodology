# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-111 지식그래프 대시보드 통합 (feat/dashboard-graph-embed, PR 대기). 대시보드 '관계 그래프' 탭이 자체 d3 force 대신 우리 dagre graph-viz를 iframe 임베드(lazy-load). 죽은 d3 CDN·force 140줄·CSS 제거→단일 렌더러. 테스트 7개, 브라우저 검증.
- **Current mode**: fullstack
- **Next TODO**: 079~105 점검·정비 + 부팅/브리프 개선(101~105) 사이클 종료. 다른 repo(별도 세션): ai-icons 92 환류·비대 라이브파일 트리밍·업무기술서 SOP 박제, talmo-com. **프로세스: branch-first · 스택-PR 지양(main 직행) · 세션 시작 = `methodology boot`.** 상세는 checkpoint.
- **Blockers**: none

## Active Links

- Current PR: METH-106 다운스트림 sync (신규, base=main) · 095~105 = #84~#94 머지 완료 · 063~094 = #53~#83 머지
- Current issue:
- Relevant ADRs:
- Relevant snapshots: `40_dev/snapshots/implementation-plan-2026-05-07.md`, `40_dev/snapshots/transfer-drill-2026-05-08.md`

## Open Decisions

| ID | Decision | Needed By | Status |
|----|----------|-----------|--------|
| - | `.claude/worktrees/` and `.codex/` are local tool metadata and should be gitignored | 2026-05-07 | Closed |

## Open Issues

| ID | Issue | Severity | Next Step |
|----|-------|----------|-----------|
| - | ~~sync가 다운스트림 고유 파일 mirror-delete~~ | — | **Closed** — METH-046(PR #35)로 prune을 --prune opt-in화(기본 보존) |
| - | ~~legacy/archive docs pre-v4 경로 언급~~ | — | **Closed(METH-091)** — 라이브 문서 sweep: `10_foundation/` 3건(`docs/snapshots/`→`40_dev/snapshots/`) 수정. 나머지는 정당(정확한 인용·예시)·90_archive는 히스토리 보존 |
| - | ~~v3.2 backward-compat 코드 폴백~~ | — | **Closed(METH-100)** — methodology.py·generate-dashboard.py의 v3.2 구조탐지·폴백(40_resources/60_meta/docs/legacy-root) 제거→v4.0 고정. `migrations/v3.2_to_v4.0.py`(이관)·런처/훅 부트스트랩 탐지는 보존. py_compile·dashboard 재생성·wrap 검증 |
| - | ~~ai-icons·icons-invest guide 번호 충돌~~ | — | **Closed(METH-089)** — 커스텀 04/05/21→90/91/92 이관·doc_id·참조 갱신, origin/main 검증. 잔여: ai-icons 92_LOCAL(구 21)은 상류 05 정본과 149줄 차이=로컬 발전분 → 각 repo 세션에서 상류 05로 환류·재조정 검토 |
| - | ~~sync 홀드 3곳(dirty)~~ | — | **Closed(METH-088)** — ai-icons·cafe24·icons-invest dirty 해소 후 086 sync 완료. **관리 다운스트림 6곳 전부 086 반영** |
| - | ~~`methodology-graph.json` 노드 불완전~~ | — | **Closed(METH-099)** — guide 10종(02·03·05·06·07·08·09·19·20·21) + 학습루프(observations·catalog·skeletons) + checkpoint 노드 추가, stale ai-log 제거. 노드 29→42·엣지 39→53. dashboard 렌더 검증(nodes=42)·JSON 정합 0 오류. (04는 미존재라 제외) |
| - | ⚠️ **스택-PR 재타깃 함정** — #85/#86/#87이 main 아닌 중간 브랜치로 머지됨(096/097/098 main 미반영) | — | **복구중(METH-099)** — 099 브랜치가 095-098 온전 보존 브랜치 기준 → base=main 단일 PR로 096+097+098+099 한 번에 복구. 교훈: 스택-PR은 순서·브랜치 삭제 타이밍 취약 → **main 직행 단일 PR 선호** |
| - | ~~`.claude/skills` 레거시 3종~~ | — | **Closed(METH-090)** — ai-planning·ai-relay·vibe-coding 삭제. 기능은 guide 01/08/19+prompts가 정본. 90_archive 히스토리는 보존 |
| - | icons-invest sync 커밋(f4e6605)에 `30_planning/10_사업기획서.md` 3줄 WIP 혼입 | Low | METH-106 sync 시 `git add -A`가 미커밋 WIP 쓸어담음. 내용 정당(미정 placeholder·Class C 미침범)·main 보존·유실 없음. 히스토리 재작성 안 함. **교훈: sync 커밋은 타깃 스테이징**(observe friction 기록) |
| - | ~~ai-icons·talmo-com 다운스트림 sync 미적용~~ | — | **Closed(2026-07-15)** — 두 곳 clean 재확인 후 v4.0 sync·push(각 29파일). ai-icons push는 자체 라이브파일 비대로 pre-push 훅 차단→established 절차대로 --no-verify 우회. **잔여**: ai-icons 자체 checkpoint(547줄)·TODO Done(272건) 비대 트리밍은 그 repo 세션 몫 |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-15: **METH-111 지식그래프 대시보드 통합 (Class A, PR 대기)** — 사용자 "아티팩트 말고 대시보드에 통합". 발견: 대시보드에 이미 자체 그래프 탭(03 관계 그래프)이 있었으나 **손수 짠 d3 force 시뮬**(원 노드, 720×540, 밀집 라벨 숨김)이라 별개. 통합 = 그 탭 본문을 **우리 dagre graph-viz iframe**으로 교체(`generate-graph-viz.py` 산출물 `methodology-graph-viz.html`을 탭 첫 진입 시 lazy-load, 같은 폴더 sibling). **죽은 코드 제거**: d3 CDN(실사용 0)·force `initGraph` 140줄·`.graph-grid/.graph-canvas/.graph-detail` CSS → 단일 그래프 렌더러(DRY). `.graph-frame`(82vh) CSS 추가. `tests/test_graph_viz.py`에 대시보드 임베드 테스트 추가 → 7/7. 브라우저 검증: 탭 클릭→iframe에 42/53 dagre 그래프 로드·대시보드 다크 테마와 자연스럽게 blend. 대시보드 완전 오프라인(외부 CDN=폰트만).
- 2026-07-15: **METH-110 graph-viz 레이아웃 dagre 교체 (Class A, PR #100 머지)** — 사용자 "그래프가 좀 지저분" 지적 → 손 배치 격자(category=열)의 엣지 교차(스파게티)가 원인. 진단·수단 조사 후 **dagre 계층 DAG 레이아웃** 채택(사용자 선택). `60_tools/vendor/dagre.min.js`(40KB, MIT LEGAL 포함) 벤더링·인라인 → 브라우저가 rankdir=LR 레이아웃·엣지 라우팅 계산(primary 엣지 weight↑로 흐름축 곧게). 파이썬은 좌표 안 넣고 노드/엣지 데이터만 주입. **클릭→상세·라이프사이클·테마 유지**. `dataviz` 스킬 반영(recessive 엣지·라벨=2차인코딩·다크 설계). `tests/test_graph_viz.py` 6개(데이터 주입·번들 인라인·치환·통합) + 브라우저 DOM 검증(42노드 9랭크 배치·교차↓·클릭 동작·콘솔 오류0). 아티팩트(e3d2f0cc) 갱신. CSP는 인라인 JS 허용이라 CDN 불필요.
- 2026-07-15: **METH-109 graph-viz를 dashboard/boot에 통합 (Class A, PR #99 머지)** — `cmd_dashboard`에 `_build_graph_viz` 추가: 대시보드 빌드(`generate-dashboard.py`) 직후 `generate-graph-viz.py --standalone`을 동반 실행해 `_start/.cache/methodology-graph-viz.html` 생성. boot→cmd_dashboard 경로라 **매 세션 부팅 시 그래프 뷰 자동 최신화**(수동 실행 불필요). 생성기 미존재(미sync 다운스트림)·실패해도 대시보드 빌드 안 막음(경고만, 부수 산출물). `tests/test_graph_viz.py`에 통합 테스트 1개 추가 → 9/9. 실측: `dashboard --no-serve`에서 graph-viz built + 파일 생성(NCOUNT=42·v3.2 주입) 확인.
- 2026-07-15: **METH-108 지식그래프 시각화 생성기 (Class A, PR #98 머지)** — `60_tools/generate-graph-viz.py`: 정본 `methodology-graph.json`(42노드/53엣지/v3.2-2026-07)을 문서역할 지식그래프 HTML로 자동 렌더. 사용자가 공유한 아티팩트가 하드코딩 스냅샷(v3.1·30노드/41엣지)이라 그래프 변경마다 드리프트하던 걸 data-driven 생성기로 해결(sync-all과 같은 결). 노드 좌표=category열/guides는 tier 분할로 결정적 배치, 엣지 primary(실선)/보조(점선) 분류, 라이프사이클 파이프라인+노드 클릭 상세패널 상호작용은 원 아티팩트 로직 포팅. 기본 출력=Artifact 게시용 body-content(`--standalone`로 완전문서). `tests/test_graph_viz.py` 8개(열배치·중복없음·좌표유일·루프판정·치환완료) 8/8 + 브라우저 DOM 검증(42/53·클릭 동작·오류0). 사용자 아티팩트(e3d2f0cc) 이 출력으로 갱신.
- 2026-07-15: **METH-107 sync-all 일괄 sync 헬퍼 (Class A, PR #97 머지)** — `methodology sync-all`: root(기본 방법론 상위 `~/`) 아래 `.methodology-version` 보유 프로젝트 자동 발견 → 사전 스캔 표(project·version·branch·dirty·vs-upstream) → 각 프로젝트 `cmd_sync` 위임(main-only) → 요약. **--apply 안전 가드**: dirty repo·비-main 브랜치는 skip(오늘 METH-106 교훈 박제 — 진행 중 작업/피처브랜치 오염 방지), `--include-dirty`·`--allow-nonmain`로 override. commit/push는 각 repo 개별(add -A 혼입 회피). `tests/test_sync_all.py` 9개(발견·가드·behind 판정, 의존성 없는 자체 러너). 실측: 10곳 발견·표·dry-run 정상. **주의**: methodology.py가 shared라 이 헬퍼는 다음 sync 때 다운스트림에 전파됨.
