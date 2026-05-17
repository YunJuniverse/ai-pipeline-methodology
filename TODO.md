# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready


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
- **notes**: hooks는 worktree마다 별도 설치 필요 (git의 hooks는 추적되지 않음). 적용 프로젝트는 다음 sync로 ship CLI를 받지만 hooks는 *그 다음 단계*에서 사용자가 1회 실행. **AI측 완료** (METH-022 로 sync commit 자동 면제까지 구현됨) — Human 1회 실행만 남음: 각 프로젝트 루트에서 `python3 60_tools/methodology.py hooks install`.

### METH-016
- **title**: SessionEnd hook 활성화 — Claude Code 환경에서 wrap 자동 호출
- **mode**: fullstack
- **change-class**: A
- **owner**: Human (settings.json 사용자 결정 영역)
- **acceptance criteria**:
  - [ ] 사용자 `.claude/settings.json` 또는 `.claude/settings.local.json`에 `SessionEnd` hook 등록
  - [ ] 다음 세션 종료 시 wrap 자동 호출 확인
- **notes**: 가이드 위치 `.ai/adapters/claude.md` §SessionEnd hook (스니펫 준비 완료). 본 항목은 *사용자 settings.json 변경*이라 AI가 직접 적용 불가 — Human 이 `.claude/settings.json` 에 SessionEnd hook 블록 복사만 하면 됨. AI측 준비 완료.

### METH-013
- **title**: 메타-방법론 격리(`70_meta/`)의 ADR 후속화 — RFC-001 → ADR-002
- **mode**: planning-only
- **change-class**: B (구조 결정)
- **owner**: Human + AI
- **notes**: RFC-001은 status 개선용으로 *재사용됨* (2026-05-12 accepted). 격리 결정의 별도 RFC/ADR은 추후 *변경 발생 시점*에 작성. 본 TODO는 *대기*.


## InProgress

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

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

