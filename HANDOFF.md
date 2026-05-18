# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-038 완료 (ship build/test 단계 npm 매니저 비호환 버그 픽스 — `npm build`→`npm run build`). talmocom ship 실패 보고 기인. ship + 4 프로젝트 sync 전파 대기.
- **Current mode**: fullstack
- **Next TODO**: METH-038/037 ship + 4 프로젝트 sync 전파, METH-036 PR 머지, 기추적 프로젝트 1회 `git rm --cached _start/.cache/dashboard.html`(Human), METH-018 (Human hooks install)
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

- 2026-05-18: **METH-038 ship npm 매니저 비호환 버그 픽스** — 사용자 보고 "talmocom ship 빌드 실패". 진단: `cmd_ship` test(4/7)·build(5/7) 가 `subprocess.call([manager, "<script>"])` — pnpm/yarn 은 bare 하위명령을 `run` alias 하나 npm 내장 단축어는 `test/start/stop/restart` 뿐 → `npm build` 무효. talmocom `package-lock.json` 단독 → manager=npm, `scripts.build="next build"` → methodology.py:1502 실패. test 는 `npm test` 가 우연히 내장이라 무증상. 수정: 두 호출을 `[manager, "run", "<script>"]` 로 통일(`npm/pnpm/yarn run` 모두 정상). `60_tools/methodology.py` 는 `shared_paths` 정본이라 본 upstream 수정 → 다운스트림은 `sync --apply` 수령. `py_compile` 통과. Class A. 잔여: ship + 4 프로젝트 sync 전파. S-021 코드 sprint 빌드 검증 선결 해소.
- 2026-05-18: **METH-037 dashboard `/api/servers/start` PATH 보강** — talmocom 사용자 보고 "프로젝트 대시보드에서 dev 서버 열기 → `명령 미발견: npm/pnpm`". 진단: dashboard 프로세스(PID 40528)가 launchd 기본 PATH `/usr/bin:/bin:/usr/sbin:/sbin` 으로 떠 있었음 (Finder 더블클릭 `open-dashboard.command` 같은 비대화형 진입점 → 사용자 shell PATH 비상속). `os.environ.copy()` 가 그대로 자식 Popen 에 상속 → `/opt/homebrew/bin/pnpm` 못 찾음. 단기 우회: 터미널에서 dashboard 재기동 (PID 41314 정상). 근본 수정 (`generate-dashboard.py`): `_augmented_path_env()` 헬퍼 — `/opt/homebrew/{bin,sbin}`·`/usr/local/bin`·`~/.local/bin`·`~/.bun/bin`·`~/Library/pnpm`·`~/.volta/bin`·최신 `~/.nvm/versions/node/*/bin` 을 PATH 앞에 prepend (존재하는 것만). `/api/servers/start` 가 이 env 사용 + `shutil.which(cmd[0], path=env["PATH"])` 로 사전 해석 → 못 찾으면 PATH 까지 포함한 명확한 에러 반환. 검증: launchd 빈약 PATH 흉내에서도 pnpm/npm/node 모두 resolve. Class A. 잔여: ship + 4 프로젝트 (icons/talmocom/gamblescan/tshome) sync 전파.
- 2026-05-18: **METH-036 방법론 생성물 전파/추적 차단** — 사용자 통증 "icons `git pull` 이 `_start/.cache/dashboard.html`·`.ai/wrap-state.json` 때문에 반복 차단". 진단: 머지 충돌 아님 — 머신 생성물이 추적됨. 근본 원인 (1) `_start` 가 `shared_paths` 라 `copy_path` 무필터 rglob 가 빌드 캐시까지 프로젝트로 전파·추적, (2) `.gitignore` 가 MANIFEST 자산 아님 → 프로젝트가 생성물 무시 못 함. 수정 (methodology.py): `_excluded_from_copy()` → copy_path 가 `.cache/__pycache__/.git/*.pyc/.DS_Store` 복사·prune 제외; `ensure_gitignore()` → init/sync 가 프로젝트 `.gitignore` 에 마커 블록(idempotent, 앱 규칙 보존) 보장. `.ai/wrap-state.json` 은 설계상 추적 대상(sha256 baseline 동일 commit 패키징)이라 무시 목록 제외 — 초기 진단의 untrack 제안은 철회. icons dry-run: gitignore 갱신 예고 + 캐시 미전파 검증. icons 자체는 사용자 요청대로 미변경. Class A. 잔여(Human): 기추적 프로젝트 1회 `git rm --cached _start/.cache/dashboard.html`.
- 2026-05-18: **PR #22/#23 4 프로젝트 sync 전파** — PR #22(MC-001/002+ADR-002)·#23(METH-035 칸반 실시간+METH-016) 머지 후 origin/main 위에서 `sync --apply` 4 프로젝트 일괄. 전부 v4.0→v4.0 (마이그레이션 0), 각 8 파일 변경 (generate-dashboard.py / methodology.py / commands.json / methodology-applied-ci.yml / _start 4 / .methodology-version). CLAUDE/AGENTS unchanged. icons 6b940a1·talmocom f285f65·gamblescan 6f7d23e·tshome 245fbea push (MC-001 명시 경로 add, METH-022 sync-commit hook 면제로 --no-verify). icons/tshome sibling worktree 각 1개는 `_worktree_sync_safety`(PR #19) 가 비-마이그레이션이라 정상 skip. 사용자 액션 잔여: dashboard 1회 재시작(METH-035 serve), METH-018 hooks install.
- 2026-05-17: **칸반 실시간 갱신 (METH-035) + METH-016 (PR #23)** — 사용자 통증 "칸반 stale, 재실행만이 답?" → dashboard.html 정적 스냅샷이 원인. `_serve_with_api(out,port,root)` + `_maybe_rebuild()`: GET `/dashboard.html` 시 소스 6종 mtime > dashboard.html 이면 자동 재생성 (재시작 불필요, ⌘R). `/api/src-mtime` + 클라이언트 4초 폴링 → 변경 배너. METH-016 SessionEnd hook 은 update-config 스킬로 settings.local.json(gitignored) 적용. PR #22 머지 후 rebase — HANDOFF/TODO HEAD 채택 + METH-016 Ready→Done + METH-035 추가.
