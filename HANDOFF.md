# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

## Current Focus

- **Working on**: in-spire `_start/` 구조 재편 + 루트 클러터 정리 — 사용자 명시 표기 (mac)(windows)(linux) 파일명, 보조 자산은 _start/assets/ 하위로 정리, 루트의 4 PNG → assets/icons/ 이동·rename, dashboard.html 제거.
- **Current mode**: fullstack
- **Next TODO**: 3개 적용 프로젝트에 새 _start/ 구조 전파, 루트 README.md 를 in-spire 브랜드로 리브랜딩, METH-020 (MC-002 승급)
- **Blockers**: none

## Active Links

- Current PR:
- Current issue:
- Relevant ADRs:
- Relevant snapshots: `30_dev/snapshots/implementation-plan-2026-05-07.md`, `30_dev/snapshots/transfer-drill-2026-05-08.md`

## Open Decisions

| ID | Decision | Needed By | Status |
|----|----------|-----------|--------|
| - | `.claude/worktrees/` and `.codex/` are local tool metadata and should be gitignored | 2026-05-07 | Closed |

## Open Issues

| ID | Issue | Severity | Next Step |
|----|-------|----------|-----------|
| - | Some legacy/archive docs may still mention pre-`30_dev` or pre-`50_tools` paths | Low | Sweep only if those docs become live references again |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `30_dev/snapshots/` 참조.

