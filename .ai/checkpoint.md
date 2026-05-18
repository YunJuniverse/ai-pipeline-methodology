# Checkpoint — 2026-05-18 (METH-038 ship npm 매니저 비호환 버그 픽스)

> ✅ METH-038: 사용자 보고 "talmocom 에서 `methodology.py ship` 빌드 단계 실패".
> 진단: `cmd_ship` 의 test(4/7)·build(5/7) 단계가
> `subprocess.call([manager, "<script>"])` 형태. pnpm/yarn 은 bare 하위명령을
> 자동으로 `run` 으로 alias 하지만 **npm 내장 단축어는 `test/start/stop/restart`
> 뿐** → `npm build` 는 유효 명령이 아님. talmocom 은 `package-lock.json` 단독
> → manager=`npm`, `package.json` 에 `scripts.build="next build"` 존재 →
> `60_tools/methodology.py:1502` 에서 `npm build` 실행 → 실패. test 단계는
> `npm test` 가 우연히 npm 내장 단축어라 무증상이었음.
> 수정: 두 호출을 `[manager, "run", "<script>"]` 로 통일 — `npm run build` /
> `pnpm run build` / `yarn run build` 모두 정상, `npm run test` 도 안전.
> `60_tools/methodology.py` 는 `MANIFEST.shared_paths` 자산이라 본 upstream
> repo 가 정본 — talmocom 등 다운스트림은 다음 `sync --apply` 로 수령.
> `python3 -m py_compile` 통과. Class A. 직전 작업(METH-037 PATH 보강,
> METH-036, PR #22-23)의 잔여(ship + 4 프로젝트 sync 전파, METH-018 hooks
> install, 기추적 프로젝트 `git rm --cached`)는 여전히 유효.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-7
- Tool: claude-code-cli
- Host: darwin-25.4
- Worktree: `.claude/worktrees/romantic-fermi-62f41c` (branch `claude/romantic-fermi-62f41c`)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-038 ship npm 매니저 비호환 버그 픽스**:

- 사용자: "talmocom 에서 발생한 오류야 확인해봐" → 진단 후 "지금 적용하고 pr까지 진행해".
- 근본 원인: `60_tools/methodology.py` 의 `cmd_ship`
  - `ship: 4/7 — test` → `subprocess.call([manager, "test"], ...)`
  - `ship: 5/7 — build` → `subprocess.call([manager, "build"], ...)`
  - manager 추정: `pnpm-lock.yaml` → pnpm, `yarn.lock` → yarn, 그 외 → **npm**.
  - npm 은 `npm test`/`start`/`stop`/`restart` 만 내장 단축어. `npm build`
    는 존재하지 않는 명령 → talmocom(npm 프로젝트, `scripts.build="next build"`)
    에서 ship 빌드 단계 실패. test 는 우연히 npm 내장이라 통과해 증상이 build
    에만 드러남. pnpm/yarn 사용 프로젝트는 bare→run alias 라 무증상이었음.
- 수정 (2곳, `60_tools/methodology.py`):
  - `:1482` `[manager, "test"]` → `[manager, "run", "test"]`
  - `:1502` `[manager, "build"]` → `[manager, "run", "build"]`
  - 근거: `npm/pnpm/yarn run <script>` 3-매니저 모두 정상. 최소 변경.
- 검증: `python3 -m py_compile 60_tools/methodology.py` 통과. talmocom 실측
  근거 확인 — `/Users/hayden/talmocom` 에 `package-lock.json` 단독,
  `scripts={dev,build:"next build",start,typecheck,db:*}`.
- 수정 위치 판단: 현재 디렉터리가 upstream(`ai-pipeline-methodology`) 정본.
  `methodology.py` 는 `shared_paths` → `sync --apply` 가 다운스트림을 항상
  덮어씀. 따라서 talmocom 로컬 수정은 sync 시 소실 — 정본만 수정이 정답.
- 라이브 파일 갱신: TODO.md(METH-038 Done, 3건 유지), HANDOFF.md(Working
  on/Next/Recent Changes, 5건으로 트림), 본 checkpoint, observe 로그.

**4 프로젝트 sync 전파 (이어서, 사용자 "전파 진행해")**:

- PR #27 머지 확인(origin/main `05c8bfa`) 후 upstream 정본
  `/Users/hayden/methodology` 기준 dry-run → `--apply` 4 프로젝트.
- 발견: 4개 모두 `HEAD==origin/main` 인데 METH-036/037 sync 가 `--apply`만
  되고 미커밋 잔여(methodology.py·generate-dashboard.py·.gitignore·
  .methodology-version). 위험 충돌 아닌 *이전 세션 미완 전파* 로 판정 →
  명시 경로 add(`-A` 금지, MC-001)로 방법론 자산 4개만 커밋.
- 비-방법론 제외: talmocom `next-env.d.ts`(stash→pop 원복),
  gamblescan `_start/.cache/dashboard.html`(미스테이지 — METH-036 Human
  `git rm --cached` 잔여).
