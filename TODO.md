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

### METH-103 · 상시 SOP 쓰기 트리거 규칙
- **notes**: 2026-07-10. Class A(7 repo). PR base=main 대기. 102가 standing SOP 읽기(boot 노출)만 완비하고 쓰기 반사신경이 없던 구멍을 메움. CLAUDE/AGENTS managed block §2에 "반복 작업 기억 (요청 시)" 규칙: "기억해줘/반복작업이야" → `standing/SOP_<topic>.md` 박제(SOP_template 형식)+절차 변경 시 갱신 제안+작업SOP(repo) vs 개인메모리(도구) 구분. _README §5 반영. managed sync 확인. branch-first.

### METH-102 · 라이브파일 경계 재분리(b) + 상시 브리프
- **notes**: 2026-07-10. Class A(7 repo). PR base=main 대기(#90 boot 포함). (b) HANDOFF=상태보드/checkpoint=서사 경계 못박아 중복 제거(checkpoint "미해결 결정사항"→HANDOFF Open Issues 참조; 템플릿 2개+CLAUDE §4 checkpoint행 신설+§2 규칙). `00_briefs/standing/`(반복작업 SOP·아카이브 안 됨)+SOP_template+boot ★노출+_README+MANIFEST(shared/init). 검증: py_compile·boot(standing/current 분리·실 SOP ★)·manifest·managed sync. branch-first.

### METH-101 · 부팅 강제 + 라이브 파일 비대화 방지
- **notes**: 2026-07-10. Class A(7 repo). PR #90 OPEN(base=main). `methodology.py boot` 신설(브리프·HANDOFF·checkpoint·사이즈·dashboard 한 번에) + wrap 사이즈 린트(`live_file_size_warnings`, HANDOFF>150·checkpoint>200·Done>6 경고). CLAUDE/AGENTS 부팅 의무 boot 정본화. ai-icons 부팅 스킵 사고 상류 대응. branch-first.

### METH-100 · v3.2 backward-compat 코드 정리
- **notes**: 2026-07-10. Class A. PR base=main 대기(096~099 포함). 현존 repo 7곳 전부 v4.0이라 dead였던 v3.2 폴백 제거. methodology.py: `_LAYOUT_V32`+`methodology_layout()` 삭제→v4.0 고정, `_observation_dir`/`_wrap_obs_dirs` 50_resources/70_meta 하드코딩. generate-dashboard.py: `_LAYOUT_V32`+`dash_layout`+`resolve_methodology_py` 탐지 삭제→v4.0 고정, `_count_observations`·`assemble`의 docs//40_resources/60_meta/legacy-root 폴백 삭제(50_resources/templates 유효 폴백만 유지), 푸터 v3.2→v4.0·stale 도크스트링. **보존**: migrations/v3.2_to_v4.0.py·런처/훅 부트스트랩 3-tier(범위 밖·synced 리스크). 검증: py_compile·dashboard 재생성(obs 107 양쪽 dir)·wrap. branch-first 준수.


> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