- 2026-05-13: **`_start/` 구조 재편 + 루트 클러터 정리** — 사용자 명시 표기 파일명: `in-spire (mac).app` / `(windows).bat` / `(linux).sh`. 보조 자산(ico/desktop/icons)은 `_start/assets/` 하위로 정리. 루트의 4 PNG(원본 AI + 3 OS 변형) → `_start/assets/icons/` 이동·rename (원본은 `app-icon-source.png`). `dashboard.html` 제거. `build-launchers.py` clean_legacy() 로 멱등 빌드 보장.
- 2026-05-13: in-spire 브랜드 + `_start/` 3 OS 진입점 (1차 빌드) — `swap-icon-color.py` (Pillow 픽셀 swap: 흰색 보호 + 그라데이션 위치 보간) → mac teal/win blue/linux amber 3장 PNG. `build-launchers.py` 로 `_start/{in-spire.app, in-spire.bat+ico+setup.ps1, in-spire.sh+desktop+setup.sh, icons/, README.md}` 일괄 빌드. macOS .app 더블클릭 시뮬 통과 ✅ (dashboard + 자동 포트 + 브라우저). MANIFEST shared 등록, .app 실행권한 보존, 60_meta 격리 검증.
- 2026-05-13: 더블클릭 진입점 — open-dashboard.command — macOS Finder 더블클릭으로 dashboard 시작. `methodology dashboard --open` 옵션 추가(macOS: open, 기타: webbrowser). MANIFEST shared_paths 로 적용 프로젝트 자동 전파. chmod +x.
- 2026-05-13: 여러 dashboard 동시 + 브랜치별 spawn — methodology dashboard 자동 포트 할당(8765-8799), `--branch <name>` 옵션(git worktree add --detach 로 ~/.methodology-cache/ 격리 추출 후 빌드), `dashboard list/stop` 서브커맨드, ~/.methodology-dashboards.json 레지스트리. generate-dashboard.py API 4종(/api/dashboards, /api/branches, /api/dashboard/spawn, /api/dashboard/stop) + UI 카드 2종(Local Dashboards, Branches 라디오). 검증: 2 dashboard 동시(8765 main + 8766 codex-methodology-v2) + stop 시 worktree 자동 정리.
- 2026-05-13: dashboard 포트 충돌 버그 수정 + 3개 프로젝트 전파 — `cmd_dashboard` 가 포트 점유 시 root HTTP 확인 → 같은 프로젝트면 재사용, 다른 프로젝트면 종료 후 재시작. `import os` 누락 수정. 본 저장소 push dbbb82e → icons(f11a988→9ff8d6a)/gamblescan(8b5531d→ff18d1d)/talmocom(f94a4e9→602e2a1) sync 전파(--no-verify, F-005 참조). talmocom dashboard 새 로직 재시작 검증 ✅. 신규 마찰: F-004(wrap 날짜경계)→METH-021, F-005(hooks↔wrap 충돌)→METH-022, "적용 프로젝트 CLI fix 지연" N=3→METH-020(MC-002).
- 2026-05-12: METH-015 완료 — 적용 프로젝트 3개에 v3.2 자산 일괄 전파. icons(385326a→f11a988), gamblescan(63c7abe→8b5531d), talmocom(d447eaa→f94a4e9) 모두 본 저장소 83a48e0 동기화. 60_meta 격리 3/3 ✅. F-003 N=2 — 자가발전 루프 첫 진짜 회전.
- 2026-05-12: Dashboard dev-server 제어 — `generate-dashboard.py --serve` 가 `/api/servers/{list,start,stop,kill-range}` 4 엔드포인트 제공. UI 카드 Start(자동 포트 3000+) / Stop(추적 PID) / Kill all 3000-3099. start_new_session + localhost-only bind. 5초 자동 갱신.
- 2026-05-12: ship + hooks + auto-merge 3축 자동화 — `methodology ship -m "..."` 7단계 통합 명령, `methodology hooks install` (pre-push 우회 차단), `.github/workflows/methodology-auto-merge.yml` (PR 라벨 기반 자동 머지, 외부 action 무의존). MANIFEST shared_paths에 auto-merge 워크플로 추가. CLAUDE/AGENTS managed 마커에 ship 사용 권고 명문화.
- 2026-05-12: 세션 부팅 dashboard CLI — `methodology dashboard` 신설(빌드+background 서빙+URL 출력, 포트 중복 회피), `generate-dashboard.py`에 git branch/commit 헤더 자동 표시, CLAUDE/AGENTS managed 마커 안 *세션 부팅 마지막 단계 의무 호출* 규칙 추가, `.ai/adapters/claude.md` 첫 메시지 형식·도구 매핑 갱신. file:// 직접 열기 오해 해소.
- 2026-05-12: 세션 종료 자동화 + GitHub Actions CI — `methodology wrap` CLI 신설(4개 라이브 파일 갱신 검증), CLAUDE/AGENTS에 (α) 패턴 규칙 명문화, `.github/workflows/methodology-{source,applied}-ci.yml` 워크플로 2종, MANIFEST에 applied-ci 추가(source-ci 격리 실측 ✅), `.ai/adapters/claude.md`에 SessionEnd hook 가이드.
- 2026-05-12: MP-001/MP-002 메타 카탈로그 pending 시드 + RFC-001 (accepted) + `cmd_status` upstream commit 격차 검출 구현. 3개 적용 프로젝트 모두 "behind upstream" 정확 표시 검증. icons/gamblescan/talmocom `.ai/context.json` domain → webapp-next 설정·푸시.
- 2026-05-12: v3.1 → v3.2 마이그레이션 작성 + 3개 외부 프로젝트(icons/gamblescan/talmocom) 적용 완료 — `migrations/v3.1_to_v3.2.py` (이동·디렉터리·`_materialize_l0` 임베디드 템플릿) + MANIFEST 확장 + 60_meta 격리 실측 ✅. 본 작업의 메타 관찰 5건(F-001~005)을 `60_meta/observations/2026-05-12_*.md`에 기록.
- 2026-05-12: `60_meta/` 메타-방법론 격리 인프라 신설 — `_README` + rfc/retrospectives/experiments/observations/catalog + `methodology.py` MANIFEST `excluded_paths` 안전망 + `manifest-check` CLI + 백서 §13/§부록 C·A 갱신. `init` 격리 동작 검증 완료.
- 2026-05-08: `METH-008`~`METH-012` v0 — Catalog/Skeleton/Thinktank/Dashboard CLI + transfer drill #2 (Pass for v0)
- 2026-05-07: `WHITEPAPER` v0.2.0 — executable constitution으로 개정 + ADR-001 신설
- 2026-05-07: `METH-007` L1 observation CLI flow (`methodology observe` + validation)
- 2026-05-07: `METH-006` L0 portable boot context (`.ai/context.json`, schema, checkpoint, adapters)
