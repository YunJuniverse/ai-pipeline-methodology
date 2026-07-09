# Checkpoint — 2026-07-09 (METH-074 마케팅기획서 지침 심화 · GEO/AEO·포스트쿠키 측정)

> ✅ METH-074: 기획서 지침군 2번째 = guide 13 마케팅기획서. 웹리서치(Reforge·Meridian·Ehrenberg-Bass·GEO/AEO·규제) → §6에 7항목 신설(§6.15~6.21).
> 핵심: **SEO→GEO(인용 최적화) · MTA→MMM+증분성 삼각측량(MER/POAS) · 퍼널→Growth Loop(복리) · 브랜드/퍼포먼스 60:40(95-5) · AI 광고 공시 의무(한국 2026.1)**.
> 🏁 다음: PR 리뷰·머지 → 지침군 계속(브랜드 14·PM 15·AI기능 16·평가 17) 또는 홀드 다운스트림 sync 재개.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-074-marketing-plan-guide-refresh` (fresh main 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-074 — 마케팅기획서 지침(guide 13, 860줄) 심화** (기획서 지침군 프로그램 2번째):

- **방법**: 웹리서치 1차 소스(Reforge growth loops·Google Meridian/eMarketer MMM·증분성·Ehrenberg-Bass/Binet&Field 60:40·95-5·GEO/AEO eMarketer·HubSpot·한국 표시광고법/AI기본법·FTC·EU AI Act). 현행 §6(타깃·여정·퍼널·채널·캠페인·전환·리텐션·콘텐츠·예산·KPI·일정·AI 도구 운영·AI 콘텐츠 평가) gap.
- **변경 (`20_guides/13_마케팅기획서_작성_지침.md`)** — §6 신규 7항목:
  - **§6.15 GEO/AEO** — AI 답변 인용 최적화(front-load·추출가능 구조·1차출처·llms.txt·신선도)·플랫폼 소스 편향·AI 리퍼럴/SOV 측정. (2025-26 최대 변화, 완전 신설)
  - **§6.16 포스트쿠키 측정** — MTA 격하→**MMM(Meridian)+증분성(geo-lift)+플랫폼 삼각측량**·**MER/POAS**·consent mode/sGTM/CDP·캠페인 증분성 증명 필수.
  - **§6.17 Growth Loops** — viral/content/paid, 퍼널 위 복리(PLG activation/aha).
  - **§6.18 채널별 유닛 이코노믹스** — CAC/payback/LTV:CAC by channel·포화 재검토·kpi-tree 연결.
  - **§6.19 브랜드/퍼포먼스** — 60:40·95-5·mental availability/CEP.
  - **§6.20 실험 엄밀성** — 사전등록·가드레일·검정력 ≥80%·p-hacking 금지.
  - **§6.21 AI 마케팅 공시/규제** — 한국 표시광고법+AI기본법 §31(2026.1)·FTC·EU AI Act §50·HITL 가드레일.
  - §8.1 목차·§16 체크리스트·§19.9 환류·README §3.2 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-074 PR 리뷰·머지.
2. **기획서 지침군 심화 계속** — 브랜드(14)·PM(15)·AI기능(16)·평가(17). 같은 패턴(현행 §6/§19 고찰 → 웹리서치 → §6 신규 항목 + §8/§16/§19/README 갱신).
3. **홀드 다운스트림 sync 재개** — ai-icons(dirty+커스텀 guide 충돌)·cafe24-renewal·icons-invest clean 후. 073~074 지침 심화분도 다음 sync에 포함.

## 미해결 결정사항 (Open Questions)

- 지침 §6 항목 증가(마케팅 14→21) — lean 유지 위해 조건부(AI·규제) 표기·심화 레이어로 관리 중. 실사용에서 무게 재점검.
- 지침군 심화 누적분(073·074~)을 다운스트림에 sync할 타이밍.

## 환경 메모

- 브랜치: `claude/meth-074-marketing-plan-guide-refresh` (fresh main 기준). main 직접 PR. branch-first 준수.
- 변경: `20_guides/13_마케팅기획서_작성_지침.md`(§6·§8·§16·§19) + `20_guides/README.md` + 라이브 4종.
- 진척: 063~071 템플릿(머지)+072 sync(#61)+073 운영지침(#62)+**074 마케팅지침(이번)**. 지침군 남음: 14·15·16·17.
