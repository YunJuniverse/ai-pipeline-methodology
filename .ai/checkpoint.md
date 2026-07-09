# Checkpoint — 2026-07-09 (METH-073 운영기획서 지침 심화 · SRE·인시던트·AI 운영)

> ✅ METH-073: 기획서 *지침군* 심화 첫 대상 = guide 12 운영기획서. 웹리서치(SRE·인시던트·ITIL·LLM 운영) → §6에 8항목 신설(§6.15~6.22).
> 핵심: "모니터링 있음"을 **SLO/error-budget 정책(기능 프리즈 레버)·형식 인시던트(SEV+IC+MTTR)·블레임리스 포스트모템**으로 격상. AI 운영은 *가드레일 위반=인시던트*·HITL·토큰 FinOps.
> 🏁 다음: PR 리뷰·머지 → 지침군 계속(마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17) 또는 홀드 다운스트림 sync 재개.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-073-ops-plan-guide-refresh` (fresh main 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-073 — 운영기획서 지침(guide 12, 760줄) 심화** (기획서 지침군 프로그램 시작):

- **방법**: 웹리서치 1차 소스(Google SRE workbook·PagerDuty/incident.io·ITIL 4·L1/L2/L3 지원·OWASP LLM01·LLM 프로덕션 운영/FinOps). 현행 §6(운영 프로세스·정책·CS·이슈대응·관리자기능·KPI·AIOps 관제·인간 검토 게이트·AI Incident) gap.
- **변경 (`20_guides/12_운영기획서_작성_지침.md`)** — §6 신규 8항목:
  - **§6.15 SLO/Error Budget** — SLI/SLO/SLA·Error Budget=1−SLO·소진 시 기능 프리즈 정책(거버넌스 레버).
  - **§6.16 형식 인시던트** — SEV1~4·IC/Comms/Ops 역할분리·라이프사이클·MTTD/MTTA/MTTR.
  - **§6.17 on-call/에스컬레이션/블레임리스 포스트모템**(핸드오프 오버랩·액션아이템 추적).
  - **§6.18 SLO 기반 알림** — 증상 기반·multi-burn-rate·알림피로 통제(3 pillars).
  - **§6.19 계층 지원 L1/L2/L3** — 계층 SLA·CSAT/CES/FCR·디플렉션·L3 부하 신호.
  - **§6.20 변경/릴리스 운영** — ITIL Std/Normal/Emergency·feature flag·canary·롤백·프리즈.
  - **§6.21 Toil 예산** — <50%·runbook 자동화·"제거한 toil" KPI.
  - **§6.22 AI 프로덕션 운영** — 프로덕션 eval(groundedness/drift)·가드레일 위반=인시던트·프롬프트 인젝션(OWASP LLM01)·provider failover(멱등키)·HITL 워크로드·토큰 FinOps.
  - §8.1 목차·§16 체크리스트·§19.6 환류 노트·README §3.2 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-073 PR 리뷰·머지.
2. **기획서 지침군 심화 계속** — 마케팅(13)·브랜드(14)·PM(15)·AI기능(16)·평가(17). 같은 패턴(현행 §6/§19 고찰 → 웹리서치 → §6 신규 항목 + §8/§16/§19 갱신).
3. **홀드 다운스트림 sync 재개** — ai-icons(dirty+커스텀 guide 충돌)·cafe24-renewal·icons-invest clean 후. 073~ 심화분도 다음 sync에 포함.

## 미해결 결정사항 (Open Questions)

- 지침군 심화 시 §6 항목이 계속 늘어남(운영은 14→22) — lean 유지 위해 조건부(AI·규제) 표기로 완화 중. 실사용에서 무게 재점검.
- 다운스트림 sync를 PR로 할지 main 직접(--no-verify)할지 — 현행 유지.

## 환경 메모

- 브랜치: `claude/meth-073-ops-plan-guide-refresh` (fresh main 기준). main 직접 PR. branch-first 준수.
- 변경: `20_guides/12_운영기획서_작성_지침.md`(§6·§8·§16·§19) + `20_guides/README.md` + 라이브 4종.
- 문서별 심화 진척: 063~071 템플릿(머지) + 072 sync(#61) + **073 지침군 시작(운영기획서)**.
