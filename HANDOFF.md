# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-082 **운영원칙(지침00) 정합 점검**. 12~17 심화 후 헌법이 신규 문서·정본을 모르던 drift 교정. **핵심 원칙: 헌법은 원칙 수준 유지 — 심화 내용을 복제하지 않고 하위 지침으로 포인터**(중복 회피). §1.3 문서 체계 완성(16·17·18·01), §3.1 분류자에 AI기능/평가/PM + 라우터 01 §5.9~5.10 disambiguation 정본 포인터, §3.5 연계 16+17 동시, §4.3 역할요약 16·17 추가 + 심화 정본=지침10~17 명문화, §5.7 frontmatter stale 경로(`briefs/updates/`→`00_briefs/current/`) 수정, §11.5 카운트 완화, §17 변경이력 신설. 내부 정합성(리서치 없음). Class A. PR 대기.
- **Current mode**: fullstack
- **Next TODO**: ① **문서별 심화 프로그램 대부분 완료** — 템플릿 13종(063~071)+지침군 6종(073~078)+오케스트레이션(079)+마스터플랜 SSOT(080)+prompts 층(081)+운영원칙(082). 남은 후보: agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs), 메타/dev 지침(02~09·19~20). ② **누적 심화분(073~082) 다운스트림 sync** — gamblescan·icons(072까지 반영됨→073~ 추가) + 홀드 3곳 clean 후. ③ **graph.json 노드 완성**(guide 02~09·19~21 누락, 별건). **프로세스: branch-first 준수.**
- **Blockers**: none

## Active Links

- Current PR: METH-082 운영원칙(00) 정합 점검 (신규) · METH-081 prompts 층 = #70 머지 완료 · 063~080 = #53~#69 머지 완료
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

