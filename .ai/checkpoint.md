# Checkpoint — 2026-07-09 (METH-076 PM기획서 지침 심화 · PMBOK7·플로우/DORA·AI 에이전트 거버넌스)

> ✅ METH-076: 기획서 지침군 4번째 = guide 15 PM기획서(937줄·최대). 웹리서치(PMBOK7·Kanban/DORA·Cagan/Seiden·Flyvbjerg·RAID·AI 증강 PM) → §6에 7항목 신설(§6.18~6.24).
> 핵심: 예측형 로그 구조를 **스펙트럼 디폴트**로 재프레이밍 + 플로우/확률예측·DORA·아웃컴/OKR·outside view·RAID·**AI 에이전트 작업 거버넌스**(방법론 자체 사례).
> 🏁 다음: PR 리뷰·머지 → 지침군 마지막 2개(AI기능 16·평가 17) 또는 홀드 다운스트림 sync 재개.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-076-pm-plan-guide-refresh` (fresh main 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-076 — PM기획서 지침(guide 15, 937줄) 심화** (기획서 지침군 프로그램 4번째):

- **방법**: 웹리서치 1차 소스(PMBOK 7 원칙+도메인·2020 Scrum Guide·ProKanban 플로우·dora.dev 5지표·Seiden 'Outcomes over Output'/Cagan·Flyvbjerg 레퍼런스클래스·Klein 프리모템·PMI AI-augmented PM). 현행 §6(개요~KPI+운영원칙+Eval 포트폴리오+인간 검토 게이트 카탈로그+AI 위험 등록부, 예측형 로그 편향) gap.
- **변경 (`20_guides/15_프로젝트_관리_기획서_작성_지침.md`)** — §6 신규 7항목:
  - **§6.18 딜리버리 모델 선언** — 예측/하이브리드/애자일 스펙트럼 + 테일러링. 기존 구조=예측형 디폴트로 재프레이밍.
  - **§6.19 플로우 메트릭 + Monte Carlo** — WIP/cycle/throughput/age/CFD·확률 예측(신뢰구간) vs %-complete.
  - **§6.20 DORA 5지표** — 배포빈도·리드타임·변경실패율·복구시간·재작업률(딜리버리 성능, 운영 MTTR과 구분; AI 처리량↑ 불안정성↑).
  - **§6.21 아웃컴/OKR** — 산출물→아웃컴 링크·선행/후행·feature factory 회피.
  - **§6.22 레퍼런스클래스 예측** — inside(3점)+outside view·낙관편향 상향(Flyvbjerg).
  - **§6.23 RAID + 프리모템** — 가정·의존을 1급 승격·크리티컬패스·kick-off 프리모템.
  - **§6.24 AI 증강 PM + AI 에이전트 작업 거버넌스** — copilot(사람 accountability) + 에이전트 스코핑·자율예산/정지(지침07)·검토게이트(6.16 확장)·throughput/품질(DORA). *방법론 자체가 사례*.
  - §8.1 목차(0번 모델 선언)·§16 체크리스트·§19.11 환류·README §3.2 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-076 PR 리뷰·머지.
2. **기획서 지침군 심화 계속** — 남은 2개: AI기능(16)·평가(17). (16·17은 이미 v3 신설·AI 특화라 gap이 다를 수 있음 — 현행 정독 후 판단.)
3. **홀드 다운스트림 sync 재개** — ai-icons·cafe24-renewal·icons-invest clean 후. 073~076 지침 심화분 포함.

## 미해결 결정사항 (Open Questions)

- 지침군 심화 완료 후(16·17까지) 누적 지침 심화분(073~077)을 다운스트림에 sync할 타이밍.
- 지침 §6 항목 증가 — lean 위해 조건부/심화레이어/기존절 보강으로 관리 중. 실사용 무게 재점검.

## 환경 메모

- 브랜치: `claude/meth-076-pm-plan-guide-refresh` (fresh main 기준). main 직접 PR. branch-first 준수.
- 변경: `20_guides/15_프로젝트_관리_기획서_작성_지침.md`(§6·§8·§16·§19) + `20_guides/README.md` + 라이브 4종.
- 진척: 063~071 템플릿+072 sync(#61)+073 운영(#62)+074 마케팅(#63)+075 브랜드(#64)+**076 PM(이번)**. 지침군 남음: 16·17.
