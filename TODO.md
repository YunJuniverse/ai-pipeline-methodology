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

### METH-090 · .claude/skills 레거시 3종 삭제
- **notes**: 2026-07-09. Class A. PR 대기. ai-planning·ai-relay·vibe-coding(2026-03, 구모델: 스프린트·기획서6종/개발명세8종·`docs/` dead 경로) 삭제. 기능은 guide 01(오케)/08(서브에이전트)/19(클린코드)+prompts가 정본이라 stale 중복, 호출 시 v4와 반대로 안내. 살릴 고유 콘텐츠 없음(릴레이 handoff≈checkpoint, 4-레이어=guide19). 다운스트림 sync 대상 아님(로컬). 잔여 참조는 90_archive 히스토리뿐 보존. 세션 관통 SSOT/anti-중복. branch-first 준수.

### METH-089 · ai-icons·icons-invest guide 번호 충돌 remediation
- **notes**: 2026-07-09. Class A. PR #78 머지. guide 02 §7 예약범위(상류 00-89/커스텀 90-99) 준수 — 레거시 커스텀 guide 90+ 이관. ai-icons: 04→90·05_회의록→91·21_산출물채널분리→92_LOCAL(상류05 정본, 149줄 차이=로컬 발전분 보존+플래그). icons-invest: 04→90·05→91. doc_id guide-9N·기능적 참조(meetings/_README·HANDOFF) 갱신, 이력 보존. git mv·--no-verify push·origin/main 검증(충돌 해소·데이터 손실 0). 잔여: ai-icons 92↔상류05 환류(각 repo). branch-first 준수.

### METH-088 · 다운스트림 sync 홀드 3곳 완료 — 관리 6곳 전부 086
- **notes**: 2026-07-09. Class A. PR #77 머지. 사용자 dirty 해소 후 ai-icons·cafe24-renewal·icons-invest 를 086까지 sync. (feature면)main 전환→sync --apply→stale SPRINTS.md rm→--no-verify commit→push→복귀. origin/main 검증: SPRINTS 제거·WIP 린트·대시보드 정리 반영, 커스텀 guide 전부 보존(데이터 손실 0). METH-087(clean 3곳)+이번 3곳=관리 6곳 전부 완료. 잔여: ai-icons(05×2·21×2)·icons-invest(05×2) guide 번호 충돌은 sync와 직교(각 repo 세션 remediation, Open Issue). branch-first 준수.

### METH-087 · 누적 다운스트림 sync (073~086) — clean 3곳
- **notes**: 2026-07-09. Class A. PR #76 머지. clean+관리 다운스트림 gamblescan·icons·tshome에 상류 누적분(072→086) 반영. repo당 main 전환→`sync --apply`→stale SPRINTS.md 수동 rm(sync는 상류 삭제분 auto-prune 안 함)→--no-verify commit→push→원브랜치 복귀. origin/main 검증 통과(SPRINTS 제거·WIP 린트·대시보드 정리, 고유 파일 보존). 홀드 dirty 3곳(ai-icons·cafe24·icons-invest)은 clean 후. ver 없는 4곳 제외. branch-first 준수.












> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
