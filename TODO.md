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

### METH-099 · methodology-graph.json 노드 보강 + 096~098 stranded 복구
- **notes**: 2026-07-09. Class A. PR base=main 대기. 대시보드 관계 그래프 노드 불완전(METH-079 Open Issue) 종결. 노드 29→42: guide 10개(02·03·05·06·07·08·09·19·20·21; 04 미존재 제외) + 학습루프(observations·catalog·skeletons) + checkpoint, stale ai-log 제거. 엣지 39→53(g00 parent-of 메타룰·g18→g21→g19/g20·observe→catalog→skeleton). tier6·learning kind·v3.2. dashboard 렌더 검증(nodes=42)·JSON 정합 0오류. **부수**: 스택-PR 재타깃 함정으로 #85/#86/#87이 중간 브랜치 머지→096/097/098 main 미반영이던 것을 이 단일 PR(base=main)로 복구. branch-first 준수.

### METH-098 · agency/ops 템플릿 배치 4 — glossary + 배치 완결
- **notes**: 2026-07-09. Class A. PR 대기. glossary.md(SI 단계별 용어규약집) 심화. 핵심=**SSOT 경계 명시**(glossary=계약·산출물 표면 라벨 통일 / context-glossary=도메인 개념 canon·코드까지, 중복 금지·링크만). 표준용어 표에 예시(용례)·상태(Approved/Deprecated) 열, 관리자=분쟁 해결권자, 폐기어 추적성. **배치 완결**: agency/ops 12종(095 QA 3·096 수주 5·097 ops 3·098 glossary 1) 전부 lean 폼 필드 보강 + 지침 참조(SSOT)로 완료. branch-first 준수.

### METH-097 · agency/ops 템플릿 배치 3 — ops 3종 (SRE·ITIL4·OTel·DORA)
- **notes**: 2026-07-09. Class A. PR 대기. ops 클러스터 3종. guide 12(§6.15~6.22)가 이미 성숙 → 템플릿은 이론 재설명 없이 **값만 채우는 lean 폼 + 지침 참조**(SSOT). operation-spec(runbook): §0 신뢰성 계약(SLI/SLO/SLA·error-budget 소진액션+집행자·의존성·SEV1-4·롤백 RTO/RPO·break-glass·유지보수창·AI-Ops)+서비스오너/on-call. post-launch-monitoring: A 골든시그널(latency/traffic/errors/saturation+임계치·burn-rate>14.4/1h 페이지·비즈니스·AI·trace_id 상관) + B 결함추적 + 리뷰 케이던스. work-request-ticket: 티켓유형(request/incident/change)·우선순위=영향×긴급 P1-P4·완료기준 DoD·변경관리(변경유형 Std/Normal/Emergency+Change Class A/B/C+롤백)·위험변경만 승인게이트·상태 워크플로. 남음: 098 glossary. branch-first 준수.

### METH-096 · agency/ops 템플릿 배치 2 — 수주 5종 (Shipley·APMP·PMBOK·SOW)
- **notes**: 2026-07-09. Class A. PR 대기. 수주 클러스터 5종 lean 폼 필드 보강. proposal-go-nogo(결정소유자+게이트일자·경쟁포지션 axis·cost-to-pursue·kill 규칙[1축 미달=포기]·Shipley 5요인). research-collection(시장 3버킷 + 프로젝트셋업 4버킷[사업목표/성공KPI·BANT·컴플라이언스·기존자산]+출처열). profitability-sheet(과금모델 enum·리스크 컨틴전시[근거=과거초과율]·gross/net 분리·손익분기·변경요청 별도). execution-plan(가정·범위제외·인수기준+승인권자·리스크레지스터·커뮤니케이션·인계 + §5 W1-W4→Phase/Milestone 재프레임). wbs(100%룰·PM/QA포함·work package 롤업·비고=WBS dictionary). 남음: 097 ops 3종·098 glossary. branch-first 준수.


















> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
