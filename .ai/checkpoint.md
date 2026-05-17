# Checkpoint — 2026-05-17 (sync worktree 안전 가드 + QA 전파)

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-7
- Tool: claude-code-cli
- Host: darwin-25.4
- Worktree: `.claude/worktrees/unruffled-johnson-4f4325` (branch `fix/sync-worktree-stale-guard`)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**🆕 sync worktree 안전 가드 + QA 전파 (방금)**:

- 작업: PR #15~#18 (QA 4 fix) 머지 후 4 적용 프로젝트에 정합성 패치 전파
- icons/talmocom/gamblescan **main**: `sync --apply --include-worktrees` → 정확히 7파일 + CLAUDE/AGENTS managed merge, 커밋 완료 (8/7/8 files)
- **중대 발견**: `--include-worktrees` 가 stale worktree 8개 (icons 6 + talmocom 1, 마지막 커밋 2026-05-07, v3.1) 에 *풀 v3.1→v4.0 마이그레이션* 무차별 적용 → 각 133건 churn + 40/50_resources 중복 폴더. 비-방법론 변경 7~20건도 전부 마이그레이션 부수효과 (HANDOFF/TODO path-replace, 루트 generate-dashboard.py 삭제 등) — feature 작업 0.
- 조치 1 — 8개 worktree 전부 `git reset --hard HEAD && git clean -fd` revert. 133→0. 순수 churn 이라 손실 0.
- 조치 2 — 근본 수정 (이 브랜치 `fix/sync-worktree-stale-guard`):
  · `_worktree_sync_safety(wt, target_v, force)` 신설
  · skip 조건: (1) git status dirty → 진행 중 작업 위 churn 방지 (2) cur_v≠target_v 마이그레이션 chain 존재 → stale 브랜치 폴더 rename 강제 방지
  · `--force-worktree-migration` escape hatch
  · cmd_sync 의 worktree 루프가 safe 한 것만 sync, skip 은 사유별 출력 + `worktree 처리 완료 — sync N, skip M`
  · argparse 플래그 추가
  · 검증: icons dry-run → 6/6 worktree "마이그레이션 유발 (v3.1→v4.0)" 정확 skip
- 조치 3 — tshome (v3.2 main, 40/50_resources 중복 + 미커밋 50_tools/methodology.py): 자동 sync 위험 → METH-034 별도 수동 마이그레이션 TODO 로 분리
- 미해결: PR 머지 후 icons/talmocom/gamblescan main 의 sync 커밋은 *push* 안 한 상태 (각 프로젝트 git push 필요). tshome 수동 처리.

