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

### METH-076 · PM기획서 지침 심화 (PMBOK7·플로우/DORA·AI 에이전트 거버넌스)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 기획서 지침군 4번째(guide 15, 937줄·최대). 웹리서치(PMBOK 7·Scrum/Kanban·DORA·Seiden/Cagan·Flyvbjerg·RAID/프리모템·AI 증강 PM) → §6 신규 7항목: **§6.18 딜리버리 모델 선언**(예측/하이브리드/애자일, 예측형 로그를 스펙트럼 디폴트로 재프레이밍) · **§6.19 플로우 메트릭+Monte Carlo**(WIP/cycle/throughput/CFD·확률 예측) · **§6.20 DORA 5지표**(배포빈도·리드타임·변경실패율·복구·재작업률) · **§6.21 아웃컴/OKR**(feature factory 회피) · **§6.22 레퍼런스클래스 예측**(outside view·낙관편향 상향) · **§6.23 RAID+프리모템**(가정·의존 승격) · **§6.24 AI 증강 PM + AI 에이전트 작업 거버넌스**(스코핑·자율예산/정지·검토게이트·throughput/품질 — 방법론 자체 사례). §8.1·§16·§19.11·README 갱신. branch-first 준수.

### METH-075 · 브랜드기획서 지침 심화 (DBA·Share of Search·브랜드 in AI)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 기획서 지침군 3번째(guide 14, 737줄). 웹리서치(April Dunford·Play Bigger·Ehrenberg-Bass/Romaniuk·Binet·브랜드 아키텍처·WCAG·소닉) → §6 신규 8항목: **§6.14 Dunford 5요소 포지셔닝**(+카테고리 창출 분기=Class C) · **§6.15 Distinctive Brand Assets**(fame×uniqueness 등록부) · **§6.16 브랜드 아키텍처+버벌/네이밍** · **§6.17 브랜드 헬스**(퍼널·NPS·**Share of Search**) · **§6.18 브랜드 in AI 답변**(AI 인식 감사, GEO/AEO 브랜드판) · **§6.19 brand-as-code 확장**(voiceProfile·bodyOfWork) · **§6.20 WCAG 접근성**(4.5:1/3:1) · **§6.21 모션·소닉**. §8.1·§16·§19.7·README 갱신. branch-first 준수.

### METH-074 · 마케팅기획서 지침 심화 (GEO/AEO·포스트쿠키 측정·그로스 루프)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 기획서 지침군 2번째(guide 13, 860줄). 웹리서치(Reforge·Google Meridian·Ehrenberg-Bass/Binet&Field·GEO/AEO·한국 표시광고법/FTC/EU AI Act) → §6 신규 7항목: **§6.15 GEO/AEO**(AI 답변 인용 최적화 — 2025-26 최대 변화) · **§6.16 포스트쿠키 측정**(MMM+증분성+플랫폼 삼각측량·MER/POAS·consent mode/CDP) · **§6.17 Growth Loops**(퍼널 위 복리) · **§6.18 채널별 유닛 이코노믹스** · **§6.19 브랜드/퍼포먼스**(60:40·95-5·mental availability) · **§6.20 실험 엄밀성**(사전등록·가드레일·검정력) · **§6.21 AI 마케팅 공시/규제**(한국 표시광고법 2026.1·FTC·EU AI Act·HITL). §8.1·§16·§19.9·README 갱신. branch-first 준수.

### METH-073 · 운영기획서 지침 심화 (SRE·인시던트·AI 운영)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 — 기획서 *지침군* 첫 대상(guide 12, 760줄). 웹리서치(Google SRE·PagerDuty/incident.io·ITIL 4·L1/L2/L3·OWASP LLM·LLM 운영) → §6에 신규 8항목: **§6.15 SLO/Error Budget**(정책=기능 프리즈 레버) · **§6.16 형식 인시던트**(SEV1-4·IC 역할·MTTD/MTTA/MTTR) · **§6.17 on-call/에스컬레이션/블레임리스 포스트모템** · **§6.18 SLO 기반 알림**(multi-burn-rate·알림피로) · **§6.19 계층 지원 L1/L2/L3**(계층 SLA·CSAT/CES/FCR) · **§6.20 변경/릴리스 운영**(ITIL 유형·feature flag·롤백·프리즈) · **§6.21 Toil 예산** · **§6.22 AI 프로덕션 운영**(프로덕션 eval·가드레일=인시던트·provider failover·HITL 워크로드·토큰 FinOps). §8.1 목차·§16 체크리스트·§19.6 환류·README 갱신. branch-first 준수.








> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
