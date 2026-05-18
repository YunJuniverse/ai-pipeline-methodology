# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready


### METH-018
- **title**: 사용자 환경에 hooks 설치 + ship 첫 일상 사용 검증
- **mode**: fullstack
- **change-class**: A
- **owner**: Human + AI
- **acceptance criteria**:
  - [ ] 사용자가 본 저장소·icons·gamblescan·talmocom 각각에서 `methodology hooks install` 1회 실행
  - [ ] 다음 작업 종료 시 `methodology ship -m "..."` 사용 — git add/commit/push 직접 호출 없이 통과
  - [ ] sensitive 파일 차단·테스트 실패 차단 동작 1회씩 우연히 시연되면 학습 신호 누적
- **notes**: hooks는 worktree마다 별도 설치 필요 (git의 hooks는 추적되지 않음). 적용 프로젝트는 다음 sync로 ship CLI를 받지만 hooks는 *그 다음 단계*에서 사용자가 1회 실행. **AI측 완료** (METH-022 로 sync commit 자동 면제까지 구현됨) — Human 1회 실행만 남음: 각 프로젝트 루트에서 `python3 60_tools/methodology.py hooks install`. **2026-05-18 갱신**: PR #22/#23 sync 전파 push 완료 (icons/talmocom/gamblescan/tshome 모두 최신 hooks 템플릿 + METH-022 sync 면제 로직 보유) → METH-018 의 전제(프로젝트가 최신 CLI/hooks 템플릿 보유) 충족됨. 이제 순수하게 Human 1회 실행만 대기.

## InProgress

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-037
- **title**: dashboard `/api/servers/start` PATH 보강 — launchd 환경에서 pnpm/npm 미발견 차단
- **notes**: Completed 2026-05-18. Class A. 사용자 보고(talmocom dashboard "프로젝트 dev 서버 열기" → `명령 미발견: npm/pnpm`). 진단: dashboard 프로세스가 Finder 더블클릭(`open-dashboard.command`) 등 비대화형 진입점으로 떠 있으면 launchd 기본 PATH `/usr/bin:/bin:/usr/sbin:/sbin` 만 상속 → `os.environ.copy()` 가 그대로 자식 Popen 에 전달 → `/opt/homebrew/bin/pnpm` 못 찾음. 수정 (`generate-dashboard.py`): `_augmented_path_env()` 헬퍼 — `/opt/homebrew/{bin,sbin}`·`/usr/local/bin`·`~/.local/bin`·`~/.bun/bin`·`~/Library/pnpm`·`~/.volta/bin`·최신 `~/.nvm/versions/node/*/bin` 을 PATH 앞에 prepend (존재하는 디렉터리만). `/api/servers/start` 가 이 env 사용 + `shutil.which(cmd[0], path=env["PATH"])` 로 사전 해석 → 못 찾으면 PATH 포함 명확한 에러. 즉시 우회로 talmocom dashboard 터미널 재기동 완료 (PID 41314). **잔여**: ship + 4 프로젝트(icons/talmocom/gamblescan/tshome) sync 전파 — sync 완료 후 사용자가 떠 있는 dashboard 1회 재기동(또는 launchd 진입점 그대로 두고 새 코드 받기).

### METH-036
- **title**: 방법론 생성물(_start/.cache, dashboard.html) 프로젝트 전파/추적 차단
- **notes**: Completed 2026-05-18. Class A. 근본 원인: (1) `_start` 가 `shared_paths` 라 `copy_path` 무필터 rglob 로 `_start/.cache/dashboard.html` 빌드 캐시가 적용 프로젝트에 전파·추적됨, (2) `.gitignore` 는 MANIFEST 자산이 아니라 프로젝트로 전파 안 됨 → 프로젝트가 생성물을 추적, dashboard 서버 재생성 시 `git pull` 영구 차단 (icons 반복 실증). 수정: `_excluded_from_copy()` 로 copy_path 가 `.cache/__pycache__/.git/*.pyc/.DS_Store` 복사·prune 제외 + `ensure_gitignore()` 가 init/sync 시 프로젝트 `.gitignore` 에 마커 블록(idempotent, 앱 규칙 보존) 보장. `.ai/wrap-state.json` 은 설계상 추적 대상이라 무시 목록 제외. icons dry-run 검증: gitignore 갱신 예고 + 캐시 미전파 확인. **잔여(Human)**: 기추적 프로젝트는 1회 `git rm --cached _start/.cache/dashboard.html` 필요 — sync 의 .gitignore 만으로 기추적 파일 untrack 안 됨.

