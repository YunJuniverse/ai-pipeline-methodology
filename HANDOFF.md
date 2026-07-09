# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-079 **오케스트레이션 지침(01) 라우팅 갱신**. 12~17 심화(073~078)로 추가된 신규 영역을 라우터에 반영 — §5.9 신규 영역 라우팅 표 + AI 주제 경계 disambiguation(brand in AI/GEO/AI기능, 에이전트 기능/작업/운영, feature/org) · §5.10 모드·템플릿 라우팅(planning-handoff·개발명세→_CATALOG/21) · §5.7 키워드 · §18.1 포인터. 내부 정합성(리서치 없음). Class A. PR 대기(main 직접).
- **Current mode**: fullstack
- **Next TODO**: ① **문서별 심화 프로그램 대부분 완료** — 템플릿 13종(063~071)+지침군 6종(073~078)+오케스트레이션(079). 남은 후보: agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs), 메타/dev 지침(00·02~09·18~20). ② **누적 심화분(073~079) 다운스트림 sync** — gamblescan·icons(072까지 반영됨→073~ 추가) + 홀드 3곳 clean 후. ③ **graph.json 노드 완성**(guide 02~09·19~21 누락, 별건). **프로세스: branch-first 준수.**
- **Blockers**: none

## Active Links

- Current PR: METH-079 오케스트레이션 지침 라우팅 (신규) · 심화 063~078 = #53~#67 머지 완료
- Current issue:
- Relevant ADRs:
- Relevant snapshots: `40_dev/snapshots/implementation-plan-2026-05-07.md`, `40_dev/snapshots/transfer-drill-2026-05-08.md`

## Open Decisions

| ID | Decision | Needed By | Status |
|----|----------|-----------|--------|
| - | `.claude/worktrees/` and `.codex/` are local tool metadata and should be gitignored | 2026-05-07 | Closed |

## Open Issues

