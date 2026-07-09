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

### METH-092 · guide 03(AI 관찰 로그) 심화 — CLI 정본화 + 학습루프
- **notes**: 2026-07-09. Class B. PR 대기. 메타/dev 지침 심화 배치 1번(내부 정합). guide 03 §5 수동 cat 요청→`observe` CLI 정본화(cat 금지=wrap fail·헌법 §2④)+`--friction` positional 형식·캡처 규칙. §6 학습 파이프라인(observe→thinktank→pending→catalog→skeleton)+"마찰 안 남기면 굶는다"+catalog/skeleton _README 교차링크. v2 이력. 다음: 093=06·07·08(리서치 반영), 094=05·09+02/19/20. branch-first 준수.

### METH-091 · legacy 경로 sweep — 라이브 문서 3건 수정
- **notes**: 2026-07-09. Class A. PR #80 머지. 라이브 문서 pre-v4 경로 점검(90_archive·마이그레이션·시점기록 제외). 실제 stale 3건 수정: `10_foundation/{KICKOFF_PROMPT,DIAGRAM,HOW_TO_APPLY}.md`의 `docs/snapshots/`→`40_dev/snapshots/`. 나머지 `docs/` 참조는 정당(guide 19 gamblescan 인용=실제 위치·api-contract=예시). 부수 발견: v3.2 backward-compat 코드 폴백 dead(7 repo 전부 v4.0)이나 별건 Open Issue. docs sweep Open Issue Closed. branch-first 준수.

### METH-090 · .claude/skills 레거시 3종 삭제
- **notes**: 2026-07-09. Class A. PR #79 머지. ai-planning·ai-relay·vibe-coding(2026-03, 구모델: 스프린트·기획서6종/개발명세8종·`docs/` dead 경로) 삭제. 기능은 guide 01(오케)/08(서브에이전트)/19(클린코드)+prompts가 정본이라 stale 중복, 호출 시 v4와 반대로 안내. 살릴 고유 콘텐츠 없음(릴레이 handoff≈checkpoint, 4-레이어=guide19). 다운스트림 sync 대상 아님(로컬). 잔여 참조는 90_archive 히스토리뿐 보존. 세션 관통 SSOT/anti-중복. branch-first 준수.

### METH-089 · ai-icons·icons-invest guide 번호 충돌 remediation
- **notes**: 2026-07-09. Class A. PR #78 머지. guide 02 §7 예약범위(상류 00-89/커스텀 90-99) 준수 — 레거시 커스텀 guide 90+ 이관. ai-icons: 04→90·05_회의록→91·21_산출물채널분리→92_LOCAL(상류05 정본, 149줄 차이=로컬 발전분 보존+플래그). icons-invest: 04→90·05→91. doc_id guide-9N·기능적 참조(meetings/_README·HANDOFF) 갱신, 이력 보존. git mv·--no-verify push·origin/main 검증(충돌 해소·데이터 손실 0). 잔여: ai-icons 92↔상류05 환류(각 repo). branch-first 준수.














> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
