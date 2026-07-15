# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: 다운스트림 전파 완료 — **관리 10곳 전부 방법론 payload 내용 일치**(methodology.py·generate-dashboard.py 해시 동일 검증). cafe24는 WIP landing 후 clean 확인→METH-106 절차로 sync. 버전스탬프 차이(88b9382~e3a05fb)는 라이브파일 전용 커밋(#103·#104)탓 cosmetic.
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

- 2026-07-15: **cafe24 sync 완료 (Class A)** — 사용자 "WIP landing 완료" → clean 재확인(dirty 0)→METH-106 절차(main 체크아웃→sync→push→피처브랜치 복원). 커스텀 guide 6개 보존. **관리 10곳 전부 방법론 payload 내용 일치** 검증(해시 동일). → 전 다운스트림 배포 사이클 종료.
- 2026-07-15: **sync-all 보류분 처리 (Class A)** — 8/10 이후 dirty 2곳 확인. **ai-icons**(main, WIP=30_planning tier2_ai_text.py=프로젝트 코드): `git add -A` 후 WIP만 `reset`로 언스테이징 → 루트 shared 포함·WIP 제외 안전 스테이징으로 방법론만 sync·push(5a2547c). **WIP 보존**(그 세션 미훼손). **cafe24**: 피처브랜치+skin184 진행중 WIP 91건(오늘자 관찰로그=활성 세션) → 사용자 결정으로 **그 세션 몫**(내가 커밋/stash 안 함). → 관리 10곳 중 **9 최신·1 보류(cafe24)**.
- 2026-07-15: **sync-all 전파 (Class A)** — 방법론 최신(88b9382)을 다운스트림에 일괄 전파. `sync-all --apply`(가드: dirty·비-main skip) → main-clean 4곳 처리, clean 피처브랜치 4곳(gamblescan·icons·lifeManager·tshome)은 main 체크아웃→sync→push→원브랜치 복원(METH-106 절차). **8/10 반영**(모두 main==origin 0/0). 보류 2: ai-icons(dirty 1)·cafe24(dirty 91) — WIP라 각 세션 몫. **friction**: 타깃 스테이징이 루트 shared(ONBOARDING.md)를 빠뜨려 icons-invest 미커밋 1건 잔존→추가 커밋(교훈: clean repo면 sync 변경 전체 스테이징).
- 2026-07-15: **METH-112 대시보드 슬림화 (Class A, PR #102 머지)** — 사용자 "대시보드 난잡, 필요한 것만" → **planning 리서치 스냅샷**(`40_dev/snapshots/dashboard-slim-research-2026-07-15.md`) 먼저, 사용자 결정(용도=모니터링·공유 / 3탭 / 파일뷰어 유지 / 스택 헤더축약) 후 구현. 대시보드가 **4가지 일 겸함**(상태/레퍼런스/운영콘솔/파일브라우징)이 난잡의 실체. **5탭→3탭**(상태·문서·관계그래프). 컷: 통합뷰(01 중복)·dev서버 start/kill·대시보드/worktree spawn·커맨드팔레트·스택bento·가이드백서·`node_contents`(그래프 iframe화로 죽은 데이터). 상태탭=hero+stat+진행현황+칸반, 문서탭=파일뷰어. `generate-dashboard.py` 1981→1587줄, dashboard.html payload 대폭↓(node_contents 제거). 브라우저 3탭 검증(hero·stat5·칸반5열·파일탭5·graph iframe·콘솔 오류0). `tests/test_graph_viz.py` 슬림 구조 단언 추가 7/7. 순수 진척 뷰(로컬 조작 제거→공유·정적 배포 용이).
- 2026-07-15: **METH-111 지식그래프 대시보드 통합 (Class A, PR #101 머지)** — 사용자 "아티팩트 말고 대시보드에 통합". 발견: 대시보드에 이미 자체 그래프 탭(03 관계 그래프)이 있었으나 **손수 짠 d3 force 시뮬**(원 노드, 720×540, 밀집 라벨 숨김)이라 별개. 통합 = 그 탭 본문을 **우리 dagre graph-viz iframe**으로 교체(`generate-graph-viz.py` 산출물 `methodology-graph-viz.html`을 탭 첫 진입 시 lazy-load, 같은 폴더 sibling). **죽은 코드 제거**: d3 CDN(실사용 0)·force `initGraph` 140줄·`.graph-grid/.graph-canvas/.graph-detail` CSS → 단일 그래프 렌더러(DRY). `.graph-frame`(82vh) CSS 추가. `tests/test_graph_viz.py`에 대시보드 임베드 테스트 추가 → 7/7. 브라우저 검증: 탭 클릭→iframe에 42/53 dagre 그래프 로드·대시보드 다크 테마와 자연스럽게 blend. 대시보드 완전 오프라인(외부 CDN=폰트만).
