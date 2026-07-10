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

### METH-101 · 부팅 강제 + 라이브 파일 비대화 방지
- **notes**: 2026-07-10. Class A(7 repo 전파). PR base=main 대기. ai-icons 새 세션이 부팅 건너뛰고 기존 프로세스 모른 채 시작(오답)한 사고의 상류 진단·수정. 진단: 기록 유실 아님. 원인 ① 부팅 의무가 강제 없는 서술뿐 ② 라이브 파일 비대화 무통제(wrap이 사이즈 안 봄→ai-icons HANDOFF 81KB 등). 수정(사용자 "둘 다"): (A) `methodology.py boot` 신설(브리프·HANDOFF·checkpoint·사이즈·dashboard 한 번에) (B) wrap 사이즈 린트(`live_file_size_warnings` 공용, HANDOFF>150·checkpoint>200·Done>6 경고). CLAUDE/AGENTS managed block: 부팅 의무를 boot 실행 정본화·"IR 질문에 바로 뛰어들지 말 것"·wrap 비대화 경고 명기. py_compile·boot 실행·린트 발화 검증. branch-first 준수.

### METH-100 · v3.2 backward-compat 코드 정리
- **notes**: 2026-07-10. Class A. PR base=main 대기(096~099 포함). 현존 repo 7곳 전부 v4.0이라 dead였던 v3.2 폴백 제거. methodology.py: `_LAYOUT_V32`+`methodology_layout()` 삭제→v4.0 고정, `_observation_dir`/`_wrap_obs_dirs` 50_resources/70_meta 하드코딩. generate-dashboard.py: `_LAYOUT_V32`+`dash_layout`+`resolve_methodology_py` 탐지 삭제→v4.0 고정, `_count_observations`·`assemble`의 docs//40_resources/60_meta/legacy-root 폴백 삭제(50_resources/templates 유효 폴백만 유지), 푸터 v3.2→v4.0·stale 도크스트링. **보존**: migrations/v3.2_to_v4.0.py·런처/훅 부트스트랩 3-tier(범위 밖·synced 리스크). 검증: py_compile·dashboard 재생성(obs 107 양쪽 dir)·wrap. branch-first 준수.

### METH-099 · methodology-graph.json 노드 보강 + 096~098 stranded 복구
- **notes**: 2026-07-09. Class A. PR base=main 대기. 대시보드 관계 그래프 노드 불완전(METH-079 Open Issue) 종결. 노드 29→42: guide 10개(02·03·05·06·07·08·09·19·20·21; 04 미존재 제외) + 학습루프(observations·catalog·skeletons) + checkpoint, stale ai-log 제거. 엣지 39→53(g00 parent-of 메타룰·g18→g21→g19/g20·observe→catalog→skeleton). tier6·learning kind·v3.2. dashboard 렌더 검증(nodes=42)·JSON 정합 0오류. **부수**: 스택-PR 재타깃 함정으로 #85/#86/#87이 중간 브랜치 머지→096/097/098 main 미반영이던 것을 이 단일 PR(base=main)로 복구. branch-first 준수.

### METH-098 · agency/ops 템플릿 배치 4 — glossary + 배치 완결
- **notes**: 2026-07-09. Class A. PR 대기. glossary.md(SI 단계별 용어규약집) 심화. 핵심=**SSOT 경계 명시**(glossary=계약·산출물 표면 라벨 통일 / context-glossary=도메인 개념 canon·코드까지, 중복 금지·링크만). 표준용어 표에 예시(용례)·상태(Approved/Deprecated) 열, 관리자=분쟁 해결권자, 폐기어 추적성. **배치 완결**: agency/ops 12종(095 QA 3·096 수주 5·097 ops 3·098 glossary 1) 전부 lean 폼 필드 보강 + 지침 참조(SSOT)로 완료. branch-first 준수.

### METH-097 · agency/ops 템플릿 배치 3 — ops 3종 (SRE·ITIL4·OTel·DORA)
- **notes**: 2026-07-09. Class A. PR 대기. ops 클러스터 3종. guide 12(§6.15~6.22)가 이미 성숙 → 템플릿은 이론 재설명 없이 **값만 채우는 lean 폼 + 지침 참조**(SSOT). operation-spec(runbook): §0 신뢰성 계약(SLI/SLO/SLA·error-budget 소진액션+집행자·의존성·SEV1-4·롤백 RTO/RPO·break-glass·유지보수창·AI-Ops)+서비스오너/on-call. post-launch-monitoring: A 골든시그널(latency/traffic/errors/saturation+임계치·burn-rate>14.4/1h 페이지·비즈니스·AI·trace_id 상관) + B 결함추적 + 리뷰 케이던스. work-request-ticket: 티켓유형(request/incident/change)·우선순위=영향×긴급 P1-P4·완료기준 DoD·변경관리(변경유형 Std/Normal/Emergency+Change Class A/B/C+롤백)·위험변경만 승인게이트·상태 워크플로. 남음: 098 glossary. branch-first 준수.


















> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