### METH-035
- **title**: 칸반보드 실시간 갱신 — serve 자동 재빌드 + 변경 감지 배너
- **notes**: Completed 2026-05-17. dashboard.html 정적 1회 스냅샷이라 stale, 서버 재실행만이 답이었음. (1) `_serve_with_api(out,port,root)` + `_maybe_rebuild()`: GET `/dashboard.html` 시 소스 6종 mtime > dashboard.html 이면 자동 재생성 — 재시작 불필요, ⌘R 만으로 최신. (2) `/api/src-mtime` + 클라이언트 4초 폴링 → 변경 시 우하단 배너(클릭 새로고침). 실측: TODO 변경 → 재빌드 YES. Class A (PR #23). 주의: 떠 있는 서버는 1회 재시작해야 새 serve 로직 적용.

### METH-016
- **title**: SessionEnd hook 활성화 — Claude Code 환경에서 wrap 자동 호출
- **notes**: Completed 2026-05-17. `update-config` 스킬로 `.claude/settings.local.json` 에 SessionEnd hook (`python3 60_tools/methodology.py wrap 2>&1 || true`) 추가. 기존 Stop hook + permissions 보존. settings.local.json gitignored — 로컬 활성화 (repo 변경 없음). 옛 "AI 직접 적용 안 함" 가정은 update-config 스킬로 해소. Class A (PR #23).

### METH-019
- **title**: MC-001 활성 승급 — sync 시 git add -A 빌드산출물 오염 패턴
- **notes**: Completed 2026-05-17. `70_meta/catalog/MC-001_git-add-A-pollutes-sync-commit.md` 활성 엔트리. N≥3 (talmocom 2026-05-12 이미지 + tshome 2026-05-17 .sanity/dist 재재발). 솔루션: 방법론 경로 명시 add 화이트리스트 + 커밋 전 오염 검증. Class B (PR #22).

### METH-020
- **title**: MC-002 활성 승급 — 적용 프로젝트 CLI fix 전파 지연 패턴
- **notes**: Completed 2026-05-17. `70_meta/catalog/MC-002_applied-project-cli-fix-lag.md` 활성 엔트리. N≥7 (METH-015 F-001/003, dashboard-port-conflict F-003, multi-dashboard F-005, QA 4건 전파). 솔루션: 절대경로 CLI / 정기 sync --include-worktrees / hooks install --force. 장기 --use-upstream. Class B (PR #22).

### METH-013
- **title**: 메타-방법론 격리 ADR — RFC-001 → ADR-002
- **notes**: Completed 2026-05-17. `40_dev/adr/ADR-002-meta-methodology-isolation.md` accepted. 70_meta 격리 = MANIFEST excluded_paths + manifest-check 이중 안전망 명문화. RFC-001 은 status 용도 소진 → ADR-002 가 단일 출처. Class B (PR #22).

### METH-022
- **title**: pre-push hook ↔ wrap 충돌 — 방법론 sync commit 면제
- **notes**: Completed 2026-05-17. hook 템플릿에 HEAD commit 메시지 case 매칭 추가 — `chore(methodology): sync*` / `chore: sync methodology*` / `chore(methodology): v*마이그레이션*` 이면 manifest-check 만 유지하고 wrap --strict skip. ship 의 `METHODOLOGY_SHIP_IN_PROGRESS` env skip 과 별개 (수동 git push 경로). 4 프로젝트 전파에서 매번 수동 `--no-verify` 한 실증 통증 제거. sh -n 검증 + case 패턴 4종 시뮬 통과. 본 저장소 hook 재설치 완료.

### METH-021
- **title**: wrap 날짜 경계 완화 — 자정 넘긴 세션 대응 (moot close)
- **notes**: Closed 2026-05-17 as moot. PR #9 가 wrap 을 mtime → sha256 콘텐츠 해시 기반으로 전면 재작성하면서 `_mtime_today` 제거됨. 현재 observation 검사는 `new_obs = [f for f in cur_obs if f not in seen]` (validated_files set-diff) 로 *날짜 무관*. wrap 의 `today` 는 표시 메시지 전용. 자정 넘긴 세션의 어제-날짜 관찰 파일도 baseline 에 없으면 "신규"로 정확 탐지 → 원래 문제(F-004) 소멸. 별도 코드 변경 불필요.

### METH-014
- **title**: 메타-카탈로그 첫 시드 — MP-001/MP-002 완료
- **notes**: Completed 2026-05-17 (실질 2026-05-12 시드 + 본 세션 모니터링 종결). `70_meta/catalog/_pending/MP-001`(status 버전 문자열 비교) + `MP-002`(sync init_files 누락) 시드 완료. 두 패턴 모두 N≥2 도달 → METH-019/020 활성 승급으로 이관 (별도 Class B PR). 모니터링 placeholder 종결.

### METH-033
- **title**: sync --include-worktrees 안전 가드 — stale worktree churn 차단
- **notes**: Completed 2026-05-17. QA 패치 전파 중 발견: `--include-worktrees` 가 stale v3.1 worktree 8개에 풀 마이그레이션 churn 무차별 적용. 8개 revert. `_worktree_sync_safety()` 신설 — dirty/마이그레이션 유발 worktree skip + `--force-worktree-migration` escape hatch.

### METH-034
- **title**: tshome v3.2→v4.0 수동 마이그레이션 (split-brain 해소)
- **notes**: Completed 2026-05-17. tshome 원격이 9커밋 앞서 + 제품 수정 4건(broken links/image opt/visual audit/studio basePath) 포함 → force-push 불가, 95-rename rebase 위험. 전략: 로컬 stale 2커밋 백업 브랜치 보존 → origin/main 리셋(제품 수정 확보) → fresh 재마이그레이션. 처리: 50_resources/ai_observations 5건 정본 통합(tshome-027 frontmatter 버전 채택), 빈 50_resources/40_dev 제거(rename 차단 해제), v3.2→v4.0 6 rename, 사업/분기 보고서 4건 백업서 복원, .sanity/dist 제외. 결과 commit 688d142 push (관찰 12/4 사업문서/0 옛폴더, 제품 9커밋 보존). 백업 브랜치 정리. **METH-034 + 전체 4 프로젝트 전파 완료** (icons/talmocom/gamblescan main push 완료, tshome 마이그레이션+push 완료).

<!-- Archived: METH-001~010 (2026-05-07~08), METH-011~012 (2026-05-08), METH-015 (2026-05-12), METH-023~032 (2026-05-15~17). 상세는 git log --grep="METH-" 및 PR #5~#20, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~5건만. -->

