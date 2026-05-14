# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: `methodology wrap` sha256 콘텐츠 해시 검증 — 동일 날짜 다중 ship 오탐 차단. wrap-state.json baseline + 부트스트랩 + ship push 성공시 새 baseline 저장.
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

- 2026-05-15: **`wrap` 콘텐츠 해시 검증** — mtime 기반 → sha256 기반. `.ai/wrap-state.json` 에 라이브 파일 (HANDOFF/TODO/checkpoint) sha256 + 검증된 관찰 로그 목록 저장. 다음 wrap 은 *콘텐츠 변경* 만 통과 (touch / 동일 내용 재저장은 차단). 최초 1회 부트스트랩, ship push 성공시 자동으로 새 baseline 갱신. 원인: 동일 날짜 다중 ship 시 옛 wrap 이 mtime 만 보고 통과 → 다음 세션이 옛 HANDOFF/TODO/checkpoint 를 진실로 신뢰 → 작업 누락 발생 (S-007/S-008/S-009).
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
