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

### METH-088 · 다운스트림 sync 홀드 3곳 완료 — 관리 6곳 전부 086
- **notes**: 2026-07-09. Class A. PR 대기. 사용자 dirty 해소 후 ai-icons·cafe24-renewal·icons-invest 를 086까지 sync. (feature면)main 전환→sync --apply→stale SPRINTS.md rm→--no-verify commit→push→복귀. origin/main 검증: SPRINTS 제거·WIP 린트·대시보드 정리 반영, 커스텀 guide 전부 보존(데이터 손실 0). METH-087(clean 3곳)+이번 3곳=관리 6곳 전부 완료. 잔여: ai-icons(05×2·21×2)·icons-invest(05×2) guide 번호 충돌은 sync와 직교(각 repo 세션 remediation, Open Issue). branch-first 준수.

### METH-087 · 누적 다운스트림 sync (073~086) — clean 3곳
- **notes**: 2026-07-09. Class A. PR #76 머지. clean+관리 다운스트림 gamblescan·icons·tshome에 상류 누적분(072→086) 반영. repo당 main 전환→`sync --apply`→stale SPRINTS.md 수동 rm(sync는 상류 삭제분 auto-prune 안 함)→--no-verify commit→push→원브랜치 복귀. origin/main 검증 통과(SPRINTS 제거·WIP 린트·대시보드 정리, 고유 파일 보존). 홀드 dirty 3곳(ai-icons·cafe24·icons-invest)은 clean 후. ver 없는 4곳 제외. branch-first 준수.

### METH-086 · SPRINTS 완전 붕괴(2층화) + TODO WIP 캡 — 웹리서치
- **notes**: 2026-07-09. Class A. PR #75 머지. 리서치 2건: TODO=베스트프랙티스 부합(무변경 핵심), SPRINTS=잉여 중간층+명칭 모순(기간 고정 안 함·velocity가 METH-076 flow와 충돌). **3층→2층**(페이즈→TODO): cadence=flow 메트릭, 그룹핑=TODO `milestone:` 태그, 게이트=페이즈. guide 02(§3 삭제·재번호)·guide 18(§14.5·§10.2)·_CATALOG·TODO 템플릿(sprint→milestone)·graph.json(sprints 노드/엣지)·대시보드(Timeline탭·gantt·sprint모달 제거, hero→phase, WIP 타일)·mention 스윕·SPRINTS.md 2개 삭제·**wrap WIP≤3 린트**. 대시보드 렌더+compile 통과. `.claude/skills` 레거시 Open Issue. 내부 정합성+리서치. branch-first 준수.

### METH-085 · friction 캡처 규칙 추가 — catalog→skeleton 학습 루프 가동
- **notes**: 2026-07-09. Class A. PR #74 머지. catalog 저활용의 진짜 원인=재료 미수집(72 로그 중 friction 2건). ① CLAUDE/AGENTS §2 ④ observe 스텝에 "비자명한 문제·재발·막힘 시 `--friction "where|cost_minutes|resolution|repeat_of"` 남겨라" 규칙(강제 아님·노이즈 방지, 194줄 유지). ② catalog `_README.md` §3 "원료 수집(파이프라인 진입점)" 신설(observe→thinktank→pending→active). ③ dogfood — 세션 실제 마찰(HANDOFF Working-on 부분교체 시 잔존, 2회)을 --friction 첫 캡처 + thinktank 재집계 확인. 내부 정합성(리서치 없음). branch-first 준수.











> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
