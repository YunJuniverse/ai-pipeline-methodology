# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready


### METH-022
- **title**: pre-push hook ↔ wrap 충돌 — 방법론 sync commit 면제
- **mode**: fullstack
- **change-class**: A
- **owner**: AI
- **acceptance criteria**:
  - [ ] pre-push hook 이 직전 commit 메시지가 `chore(methodology): sync` 로 시작하면 wrap --strict 면제 (manifest-check 는 유지)
  - [ ] 또는 wrap 에 `--allow-sync-only` — diff 가 60_tools/ + .methodology-version + .github/workflows/methodology-* + .ai/adapters/ 만이면 통과
  - [ ] 적용 프로젝트에서 sync commit push 가 --no-verify 없이 통과하는지 검증
- **notes**: 2026-05-13 fix 전파 중 발견 (F-005). hooks install 한 적용 프로젝트는 방법론 sync 마다 --no-verify 필요 — 불편 + 우회 습관화 위험.

### METH-021
- **title**: wrap 날짜 경계 완화 — 자정 넘긴 세션 대응
- **mode**: fullstack
- **change-class**: A
- **owner**: AI
- **acceptance criteria**:
  - [ ] `cmd_wrap` 의 `_mtime_today` / ai_observations 파일명 매칭을 *최근 N일*(기본 2일) 허용으로 완화
  - [ ] `--days N` 옵션 추가 (CI 는 엄격하게 1일 가능)
  - [ ] 자정 넘긴 세션에서 ship 이 false-fail 안 하는지 검증
- **notes**: 2026-05-13 dashboard fix 작업 중 발견 (F-004). 세션 resume 으로 자정 넘기면 관찰 파일이 어제 날짜라 wrap 이 못 찾음. 장시간 세션은 흔함.

### METH-020
- **title**: "적용 프로젝트가 CLI fix 즉시 못 받음" 패턴 — MC-002 승급 후보 (N=7+ 패턴 확정)
- **mode**: planning-only
- **change-class**: B (Catalog 활성 승급)
- **owner**: AI → Human 머지
- **acceptance criteria**:
  - [ ] N≥4 목격 확인 (meth-015 F-001, meth-015 F-003, dashboard-port-conflict-fix F-003, multi-dashboard F-005)
  - [ ] `70_meta/catalog/MC-002_*.md` 활성 승급 — "본 저장소 CLI 변경 시 적용 프로젝트는 *다음 sync 전까지* 옛 동작. fix 가 시급하면 본 저장소 절대경로 CLI 직접 호출 (`python3 /path/to/methodology/60_tools/methodology.py <cmd> --path <project>`)"
  - [ ] 솔루션 후보: methodology 명령에 `--use-upstream` 플래그 (본 저장소 CLI 강제 사용) 또는 적용 프로젝트가 본 저장소 CLI 를 symlink
- **notes**: dashboard 포트 충돌 fix 도 같은 패턴 — 3개 적용 프로젝트가 옛 dashboard 코드라 fix 못 받음.

### METH-019
- **title**: MC-001 승급 — talmocom 이미지 add 패턴 (N=2 도달)
- **mode**: planning-only
- **change-class**: B (Catalog 활성 승급 — PR rationale/impact/rollback 필수)
- **owner**: AI → Human 머지
- **acceptance criteria**:
  - [ ] `70_meta/catalog/_pending/MP-003_*.md` 신설 또는 즉시 `70_meta/catalog/MC-001_*.md` 활성 승급 (N≥2 충족)
  - [ ] 솔루션: "방법론 sync 시 *명시 add 패턴* — `git add -u` + 신규 폴더 명시. `git add -A` 회피."
  - [ ] 다음 sync 자동화 후보로 ship/sync 흐름에 반영
- **notes**: 본 마찰 *재발*은 자가발전 루프의 진짜 첫 회전. 70_meta/observations/2026-05-12_meth-015-propagation.md F-003 의 repeat_of: F-004(2026-05-12_v3.1-to-v3.2-migration). 시스템이 학습한 결과를 *코드/문서로* 박는 단계.

### METH-018
- **title**: 사용자 환경에 hooks 설치 + ship 첫 일상 사용 검증
- **mode**: fullstack
- **change-class**: A
- **owner**: Human + AI
- **acceptance criteria**:
  - [ ] 사용자가 본 저장소·icons·gamblescan·talmocom 각각에서 `methodology hooks install` 1회 실행
  - [ ] 다음 작업 종료 시 `methodology ship -m "..."` 사용 — git add/commit/push 직접 호출 없이 통과
  - [ ] sensitive 파일 차단·테스트 실패 차단 동작 1회씩 우연히 시연되면 학습 신호 누적
