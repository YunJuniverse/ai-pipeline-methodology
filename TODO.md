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

### METH-104 · SOP 트리거에 "인식 신호" 항목 추가
- **notes**: 2026-07-10. Class A(7 repo). PR base=main 대기. 반복작업 매칭이 문자열 아닌 LLM 의미추론이라, SOP 트리거에 "어떤 요청/말이 이 작업을 의미하는가"(인식 신호) 앵커를 명시해 매칭 신뢰도↑. `SOP_template.md` 트리거=인식신호+주기/이벤트로 분리, `_README §standing` 반영. branch-first.

### METH-103 · 상시 SOP 쓰기 트리거 규칙
- **notes**: 2026-07-10. Class A(7 repo). PR base=main 대기. 102가 standing SOP 읽기(boot 노출)만 완비하고 쓰기 반사신경이 없던 구멍을 메움. CLAUDE/AGENTS managed block §2에 "반복 작업 기억 (요청 시)" 규칙: "기억해줘/반복작업이야" → `standing/SOP_<topic>.md` 박제(SOP_template 형식)+절차 변경 시 갱신 제안+작업SOP(repo) vs 개인메모리(도구) 구분. _README §5 반영. managed sync 확인. branch-first.

### METH-102 · 라이브파일 경계 재분리(b) + 상시 브리프
- **notes**: 2026-07-10. Class A(7 repo). PR base=main 대기(#90 boot 포함). (b) HANDOFF=상태보드/checkpoint=서사 경계 못박아 중복 제거(checkpoint "미해결 결정사항"→HANDOFF Open Issues 참조; 템플릿 2개+CLAUDE §4 checkpoint행 신설+§2 규칙). `00_briefs/standing/`(반복작업 SOP·아카이브 안 됨)+SOP_template+boot ★노출+_README+MANIFEST(shared/init). 검증: py_compile·boot(standing/current 분리·실 SOP ★)·manifest·managed sync. branch-first.

### METH-101 · 부팅 강제 + 라이브 파일 비대화 방지
- **notes**: 2026-07-10. Class A(7 repo). PR #90 OPEN(base=main). `methodology.py boot` 신설(브리프·HANDOFF·checkpoint·사이즈·dashboard 한 번에) + wrap 사이즈 린트(`live_file_size_warnings`, HANDOFF>150·checkpoint>200·Done>6 경고). CLAUDE/AGENTS 부팅 의무 boot 정본화. ai-icons 부팅 스킵 사고 상류 대응. branch-first.

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
