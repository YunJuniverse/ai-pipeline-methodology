# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

### METH-044
- **title**: 모드별 템플릿 선택 체계 — `_CATALOG.md` + CLAUDE.md Mode 확장 (작업 용도에 따라 필요한 템플릿만)
- **gate**: ⚠️ **PR #32(METH-043) 머지 후 착수**. PR #31(METH-040/041/042)은 머지 완료(main `e12750f`). 카탈로그가 deliverable 템플릿 25종 전체를 참조하므로 #32까지 머지된 clean main에서 작성(dangling 참조·브랜치 스택 회피). 이번 세션 역주입 작업들의 capstone.
- **design (확정)**:
  - **6개 모드 → 세트**: `planning`(기획전용: prd·requirements-spec·ia-spec·service-policy·user-story·kpi-tree·context-glossary·microcopy) · `dev`(개발전용: architecture·data-model·user-flow·wireframe-spec·functional-spec) · `fullstack`(planning∪dev+wbs) · `agency`(외주 SI 라이프사이클: proposal-go-nogo·research-collection-checklist·profitability-sheet·execution-plan·wbs·qa 3종·operation-spec·post-launch-monitoring·work-request-ticket·glossary + 기획/개발) · `lean`(경량: prd·architecture·context-glossary·ADR) · `ops`(운영: operation-spec·post-launch-monitoring·work-request-ticket·qa 3종).
  - **메커니즘(비파괴적, flat 경로 유지)**: ① `50_resources/templates/_CATALOG.md` — 25종 한 줄 카탈로그(카테고리별) + 모드×템플릿 매트릭스 + 모드별 권장 세트. ② CLAUDE.md `Mode` 필드 확장 `[planning/dev/fullstack/agency/lean/ops]`(현재 fullstack/planning-only). ③ 지침 00 "작업 모드 → 카탈로그에서 필요한 템플릿만 로드" 원칙 1줄. ④ (선택·후속) CLI `methodology templates --mode <mode>` — methodology.py 작업이라 별도.
  - **폴더 재구성 금지**: planning/·dev/ 하위 이동 시 METH-039~043 참조 flat 경로 전부 깨짐 → 카탈로그(매핑 문서)로 해결.
- **acceptance**: `_CATALOG.md`에 25종 전부 분류·6모드 매트릭스 완비 + CLAUDE.md Mode 확장 + 지침 00 원칙 1줄. Class A. 머지 후 다운스트림 sync 합산.

## Ready

## InProgress

### METH-043
- **title**: 적용 프로젝트(icons-ip) 경량 파이프라인 문서 craft 역주입 — PRD/ARCHITECTURE/CONTEXT 템플릿 + ADR 강화 + 경량 모드
- **notes**: 작업 완료, **PR #32 대기**(머지 전). Class A. 별도 PR(브랜치 `claude/inject-lean-doc-craft-from-icons-ip`). PR #31(METH-040/041/042) 머지 후 본 브랜치에 origin/main 머지로 라이브 파일 충돌 해소 완료(craft 파일은 비충돌). icons-ip(방법론 미적용 lean 코드베이스)의 PRD 작성 craft 중 순수 doc craft 7종 채택(GitHub-Issues 트래커는 file-based 설계 충돌이라 제외). ① 신규 템플릿 3종: `prd.md`(무엇·M/S·Pn=출시순서·규제 요구사항 표·현황 갭) · `architecture.md`(어떻게·as-built→목표→이전경로·규제 기술매핑) · `context-glossary.md`(도메인 용어집 _Avoid_+예시대화). ② `ADR-template.md` 강화(제목=결정문장·Considered Options·되돌리기 비용). ③ `requirements-spec.md` M/S+Pn 보강 · 지침 00 §11.5~11.7(경량 모드·문서 충돌 surfacing·작업유형 라우팅). 머지 후 다운스트림 sync(METH-039~043 합산).

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-042
- **notes**: Completed 2026-06-23. **PR #31 머지 완료**(main `e12750f`). Class A. 적용 프로젝트 ICONS가 학습한 *원본* 기획 코퍼스(`~/Downloads/사업기획학습`·`서비스기획학습` 510종)를 AI가 직접 정독 → ICONS 정제본(2차 lossy)이 흘린 craft 회수. office 84종 LibreOffice 변환, 6 클러스터 병렬 학습(PNG 325 IA캡처·hwp 중복 제외). **신규 템플릿 12종**(제안·검수·운영·수익관리: proposal-go-nogo·profitability-sheet·qa-acceptance-plan·qa-test-scenario·qa-acceptance-signoff·research-collection-checklist·operation-spec·post-launch-monitoring·work-request-ticket·glossary·execution-plan·microcopy) + 지침 10/11/13/15 §19 대량 보강 + 16 §15 신설. 잔여: 다운스트림 sync(METH-039~043 합산).

### METH-041
- **notes**: Completed 2026-06-23. **PR #31 머지 완료**. Class A. ICONS knowledge §19 압축 누락 보충(METH-039 후속) — ICONS 학습은 이미 METH-039로 주입됐으나 §19 압축 시 "이름만 남고 본문 증발"한 체크리스트 6건 복원: 지침 10(협업·커뮤니케이션 KJ법·블루캡·개발/디자인 대화법, Exec Summary 8칸), 11(서비스정의 3종·UIUX 7루브릭·용어사전/페이퍼목업/신개념 온보딩), 15(WBS 3계층·Task 5요소·제안서 3 Style·품질검토 8항목). 마케팅 13은 완전 커버라 제외.

### METH-040
- **notes**: Completed 2026-06-23. **PR #31 머지 완료**. Class A. 적용 프로젝트 GambleScan 실전 풀 기획 코퍼스(methodology-v1/planning·development·docs/planning·research, ~9천 줄)를 6 영역 병렬 학습 → 일반 craft만 역주입(METH-039 ICONS 패턴의 GambleScan판). **§19 없던 지침 12(운영)·14(브랜드) §19 신설 + 18(마스터플랜) §18 신설** + 기존 §19 보강(10·11·13·15) + **개발명세 템플릿 4종**(data-model·user-flow·wireframe-spec·functional-spec — 기획↔빌드 빈 층). 관통: 다면(N-sided) 시장 기획 + 거버넌스/추적. ICONS와 비중복.

<!-- Archived: METH-001~010 · 011~012 · 015 · 023~032 (2026-05). METH-039(PR #30)·038·037·036·018(2026-05~06-23). 상세는 git log --grep="METH-" 및 PR #5~#31, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~3건만. -->
