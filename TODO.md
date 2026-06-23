# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

### METH-040
- **title**: 적용 프로젝트(GambleScan) 기획 craft 역주입 — 지침 10/11/12/13/14/15/18 §19 보강·신설 + 개발명세 템플릿 4종 신설
- **notes**: 작업 완료, PR 대기(머지 전). Class A (shared 자산 — 다운스트림 `sync --apply` 수령). 적용 프로젝트 GambleScan의 실전 풀 기획 코퍼스(methodology-v1/planning·development·docs/planning·research)를 방법론으로 **역환류**(METH-039 ICONS 패턴의 GambleScan판). ① §19가 없던 **지침 12(운영)·14(브랜드) §19 신설** + **지침 18(마스터플랜) §18 신설** + 기존 §19 보강(10 사업·11 서비스·13 마케팅·15 PM). ② **개발명세 템플릿 4종 신설**(`50_resources/templates/`): data-model·user-flow·wireframe-spec·functional-spec — 기획↔빌드 사이 빈 층. 관통 주제: 다면(N-sided) 시장 기획 + 거버넌스/추적 craft. 모두 일반 craft(GambleScan 도메인 특화 제외)+출처 명시. 브랜치 `claude/inject-planning-craft-from-gamblescan` → PR(대표 머지=승인 증빙). 머지 후 다운스트림(icons·ai-icons·gamblescan, cafe24 경로 미확인) sync 전파.

### METH-041
- **title**: ICONS knowledge §19 압축 누락 보충 (METH-039 후속) — 지침 10/11/15 §19 체크리스트 본문 복원
- **notes**: 작업 완료, PR #31에 METH-040과 **묶음**(같은 §19 섹션 편집이라 별도 PR이면 충돌). Class A. 사용자 "icons에서도 역주입" 지시 → 확인 결과 ICONS 기획 학습 코퍼스(`icons:40_dev/knowledge/` 01~05 + 학습보고서)는 **이미 METH-039(PR #30 머지)로 주입 완료**된 바로 그 출처. 단 METH-039가 §19로 *압축*하며 "이름만 남고 본문이 증발"한 체크리스트 6건 발견(정밀 대조) → 보충: 지침 10(§19.9 협업·커뮤니케이션 KJ법·블루캡·개발/디자인 대화법, §19.10 Exec Summary 8칸), 11(§19.10 서비스정의 3종·UIUX 7루브릭·용어사전/페이퍼목업/신개념 온보딩), 15(§19.8 WBS 3계층·Task 5요소·제안서 3 Style·품질검토 8항목). 마케팅 13은 완전 커버라 제외. ICONS 도메인 특화 제외. 머지 후 다운스트림 sync(METH-039/040과 합산).

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-039
- **title**: 적용 프로젝트(ICONS) 기획 craft 역주입 — 10/11/13/15 지침 §19 보강 + 기획 양식 템플릿 6종 신설
- **notes**: Completed 2026-06-23. Class A (shared 자산 추가 — 다운스트림은 `sync --apply` 시 수령). 적용 프로젝트 ICONS의 기획 학습 코퍼스(사업/서비스기획 강의·실무·케이스) 정제본(`icons:40_dev/knowledge/` 6종)을 방법론으로 **역환류**. ① 지침 §19 "실무 craft 부록(현장 패턴·적용 프로젝트 환류)" 추가 — `10_사업기획서`(핵심가치 도출·검증 우선순위 게이트·KPI 단위경제 트리·분석틀·보고서 worked-example) · `11_서비스기획서`(ASIS→TOBE·12단계 산출물 체계·데이터 무결성·정책 ON/OFF·스토리보드 8요소·Admin) · `13_마케팅기획서`(Triple Media·4유발 퍼널·채널별·E.C.C.S) · `15_프로젝트_관리`(WBS·Kick-off·제안 5단계). ② `50_resources/templates/` 기획 양식 6종 신설 — requirements-spec·ia-spec·service-policy·user-story·kpi-tree·wbs. 모두 일반 craft(프로젝트 특화 제외)+출처 명시. **PR #30 머지 완료**(2026-06-23 05:25 UTC, 대표 머지=승인 증빙, main `2c6e60c`, `origin/main` 동기). **잔여**: 다운스트림 `sync --apply` 전파 — icons·ai-icons·gamblescan(템플릿 6종 미수령 확인됨), cafe24 경로 미확인.