- 2026-07-09: **METH-082 운영원칙(지침00) 정합 점검 — 인벤토리·포인터 갱신 (Class A, PR 대기)** — 사용자 지시("운영원칙 점검"). 12~17 심화·신규 문서(16·17·18)·현행화(079~081) 후 헌법이 이를 모르던 drift 교정. **핵심 원칙 재확인: 헌법은 원칙 수준 유지 — 심화 내용을 복제하지 않고 하위 지침(10~17)·라우터(01)·_CATALOG로 포인터**(이번 세션 관통 SSOT 주제). 변경: §1.3 문서 체계 완성(16·17·18·01 명시), §3.1 분류자에 AI기능/평가/PM + **라우터 01 §5.9~5.10 disambiguation 정본 포인터**, §3.5 연계 16+17 동시 제안, §4.3 역할요약 16·17 추가 + "심화 정본=지침10~17, 헌법 복제 금지" 명문화, §5.7 frontmatter stale 경로(`briefs/updates/`→`00_briefs/current/`, prompts와 동일 drift) 수정, §11.5 stale 카운트 완화, §17 변경이력 신설. 내부 정합성(리서치 없음).
- 2026-07-09: **METH-081 prompts/ 층 전면 현행화 — drift 해소 + _README 신설 (Class A, PR #70 머지)** — 사용자 질문(운영원칙 지침00·prompts 역할)에서 프롬프트층이 나머지 방법론과 심하게 drift 발견(라우터 079 문제와 동종). **구모델→현모델**: 입력 `briefs/`→`00_briefs/current/`, 산출 `40_dev/snapshots/plans/xxx/vN`→`30_planning/NN_*.md`(라이브 in-place), "항상 6종"→모드 선택 로딩. **목차 복제 제거**(구조 SSOT=지침, METH-080과 동일 교정). 기획서 프롬프트 6종(business/service/ops/marketing/brand/pm) 재작성 + **ai-feature(16)·eval-guardrail(17) 신설**(기획서 8종 전체 커버) + 코드-역문서화 4종(architecture/data-model/api-spec/service-spec) 역할 명확화(전방 설계=템플릿 vs 역문서화=프롬프트) + dev-spec 현행화(지침21·개발명세 5종·planning-handoff) + plan-routing/re-plan/plan 현행화 + **`_README.md` 신설**(프롬프트↔지침↔템플릿↔모드 매핑, _CATALOG 대응). 상위 문서(README·50_resources/_README "스냅샷 생성"→"AI 실행 프롬프트") 정정. 17개 파일. 내부 정합성(리서치 없음).
- 2026-07-09: **METH-080 마스터플랜(지침18) SSOT 정합 — 인라인→ID 참조 (Class A, PR #69 머지)** — 사용자 재점검 요청("마스터플랜 역할·필요성 다시 점검"). **결론: 슬롯은 고유**(빌드 순서·페이즈·MVP-lock·게이트 인스턴스 — 다른 문서 미소유) → 폐기 아님. 단 v2 "11 기능 정의 *인라인 복제*"가 11↔18 이중관리·SSOT 위반 안티패턴(개발기획서 재번들·서비스기획서 컨테이너 논쟁과 동형)으로 확인 → **ID 참조 + 페이즈 오버레이(v5)**로 완화: §1 목적·§14.1 경계·§16 실수·§17 프롬프트(OUTPUT/RULES/BOUNDARY)·인트로 개정. **15↔18 경계 재조정**(METH-076으로 15에 딜리버리/플로우/DORA/OKR 추가 후): "15=표준 정의 → 18=프로젝트 인스턴스" §14.2 명문화. 템플릿 SSOT 주석 + stale 경로(docs/archive→20_guides) 수정. 내부 정합성(리서치 없음). 왜 안 건드렸었나: 18은 dev-transition 밴드(18~20)라 기획서 지침군(12~17) 심화 순번 밖 + 이미 v4로 성숙.
- 2026-07-09: **METH-079 오케스트레이션 지침(01) 라우팅 갱신 — 심화 반영 (Class A, PR #68 머지)** — 내부 정합성(리서치 없음). 12~17 심화(073~078)로 추가된 신규 영역을 라우터(guide 01)에 반영: **§5.9 신규 영역 라우팅 표**(SLO/인시던트/AI운영→운영12 · GEO/AEO/MMM→마케팅13 · DBA/Share of Search/brand in AI→브랜드14 · 딜리버리/DORA/에이전트 거버넌스→PM15 · MCP/RAG/구조화출력→AI기능16 · NIST/ISO/레드팀→평가17) + **AI 주제 경계 disambiguation**(brand in AI[14] vs GEO[13] vs AI기능[16] / 에이전트 기능설계[16] vs 작업관리[15] vs 장애대응[12] / feature eval[16] vs org 카탈로그[17]) · **§5.10 모드·템플릿 라우팅**(planning-handoff·개발명세 → _CATALOG/지침21) · §5.7 키워드(MCP·구조화출력·컨텍스트) · §18.1 포인터. graph.json 노드 누락(02~09·19~21)은 Open Issue 등재(별건).
- 2026-07-09: **METH-078 평가·가드레일 지침 심화 — 거버넌스 3축·judge bias·trajectory eval (Class A, PR #67 머지)** — **기획서 지침군(12~17) 심화 완결**(guide 17, org eval/guard 카탈로그). 웹리서치(MT-Bench/G-Eval·RAGAS·NIST AI RMF+GenAI Profile AI 600-1·ISO/IEC 42001·EU AI Act GPAI Code of Practice·OpenTelemetry GenAI semconv·Garak/PyRIT) → 신규: **§3.7 LLM-judge bias & 완화**(position/verbosity/self-preference/sycophancy·순서스왑·pairwise·G-Eval·calibration 게이트·judge 버전 pin) · **§3.8 에이전트/trajectory eval**(task성공·tool-call 정확성·trajectory·비용, (state,action) judge 기하평균) · **§3.9 RAG 메트릭 카탈로그**(RAGAS 4종·검색vs생성 실패 진단) · **§3.10 eval 데이터 위생**(오염·홀드아웃·버전·합성데이터 검토) · **§4.4 EU AI Act GPAI 갱신**(2025.8 적용/2026.8 집행·CoP 3장·Art.55 systemic·Art.50) · **§4.5 레드팀 pre-release 게이트**(Garak/PyRIT·finding→regression CI) · **§4.6 거버넌스 3축 매핑**(NIST AI RMF Govern/Map/Measure/Manage+600-1·ISO 42001 AIMS·EU AI Act) · **§6 OTel GenAI semconv 정렬** · §10 환류. README 갱신. 16(feature)↔17(org) 경계 재확인.
