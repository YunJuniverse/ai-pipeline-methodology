# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-018
- **title**: 적용 프로젝트 pre-push hook 최신화 (stale v3.x → v4.0 재설치)
- **notes**: Completed 2026-05-18. Class A. 진단: icons/talmocom/gamblescan/tshome 모두 pre-push hook 이 "활성"이나 **구버전(v3.x) 템플릿** — `[ -f "50_tools/methodology.py" ]` 만 검사. 프로젝트는 v4.0(`60_tools/`)이라 항상 else 로 빠져 "검증 skip" → manifest-check·wrap --strict 안전망이 사실상 무력화 상태였음. (HANDOFF/TODO 의 "미설치, Human 1회 실행 대기" 프레이밍은 부정확했음 — 실제로는 stale 설치.) 조치: `hooks install --force` 로 4 프로젝트 재설치 → 현재 템플릿(3-tier 경로탐지 60→50→root + `METHODOLOGY_SHIP_IN_PROGRESS` ship-skip + METH-022 sync-commit 면제) 반영. 검증: 4개 모두 60_tools 인식·ship-skip·sync면제 포함 확인. 정본 repo 는 이미 최신. **worktree 메모 정정**: git 공용 `.git/hooks` 공유라 repo당 1회면 worktree 전부 커버 (기존 "worktree마다 별도 설치" 메모는 이 구성에선 부정확). 잔여(Human): ship/sensitive·test 차단 동작은 일상 사용 중 자연 검증.

### METH-038
- **title**: ship build/test 단계 npm 매니저 비호환 버그 픽스 (`npm build` → `npm run build`)
- **notes**: Completed 2026-05-18. Class A. 사용자 보고(talmocom ship 실패). 진단: `cmd_ship` 의 test(4/7)·build(5/7) 단계가 `subprocess.call([manager, "<script>"])` 형태 — pnpm/yarn 은 bare 하위명령을 `run` 으로 alias 하지만 **npm 은 `test/start/stop/restart` 만 내장 단축어**라 `npm build` 가 유효 명령이 아님. talmocom 은 `package-lock.json` 단독 → manager=`npm`, `scripts.build="next build"` 존재 → [methodology.py:1502] 에서 실패. test 단계는 `npm test` 가 우연히 내장 단축어라 무증상이었음. 수정: 두 호출을 `[manager, "run", "<script>"]` 로 통일 (`npm/pnpm/yarn run <script>` 모두 정상, `npm run test` 도 안전). `60_tools/methodology.py` 는 `shared_paths` 자산이라 본 upstream repo 가 정본. **2026-05-18 전파 완료**: PR #27 머지(origin/main `05c8bfa`) 후 4 프로젝트 `sync --apply` — icons `02ce074`·talmocom `992776c`·gamblescan `7e23e9e`·tshome `f6a229f`, 전부 픽스 2/2·origin/main 동기 검증. METH-036/037 미커밋 잔여도 동반 정상 전파(명시경로 add, 비-방법론 제외, 원격 선행분 무겹침 rebase). 잔여: talmocom 에서 `ship` 실측(build `npm run build` 정상 통과 — S-021 선결).

### METH-037
- **title**: dashboard `/api/servers/start` PATH 보강 — launchd 환경에서 pnpm/npm 미발견 차단
- **notes**: Completed 2026-05-18. Class A. 사용자 보고(talmocom dashboard "프로젝트 dev 서버 열기" → `명령 미발견: npm/pnpm`). 진단: dashboard 프로세스가 Finder 더블클릭(`open-dashboard.command`) 등 비대화형 진입점으로 떠 있으면 launchd 기본 PATH `/usr/bin:/bin:/usr/sbin:/sbin` 만 상속 → `os.environ.copy()` 가 그대로 자식 Popen 에 전달 → `/opt/homebrew/bin/pnpm` 못 찾음. 수정 (`generate-dashboard.py`): `_augmented_path_env()` 헬퍼 — `/opt/homebrew/{bin,sbin}`·`/usr/local/bin`·`~/.local/bin`·`~/.bun/bin`·`~/Library/pnpm`·`~/.volta/bin`·최신 `~/.nvm/versions/node/*/bin` 을 PATH 앞에 prepend (존재하는 디렉터리만). `/api/servers/start` 가 이 env 사용 + `shutil.which(cmd[0], path=env["PATH"])` 로 사전 해석 → 못 찾으면 PATH 포함 명확한 에러. 즉시 우회로 talmocom dashboard 터미널 재기동 완료 (PID 41314). **잔여**: ship + 4 프로젝트(icons/talmocom/gamblescan/tshome) sync 전파 — sync 완료 후 사용자가 떠 있는 dashboard 1회 재기동(또는 launchd 진입점 그대로 두고 새 코드 받기).

<!-- Archived: METH-001~010 (2026-05-07~08), METH-011~012 (2026-05-08), METH-015 (2026-05-12), METH-023~032 (2026-05-15~17). 상세는 git log --grep="METH-" 및 PR #5~#20, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~5건만. -->