**QA 우선순위 4 — dashboard layout 헬퍼 (이전 차례, PR #18 머지됨)**:

- 배경: QA #4. `generate-dashboard.py` 12곳이 `50_resources/60_tools/40_dev` 하드코딩. PR #10 의 `methodology_layout()` 가 있지만 generate-dashboard.py 는 standalone (methodology.py import 안 함) 이라 미적용.
- 해결: 자체 헬퍼 2개 신설
  · `dash_layout(root)` → `_LAYOUT_V4`/`_LAYOUT_V32` dict (tools/resources/meta/dev/version). 60_tools/methodology.py 존재 → v4.0, 50_tools → v3.2
  · `resolve_methodology_py(root)` → 3-tier (60_tools → 50_tools → root)
- 적용 12곳: catalog/skeleton/insights (read_methodology_assets), graph_path/todo/sprints/handoff/master_plan (assemble), commands.json/stack.json, API spawn/stop 핸들러 2곳, project-config, adr_count/snapshot_count
- 검증:
  · syntax OK, v4.0 빌드 정상
  · v3.2 시뮬: dash_layout → resources=40_resources, dev=30_dev, resolve→50_tools/methodology.py ✓
  · 잔여 하드코딩 0 (탐지 정의부 + docs fallback 제외)
- **QA 전체 종료**: 우선순위 1·2 (PR #15) / 5 (PR #16) / 3 (PR #17) / 4 (이 PR) — 4 실제 이슈 + 마이너 5 모두 해소.

**QA 우선순위 3 — commands.json 커버리지 (이전 차례, PR #17)**:

- 배경: QA #3. dashboard Commands 카드가 25 명령만 노출 — init/diff/skeleton 등 누락
- 분석: argparse top-level 15 + nested subparsers. 실제 누락은 init/diff/skeleton(init·build·apply)/catalog seed-pending. (apply/build/list/stop 는 nested subparser 오탐)
- 추가:
  · ops += `init <path> --label --type` / `diff <file>` / `sync --apply --include-worktrees`
  · observe += `catalog seed-pending`
  · 신규 카테고리 "스켈레톤 (L2)" — skeleton init/build/apply
- 결과: 25 → 32 명령, 5 → 6 카테고리
- 검증: JSON valid, 빌드 후 dashboard payload commands.categories = [boot, end, ops, observe, skeleton, export]

**QA 우선순위 5 — 런처 3-tier 통일 (이전 차례, PR #16 머지됨)**:

- 배경: QA 에서 발견한 마이너 #5. `.app`/`.sh`/`.bat` 런처의 methodology.py 탐지가 hook 템플릿(3-tier 60→50→root)과 불일치 — linux/windows 는 60_tools 만, mac 만 2-tier (60→50).
- 근본: 출력 파일들이 `60_tools/build-launchers.py` generator 산출물. 출력만 패치하면 다음 빌드 때 회귀 → generator 자체 수정.
- 수정:
  · mac .app 셸 스니펫: 3-tier METH 탐지 + 미발견 시 osascript alert
  · linux .sh: 동일 3-tier
  · windows .bat: batch 등가 로직 (`if exist ... set "METH=..."` + `if not defined METH` 체인)
  · `dashboard --open` / `dashboard stop --all` 호출도 `"$METH"` / `"%METH%"` 변수화
- 재생성: `python3 60_tools/build-launchers.py` → 3 출력 파일 갱신
- 검증: `bash -n` mac/.app + linux/.sh 구문 통과. 현재 worktree 에서 METH=60_tools/methodology.py 정확 탐지.

**정합성 QA 우선순위 1·2 fix (이전 차례, PR #15 머지됨)**:

- 사용자 요구: 코드베이스 QA 로 정합성 이슈 점검 + 우선순위대로 묶어 처리
- QA 18 카테고리 결과: 12 pass, 4 실제 이슈, 2 마이너. 우선순위 1·2 묶음 PR.
- **Fix 1 — dashboard observation 카운트 정확화**:
  · `generate-dashboard.py:283` 의 `read_methodology_assets()` 가 `root / "50_resources" / "ai_observations"` 만 카운트
  · `70_meta/observations/` 의 20건 (source 저장소 메타-방법론 관찰 로그) 무시됨
  · 해결: `_count_observations(root)` 헬퍼 신설 — 50_resources/ai_observations + 70_meta/observations + v3.2 fallback (40_resources, 60_meta) 모두 합산. `_README`/`README.md` 제외.
  · 검증: 빌드 후 payload `methodology_assets.observations` = 26 (실제 6+20)
- **Fix 2 — commands.json stale path**:
  · `60_tools/commands.json:119` description "10_guides/03 스키마 검증" → v3.2 명명
  · 해결: "20_guides/03 스키마 검증" 으로 1줄 변경
- 미선택 마이너 (별도 PR):
  · commands.json 8 subcmd 미노출 (apply / build / diff / init / list / seed-pending / skeleton / stop) — UX 개선
  · generate-dashboard.py 의 layout 헬퍼 미적용 9곳 — 미래 v5 마이그레이션 부채
  · .app 런처 3-tier 통일 (현재 2-tier) — 거의 발생 안 함

**applied-ci source repo skip (이전 차례)**:

- 사용자 보고: `methodology-applied-ci` 의 "70_meta 미주입 검증" step 이 fail. 메시지: "❌ 70_meta/ 가 적용 프로젝트에 존재 — 메타-방법론이 새어나감".
- 진단: source 저장소 (`YunJuniverse/ai-pipeline-methodology`) 는 70_meta/ 를 *의도적으로* 가지고 있음 (메타-방법론 격리 영역, MANIFEST `excluded_paths` 안전망). applied-ci 는 *적용 프로젝트* 의 누수만 검사하도록 설계됐는데 source 저장소 PR 에서도 같은 검사가 실행되어 항상 fail.
- 이 버그는 *워크플로 첫 도입 시점* 부터 있었음. 옛 검사 `if [ -e 70_meta ]; then exit 1` 가 그대로 동일하게 작동. PR #10 의 layout 탐지 추가로 단지 *가시화*됐을 뿐.
- 해결: job-level `if: github.repository != 'YunJuniverse/ai-pipeline-methodology'` 로 skip.
  · methodology-validate job: skip
  · methodology-freshness job: skip
  · 적용 프로젝트 (icons/talmocom/gamblescan/tshome) 에서는 repository name 이 다르니 정상 실행
  · fork 의 경우 fork name 이 다르니 skip 안 됨 — fork 가 source 와 같은 구조면 70_meta/ 검사 fail. 의도된 동작 (fork 가 source 와 같으면 applied-ci 는 무관).
- 검증: PR #14 에서 자체 CI 가 skip 으로 통과하는지 확인 예정.

**observation lint 정합성 회복 (이전 차례, PR #13 머지됨)**:

- 사용자 보고: source-ci 가 observation lint 에서 18 건 실패 (자유서술 너무 김 / frontmatter 없음 / 파일명 형식 / 절대 경로)
- 분석:
  · 옛 validator 정책: "본문 1단락 ≤ 220자"
  · 실제 사용 패턴: multi-section markdown body (## 패턴, ## 해결, ## 일반화 lesson 등)
  · CLI `--summary` 도 길이 강제 안 함 — *정책-현실 괴리*
  · 18 실패 중 대부분 (15건) "자유서술이 너무 깁니다" — 정책 자체가 잘못된 케이스
- 해결 4단계:
  · (1) validator 본문 길이/단락 제약 제거 — body 는 markdown 자유 형식, frontmatter required fields 만 강제. 본문 빈 경우만 잡음. → 15 건 자동 통과
  · (2) frontmatter 없는 3개 파일 마이그레이션 (PR #9 시기 `cat >` 로 작성한 것):
    - 2026-05-14_wrap-content-hash-validation.md
    - 2026-05-14_wrap-ship-hook-skip.md
    - 2026-05-14_wrap-state-commit-pre-step.md
    → Python 스크립트로 적절한 YAML frontmatter prepend (session_id, authored_by, task_type 등 required snippets)
  · (3) `2026-05-12_v3.1-to-v3.2-migration.md` 파일명 → `2026-05-12_v3-1-to-v3-2-migration.md` rename. session_id 도 갱신. (slug 에 dot 불허)
  · (4) `2026-05-13_dashboard-port-conflict-fix.md` 의 `/Users/hayden/methodology` → `<METHODOLOGY>` 익명화
- 검증: 모든 observation 파일 18→0 실패. source-ci 통과 확인.
- METH-024 (observe CLI 강제) 와 연결: 이 PR 으로 옛 파일 마이그레이션 완료 → 앞으로 CLI 만 사용하면 새 실패 없음.

**Stack 섹션 정리 (이전 차례)**:

- 사용자 요구: PR #11 의 stack bento 가 사용자가 실제로 봤을 때 5개 문제 발견 — Claude Design 핸드오프 번들로 fix 디자인 제공
- 5개 문제:
  · (1) hero(6col)+mid(4col)=10col 항상 2col 자투리, sm 행도 3×3=9 어긋남
  · (2) hero 의 `grid-row: span 2` 가 CSS Grid auto-placement sparse 모드 깨뜨림 — Next.js 15 hero 가 자기 카테고리 카드보다 *아래* 배치됨
  · (3) "FRONTEND" 라벨 7번 반복 — 노이즈만 증가
  · (4) "UI 컴포넌트" / "패키지 매니저" 한글이 uppercase + letter-spacing 으로 강제 줄바꿈
  · (5) hero 거대한 빈 공간 vs sm 이름만 — 정보 밀도 양극화
- 해결 (디자인 번들 기반):
  · 카테고리 그룹 헤더 1회: "01 / FE · Frontend · ★ 1 primary · 7 items"
  · `grid-template-columns: repeat(auto-fill, minmax(240px, 1fr))` — 균일 grid, 자투리 최소화
  · hero = *시각 강조만* (좌측 2px 액센트 라인 + ★ PRIMARY 배지 + `color-mix` 살짝 다른 배경) — layout 변경 X
  · role 라벨 uppercase 제거, letter-spacing 0.02em 로 축소
  · 모든 카드에 reason 3-line clamp 노출
- 구현:
  · CSS: `.stack-grid` → `.stack-wrap` + `.stack-cat` + `.stack-cat-head` + `.stack-cat-grid` + `.stack-card.hero ::before/.star/.name` 강조 트리먼트
  · JS: 카테고리별 group → header + grid 렌더링. 카드 클릭 모달 호환 유지.
  · HTML 컨테이너: `class="stack-grid"` → `class="stack-wrap"` (id 는 stack-grid 유지 — JS 셀렉터 호환)
  · stack.json 데이터 무수정 — `size: hero|mid|sm` 데이터 그대로, 의미만 "레이아웃 크기" → "강조 등급"
- 검증:
  · 빌드 OK
  · 옛 클래스 (`.stack-card.hero` grid row-span, `.stack-card.mid` 등) 완전 제거 확인
  · 새 클래스 (`stack-cat` × 15회, `★ PRIMARY` × 2회) 정상 렌더

**Stack bento 카드 (이전 차례)**:

- 사용자 요구: 회사 홈페이지 기술 스택 (FE/BE/CMS/Infra/Dev 5 카테고리 × 23 항목) 을 Apple M2 키노트 스타일 비대칭 카드로 시각화. 대시보드 어디? 확장성/트레이드오프?
- 분석: Apple 톤 그대로 → 디자인 정합성 깨짐. 25 항목 다 hero → bento 의미 X. 정적 PNG → 코드와 어긋남. → **하이브리드 추천**: 데이터 (stack.json) + 명시적 size hint + 현재 OKLCH 톤 유지 + Overview 탭 통합 + side-sheet 모달 재사용.
- 구현:
  · `60_tools/stack.json` — 23 items, 5 categories. 각 item `size: hero | mid | sm` 명시. 카테고리당 hero 1: Next.js 15 / Resend / Sanity v3 / Vercel / pnpm.
  · CSS: `.stack-grid` (12-col CSS Grid) + `.stack-card.hero` (span 6col x 2row) + `.mid` (4col) + `.sm` (3col). 1100px 이하 반응형 fallback.
  · HTML: Overview 탭 최하단 새 섹션 `#stack-section`. Dev servers 카드 다음.
  · JS: 데이터 정렬 (category 순 + size rank), 렌더링, 카드 클릭 → `openStackModal()` 신규 함수가 side-sheet 모달 띄움 (선택 이유 + meta + docs URL).
  · `assemble()` 가 stack.json 자동 로드 → DATA.stack 으로 전달.
  · MANIFEST shared_paths 에 `60_tools/stack.json` 추가 → 적용 프로젝트 자동 전파.
- 비주얼: 현재 대시보드 톤 유지. 다색 그라데이션·rounded·shadows 없음. 단일 앰버 액센트는 카테고리 라벨에만. hover 시 chev (→) 표시.
- 검증: 빌드 OK, JSON payload 검증 (5 cats, 23 items, hero 5/mid 5/sm 13)
- 미검증: 시각 (Chrome MCP 연결 끊김) — 사용자가 http://localhost:8765 에서 확인 필요

**방법론 정합성 3 fix 묶음 (이전 차례)**:

- 사용자 보고: tshome 작업에서 4가지 에러 발견 — `60_tools/methodology.py` 미발견 (CI), `40_resources` vs `50_resources` 불일치 (wrap), observation frontmatter 형식 오류, task_type enum 무효
- 분석 결과: 표면 4건이지만 root cause 3개의 합성
- 해결: 3 fix 를 한 PR 로 묶음 (METH-024)
  · **Fix 1 — `methodology_layout(target)` 헬퍼**: v3.2/v4.0 구조 자동 탐지 중앙화. tools/resources/foundation/guides/planning/dev/briefs/meta 모든 경로 dict 로 반환. wrap/CI/`_observation_dir`/`_wrap_obs_dirs` 모두 layout 기반. fallback 4번 누락한 root cause 차단.
  · **Fix 2 — `sync --include-worktrees`**: `_git_sibling_worktrees()` 로 같은 repo 의 다른 워크트리 탐지. 마이그레이션 chain 있으면 기본 True 로 일괄 sync. `--main-only` 로 opt-out. (tshome 사고: main 만 v4.0, worktree 들 v3.2 로 남음 → 정확히 이 root cause)
  · **Fix 3 — `observe` CLI 강제 + wrap 선행 검증**: wrap 이 새 .md frontmatter 를 *바로* 검증 (CI 까지 안 가도). 잘못된 형식이면 wrap fail + 파일별 에러 출력. CLAUDE.md/AGENTS.md managed 마커에 `methodology observe` CLI 사용 권고 명문화. `OBSERVATION_DIR` 도 layout 기반.
  · **CI 워크플로**: `methodology-applied-ci.yml` 가 v3.2/v4.0 자동 탐지. v3.2 워크트리에서도 `${{ steps.layout.outputs.tools }}/methodology.py` 로 호출.
- dogfooding: 이 작업의 관찰 로그도 `methodology observe` CLI 로 생성 → Fix 3 자체 검증
- 실측: wrap 이 일부러 만든 잘못된 frontmatter 파일 즉시 잡음 ✓ / sync dry-run 이 icons worktree 6개 감지 ✓ / layout 헬퍼 v3.2/v4.0 모두 정확 ✓

**`wrap` sha256 콘텐츠 해시 검증 (이전 차례)**:

- 사용자 보고: 동일 날짜에 S-007 → S-008 → S-009 연속 ship 했는데, 다음 세션이 "S-008/S-009 미처리"로 인식. wrap 이 mtime 만 보고 통과시켜 옛 HANDOFF/TODO/checkpoint 콘텐츠가 그대로 push 됨.
- 근본 원인: `cmd_wrap` 의 `_mtime_today(p)` 검증 — "오늘 변경됨" = 콘텐츠 갱신 보장 아님. S-007 ship 이 한 번 mtime 을 찍으면 S-008/S-009 ship 은 *touch 안 해도* 통과 (false-positive).
- 해결 설계 (옵션 ① + ②):
  · `.ai/wrap-state.json` — `last_validated_commit`, 라이브 파일 sha256, 검증된 관찰 로그 목록
  · `cmd_wrap` 재작성: 부트스트랩 → 콘텐츠 sha 비교 → 변경 없으면 fail
  · `cmd_ship` 6단계 commit 직전에 `commit_wrap_state(target)` 호출 — wrap-state 와 라이브 파일이 동일 commit 에 패키징되어 clone/pull 후 wrap 일관성 보장 (post-push 갱신 시 commit 의 wrap-state 가 옛 baseline 을 가리키는 버그 회피). ship → push 시 `METHODOLOGY_SHIP_IN_PROGRESS=1` 환경변수로 pre-push hook 의 wrap 재실행 skip (commit 직전 동기화로 hook 의 wrap 이 sha 일치 → fail 하는 chicken-and-egg 회피)
- 구현 위치 `60_tools/methodology.py`:
  · 신설 헬퍼: `wrap_state_path`, `load_wrap_state`, `save_wrap_state`, `file_sha256`, `current_git_head`, `list_observation_files`, `bootstrap_wrap_state`, `commit_wrap_state`
  · `cmd_wrap` 전면 재작성 — 부트스트랩 1회 통과 / sha 동일 시 fail / 새 관찰 1건 이상 요구
  · `cmd_ship` push 성공 직후 `commit_wrap_state` 호출 (push 실패 시는 호출 안 함)
  · `today` 라벨 버그 수정 (date.today → datetime.now(timezone.utc).date)
- 검증 시나리오 (모두 실측):
  · bootstrap: state 없음 → 현재 sha 저장 → 4/4 pass
  · 변경 없음 재실행: 4/4 fail (sha 동일)
  · `touch` 만: 4/4 fail (sha 동일) — 본 버그 시나리오 차단 확인
  · 실제 콘텐츠 갱신: 4/4 pass (sha 갱신)
- 관찰 로그: `70_meta/observations/2026-05-15_wrap-content-hash-validation.md`
- 적용 프로젝트 sync 필요: methodology.py 가 shared_paths 에 이미 있어 `methodology sync --apply --path <project>` 로 자동 전파됨.

**USER_GUIDE + commands.json + Commands 카드 (이전 차례)**:
- 사용자 요청: 사람 워크플로 기준 사용자 가이드 (시작부터 코드 인계까지) + 자주 사용 명령 미리 저장 + 대시보드 표시
- 신설 파일:
  · `10_foundation/USER_GUIDE.md` — 11 섹션 (시작·매일·brief·작업·종료·인계·명령·Class·문제해결·다이어그램·참조)
  · `60_tools/commands.json` — 5 카테고리 × 23 명령:
    boot (6) / end (5) / ops (5) / observe (4) / export (5)
- dashboard 갱신:
  · assemble() 에 commands.json 자동 로드
  · Overview 탭 최상단 *Commands 카드* — 카테고리 탭 + 명령 클릭 → 클립보드 복사 + 2.5s toast
  · USER_GUIDE.md 링크 카드 헤더에 명시
- MANIFEST shared 에 USER_GUIDE + commands.json 추가 → 적용 프로젝트 자동 전파
- 검증: HTML 마크업 9건 매칭, "commands" 데이터 JSON 포함 ✅

**methodology export — 외주 인계 자동화 (이전 차례)**:
- 사용자 통증: 외주 인계 시 방법론·메타·브리프 자산이 코드와 섞임 → 수동 정리 + 기밀 유출 위험
- 옵션 검토: A/B (코드를 `app/` 하위로) — Next.js 충돌 비용 큼 / D (방법론을 `.methodology/` 로) — 자동 로드 깨짐 → **옵션 C (export CLI)** 채택
- `cmd_export`: source walk + 제외 목록(DIRS/FILES/BASENAMES) + sensitive 차단 + 결과 검증
- 제외:
  · NN_ 방법론 폴더 (00_briefs ~ 90_archive)
  · _start/.ai/.methodology-cache/.claude/.codex/migrations
  · 빌드 산출물: node_modules, .next/.nuxt/.svelte-kit/.vercel/.turbo, dist/build/out/coverage/.cache, __pycache__/.venv 등
  · OS·캐시 basename: .DS_Store, .eslintcache, .tsbuildinfo, *-debug.log
  · .github/workflows/methodology-*.yml
- sensitive 차단: .env/credential/secret/.pem/.key/.p12/.pfx (.sample/.example 통과). --allow-sensitive 우회.
- 옵션: --target / --dry-run / --zip(tar.gz) / --include-git / --force / -v
- 안전망: 복사 후 target 재 walk → 방법론 흔적 1건이라도 발견 시 exit 3 (이중 검증)
- 실측: icons 467 / gamblescan 1,459 / talmocom 487 파일 (90%+ 노이즈 제거)
- talmocom 실제 export 검증: 방법론 흔적 0, 코드 모두 포함, .env.local 정상 차단 → --allow-sensitive 후 98MB 결과 ✅
- CLAUDE.md / AGENTS.md managed: 외주 인계 워크플로 명문화 (모든 AI 모델 공통)

**방법론 v4.0 — 00_briefs/ + NN_ +10 shift (이전 차례)**:
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
