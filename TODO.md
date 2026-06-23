# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

### METH-044
- **title**: 모드별 템플릿 선택 체계 — `_CATALOG.md` + CLAUDE.md Mode 확장 (작업 용도에 따라 필요한 템플릿만)
- **gate**: ⚠️ **PR #32 머지 후 착수**. 카탈로그가 deliverable 템플릿 25종 전체를 참조하므로 #32(041/042/043 포함)까지 머지된 clean main에서 작성. 이번 세션 역주입 작업들의 capstone.
- **design (확정)**:
  - **6개 모드 → 세트**: `planning`(기획전용: prd·requirements-spec·ia-spec·service-policy·user-story·kpi-tree·context-glossary·microcopy) · `dev`(개발전용: architecture·data-model·user-flow·wireframe-spec·functional-spec) · `fullstack`(planning∪dev+wbs) · `agency`(외주 SI 라이프사이클: proposal-go-nogo·research-collection-checklist·profitability-sheet·execution-plan·wbs·qa 3종·operation-spec·post-launch-monitoring·work-request-ticket·glossary + 기획/개발) · `lean`(경량: prd·architecture·context-glossary·ADR) · `ops`(운영: operation-spec·post-launch-monitoring·work-request-ticket·qa 3종).
  - **메커니즘(비파괴적, flat 경로 유지)**: ① `50_resources/templates/_CATALOG.md` — 25종 한 줄 카탈로그(카테고리별) + 모드×템플릿 매트릭스 + 모드별 권장 세트. ② CLAUDE.md `Mode` 필드 확장 `[planning/dev/fullstack/agency/lean/ops]`(현재 fullstack/planning-only). ③ 지침 00 "작업 모드 → 카탈로그에서 필요한 템플릿만 로드" 원칙 1줄. ④ (선택·후속) CLI `methodology templates --mode <mode>` — methodology.py 작업이라 별도.
  - **폴더 재구성 금지**: planning/·dev/ 하위 이동 시 METH-039~043 참조 flat 경로 전부 깨짐 → 카탈로그(매핑 문서)로 해결.
- **acceptance**: `_CATALOG.md`에 25종 전부 분류·6모드 매트릭스 완비 + CLAUDE.md Mode 확장 + 지침 00 원칙 1줄. Class A. 머지 후 다운스트림 sync 합산.

## Ready

## InProgress

> ⚠️ **PR #31은 METH-040까지만(commit `450045a`) 머지됨 — METH-041/042는 누락**. gamblescan 브랜치(`18d3784`)에 살아 있던 041/042를 **PR #32 브랜치로 통합** → 이제 PR #32가 **041+042+043**을 한 번에 운반. PR #32 머지 시 전부 main 안착.

### METH-043
- **title**: 적용 프로젝트(icons-ip) 경량 파이프라인 문서 craft 역주입 — PRD/ARCHITECTURE/CONTEXT 템플릿 + ADR 강화 + 경량 모드
- **notes**: 작업 완료, **PR #32 대기**. Class A. icons-ip(방법론 미적용 lean) PRD 작성 craft 중 순수 doc craft 7종 채택. 신규 템플릿 3종(`prd.md`·`architecture.md`·`context-glossary.md`) + `ADR-template.md` 강화(결정문장 제목·Considered Options·되돌리기 비용) + `requirements-spec.md`(M/S+Pn) + 지침 00 §11.5~11.7(경량 모드·문서 충돌 surfacing·작업유형 라우팅). GitHub-Issues 트래커는 file-based 설계 충돌이라 제외.

### METH-042
- **title**: 원본 기획 학습 코퍼스(다운로드 510종) 직접 정독 역주입 — 신규 템플릿 12종 + 지침 10/11/13/15/16 §19 대량 보강
- **notes**: 작업 완료, **PR #32 대기**(원래 PR #31 묶음이었으나 #31이 040까지만 머지돼 #32로 재통합). Class A. ICONS 정제본이 흘린 craft를 원본 직접 정독으로 회수(office 84종 변환, 6 클러스터 병렬). **신규 템플릿 12종**(제안·검수·운영·수익관리: proposal-go-nogo·profitability-sheet·qa-acceptance-plan·qa-test-scenario·qa-acceptance-signoff·research-collection-checklist·operation-spec·post-launch-monitoring·work-request-ticket·glossary·execution-plan·microcopy) + 지침 10/11/13/15 §19 보강 + 16 §15 신설.

### METH-041
- **title**: ICONS knowledge §19 압축 누락 보충 (METH-039 후속) — 지침 10/11/15 §19 체크리스트 본문 복원
- **notes**: 작업 완료, **PR #32 대기**(원래 PR #31 묶음, #32로 재통합). Class A. METH-039 압축 시 "이름만 남고 본문 증발"한 체크리스트 6건 복원: 지침 10(협업·커뮤니케이션 KJ법·블루캡·개발/디자인 대화법·Exec Summary 8칸), 11(서비스정의 3종·UIUX 7루브릭·용어사전/페이퍼목업/신개념), 15(WBS 3계층·Task 5요소·제안서 3 Style·품질검토 8항목). 마케팅 13은 완전 커버라 제외.

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-040
- **notes**: Completed 2026-06-23. **PR #31 머지 완료**(main `e12750f`, commit `450045a`). Class A. GambleScan 실전 풀 기획 코퍼스 6 영역 병렬 학습 → 일반 craft만 역주입. **§19 없던 지침 12(운영)·14(브랜드) §19 신설 + 18(마스터플랜) §18 신설** + 기존 §19 보강(10·11·13·15) + **개발명세 템플릿 4종**(data-model·user-flow·wireframe-spec·functional-spec). 관통: 다면 시장 + 거버넌스/추적. (주의: 같은 PR #31의 METH-041/042는 미머지 → PR #32로 운반 중.)

### METH-039
- **notes**: Completed 2026-06-23. **PR #30 머지 완료**(main `2c6e60c`). Class A. ICONS 기획 학습 정제본(`icons:40_dev/knowledge/` 6종) 환류. 지침 10/11/13/15 §19 "실무 craft 부록" + 기획 양식 템플릿 6종(requirements-spec·ia-spec·service-policy·user-story·kpi-tree·wbs) 신설.

### METH-038
- **notes**: Completed 2026-05-18. Class A. ship build/test 단계 npm 매니저 비호환 버그 픽스(`npm build`→`npm run build`). `60_tools/methodology.py` cmd_ship 2-라인. PR #27 머지 + 4 프로젝트 sync 전파 완료.

<!-- Archived: METH-001~037(2026-05~06) · 018·036·037. 상세는 git log --grep="METH-" 및 PR #5~#31, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~3건만. -->