- **notes**: hooks는 worktree마다 별도 설치 필요 (git의 hooks는 추적되지 않음). 적용 프로젝트는 다음 sync로 ship CLI를 받지만 hooks는 *그 다음 단계*에서 사용자가 1회 실행.

### METH-016
- **title**: SessionEnd hook 활성화 — Claude Code 환경에서 wrap 자동 호출
- **mode**: fullstack
- **change-class**: A
- **owner**: Human (settings.json 사용자 결정 영역)
- **acceptance criteria**:
  - [ ] 사용자 `.claude/settings.json` 또는 `.claude/settings.local.json`에 `SessionEnd` hook 등록
  - [ ] 다음 세션 종료 시 wrap 자동 호출 확인
- **notes**: 가이드 위치 `.ai/adapters/claude.md`. 본 항목은 *사용자 설정 변경*이라 AI가 직접 적용하지 않음.

### METH-013
- **title**: 메타-방법론 격리(`70_meta/`)의 ADR 후속화 — RFC-001 → ADR-002
- **mode**: planning-only
- **change-class**: B (구조 결정)
- **owner**: Human + AI
- **notes**: RFC-001은 status 개선용으로 *재사용됨* (2026-05-12 accepted). 격리 결정의 별도 RFC/ADR은 추후 *변경 발생 시점*에 작성. 본 TODO는 *대기*.

### METH-014
- **title**: 메타-카탈로그 첫 시드 — MP-001/MP-002 완료
- **mode**: planning-only
- **change-class**: A
- **owner**: AI
- **notes**: 2026-05-12 MP-001(status 버전 문자열만 비교) + MP-002(sync init_files 누락) 시드 완료. N≥2 목격 시 active(MC) 승급. 본 TODO는 *지속 모니터링* 상태로 남음.

## InProgress

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-030
- **title**: QA 우선순위 5 — 3 OS 런처 3-tier 구조 탐지 통일
- **notes**: Completed 2026-05-15. `_start/` 의 mac `.app` / linux `.sh` / windows `.bat` 런처 + `build-launchers.py` generator 의 methodology.py 탐지가 60_tools 하드코딩 (mac 만 2-tier). hook 템플릿의 3-tier (60→50→root) 와 통일. shell 스니펫 + Windows batch 동등 로직. generator 재실행으로 3개 출력 파일 재생성. bash -n 검증 통과.

### METH-029
- **title**: 정합성 QA 우선순위 1·2 — dashboard observation 카운트 + commands.json stale path
- **notes**: Completed 2026-05-15. 18개 카테고리 QA 후 4 정합성 이슈 발견. 우선순위 묶어 처리: (1) `generate-dashboard.py` 의 `read_methodology_assets()` 가 `50_resources/ai_observations` 만 카운트 → `_count_observations()` 헬퍼 도입 후 50_resources + 70_meta + v3.2 fallback 모두 합산. source 저장소 dashboard 가 6 → 26 정확 보고. (2) `commands.json:119` "10_guides/03" → "20_guides/03" (v4.0 명명). 남은 마이너 이슈 (commands.json 8 subcmd 미노출 / generate-dashboard layout 헬퍼 9곳 / .app 3-tier) 는 별도 PR.

### METH-028
- **title**: applied-ci source repo skip — `70_meta/` 격리 검사가 source 에서 항상 fail
- **notes**: Completed 2026-05-15. `methodology-applied-ci.yml` 가 source 저장소(`YunJuniverse/ai-pipeline-methodology`) PR 에서 *항상 fail* — source 는 70_meta/ 를 의도적으로 가지고 있는데 워크플로의 누수 검사가 그걸 잡아냄. 처음부터 있던 버그였으나 PR #10 의 layout 탐지 추가로 가시화됨. job-level `if: github.repository != ...` 로 skip. validate / freshness 두 job 모두 적용. source 자체 검증은 source-ci 담당.

### METH-027
- **title**: observation lint 정합성 회복 — validator 정책 현실화 + 옛 파일 마이그레이션
- **notes**: Completed 2026-05-15. source-ci 가 18개 파일에서 실패. 분석 결과 validator 의 "본문 1단락 ≤ 220자" 가 *실제 사용 (multi-section markdown body)* 과 어긋남. 정책 완화 (body 는 markdown 자유 형식, frontmatter required fields 만 강제) + 진짜 위반 5개 (frontmatter 없음 3, 파일명 슬러그 dot 1, 절대 경로 1) 개별 fix. 결과 18→0 실패.

