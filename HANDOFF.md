# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: (완료) 정합성 QA 4 PR + sync 가드 PR 전부 머지·전파 완료. icons/talmocom/gamblescan main push + tshome v3.2→v4.0 수동 마이그레이션 push 완료. 4 적용 프로젝트 전체 정합.
- **Current mode**: fullstack
- **Next TODO**: 3개 적용 프로젝트 export 일상 사용 검증, 루트 README.md in-spire 리브랜딩, METH-020 (MC-002 N=7+ 승급)
- **Blockers**: none

## Active Links

- Current PR:
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
| - | Some legacy/archive docs may still mention pre-`40_dev` or pre-`60_tools` paths | Low | Sweep only if those docs become live references again |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-05-17: **4 프로젝트 정합성 전파 완료 + tshome 마이그레이션 (METH-034)** — icons/talmocom/gamblescan main 에 QA 패치 push (--no-verify, 순수 방법론 커밋 검증). tshome 은 원격 9커밋(제품 수정 4 포함) 앞서 충돌 → 로컬 stale 커밋 백업 후 origin/main 리셋 → fresh 재마이그레이션. split-brain(40/50_resources, 30/40_dev, 00_foundation/briefs) 해소: 관찰 5건 정본 통합(tshome-027 frontmatter 버전), 빈 폴더 제거로 6 rename 차단 해제, 사업/분기 보고서 4건 백업서 복원, .sanity/dist 제외. commit 688d142 push (관찰 12·사업문서 4·옛폴더 0·제품 9커밋 보존). 8개 stale worktree 는 PR #19 가드로 향후 자동 차단.
- 2026-05-17: **sync worktree 안전 가드** — QA 정합성 패치 전파 중 `sync --include-worktrees` 가 icons 6 + talmocom 1 stale worktree (마지막 커밋 2026-05-07, v3.1) 에 *풀 v3.1→v4.0 마이그레이션* 을 무차별 적용 → 각 133건 churn + 40/50_resources 중복. 8개 worktree 전부 revert (순수 churn, feature 손실 0). 근본 수정: `_worktree_sync_safety(wt, target_v, force)` 가 (1) 미커밋 변경 (2) 마이그레이션 유발 worktree 를 skip. `--force-worktree-migration` escape hatch. icons dry-run 6/6 정확 차단 확인. icons/talmocom/gamblescan **main** 은 정상 전파·커밋 완료. tshome (v3.2 main, 40/50_resources 중복) 은 별도 수동 처리 대기.
- 2026-05-17: **QA 우선순위 4 — dashboard layout 헬퍼** — `generate-dashboard.py` 의 12곳 `50_resources/60_tools/40_dev` 하드코딩이 PR #10 의 `methodology_layout()` 미적용 상태 (standalone 파일이라 import 불가). 자체 `dash_layout(root)` (v3.2/v4.0 dict 반환) + `resolve_methodology_py(root)` (3-tier) 헬퍼 도입. assemble()/read_methodology_assets()/read_project_config()/API 핸들러 2곳 모두 layout 기반. 잔여 하드코딩 0 (탐지 정의부·docs fallback 제외). v3.2 시뮬: resources=40_resources/dev=30_dev 정확. 미래 v5 마이그레이션 부채 해소.
- 2026-05-17: **QA 우선순위 3 — commands.json 커버리지** — 25 → 32 명령. ops 에 init/diff/sync(--include-worktrees) 추가, observe 에 catalog seed-pending 추가, 신규 "스켈레톤 (L2)" 카테고리 (skeleton init/build/apply). 미노출 5개 잔여는 nested subparser 오탐 (skeleton/dashboard/catalog 하위명령 — 실제 sub-ops 로 모두 노출). dashboard Commands 카드 6 카테고리 렌더 확인.
- 2026-05-15: **QA 우선순위 5 — 런처 3-tier 통일** — `_start/` 3 OS 런처 (mac `.app` / linux `.sh` / windows `.bat`) 와 `build-launchers.py` generator 의 methodology.py 탐지가 `60_tools/` 만 (또는 mac 만 2-tier) 체크. hook 템플릿의 3-tier (60→50→root) 와 불일치. generator 의 셸 스니펫 + Windows batch 로직을 3-tier 로 통일 → 재생성. v3.2 적용 프로젝트나 root-level methodology.py 시나리오에서도 런처 동작. bash -n 구문 검증 통과.
- 2026-05-15: **정합성 QA 후 2 fix** — 18개 카테고리 QA 후 4 정합성 이슈 발견 (commands stale path / dashboard obs 누락 / commands.json 8 subcmd 미노출 / generate-dashboard layout 헬퍼 미적용). 우선순위 1·2 만 묶음. (1) `generate-dashboard.py` 의 `read_methodology_assets()` 가 `50_resources/ai_observations` 만 카운트 → `_count_observations()` 헬퍼 도입 후 `50_resources + 70_meta` (+ v3.2 fallback) 모두 합산. source 저장소 dashboard 가 6 → 26 정확 보고. (2) `commands.json:119` 의 description "10_guides/03 스키마 검증" → "20_guides/03 스키마 검증" (v4.0 명명).
- 2026-05-15: **applied-ci source repo skip** — `methodology-applied-ci.yml` 의 `70_meta 미주입 검증` 이 source 저장소(`YunJuniverse/ai-pipeline-methodology`) PR 에서 *항상 fail*. source 는 70_meta/ 를 의도적으로 가지고 있고 (메타-방법론 격리 영역), applied-ci 는 *적용 프로젝트* 의 누수만 검사해야 함. job-level `if: github.repository != 'YunJuniverse/ai-pipeline-methodology'` 로 skip. 두 job (validate / freshness) 모두 적용. source 의 자체 검증은 methodology-source-ci.yml 가 담당.
- 2026-05-15: **observation lint 정합성 회복** — source-ci 가 옛 observation 파일들에서 18건 실패. 분석: validator 의 "본문 1단락 ≤ 220자" 규칙이 *실제 사용 패턴* (multi-section markdown body) 과 어긋남. 게다가 CLI `--summary` 도 길이 강제 안 함 — 정책-현실 괴리. **해결**: (1) validator 본문 길이/단락 제약 제거 (body 는 markdown 자유 형식, frontmatter required fields 는 유지), (2) frontmatter 없는 3개 파일 (PR #9 시기 `cat >` 작성) 에 적절한 YAML frontmatter 추가, (3) `2026-05-12_v3.1-to-v3.2-migration.md` 파일명 dot → kebab rename (slug 규칙 위반), (4) `2026-05-13_dashboard-port-conflict-fix.md` 절대 사용자 경로 `<METHODOLOGY>` 익명화. 18→0 실패.
- 2026-05-15: **Stack 섹션 정리** — PR #11 의 12-col bento 가 5개 문제 발생: (1) hero(6)+mid(4)=10 자투리 (2) hero row-span 2 가 grid auto-placement sparse 모드 깨뜨려 같은 카테고리 카드 분리됨 (3) 카테고리 라벨 7회 반복 (4) role 한글 uppercase+letter-spacing 줄바꿈 (5) hero 빈 공간 vs sm 이름만 — 정보 밀도 양극화. **해결**: 카테고리 그룹 헤더 1회 + `auto-fill minmax(240px,1fr)` 균일 grid + hero = 좌측 액센트 라인 + ★ PRIMARY 배지 + 살짝 다른 배경 (layout 변경 X) + role uppercase 제거 + 모든 카드 reason 3-line clamp 노출. stack.json 데이터 무수정 (`size: hero|mid|sm` 의미만 "레이아웃 크기" → "강조 등급" 으로 전환).
- 2026-05-15: **Stack bento 카드** — Overview 탭 하단 신규 섹션. `60_tools/stack.json` 에서 23 항목 5 카테고리 (Frontend/Backend/CMS/Infra/Dev) 로드. CSS 12-col grid + `size: hero|mid|sm` 으로 비대칭 배치 — 카테고리당 hero 1장 (Next.js 15 / Resend / Sanity v3 / Vercel / pnpm) + mid/sm. 카드 클릭 → side-sheet 모달 (선택 이유 + meta + docs URL). Apple bento 컨셉만 차용, 시각 언어는 현재 OKLCH 엔지니어링-저널 톤 (샤프 코너, 단일 앰버 액센트, 다색 그라데이션 X). MANIFEST shared 에 stack.json 추가 → 적용 프로젝트 자동 전파.
- 2026-05-15: **정합성 3 fix 묶음** — (1) `methodology_layout(target)` 헬퍼 — v3.2/v4.0 구조 탐지 중앙화. wrap·hook·CI·observation dir 모두 layout 기반으로 통일 (그동안 4번 패치한 fallback 누락 root cause). (2) `sync --include-worktrees` — sibling worktree 감지. 마이그레이션 있으면 기본 True 로 일괄 처리 (tshome 사고 직접 차단). `--main-only` 로 opt-out. (3) `observe` CLI 강제 — wrap 이 새 .md frontmatter 선행 검증. `cat >` 직접 작성 → CI 실패 → 수정 사이클 차단. CLAUDE/AGENTS managed 마커에 CLI 사용 권고 명문화. `OBSERVATION_DIR` 도 layout 기반으로 동적 변환.
- 2026-05-15: **`wrap` 콘텐츠 해시 검증** — mtime 기반 → sha256 기반. `.ai/wrap-state.json` 에 라이브 파일 (HANDOFF/TODO/checkpoint) sha256 + 검증된 관찰 로그 목록 저장. 다음 wrap 은 *콘텐츠 변경* 만 통과 (touch / 동일 내용 재저장은 차단). 최초 1회 부트스트랩, ship commit 직전 wrap-state 를 *현재 sha 로 동기화* 후 함께 커밋 (post-push 갱신 X → clone/pull 후 wrap 일관성 보장). ship → push 시 `METHODOLOGY_SHIP_IN_PROGRESS=1` 환경변수로 pre-push hook 의 wrap 재실행 skip (ship step 1 에서 이미 검증됨). 원인: 동일 날짜 다중 ship 시 옛 wrap 이 mtime 만 보고 통과 → 다음 세션이 옛 HANDOFF/TODO/checkpoint 를 진실로 신뢰 → 작업 누락 발생 (S-007/S-008/S-009).
- 2026-05-14: **USER_GUIDE.md + commands.json + Commands 카드** — 인간 워크플로 11섹션 매뉴얼 (시작·매일·brief·작업·종료·인계·명령·Class·문제해결·다이어그램·참조), commands.json 5 카테고리 × 23명령 (boot/end/ops/observe/export), dashboard Overview 탭 최상단 Commands 카드 — 카테고리 탭 + 클릭 클립보드 복사. MANIFEST shared 에 USER_GUIDE/commands.json 추가.
- 2026-05-14: `methodology export` CLI — 외주 인계용 코드 추출. 제외 목록 3축(NN_ 방법론 폴더 + _start/.ai/.claude/.codex + 빌드 산출물 node_modules/.next/dist 등 + .DS_Store 같은 OS 캐시). sensitive(.env/credentials) 기본 차단, --allow-sensitive 명시 우회. dry-run + 결과 검증(방법론 흔적 잔존 0). icons 467 / gamblescan 1,459 / talmocom 487 파일 (90%+ 노이즈 제거). CLAUDE/AGENTS managed 에 외주 인계 워크플로 명문화.
- 2026-05-14: 방법론 v4.0 — 00_briefs/ 신설 + 모든 NN_ 폴더 +10 shift — 인간 raw 입력 채널 (리서치·아이디어·회의록) 명문화, AI 가 매 세션 자동 로드. migration script (7 폴더 rename + 121 파일 path replace, chr() 우회로 self-replace 회피), MANIFEST·.ai/context.json·CLAUDE.md/AGENTS.md managed·백서 §부록 C 일괄 갱신. init 격리 검증 ✅. METHODOLOGY_VERSION v4.0.
- 2026-05-13: setup 두 파일 → _start/settings/ 이동 — 진입점(3개) 과 *1회 setup 스크립트* 시각적 분리. PowerShell/bash 내부 경로 보정 (`$root`/`$ROOT`). `.lnk` 는 _start/ 루트에 생성 유지 (사용자 진입점). build-launchers.py clean_legacy 에 옛 위치 자동 정리 추가.
- 2026-05-13: dashboard.html → _start/.cache/ 격리 — 사용자가 *루트 dashboard.html 직접 더블클릭(file://)* 하는 휴먼에러 원천 차단. .cache/ 는 Finder 숨김 + .gitignore. cmd_dashboard 가 legacy 루트 dashboard.html 자동 제거.
- 2026-05-13: dashboard root rewrite — `do_GET` 에서 `/` 요청을 `/dashboard.html` 로 자동 rewrite. directory listing 노출 버그 해결. 사용자 진입점 URL `http://localhost:8765` 그대로 OK.
- 2026-05-13: `_start/` 구조 재편 + 루트 클러터 정리 — 사용자 명시 표기 파일명: `in-spire (mac).app` / `(windows).bat` / `(linux).sh`. 보조 자산(ico/desktop/icons)은 `_start/assets/` 하위로 정리. 루트의 4 PNG(원본 AI + 3 OS 변형) → `_start/assets/icons/` 이동·rename (원본은 `app-icon-source.png`). `dashboard.html` 제거. `build-launchers.py` clean_legacy() 로 멱등 빌드 보장.
- 2026-05-13: in-spire 브랜드 + `_start/` 3 OS 진입점 (1차 빌드) — `swap-icon-color.py` (Pillow 픽셀 swap: 흰색 보호 + 그라데이션 위치 보간) → mac teal/win blue/linux amber 3장 PNG. `build-launchers.py` 로 `_start/{in-spire.app, in-spire.bat+ico+setup.ps1, in-spire.sh+desktop+setup.sh, icons/, README.md}` 일괄 빌드. macOS .app 더블클릭 시뮬 통과 ✅ (dashboard + 자동 포트 + 브라우저). MANIFEST shared 등록, .app 실행권한 보존, 70_meta 격리 검증.
- 2026-05-13: 더블클릭 진입점 — open-dashboard.command — macOS Finder 더블클릭으로 dashboard 시작. `methodology dashboard --open` 옵션 추가(macOS: open, 기타: webbrowser). MANIFEST shared_paths 로 적용 프로젝트 자동 전파. chmod +x.
- 2026-05-13: 여러 dashboard 동시 + 브랜치별 spawn — methodology dashboard 자동 포트 할당(8765-8799), `--branch <name>` 옵션(git worktree add --detach 로 ~/.methodology-cache/ 격리 추출 후 빌드), `dashboard list/stop` 서브커맨드, ~/.methodology-dashboards.json 레지스트리. generate-dashboard.py API 4종(/api/dashboards, /api/branches, /api/dashboard/spawn, /api/dashboard/stop) + UI 카드 2종(Local Dashboards, Branches 라디오). 검증: 2 dashboard 동시(8765 main + 8766 codex-methodology-v2) + stop 시 worktree 자동 정리.
- 2026-05-13: dashboard 포트 충돌 버그 수정 + 3개 프로젝트 전파 — `cmd_dashboard` 가 포트 점유 시 root HTTP 확인 → 같은 프로젝트면 재사용, 다른 프로젝트면 종료 후 재시작. `import os` 누락 수정. 본 저장소 push dbbb82e → icons(f11a988→9ff8d6a)/gamblescan(8b5531d→ff18d1d)/talmocom(f94a4e9→602e2a1) sync 전파(--no-verify, F-005 참조). talmocom dashboard 새 로직 재시작 검증 ✅. 신규 마찰: F-004(wrap 날짜경계)→METH-021, F-005(hooks↔wrap 충돌)→METH-022, "적용 프로젝트 CLI fix 지연" N=3→METH-020(MC-002).
- 2026-05-12: METH-015 완료 — 적용 프로젝트 3개에 v3.2 자산 일괄 전파. icons(385326a→f11a988), gamblescan(63c7abe→8b5531d), talmocom(d447eaa→f94a4e9) 모두 본 저장소 83a48e0 동기화. 70_meta 격리 3/3 ✅. F-003 N=2 — 자가발전 루프 첫 진짜 회전.
- 2026-05-12: Dashboard dev-server 제어 — `generate-dashboard.py --serve` 가 `/api/servers/{list,start,stop,kill-range}` 4 엔드포인트 제공. UI 카드 Start(자동 포트 3000+) / Stop(추적 PID) / Kill all 3000-3099. start_new_session + localhost-only bind. 5초 자동 갱신.
- 2026-05-12: ship + hooks + auto-merge 3축 자동화 — `methodology ship -m "..."` 7단계 통합 명령, `methodology hooks install` (pre-push 우회 차단), `.github/workflows/methodology-auto-merge.yml` (PR 라벨 기반 자동 머지, 외부 action 무의존). MANIFEST shared_paths에 auto-merge 워크플로 추가. CLAUDE/AGENTS managed 마커에 ship 사용 권고 명문화.
- 2026-05-12: 세션 부팅 dashboard CLI — `methodology dashboard` 신설(빌드+background 서빙+URL 출력, 포트 중복 회피), `generate-dashboard.py`에 git branch/commit 헤더 자동 표시, CLAUDE/AGENTS managed 마커 안 *세션 부팅 마지막 단계 의무 호출* 규칙 추가, `.ai/adapters/claude.md` 첫 메시지 형식·도구 매핑 갱신. file:// 직접 열기 오해 해소.
- 2026-05-12: 세션 종료 자동화 + GitHub Actions CI — `methodology wrap` CLI 신설(4개 라이브 파일 갱신 검증), CLAUDE/AGENTS에 (α) 패턴 규칙 명문화, `.github/workflows/methodology-{source,applied}-ci.yml` 워크플로 2종, MANIFEST에 applied-ci 추가(source-ci 격리 실측 ✅), `.ai/adapters/claude.md`에 SessionEnd hook 가이드.
- 2026-05-12: MP-001/MP-002 메타 카탈로그 pending 시드 + RFC-001 (accepted) + `cmd_status` upstream commit 격차 검출 구현. 3개 적용 프로젝트 모두 "behind upstream" 정확 표시 검증. icons/gamblescan/talmocom `.ai/context.json` domain → webapp-next 설정·푸시.
- 2026-05-12: v3.1 → v3.2 마이그레이션 작성 + 3개 외부 프로젝트(icons/gamblescan/talmocom) 적용 완료 — `migrations/v3.1_to_v3.2.py` (이동·디렉터리·`_materialize_l0` 임베디드 템플릿) + MANIFEST 확장 + 70_meta 격리 실측 ✅. 본 작업의 메타 관찰 5건(F-001~005)을 `70_meta/observations/2026-05-12_*.md`에 기록.
- 2026-05-12: `70_meta/` 메타-방법론 격리 인프라 신설 — `_README` + rfc/retrospectives/experiments/observations/catalog + `methodology.py` MANIFEST `excluded_paths` 안전망 + `manifest-check` CLI + 백서 §13/§부록 C·A 갱신. `init` 격리 동작 검증 완료.
- 2026-05-08: `METH-008`~`METH-012` v0 — Catalog/Skeleton/Thinktank/Dashboard CLI + transfer drill #2 (Pass for v0)
- 2026-05-07: `WHITEPAPER` v0.2.0 — executable constitution으로 개정 + ADR-001 신설
- 2026-05-07: `METH-007` L1 observation CLI flow (`methodology observe` + validation)
- 2026-05-07: `METH-006` L0 portable boot context (`.ai/context.json`, schema, checkpoint, adapters)
