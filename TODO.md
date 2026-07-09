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

### METH-082 · 운영원칙(지침00) 정합 점검 — 인벤토리·포인터 갱신
- **notes**: 2026-07-09. Class A. PR 대기. 사용자 지시("운영원칙 점검"). 12~17 심화·신규 문서(16·17·18)·현행화(079~081) 후 헌법 drift 교정. **핵심 원칙: 헌법은 원칙 수준 유지 — 심화 복제 금지, 하위 지침(10~17)·라우터(01)·_CATALOG로 포인터**(세션 관통 SSOT). §1.3 문서체계 완성(16·17·18·01), §3.1 분류자+라우터01 §5.9~5.10 disambiguation 포인터, §3.5 16+17 동시, §4.3 16·17 역할요약+심화정본 명문화, §5.7 frontmatter stale 경로(`briefs/updates/`→`00_briefs/current/`) 수정, §11.5 카운트 완화, §17 변경이력 신설. 내부 정합성(리서치 없음). branch-first 준수.

### METH-081 · prompts/ 층 전면 현행화 — drift 해소 + _README 신설
- **notes**: 2026-07-09. Class A. PR #70 머지. 사용자 질문(운영원칙 지침00·prompts 역할)에서 프롬프트층 drift 발견(라우터 079와 동종). **구모델→현모델**: `briefs/`→`00_briefs/current/`, `40_dev/snapshots/plans/xxx/vN`→`30_planning/NN_*.md`(라이브), "항상 6종"→모드 선택. **목차 복제 제거**(구조 SSOT=지침, 080과 동형). 기획서 6종 재작성 + **ai-feature(16)·eval-guardrail(17) 신설**(8종 커버) + 코드-역문서화 4종 역할 명확화(전방=템플릿/역=프롬프트) + dev-spec 현행화 + plan-routing/re-plan/plan + **`_README.md` 신설**(프롬프트↔지침↔템플릿↔모드). README·50_resources/_README 정정. 17파일. prompts는 shared_path라 sync 자동 전파. 내부 정합성(리서치 없음). branch-first 준수.

### METH-080 · 마스터플랜(지침18) SSOT 정합 — 인라인→ID 참조
- **notes**: 2026-07-09. Class A. PR #69 머지. 사용자 재점검 요청. **결론: 마스터플랜 슬롯 고유**(빌드 순서·페이즈·MVP-lock·게이트 인스턴스) → 폐기 아님. v2 "11 기능 정의 인라인 복제"가 11↔18 이중관리·SSOT 위반(개발기획서 재번들·서비스기획서 컨테이너 논쟁과 동형)으로 확인 → **ID 참조 + 페이즈 오버레이(v5)**: §1·§14.1·§16·§17(OUTPUT/RULES/BOUNDARY)·인트로 개정. **15↔18 경계 재조정**(METH-076 후, 딜리버리/플로우/DORA/OKR/게이트/리스크 = 15표준→18인스턴스) §14.2 명문화. 템플릿 SSOT 주석+stale 경로 수정. 내부 정합성(리서치 없음). branch-first 준수.

### METH-079 · 오케스트레이션 지침(01) 라우팅 갱신 (심화 반영)
- **notes**: 2026-07-09. Class A. PR #68 머지. 내부 정합성 작업(리서치 없음) — 12~17 심화(073~078)로 추가된 신규 영역을 라우터(guide 01)에 반영. **§5.9 신규 영역 라우팅 표**(SLO/인시던트/AI운영→12, GEO/AEO/MMM→13, DBA/Share of Search/brand in AI→14, 딜리버리/DORA/에이전트 거버넌스→15, MCP/RAG/구조화출력→16, NIST/ISO/레드팀→17) + **AI 주제 경계 disambiguation**(brand in AI[14] vs GEO[13] vs AI기능[16] / 에이전트 기능설계[16] vs 에이전트 작업관리[15] vs AI 장애대응[12] / feature eval[16] vs org 카탈로그[17]) · **§5.10 모드·템플릿 라우팅**(planning-handoff·개발명세 → _CATALOG/지침21) · §5.7 키워드(MCP·구조화출력·컨텍스트) · §18.1 체크리스트 포인터. **팔로우업**: graph.json에 guide 02~09·19~21 노드 누락(기존 staleness, 별건). branch-first 준수.











> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
