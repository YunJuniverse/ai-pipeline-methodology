# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-039 기획 craft 역주입(ICONS 학습→방법론) — 지침 10/11/13/15 §19 보강 + 기획 양식 템플릿 6종 신설. 브랜치 `claude/inject-planning-craft-from-icons`, PR 대기.
- **Current mode**: fullstack
- **Next TODO**: METH-039 PR 머지 후 다운스트림 `sync --apply` 전파(icons·ai-icons·cafe24·gamblescan). 그 외 다음 지시 대기.
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

- 2026-06-23: **METH-039 기획 craft 역주입** — 적용 프로젝트 ICONS의 기획 학습 정제본(`icons:40_dev/knowledge/` 6종)을 방법론으로 환류. 지침 10/11/13/15에 §19 "실무 craft 부록" 추가(핵심가치 도출·검증 우선순위 게이트·KPI 트리·ASIS→TOBE·12단계 산출물·데이터 무결성·Triple Media·4유발 퍼널·WBS·제안 5단계) + `50_resources/templates/` 기획 양식 6종(requirements/ia/service-policy/user-story/kpi-tree/wbs) 신설. 일반 craft만(프로젝트 특화 제외)·출처 명시. Class A(shared, sync 전파). 브랜치 `claude/inject-planning-craft-from-icons` → PR, 머지 후 다운스트림 sync.
- 2026-05-18: **Human 잔여 종결 — METH-036/038 완전 마감** — 사용자 보고 "휴먼작업 모두 완료" → 검증: gamblescan `_start/.cache/dashboard.html` ✅ untracked(`git rm --cached` 완료, METH-036 마감), talmocom methodology.py 픽스 2/2·`build:"next build"` 확인(ship 실측 정상 전제 충족, METH-038 마감). PR #27(픽스)·#28(기록) 머지·pull 완료, 브랜치 origin/main 동기(ahead 0). 이번 세션 작업(METH-038/037/036/018) 전부 main 안착·종결. 활성 백로그 비움 — 다음 후보 S-021 코드 sprint.
- 2026-05-18: **METH-018 pre-push hook 최신화 (stale→v4.0)** — 발견: icons/talmocom/gamblescan/tshome 모두 hook "활성"이나 구버전(v3.x) 템플릿 — `[ -f "50_tools/methodology.py" ]` 만 검사 → v4.0(`60_tools/`)에선 항상 else "검증 skip" → manifest-check·wrap --strict 안전망이 사실상 무력화. (TODO/HANDOFF 의 "미설치, Human 1회 대기" 프레이밍이 부정확했음 — 실제 stale 설치.) `hooks install --force` 4개 재설치 → 최신 템플릿(3-tier 60→50→root + `METHODOLOGY_SHIP_IN_PROGRESS` ship-skip + METH-022 sync-commit 면제) 반영, 4개 모두 검증. 정본 repo 는 이미 최신. git 공용 `.git/hooks` 공유라 repo당 1회면 worktree 전부 커버 — "worktree마다 별도" 메모 정정. Class A.
- 2026-05-18: **METH-038/037/036 4 프로젝트 sync 전파 완료** — PR #27(METH-038) 머지(origin/main `05c8bfa`) 후 icons/talmocom/gamblescan/tshome 에 `sync --apply` 일괄. 발견: 4개 모두 `HEAD==origin/main` 인데 METH-036/037 sync 가 `--apply`만 되고 미커밋 잔여(methodology.py·generate-dashboard.py·.gitignore·.methodology-version) — 위험 충돌 아닌 이전 세션 미완 전파로 판정. 명시 경로 add(MC-001, `-A` 금지)로 방법론 자산 4개만 커밋, 비-방법론 제외(talmocom `next-env.d.ts` stash·pop, gamblescan `_start/.cache/dashboard.html` 미스테이지 — METH-036 Human `git rm --cached` 잔여). icons 직접 push, talmocom/gamblescan/tshome 은 원격 2커밋(타 세션 dev-spec/관찰/앱) 선행 → 파일 무겹침 확인 후 rebase(force 금지). tshome 은 미추적 `ts-service-plan.html` 가 origin/main 추적본과 바이트 동일 확인 후 제거→rebase(백업 보관). 최종: 4개 픽스 2/2·origin/main 동기 검증. 잔여: talmocom `ship` 실측.
- 2026-05-18: **METH-038 ship npm 매니저 비호환 버그 픽스** — 사용자 보고 "talmocom ship 빌드 실패". 진단: `cmd_ship` test(4/7)·build(5/7) 가 `subprocess.call([manager, "<script>"])` — pnpm/yarn 은 bare 하위명령을 `run` alias 하나 npm 내장 단축어는 `test/start/stop/restart` 뿐 → `npm build` 무효. talmocom `package-lock.json` 단독 → manager=npm, `scripts.build="next build"` → methodology.py:1502 실패. test 는 `npm test` 가 우연히 내장이라 무증상. 수정: 두 호출을 `[manager, "run", "<script>"]` 로 통일(`npm/pnpm/yarn run` 모두 정상). `60_tools/methodology.py` 는 `shared_paths` 정본이라 본 upstream 수정 → 다운스트림은 `sync --apply` 수령. `py_compile` 통과. Class A. 잔여: ship + 4 프로젝트 sync 전파. S-021 코드 sprint 빌드 검증 선결 해소.
- 2026-05-18: **METH-037 dashboard `/api/servers/start` PATH 보강** — talmocom 사용자 보고 "프로젝트 대시보드에서 dev 서버 열기 → `명령 미발견: npm/pnpm`". 진단: dashboard 프로세스(PID 40528)가 launchd 기본 PATH `/usr/bin:/bin:/usr/sbin:/sbin` 으로 떠 있었음 (Finder 더블클릭 `open-dashboard.command` 같은 비대화형 진입점 → 사용자 shell PATH 비상속). `os.environ.copy()` 가 그대로 자식 Popen 에 상속 → `/opt/homebrew/bin/pnpm` 못 찾음. 단기 우회: 터미널에서 dashboard 재기동 (PID 41314 정상). 근본 수정 (`generate-dashboard.py`): `_augmented_path_env()` 헬퍼 — `/opt/homebrew/{bin,sbin}`·`/usr/local/bin`·`~/.local/bin`·`~/.bun/bin`·`~/Library/pnpm`·`~/.volta/bin`·최신 `~/.nvm/versions/node/*/bin` 을 PATH 앞에 prepend (존재하는 것만). `/api/servers/start` 가 이 env 사용 + `shutil.which(cmd[0], path=env["PATH"])` 로 사전 해석 → 못 찾으면 PATH 까지 포함한 명확한 에러 반환. 검증: launchd 빈약 PATH 흉내에서도 pnpm/npm/node 모두 resolve. Class A. 잔여: ship + 4 프로젝트 (icons/talmocom/gamblescan/tshome) sync 전파.