### METH-026
- **title**: Stack 섹션 정리 — bento 자투리·hero row-span·카테고리 반복 문제 해결
- **notes**: Completed 2026-05-15. Claude Design 핸드오프 번들 (stack-cleanup.html) 기반. PR #11 의 12-col bento 5개 문제 (자투리 / hero row-span / 라벨 반복 / 한글 줄바꿈 / 정보 밀도 양극화) 모두 해결. 카테고리 그룹 헤더 + auto-fill grid + hero 시각 강조 (좌측 액센트 + ★ PRIMARY 배지) + role uppercase 제거 + 모든 카드 reason 3-line clamp. `size: hero|mid|sm` 의미 전환 (레이아웃 크기 → 강조 등급), stack.json 데이터 무수정.

### METH-025
- **title**: Overview 탭 *기술 스택* bento 카드
- **notes**: Completed 2026-05-15. 데이터: `60_tools/stack.json` (23 항목 × 5 카테고리, 카테고리당 hero 1장 + mid/sm). 비대칭 CSS grid (12-col, hero=6colx2row / mid=4col / sm=3col). 카드 클릭 → side-sheet 모달로 선택 이유 + docs URL 표시. 시각 언어는 현재 대시보드 OKLCH 톤 유지 (Apple bento 컨셉만 차용). MANIFEST shared 추가 → 적용 프로젝트 자동 전파.

### METH-024
- **title**: 방법론 정합성 3 fix 묶음 — 구조 탐지 / sync worktree / observe CLI 강제
- **notes**: Completed 2026-05-15. tshome 사고로 발견된 3개 root cause 를 한 PR 로 묶음. (1) `methodology_layout(target)` 헬퍼 — v3.2/v4.0 구조 탐지 중앙화. 그동안 hook·.app·CI·wrap 에서 fallback 4번 누락한 root cause. (2) `sync --include-worktrees` — sibling git worktree 감지. 마이그레이션 시 기본 True. (3) `observe` CLI 강제 + wrap 선행 frontmatter 검증 — `cat > .md` 직접 작성 차단. CLAUDE/AGENTS managed 에 CLI 사용 권고 명문화. CI 워크플로도 구조 자동 탐지 (v3.2 워크트리에서 60_tools 못 찾던 버그 차단).

### METH-023
- **title**: `wrap` 콘텐츠 해시 검증 — 동일 날짜 다중 ship 오탐 차단
- **notes**: Completed 2026-05-15. mtime-only → sha256 콘텐츠 해시. `.ai/wrap-state.json` baseline + 부트스트랩 + ship commit 직전 wrap-state 동기화 (push 후 갱신은 clone/pull 후 wrap 오탐 유발 → commit 직전으로 이동). pre-push hook 의 wrap 재실행은 `METHODOLOGY_SHIP_IN_PROGRESS` env 로 skip (commit 직전 동기화로 인한 sha 일치 chicken-and-egg 회피). `touch` 만으로는 통과 못 함. 원인: S-007/S-008/S-009 동일 날짜 ship 시 옛 wrap 이 옛 콘텐츠를 *오늘 mtime* 만으로 통과시켜 다음 세션이 누락 작업을 발견 — root cause 차단.

### METH-015
- **title**: 적용 프로젝트 3개에 applied-ci/auto-merge 워크플로 + 신규 CLI 자동 전파
- **notes**: Completed 2026-05-12. icons/gamblescan/talmocom 3개 모두 v3.2 본 저장소 commit 83a48e0 동기화. ship/hooks/dashboard/wrap CLI + dev-server API + workflow 2종 + managed 규칙 갱신 자동 전파. 격리 3/3 ✅. 자가발전 루프 첫 진짜 회전 (F-003 repeat_of) → METH-019 트리거.

### METH-012
- **title**: 인계 시뮬레이션과 온보딩 검증
- **notes**: Completed 2026-05-08. Added `40_dev/snapshots/transfer-drill-2026-05-08.md`.

### METH-011
- **title**: Dashboard L0~L4 패널 통합
- **notes**: Completed 2026-05-08. Dashboard data now includes L0 adapters, observations, Catalog counts, Skeleton counts, and Thinktank reports.

<!-- Archived: METH-001 ~ METH-010 (2026-05-07 ~ 2026-05-08). See git history. -->

