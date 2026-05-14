# Checkpoint — 2026-05-14 (방법론 v4.0 — 00_briefs + NN_ shift)

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-sonnet-4-6
- Tool: claude-code-cli
- Host: darwin-25.4
- Worktree: `.claude/worktrees/lucid-grothendieck-5a6562` (branch `claude/lucid-grothendieck-5a6562`)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**🆕 방법론 v4.0 — 00_briefs/ + NN_ +10 shift (방금)**:
- 사용자 요구: 인간 입력 채널 신설 (리서치·아이디어·회의록), AI 가 *매 세션 자동 로드*
- 00_briefs/{current,archived,meetings} 신설 (.gitkeep 으로 빈 디렉터리 init 보장)
- 옛 NN_ → 새 NN_ +10 shift: 00_foundation→10, 10_guides→20, ..., 60_meta→70
- migrations/v3.2_to_v4.0.py — PATH_MAP + re 매칭 + chr() 우회로 self-replace 회피 (7 폴더 rename, 121 파일 path replace)
- METHODOLOGY_VERSION → v4.0
- MANIFEST 갱신: 00_briefs/_README.md → shared_paths, current/archived/meetings → init_paths
- .ai/context.json must_read_optional 에 00_briefs/current/*.md 추가
- CLAUDE.md / AGENTS.md managed 마커: 세션 부팅 시 brief 자동 로드 규칙 명시
- 백서 §부록 C 표 갱신 — 00=Briefs, 10=Foundation, ..., 70=Meta
- 검증: version v4.0 ✅, manifest-check ✅, init 격리 (00_briefs 전파 + 70_meta 미주입) ✅

**setup → _start/settings/ 분리 (이전 차례)**:
- 사용자 요구: setup-windows.ps1 + setup-linux.sh 를 settings/ 하위 폴더에 모음
- build_windows / build_linux: settings 디렉터리 mkdir + 거기에 setup 작성
- 스크립트 내부 경로 보정:
  · PowerShell: `$here = settings/`, `$root = parent`, $batPath = root/.bat, $lnkPath = root/.lnk
  · bash: HERE=settings/, ROOT=parent, EXEC=ROOT/.sh, DESKTOP=ROOT/assets/.desktop
- clean_legacy() 에 옛 위치 setup-*.{ps1,sh} 추가 (멱등)
- README.md: settings/ 경로 명시
- 빌드 검증: _start/{진입점 3 + README + assets/ + settings/ + .cache/} ✅
- .app 더블클릭 시뮬 정상 (HTTP 200 size=438442)

**dashboard.html → _start/.cache/ 격리 (이전 차례)**:
- 사용자 통증: 루트의 dashboard.html 을 *직접 더블클릭* 하면 file:// 로 열려 fetch 차단 → 정적·반쪽 작동. 휴먼에러 우려.
- 수정: cmd_dashboard 기본 out_path 를 _start/.cache/dashboard.html 로 변경
  · _start/ 미존재 환경 fallback: 루트 (legacy)
  · cmd_dashboard 가 *옛 루트 dashboard.html* 자동 unlink (자가 정리)
- .gitignore 에 `_start/.cache/` 추가
- 검증: 빌드 → _start/.cache/dashboard.html (437,870 bytes), 루트 깨끗, http://localhost:8765 정상 200
- Finder 기본 숨김(.접두) + SimpleHTTPRequestHandler path traversal 차단 → *사용자가 dashboard.html 볼 가능성 0*

**dashboard root rewrite (이전 차례)**:
- 사용자 보고: `http://localhost:8765/` 가 'Directory listing for /' 페이지로 랜딩
- 원인: SimpleHTTPRequestHandler 기본 동작 — index.html 미존재 시 directory listing. 우리는 dashboard.html 이름이라 미매칭.
- 수정: do_GET 첫 줄에서 `self.path == "/"` 시 `/dashboard.html` 로 rewrite. 쿼리스트링도 보존.
- 검증: HTTP 200 size=437,542 (dashboard.html 전체 응답), 'Directory listing' 매칭 0건 ✅
- 디버깅 비용 6분 — closure 캡처 의심했으나 진짜 원인은 *background server 재시작 누락*. 코드 수정 후 stop --all + 새 dashboard 호출 필수.

**_start/ 구조 재편 + 루트 정리 (이전 차례)**:
- 사용자 명시 표기 적용 — 파일명에 OS 식별자 괄호 포함:
  - `in-spire (mac).app`
  - `in-spire (windows).bat`
  - `in-spire (linux).sh`
- 보조 자산을 `_start/assets/` 하위로 분리: `in-spire.ico`, `in-spire.desktop`, `icons/`
- `_start/` 루트에는 진입점 5개 + README — 6개 항목만 노출
- 루트 클러터 정리:
  - `app-icon--1024x1024-png--squircle-rounded-square-b.png` → `_start/assets/icons/app-icon-source.png` (원본 보존, rename)
  - `in-spire-{mac,win,linux}.png` 루트 → 루트에서 삭제 (assets/icons/ 에 이미 있음)
  - `dashboard.html` 제거 (빌드 산출물)
- `build-launchers.py` 갱신:
  - `find_source_pngs()` — assets/icons 우선·루트 fallback
  - `clean_legacy()` — 옛 _start 구조 자동 제거 (멱등 빌드)
  - setup-windows.ps1 / setup-linux.sh 내부 파일명·경로 갱신

격리 검증 ✅ (init 시 새 구조 + .app 실행권한 보존 + 70_meta 격리 모두 통과).

**in-spire 브랜드 첫 시각 자산 (이전 차례)**:
- 사용자 결정: 브랜드명 **in-spire** (이중 의미: in spire + inspire), 배경색만 차등 (옵션 A), 실행파일만 폴더로 (옵션 3)
- AI 생성: macOS teal/navy 나선 1장 (Recraft) → 의외의 행운: 두 갈래 나선 (DNA double helix, 자가복제 메타포)
- `60_tools/swap-icon-color.py` — Pillow 픽셀 swap (흰색 stroke·외부 배경 보호 + 그라데이션 위치 보간) → win blue/linux amber 2장 자동 생성
- `60_tools/build-launchers.py` — 3 PNG → `_start/` 전체 자산 일괄:
  - macOS: in-spire.app (Info.plist + AppIcon.icns 10 사이즈 + MacOS/in-spire 셸 스크립트)
  - Windows: in-spire.bat + in-spire.ico (7 사이즈) + setup-windows.ps1 (.lnk 자동 생성)
  - Linux: in-spire.sh + in-spire.desktop (템플릿) + setup-linux.sh (Exec/Icon 절대경로 치환) + 256 PNG
  - icons/ 원본 PNG 4장 + README.md
- macOS .app 더블클릭 시뮬 실측 통과 ✅
- MANIFEST shared_paths 에 _start/ 추가 → 적용 프로젝트 자동 전파 (.app 실행권한·.icns 멀티사이즈 보존)

**더블클릭 진입점 open-dashboard.command (이전 차례)**:
- `open-dashboard.command` (macOS, +x) — 폴더 루트에서 Finder 더블클릭 → Terminal 에서 자동 실행 → dashboard --open
- `methodology dashboard --open` 옵션 — 기동 후 브라우저 자동 열기 (macOS: subprocess.Popen(['open', url]) / 기타: webbrowser.open)
- MANIFEST shared_paths 에 추가 → 적용 프로젝트 자동 전파 (shutil.copy2 가 mode 보존)
- 사용자 의도: 터미널 명령 외우지 않고 *폴더에서 더블클릭* 으로 dashboard 시작

**여러 dashboard 동시 + 브랜치별 spawn (이전 차례)**:
- `methodology dashboard` 자동 포트 할당 (8765-8799 빈 포트 탐색)
- `--branch <name>` 옵션 — git worktree add --detach → ~/.methodology-cache/<project>/<branch-slug>/ 격리 빌드 → 별도 포트 서빙. working tree 안 건드림.
- `dashboard list` — ~/.methodology-dashboards.json 레지스트리 조회 + 죽은 항목 자동 정리
- `dashboard stop --port N | --all` — 종료 + worktree remove --force 자동
- generate-dashboard.py API: /api/dashboards, /api/branches, /api/dashboard/spawn, /api/dashboard/stop
- UI 카드 2종 신설: Local Dashboards (포트별 표 + Stop 버튼), Branches (라디오 + Open dashboard 버튼)
- 검증: 본 저장소 main(8765) + codex-methodology-v2(8766) 동시 운영 ✅. stop --all 후 worktree·레지스트리 정리 ✅.

**dashboard 포트 충돌 버그 수정 (이전 차례)**:
- 증상: talmocom 에서 `methodology dashboard` 호출했는데 8765 에 떠 있던 *본 저장소* dashboard 가 표시됨
- 원인: cmd_dashboard 가 포트 점유 시 "어느 프로젝트인지" 무시하고 무조건 "기존 URL 보고"
- 수정: `_running_dashboard_root(port)` (HTTP GET → "root": 추출) + `_kill_port_listeners(port)` — 다른 프로젝트면 종료 후 재시작. `import os` 누락도 수정.
- 검증: 본 저장소 ↔ talmocom 전환 시 자동 kill+재시작 동작 확인 (단, 적용 프로젝트의 옛 methodology.py 는 아직 fix 없음 — sync 전파 필요)
- 임시 우회: `python3 /Users/hayden/methodology/60_tools/methodology.py dashboard --path ~/talmocom --port 8765` (본 저장소 새 코드 사용)
- 전파 완료: 본 저장소 push dbbb82e → icons 9ff8d6a / gamblescan ff18d1d / talmocom 602e2a1 (sync --no-verify, F-005)
- talmocom dashboard 새 로직 재시작 검증 ✅ ("포트 8765에 다른 dashboard(root: methodology) — 종료 후 talmocom 로 재시작")
- 신규 마찰: F-004(wrap 날짜경계)→METH-021, F-005(hooks↔wrap)→METH-022, "적용프로젝트 CLI fix 지연" N=3→METH-020(MC-002)

## ⚠️ 다음 사람: 우선 처리 후보
- METH-022 (hooks↔wrap 충돌): 적용 프로젝트가 방법론 sync 마다 --no-verify 필요 — *우회 습관화 위험*. pre-push hook 이 `chore(methodology): sync` commit 면제하도록 빠른 fix 권장.
- METH-021 (wrap 날짜경계): 자정 넘긴 세션에서 ship false-fail. `--days 2` 완화.

**METH-015 적용 프로젝트 일괄 전파 (이전)**:
- icons sync → commit f11a988 → push 385326a..f11a988
- gamblescan sync → commit 8b5531d → push 63c7abe..8b5531d
- talmocom sync → commit f94a4e9 (이미지 제외 명시 add) → push d447eaa..f94a4e9
- 3/3 70_meta 격리 ✅, applied-ci/auto-merge 워크플로 주입 ✅
- 자가발전 루프 첫 진짜 회전: F-003(talmocom 이미지 add 패턴) N=2 도달 → METH-019(MC-001 승급) 활성

**0. Dashboard dev-server 제어 패널** (이전 세션):
- `generate-dashboard.py --serve` 가 BaseHTTPRequestHandler 기반 커스텀 핸들러로 진화
- API 엔드포인트 4개: GET /api/servers, POST /api/servers/start, POST /api/servers/{pid}/stop, POST /api/servers/kill-range
- UI 카드: cwd/cmd 입력 → Start (포트 3000부터 자동) / 행별 Stop / Kill all 3000-3099 (추적 외 포함) / 5초 자동 갱신
- 보안: bind 127.0.0.1 only, CORS 미설정, 죽은 PID 자동 정리
- 자식 프로세스: start_new_session=True + os.killpg(getpgid, SIGTERM) — pnpm/node child 함께 정리
- 외부 패키지 0개

**A. ship + hooks + auto-merge** (이전 세션):
- `methodology ship -m "..."` — 7단계 통합 (wrap → manifest-check → sensitive → test → build → add+commit → push). 각 옵션 (--no-test/build/push/commit/add-all/allow-sensitive)
- `methodology hooks install` — `.git/hooks/pre-push` 자동 설치 (manifest-check + wrap --strict). 우회 `git push --no-verify`
- `.github/workflows/methodology-auto-merge.yml` — PR 'auto-merge' 라벨 시 자동 squash 머지 (외부 action 무의존)
- MANIFEST shared_paths에 auto-merge.yml 추가
- CLAUDE.md / AGENTS.md managed 마커에 ship 사용 권고 + hooks 1회 설치 안내

**B. dashboard CLI** (이전 세션):
- `methodology dashboard` — 빌드 + background 서빙 + URL 출력 (branch/commit/pid). 포트 중복 회피.

0. **dashboard CLI 신설** — `60_tools/methodology.py cmd_dashboard` + 서브커맨드 등록.
   - `--port` (기본 8765), `--no-serve`, `--path`, `--out`, `--background` 옵션
   - 빌드 → background 서빙 → URL + branch + commit + pid 출력
   - 포트 중복 회피 (socket 점검). 이미 떠 있으면 기존 URL 보고.
0a. **generate-dashboard.py 헤더 보강** — assemble()에 git branch + commit short SHA 자동 호출, HTML meta span 에 표시. file:// 직접 열기 시도에서도 *어느 브랜치/시점*인지 즉시 확인 가능.
0b. **CLAUDE.md / AGENTS.md (managed 마커 안)** — 세션 부팅 *마지막 단계* 의무 호출 규칙 추가. 모든 AI 모델 공통. sync 시 적용 프로젝트 자동 전파.
0c. **`.ai/adapters/claude.md`** — 첫 메시지 권장 형식·도구 매핑에 dashboard CLI 반영.

1. (이전 세션) **wrap CLI 신설** — `60_tools/methodology.py cmd_wrap` + 서브커맨드 등록.
   - 4개 라이브 파일(`HANDOFF.md`, `TODO.md`, `.ai/checkpoint.md`, ai_observations) 오늘 갱신 여부 검증
   - git status 요약 출력
   - `--strict` 옵션: 누락 시 exit 1 (CI/hook용)
2. **CLAUDE.md / AGENTS.md 보강** — managed 마커 안에 "세션·작업 종료 절차" 규칙 명문화 (모든 AI 모델 공통). (α) 패턴: AI 자동 작성 → wrap 검증 → 사용자 다음 turn에서 수정 가능.
3. **GitHub Actions 워크플로 2종 신설**:
   - `.github/workflows/methodology-source-ci.yml` — 본 저장소 전용 (manifest-check, 70_meta 격리 실측, observation lint, idempotency, dashboard build)
   - `.github/workflows/methodology-applied-ci.yml` — 적용 프로젝트 주입용 (70_meta 미주입, manifest-check, observation lint, dashboard build, wrap/status warn-only)
4. **MANIFEST 확장** — applied-ci 워크플로를 `shared_paths`에 추가. source-ci는 격리(실측 검증 완료).
5. **`.ai/adapters/claude.md` 갱신** — SessionEnd hook 설정 가이드 추가.
6. 본 세션 메타-관찰 기록 (`70_meta/observations/2026-05-12_wrap-cli-and-ci-workflows.md`).

## 다음 사람에게 (구체적 첫 행동)

1. **METH-015 — 적용 프로젝트 3개에 applied-ci 워크플로 주입**:
   - 본 커밋 후 `cd ~/icons && python3 60_tools/methodology.py sync --apply` (gamblescan/talmocom 동일)
   - 단, 각 적용 프로젝트의 *로컬 60_tools/methodology.py가 옛 버전*일 수 있음 — 본 저장소 methodology.py로 sync 호출 권장: `python3 /Users/hayden/methodology/60_tools/methodology.py sync --path ~/icons --apply`
   - GitHub에서 워크플로 첫 실행 결과 점검 — 70_meta 미주입 / manifest-check / observation lint 모두 ✅이어야
   - 실패 시 워크플로 또는 검증 로직 조정
2. **METH-016 — SessionEnd hook 활성화**: 사용자 결정 영역. `.claude/settings.json`에 `SessionEnd` hook 등록 안내 (`.ai/adapters/claude.md` 참조).
3. (선택) 분기 회고 시점 — `70_meta/retrospectives/2026-Q2_methodology-review.md` 작성. 단, 백서 §10 Stage 1~2 단계라 *지표 누적 부족* — 회고 가치 낮음. 데이터 더 쌓인 후 진행.

## 막혔던 지점 / 시도해봤지만 안 된 것

- 없음. 본 세션은 두 가지 통증(TODO 미갱신 + CI 부재)을 단일 패치로 해소.

## 미해결 결정사항 (Open Questions)

- wrap CLI의 `--strict` 모드 CI 도입 — 현재 warn-only. 신선도 강제 시점은 데이터 누적 후 분기 회고에서 결정.
- 다른 AI 도구(Cursor, Codex CLI 등)의 SessionEnd 등가물 — `.ai/adapters/{cursor,codex}.md` 신설 시 동일 가이드 추가 후보.

## 환경 메모

- 본 저장소 main 현재 head: 곧 새 커밋 (f1a993f → 다음).
- 적용 프로젝트 3개 모두 `applied_commit: 6c99091` — 본 커밋 후 격차 더 커짐. `methodology status` 가 자동으로 "behind upstream" 표시.
- 70_meta 격리 안전망: init/sync/source-ci 모두 격리 실측 통과.