### METH-038
- **title**: ship build/test 단계 npm 매니저 비호환 버그 픽스 (`npm build` → `npm run build`)
- **notes**: Completed 2026-05-18. Class A. 사용자 보고(talmocom ship 실패). 진단: `cmd_ship` 의 test(4/7)·build(5/7) 단계가 `subprocess.call([manager, "<script>"])` 형태 — pnpm/yarn 은 bare 하위명령을 `run` 으로 alias 하지만 **npm 은 `test/start/stop/restart` 만 내장 단축어**라 `npm build` 가 유효 명령이 아님. talmocom 은 `package-lock.json` 단독 → manager=`npm`, `scripts.build="next build"` 존재 → [methodology.py:1502] 에서 실패. test 단계는 `npm test` 가 우연히 내장 단축어라 무증상이었음. 수정: 두 호출을 `[manager, "run", "<script>"]` 로 통일 (`npm/pnpm/yarn run <script>` 모두 정상, `npm run test` 도 안전). `60_tools/methodology.py` 는 `shared_paths` 자산이라 본 upstream repo 가 정본. **2026-05-18 전파 완료**: PR #27 머지(origin/main `05c8bfa`) 후 4 프로젝트 `sync --apply` — icons `02ce074`·talmocom `992776c`·gamblescan `7e23e9e`·tshome `f6a229f`, 전부 픽스 2/2·origin/main 동기 검증. METH-036/037 미커밋 잔여도 동반 정상 전파(명시경로 add, 비-방법론 제외, 원격 선행분 무겹침 rebase). **2026-05-18 완전 종결**: talmocom methodology.py 픽스 2/2·`build:"next build"` 확인 + 사용자 ship 실측 완료 보고. gamblescan `_start/.cache/dashboard.html` untracked(METH-036 Human 잔여 마감) 검증. PR #27(픽스)/#28(기록) 머지·pull, 브랜치 origin/main 동기.

### METH-037
- **title**: dashboard `/api/servers/start` PATH 보강 — launchd 환경에서 pnpm/npm 미발견 차단
- **notes**: Completed 2026-05-18. Class A. 사용자 보고(talmocom dashboard "프로젝트 dev 서버 열기" → `명령 미발견: npm/pnpm`). 진단: dashboard 프로세스가 Finder 더블클릭(`open-dashboard.command`) 등 비대화형 진입점으로 떠 있으면 launchd 기본 PATH `/usr/bin:/bin:/usr/sbin:/sbin` 만 상속 → `os.environ.copy()` 가 그대로 자식 Popen 에 전달 → `/opt/homebrew/bin/pnpm` 못 찾음. 수정 (`generate-dashboard.py`): `_augmented_path_env()` 헬퍼 — `/opt/homebrew/{bin,sbin}`·`/usr/local/bin`·`~/.local/bin`·`~/.bun/bin`·`~/Library/pnpm`·`~/.volta/bin`·최신 `~/.nvm/versions/node/*/bin` 을 PATH 앞에 prepend (존재하는 디렉터리만). `/api/servers/start` 가 이 env 사용 + `shutil.which(cmd[0], path=env["PATH"])` 로 사전 해석 → 못 찾으면 PATH 포함 명확한 에러. 즉시 우회로 talmocom dashboard 터미널 재기동 완료 (PID 41314). **잔여**: ship + 4 프로젝트(icons/talmocom/gamblescan/tshome) sync 전파 — sync 완료 후 사용자가 떠 있는 dashboard 1회 재기동(또는 launchd 진입점 그대로 두고 새 코드 받기).

<!-- Archived: METH-001~010 (2026-05-07~08), METH-011~012 (2026-05-08), METH-015 (2026-05-12), METH-023~032 (2026-05-15~17). 상세는 git log --grep="METH-" 및 PR #5~#20, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~5건만. -->

