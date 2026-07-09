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

### METH-077 · AI기능기획서 지침 심화 (에이전트·MCP·RAG·컨텍스트 엔지니어링)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 기획서 지침군 5번째(guide 16, AI-native ~2026-05). 웹리서치(Anthropic Building Effective Agents·context engineering·MCP 스펙·OpenAI structured outputs·RAGAS·OWASP LLM Top10 2025) → §5 신규 7항목(2026-05 이후 발전): **§5.15 에이전트 아키텍처**(workflow vs agent 게이트·loop 패턴·정지조건=LLM10 방어) · **§5.16 에이전트 메모리**(short/long-term) · **§5.17 MCP 통합**(tool/resource·OAuth·미신뢰 응답=LLM01) · **§5.18 RAG 설계+RAG-eval**(RAGAS faithfulness·agentic RAG) · **§5.19 구조화 출력 메커니즘**(JSON Schema·constrained decoding·strict=LLM05 방어) · **§5.20 컨텍스트 엔지니어링+모델 적응 결정트리**(context rot·프롬프트→RAG→FT→추론 사다리) · **§5.21 OWASP LLM Top10 feature 체크**. §7 목차·§15.2 환류·README 갱신. 조직 eval/guard 카탈로그는 17번(중복 회피). branch-first 준수.

### METH-076 · PM기획서 지침 심화 (PMBOK7·플로우/DORA·AI 에이전트 거버넌스)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 기획서 지침군 4번째(guide 15, 937줄·최대). 웹리서치(PMBOK 7·Scrum/Kanban·DORA·Seiden/Cagan·Flyvbjerg·RAID/프리모템·AI 증강 PM) → §6 신규 7항목: **§6.18 딜리버리 모델 선언**(예측/하이브리드/애자일, 예측형 로그를 스펙트럼 디폴트로 재프레이밍) · **§6.19 플로우 메트릭+Monte Carlo**(WIP/cycle/throughput/CFD·확률 예측) · **§6.20 DORA 5지표**(배포빈도·리드타임·변경실패율·복구·재작업률) · **§6.21 아웃컴/OKR**(feature factory 회피) · **§6.22 레퍼런스클래스 예측**(outside view·낙관편향 상향) · **§6.23 RAID+프리모템**(가정·의존 승격) · **§6.24 AI 증강 PM + AI 에이전트 작업 거버넌스**(스코핑·자율예산/정지·검토게이트·throughput/품질 — 방법론 자체 사례). §8.1·§16·§19.11·README 갱신. branch-first 준수.

### METH-075 · 브랜드기획서 지침 심화 (DBA·Share of Search·브랜드 in AI)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 기획서 지침군 3번째(guide 14, 737줄). 웹리서치(April Dunford·Play Bigger·Ehrenberg-Bass/Romaniuk·Binet·브랜드 아키텍처·WCAG·소닉) → §6 신규 8항목: **§6.14 Dunford 5요소 포지셔닝**(+카테고리 창출 분기=Class C) · **§6.15 Distinctive Brand Assets**(fame×uniqueness 등록부) · **§6.16 브랜드 아키텍처+버벌/네이밍** · **§6.17 브랜드 헬스**(퍼널·NPS·**Share of Search**) · **§6.18 브랜드 in AI 답변**(AI 인식 감사, GEO/AEO 브랜드판) · **§6.19 brand-as-code 확장**(voiceProfile·bodyOfWork) · **§6.20 WCAG 접근성**(4.5:1/3:1) · **§6.21 모션·소닉**. §8.1·§16·§19.7·README 갱신. branch-first 준수.

### METH-074 · 마케팅기획서 지침 심화 (GEO/AEO·포스트쿠키 측정·그로스 루프)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 기획서 지침군 2번째(guide 13, 860줄). 웹리서치(Reforge·Google Meridian·Ehrenberg-Bass/Binet&Field·GEO/AEO·한국 표시광고법/FTC/EU AI Act) → §6 신규 7항목: **§6.15 GEO/AEO**(AI 답변 인용 최적화 — 2025-26 최대 변화) · **§6.16 포스트쿠키 측정**(MMM+증분성+플랫폼 삼각측량·MER/POAS·consent mode/CDP) · **§6.17 Growth Loops**(퍼널 위 복리) · **§6.18 채널별 유닛 이코노믹스** · **§6.19 브랜드/퍼포먼스**(60:40·95-5·mental availability) · **§6.20 실험 엄밀성**(사전등록·가드레일·검정력) · **§6.21 AI 마케팅 공시/규제**(한국 표시광고법 2026.1·FTC·EU AI Act·HITL). §8.1·§16·§19.9·README 갱신. branch-first 준수.









> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
