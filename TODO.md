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

### METH-086 · SPRINTS 완전 붕괴(2층화) + TODO WIP 캡 — 웹리서치
- **notes**: 2026-07-09. Class A. PR 대기. 리서치 2건: TODO=베스트프랙티스 부합(무변경 핵심), SPRINTS=잉여 중간층+명칭 모순(기간 고정 안 함·velocity가 METH-076 flow와 충돌). **3층→2층**(페이즈→TODO): cadence=flow 메트릭, 그룹핑=TODO `milestone:` 태그, 게이트=페이즈. guide 02(§3 삭제·재번호)·guide 18(§14.5·§10.2)·_CATALOG·TODO 템플릿(sprint→milestone)·graph.json(sprints 노드/엣지)·대시보드(Timeline탭·gantt·sprint모달 제거, hero→phase, WIP 타일)·mention 스윕·SPRINTS.md 2개 삭제·**wrap WIP≤3 린트**. 대시보드 렌더+compile 통과. `.claude/skills` 레거시 Open Issue. 내부 정합성+리서치. branch-first 준수.

### METH-085 · friction 캡처 규칙 추가 — catalog→skeleton 학습 루프 가동
- **notes**: 2026-07-09. Class A. PR #74 머지. catalog 저활용의 진짜 원인=재료 미수집(72 로그 중 friction 2건). ① CLAUDE/AGENTS §2 ④ observe 스텝에 "비자명한 문제·재발·막힘 시 `--friction "where|cost_minutes|resolution|repeat_of"` 남겨라" 규칙(강제 아님·노이즈 방지, 194줄 유지). ② catalog `_README.md` §3 "원료 수집(파이프라인 진입점)" 신설(observe→thinktank→pending→active). ③ dogfood — 세션 실제 마찰(HANDOFF Working-on 부분교체 시 잔존, 2회)을 --friction 첫 캡처 + thinktank 재집계 확인. 내부 정합성(리서치 없음). branch-first 준수.

### METH-084 · skeleton 서브시스템 활성화 + 죽은 필드 정리
- **notes**: 2026-07-09. Class A. PR #73 머지. 사용자 "skeleton 필요한가?" 점검 → **판정: 유지**(AI-LOG와 달리 catalog→skeleton→주입 환류 루프는 고유·자기완결·실체 있음; 프론트/아이콘 포트폴리오가 사용처). 문제는 중복 아닌 저활용 → **활성화**: ① end-to-end 검증(init→build→apply, frontend-design-tokens 9파일+lock 정상 주입) ② `bakes-in.json.last_built` = init 때 null로만 쓰이고 아무도 갱신·참조 안 하는 죽은 필드(실제 시각=lock `built_at` SSOT, AI-LOG 유령 필드와 동종) → CLI init·양 bakes-in·_README에서 제거 + _README 명문화. 양 도메인 lock 재빌드. 후속: 레슨→catalog 엔트리 축적(현재 C-001 1개). 내부 정합성(리서치 없음). branch-first 준수.

### METH-083 · 메타 파일(CLAUDE/AGENTS/HANDOFF/AI-LOG) 최신화 — 웹리서치 기반
- **notes**: 2026-07-09. Class A. PR #72 머지. 사용자 지시("존재의의·정합성·군더더기 파악 + 웹리서치 최신화"). 리서치 2건(AGENTS.md 오픈표준[Linux Foundation·~24툴·60k레포]·CLAUDE 관계 / 핸드오프·협업로그 2025-26). 판정: 파일군 대체로 베스트프랙티스 부합(HANDOFF=교과서, checkpoint=pre-compaction flush 정석 → 무변경). 조치(사용자 승인 3안): ① CLAUDE/AGENTS **217→194줄**(Anthropic <200 권장; §2 절차→지침06/07/08 포인터 압축, load-bearing 전부 유지) ② **CLI 미러 유지** ③ **AI-LOG 헌법 제거**(§2·§4 — 유령 규칙+git/PR·ADR·HANDOFF 삼중 중복+observe가 이미 협업로그). 미러 패리티 정상. 내부 정합성+리서치. branch-first 준수.











> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