| ID | Issue | Severity | Next Step |
|----|-------|----------|-----------|
| - | ~~sync가 다운스트림 고유 파일 mirror-delete~~ | — | **Closed** — METH-046(PR #35)로 prune을 --prune opt-in화(기본 보존) |
| - | Some legacy/archive docs may still mention pre-`40_dev` or pre-`60_tools` paths | Low | Sweep only if those docs become live references again |
| - | ai-icons 레거시 커스텀 guide 번호 충돌 (04 문서보관·05 회의록·21 산출물채널분리) — 상류 05와 번호/내용 충돌로 sync 홀드 | Med | ai-icons 세션: 21→상류 05 dedup + 04·05를 guide 02 §8 예약범위(90+) 마이그레이션 → sync 재개 |
| - | METH-072 sync 홀드 3곳(dirty) — ai-icons(6)·cafe24-renewal(7)·icons-invest(8) | Low | 각 repo working tree clean 후 `sync --apply`(main 전환→sync→--no-verify 커밋→복귀). gamblescan·icons는 072까지 반영 — 073~079 추가 sync 필요 |
| - | `methodology-graph.json` 노드 불완전 — guide 02~09·19~21 누락(00·01·10~18만) | Low | 대시보드 시각화 그래프. METH-079에서 발견. 노드/엣지 보강은 별건(대시보드 렌더 영향 확인 후) |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-09: **METH-079 오케스트레이션 지침(01) 라우팅 갱신 — 심화 반영 (Class A, PR 대기)** — 내부 정합성(리서치 없음). 12~17 심화(073~078)로 추가된 신규 영역을 라우터(guide 01)에 반영: **§5.9 신규 영역 라우팅 표**(SLO/인시던트/AI운영→운영12 · GEO/AEO/MMM→마케팅13 · DBA/Share of Search/brand in AI→브랜드14 · 딜리버리/DORA/에이전트 거버넌스→PM15 · MCP/RAG/구조화출력→AI기능16 · NIST/ISO/레드팀→평가17) + **AI 주제 경계 disambiguation**(brand in AI[14] vs GEO[13] vs AI기능[16] / 에이전트 기능설계[16] vs 작업관리[15] vs 장애대응[12] / feature eval[16] vs org 카탈로그[17]) · **§5.10 모드·템플릿 라우팅**(planning-handoff·개발명세 → _CATALOG/지침21) · §5.7 키워드(MCP·구조화출력·컨텍스트) · §18.1 포인터. graph.json 노드 누락(02~09·19~21)은 Open Issue 등재(별건).
- 2026-07-09: **METH-078 평가·가드레일 지침 심화 — 거버넌스 3축·judge bias·trajectory eval (Class A, PR #67 머지)** — **기획서 지침군(12~17) 심화 완결**(guide 17, org eval/guard 카탈로그). 웹리서치(MT-Bench/G-Eval·RAGAS·NIST AI RMF+GenAI Profile AI 600-1·ISO/IEC 42001·EU AI Act GPAI Code of Practice·OpenTelemetry GenAI semconv·Garak/PyRIT) → 신규: **§3.7 LLM-judge bias & 완화**(position/verbosity/self-preference/sycophancy·순서스왑·pairwise·G-Eval·calibration 게이트·judge 버전 pin) · **§3.8 에이전트/trajectory eval**(task성공·tool-call 정확성·trajectory·비용, (state,action) judge 기하평균) · **§3.9 RAG 메트릭 카탈로그**(RAGAS 4종·검색vs생성 실패 진단) · **§3.10 eval 데이터 위생**(오염·홀드아웃·버전·합성데이터 검토) · **§4.4 EU AI Act GPAI 갱신**(2025.8 적용/2026.8 집행·CoP 3장·Art.55 systemic·Art.50) · **§4.5 레드팀 pre-release 게이트**(Garak/PyRIT·finding→regression CI) · **§4.6 거버넌스 3축 매핑**(NIST AI RMF Govern/Map/Measure/Manage+600-1·ISO 42001 AIMS·EU AI Act) · **§6 OTel GenAI semconv 정렬** · §10 환류. README 갱신. 16(feature)↔17(org) 경계 재확인.
- 2026-07-09: **METH-077 AI기능기획서 지침 심화 — 에이전트·MCP·RAG·컨텍스트 엔지니어링 (Class A, PR #66 머지)** — 기획서 지침군 5번째(guide 16, AI-native ~2026-05). 웹리서치(Anthropic Building Effective Agents·effective context engineering·MCP 스펙·OpenAI structured outputs·RAGAS·OWASP LLM Top10 2025) → §5 신규 7항목(2026-05 이후 발전분): **§5.15 에이전트 아키텍처**(workflow vs agent 게이트·ReAct/plan-execute·정지조건=LLM10 방어) · **§5.16 에이전트 메모리**(short/long-term·PII) · **§5.17 MCP 통합**(tools/resources·OAuth RFC 8707·tool 응답=미신뢰=LLM01) · **§5.18 RAG 설계+RAG-eval**(chunking/rerank·grounding·RAGAS faithfulness/context recall·agentic RAG) · **§5.19 구조화 출력 메커니즘**(JSON Schema·constrained decoding·strict function calling=LLM05 방어) · **§5.20 컨텍스트 엔지니어링+모델 적응 결정트리**(prompt caching·compaction·context rot·프롬프트→RAG→FT→추론 사다리) · **§5.21 OWASP LLM Top10 2025 feature 체크**. §7 목차·§15.2 환류·README 갱신. 조직 eval/guard 카탈로그는 17번(중복 회피).
- 2026-07-09: **METH-076 PM기획서 지침 심화 — PMBOK7·플로우/DORA·AI 에이전트 거버넌스 (Class A, PR #65 머지)** — 기획서 지침군 4번째(guide 15, 937줄·최대). 웹리서치(PMBOK 7·Scrum/Kanban ProKanban·DORA dora.dev·Seiden/Cagan·Flyvbjerg 레퍼런스클래스·Klein 프리모템·AI 증강 PM) → §6 신규 7항목: **§6.18 딜리버리 모델 선언**(PMBOK7 예측/하이브리드/애자일, 기존 예측형 로그를 스펙트럼 디폴트로 재프레이밍) · **§6.19 플로우 메트릭+Monte Carlo**(WIP/cycle/throughput/CFD·확률 예측 vs %-complete) · **§6.20 DORA 5지표**(배포빈도·리드타임·변경실패율·복구·재작업률; AI는 처리량↑ 불안정성↑ 경고) · **§6.21 아웃컴/OKR**(feature factory 회피, 산출물→아웃컴 링크) · **§6.22 레퍼런스클래스 예측**(inside 3점 + outside view·낙관편향 상향) · **§6.23 RAID+프리모템**(가정·의존 1급 승격) · **§6.24 AI 증강 PM + AI 에이전트 작업 거버넌스**(copilot는 보조·사람 accountability / 에이전트 스코핑·자율예산·검토게이트·throughput·품질 — 방법론 자체가 사례). §8.1·§16·§19.11·README 갱신.
- 2026-07-09: **METH-075 브랜드기획서 지침 심화 — DBA·Share of Search·브랜드 in AI (Class A, PR #64 머지)** — 기획서 지침군 3번째(guide 14, 737줄). 웹리서치(April Dunford·Play Bigger·Ehrenberg-Bass/Romaniuk·Binet·브랜드 아키텍처·WCAG 2.2·소닉 브랜딩) → §6 신규 8항목: **§6.14 Dunford 5요소 포지셔닝**(경쟁대안→고유속성→가치→세그먼트→카테고리 + 카테고리 창출=Class C 분기) · **§6.15 Distinctive Brand Assets**(fame×uniqueness 등록부·로고 없이 성립) · **§6.16 브랜드 아키텍처(4유형)+버벌/네이밍**(tagline vs slogan·금칙어 lexicon) · **§6.17 브랜드 헬스**(퍼널·NPS·**Share of Search** 선행지표) · **§6.18 브랜드 in AI 답변**(AI 인식 감사 — GEO/AEO 브랜드판, 생성통제와 다른 인식 모니터링 축) · **§6.19 brand-as-code 확장**(voiceProfile 4축·promptLibrary·bodyOfWork) · **§6.20 WCAG 접근성**(본문 4.5:1·UI 3:1) · **§6.21 모션·소닉**. §8.1·§16·§19.7·README 갱신.
