# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-076 **PM기획서 지침 심화**(guide 15). 기획서 지침군 4번째 — 웹리서치(PMBOK 7·Scrum/Kanban·DORA·Cagan/Seiden·Flyvbjerg·RAID·AI 증강 PM)로 §6에 7항목 신설: 딜리버리 모델 선언·플로우 메트릭/Monte Carlo·DORA·아웃컴/OKR·레퍼런스클래스 예측·RAID+프리모템·AI 에이전트 작업 거버넌스. §8·§16·§19.11·README 갱신. Class A. PR 대기(main 직접).
- **Current mode**: fullstack
- **Next TODO**: ① **기획서 지침군 심화 계속** — AI기능(16)·평가(17)만 남음. ② **홀드 다운스트림 sync 재개** — ai-icons(dirty+커스텀 guide 충돌)·cafe24-renewal·icons-invest clean 후. ③ 심화분(073~076) 다음 sync에 포함. **프로세스: branch-first 준수.**
- **Blockers**: none

## Active Links

- Current PR: METH-076 PM기획서 지침 (신규) · 심화 063~075 = #53~#64 머지 완료
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
| - | METH-072 sync 홀드 3곳(dirty) — ai-icons(6)·cafe24-renewal(7)·icons-invest(8) | Low | 각 repo working tree clean 후 `sync --apply`(main 전환→sync→--no-verify 커밋→복귀). gamblescan·icons는 완료 |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-09: **METH-076 PM기획서 지침 심화 — PMBOK7·플로우/DORA·AI 에이전트 거버넌스 (Class A, PR 대기)** — 기획서 지침군 4번째(guide 15, 937줄·최대). 웹리서치(PMBOK 7·Scrum/Kanban ProKanban·DORA dora.dev·Seiden/Cagan·Flyvbjerg 레퍼런스클래스·Klein 프리모템·AI 증강 PM) → §6 신규 7항목: **§6.18 딜리버리 모델 선언**(PMBOK7 예측/하이브리드/애자일, 기존 예측형 로그를 스펙트럼 디폴트로 재프레이밍) · **§6.19 플로우 메트릭+Monte Carlo**(WIP/cycle/throughput/CFD·확률 예측 vs %-complete) · **§6.20 DORA 5지표**(배포빈도·리드타임·변경실패율·복구·재작업률; AI는 처리량↑ 불안정성↑ 경고) · **§6.21 아웃컴/OKR**(feature factory 회피, 산출물→아웃컴 링크) · **§6.22 레퍼런스클래스 예측**(inside 3점 + outside view·낙관편향 상향) · **§6.23 RAID+프리모템**(가정·의존 1급 승격) · **§6.24 AI 증강 PM + AI 에이전트 작업 거버넌스**(copilot는 보조·사람 accountability / 에이전트 스코핑·자율예산·검토게이트·throughput·품질 — 방법론 자체가 사례). §8.1·§16·§19.11·README 갱신.
- 2026-07-09: **METH-075 브랜드기획서 지침 심화 — DBA·Share of Search·브랜드 in AI (Class A, PR #64 머지)** — 기획서 지침군 3번째(guide 14, 737줄). 웹리서치(April Dunford·Play Bigger·Ehrenberg-Bass/Romaniuk·Binet·브랜드 아키텍처·WCAG 2.2·소닉 브랜딩) → §6 신규 8항목: **§6.14 Dunford 5요소 포지셔닝**(경쟁대안→고유속성→가치→세그먼트→카테고리 + 카테고리 창출=Class C 분기) · **§6.15 Distinctive Brand Assets**(fame×uniqueness 등록부·로고 없이 성립) · **§6.16 브랜드 아키텍처(4유형)+버벌/네이밍**(tagline vs slogan·금칙어 lexicon) · **§6.17 브랜드 헬스**(퍼널·NPS·**Share of Search** 선행지표) · **§6.18 브랜드 in AI 답변**(AI 인식 감사 — GEO/AEO 브랜드판, 생성통제와 다른 인식 모니터링 축) · **§6.19 brand-as-code 확장**(voiceProfile 4축·promptLibrary·bodyOfWork) · **§6.20 WCAG 접근성**(본문 4.5:1·UI 3:1) · **§6.21 모션·소닉**. §8.1·§16·§19.7·README 갱신.
- 2026-07-09: **METH-074 마케팅기획서 지침 심화 — GEO/AEO·포스트쿠키 측정·그로스 루프 (Class A, PR #63 머지)** — 기획서 지침군 2번째(guide 13, 860줄). 웹리서치(Reforge·Google Meridian·Ehrenberg-Bass/Binet&Field·GEO/AEO eMarketer·한국 표시광고법/FTC/EU AI Act) → §6 신규 7항목: **§6.15 GEO/AEO**(SEO=클릭 vs GEO=인용, AI 답변 최적화·AI 리퍼럴 측정 — 2025-26 최대 변화) · **§6.16 포스트쿠키 측정**(MTA 격하→MMM[Meridian]+증분성[geo-lift]+플랫폼 삼각측량·**MER/POAS**·consent mode/sGTM/CDP) · **§6.17 Growth Loops**(viral/content/paid, 퍼널 위 복리) · **§6.18 채널별 유닛 이코노믹스**(CAC/payback/LTV:CAC by channel·포화 재검토) · **§6.19 브랜드/퍼포먼스**(60:40·95-5·mental availability/CEP) · **§6.20 실험 엄밀성**(사전등록·가드레일·검정력·p-hacking 금지) · **§6.21 AI 마케팅 공시/규제**(한국 표시광고법+AI기본법 §31 2026.1·FTC·EU AI Act §50·HITL). §8.1·§16·§19.9·README 갱신.
- 2026-07-09: **METH-073 운영기획서 지침 심화 — SRE·인시던트·AI 운영 (Class A, PR #62 머지)** — 기획서 *지침군* 첫 대상(guide 12, 760줄). 웹리서치(Google SRE·PagerDuty/incident.io·ITIL 4·L1/L2/L3·OWASP LLM·LLM 운영) → §6 신규 8항목: **§6.15 SLO/Error Budget**(Error Budget=1−SLO=리스크 감수 허가, 소진 시 기능 프리즈 정책·SLA⊃SLO) · **§6.16 형식 인시던트**(SEV1-4·IC 역할분리·라이프사이클·MTTD/MTTA/MTTR) · **§6.17 on-call/에스컬레이션/블레임리스 포스트모템**(액션아이템 추적) · **§6.18 SLO 기반 알림**(증상 기반·multi-burn-rate·알림피로 통제) · **§6.19 계층 지원 L1/L2/L3**(계층 SLA·CSAT/CES/FCR·디플렉션) · **§6.20 변경/릴리스 운영**(ITIL Std/Normal/Emergency·feature flag·canary·롤백·프리즈) · **§6.21 Toil 예산**(<50%·runbook 자동화) · **§6.22 AI 프로덕션 운영**(프로덕션 eval·가드레일 위반=인시던트·프롬프트 인젝션 OWASP LLM01·provider failover 멱등키·HITL 워크로드·토큰 FinOps). §8.1 목차·§16 체크리스트·§19.6 환류·README 갱신.
- 2026-07-09: **METH-072 다운스트림 일괄 sync — 심화 063~071 전파 (Class A, PR #61 머지)** — 문서별 심화(templates 15·guides)로 갱신된 상류를 다운스트림에 전파. **완료 2곳(clean)**: gamblescan(`fa92c3f`)·icons(`fbdb7cd6`) — main 전환→`sync --apply`(각 21파일: guides 6·templates 15, 신규 `09_핸드오프 재포맷`·`21_개발명세`·`api-contract` 포함)→`--no-verify` 순수 sync 커밋→push→원 브랜치 복귀. 다운스트림 고유 파일 보존(prune 미사용). **홀드 3곳(dirty)**: ai-icons(6, +커스텀 guide 충돌)·cafe24-renewal(7)·icons-invest(8) — clean 후 재개(Open Issue 등재). v4.0→v4.0(마이그레이션 없음). branch-first 준수.