- push: icons 직접. talmocom/gamblescan/tshome 은 원격이 2커밋(타 세션
  dev-spec/관찰/앱) 선행 → 우리 4파일과 무겹침 확인 후 `git rebase`
  (force push 절대 안 함). tshome 은 미추적 `ts-service-plan.html` 가
  origin/main 추적본과 바이트 동일 확인 → 백업 후 제거→rebase.
- 결과: icons `02ce074`·talmocom `992776c`·gamblescan `7e23e9e`·
  tshome `f6a229f`, 4개 픽스 2/2·origin/main 동기 검증 완료.

**METH-018 pre-push hook 최신화 (이어서, 사용자 "진행해줘")**:

- 사용자 "METH-018 hooks install 은 뭐하면 돼?" → 상태 점검 중 발견:
  4 프로젝트 hook 이 "활성"이나 구버전(v3.x) 템플릿 — `[ -f
  "50_tools/methodology.py" ]` 만 검사. v4.0(`60_tools/`)이라 항상
  else "검증 skip" → manifest-check·wrap --strict 안전망 사실상 무력화.
  TODO/HANDOFF 의 "미설치, Human 1회 대기" 프레이밍이 부정확했음.
- 조치: `hooks install --force` 4 프로젝트 재설치 → 최신 템플릿
  (3-tier 60→50→root + `METHODOLOGY_SHIP_IN_PROGRESS` ship-skip +
  METH-022 sync-commit 면제) 반영. 4개 모두 검증 통과. 정본 repo 는
  이미 최신. git 공용 `.git/hooks` 공유 → repo당 1회면 worktree 커버
  ("worktree마다 별도" 메모 정정).
- 안전망(매 push 시 manifest-check + wrap --strict, sync-commit 면제)
  이 4 프로젝트에서 실제 동작 가능 상태로 복구됨.

## ⚠️ 다음 사람: 우선 처리 후보

- **PR #27 머지·4 프로젝트 전파: 완료** (2026-05-18). icons `02ce074`,
  talmocom `992776c`, gamblescan `7e23e9e`, tshome `f6a229f` — 전부
  METH-038 픽스 2/2 라인 + `origin/main` 동기 검증. METH-036/037 미커밋
  잔여도 같은 커밋에 동반 정상 전파됨.
- **남은 검증**: talmocom 에서 실제 `ship -m "..."` 1회 — build 단계가
  `npm run build` 로 정상 통과하는지 실측 (S-021 코드 sprint 빌드 검증 선결).
  단, talmocom 은 PR #27 머지 후 hooks 미설치(METH-018 대기) 상태일 수 있음.

## 다음 사람에게 (구체적 첫 행동)

1. talmocom 에서 `ship` 실측으로 build 단계(`npm run build`) 정상 확인
   → METH-038 완전 종결. 실패 시 talmocom 로컬 methodology.py 가 최신인지
   (`grep 'manager, "run"' 60_tools/methodology.py` = 2/2) 먼저 확인.
2. ~~METH-018 hooks install~~ — 완료 (stale v3.x → v4.0 `--force` 재설치).
3. (Human) METH-036 잔여: gamblescan 에서 1회
   `git rm --cached _start/.cache/dashboard.html` (기추적 빌드산출물 untrack).
4. tshome: 미추적 `ts-admin-guide.html` 는 순수 로컬(origin 무관) — 사용자
   판단 영역. `ts-service-plan.html` 는 origin/main 추적본으로 정착됨
   (백업 `/tmp/tshome-ts-service-plan.html.bak`, 내용 동일).

## 막혔던 지점 / 시도해봤지만 안 된 것

- 없음. 단일 진단 → 2-라인 픽스로 해소. 부트 시 dashboard CLI 호출은
  본 세션에서 미실행(포커스된 핫픽스 작업) — 다음 세션 부팅 시 정상 절차 복귀.

## 미해결 결정사항 (Open Questions)

- ship build/test 단계에 `scripts` 존재 여부는 검사하나, npm 외 매니저에서
  스크립트명 충돌(예: 사용자 정의 `start`) 가능성은 현 범위 밖 — 필요 시 별도.
- S-021 코드 sprint 진입 전 ship 의 test 단계 실측 검증(현재 build 만 talmocom
  으로 간접 확인) — 코드 sprint 첫 ship 에서 자연 검증 예정.

## 환경 메모

- 본 작업 worktree: `.claude/worktrees/romantic-fermi-62f41c`
  (branch `claude/romantic-fermi-62f41c`). main head: 72e291a.
- 변경 파일: `60_tools/methodology.py`(2-라인), `TODO.md`, `HANDOFF.md`,
  `.ai/checkpoint.md`, 신규 observation 로그 1건.
- talmocom: `/Users/hayden/talmocom`, npm(`package-lock.json`),
  Next.js(`scripts.build="next build"`). 본 픽스의 직접 수혜 대상.
- 70_meta 격리 안전망: 본 변경은 60_tools 정본 수정이라 무관 — 정상.
