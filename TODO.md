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

### METH-095 · agency/ops 템플릿 배치 1 — QA 3종 (ISO 29119-3·ISTQB)
- **notes**: 2026-07-09. Class A. PR 대기. agency/ops 12종 심화(전부 웹리서치) 배치. 리서치 3건(QA·수주·ops). QA 클러스터: qa-acceptance-plan(진입기준·검수유형·정량 exit·심각도≠우선순위·테스트데이터·RTM), qa-test-scenario(케이스ID·요구사항·사전조건·실제결과·부정/경계 태그·GWT 옵션), qa-acceptance-signoff(버전 pin·종료기준 충족·개방결함+웨이버·조건부 기한·증거·하자보수). 3종=RTM 폐루프. lean 폼. 남음: 096 수주 5종·097 ops 3종·098 glossary. branch-first 준수.

### METH-094 · guide 20 DTCG 상호운용 + 메타/dev 배치 완결
- **notes**: 2026-07-09. Class A. PR #83 머지. 배치 3번(마무리). guide 20에 실제 gap(W3C DTCG 미언급) → §8 상호운용 표준 신설(DTCG JSON·Style Dictionary·Tokens Studio·도입 트리거·4기둥↔DTCG 매핑·"필요할 때만"·v3). **05·09·02·19는 검토=성숙, 콘텐츠 추가 없음**(bloat 회피). 배치 총괄: 심화분 03·06·07·08·20 완료, 나머지 5개 적정 확인. branch-first 준수.

### METH-093 · guide 06·07·08 심화 — 에이전트 메카닉 웹리서치
- **notes**: 2026-07-09. Class B. PR 대기(#81 위 스택). 메타/dev 배치 2번, 리서치 3건. 얇던 3개에 §SOTA 보강+v2: 06=두층 임계치·auto-survive·safest-first·post검증·subagent isolation / 07=이중예산(SDK 무제한 경고)·6 circuit breaker·ground-truth·ask→escalate·비가역=Class C·stop report·재선언 전 checkpoint / 08=fan-out vs single-writer(Cognition)·sizing·model/effort·concurrency cap·completeness critic·artifact memory·Workflow escape. 남음: 094=05·09+02/19/20. branch-first 준수.

### METH-092 · guide 03(AI 관찰 로그) 심화 — CLI 정본화 + 학습루프
- **notes**: 2026-07-09. Class B. PR #81 대기. 메타/dev 지침 심화 배치 1번(내부 정합). guide 03 §5 수동 cat 요청→`observe` CLI 정본화(cat 금지=wrap fail·헌법 §2④)+`--friction` positional 형식·캡처 규칙. §6 학습 파이프라인(observe→thinktank→pending→catalog→skeleton)+"마찰 안 남기면 굶는다"+catalog/skeleton _README 교차링크. v2 이력. 다음: 093=06·07·08(리서치 반영), 094=05·09+02/19/20. branch-first 준수.

















> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
