# Checkpoint — 2026-07-09 (METH-078 평가·가드레일 지침 심화 · 기획서 지침군 완결)

> ✅ METH-078: 기획서 지침군(12~17) 심화 **완결** = guide 17 org eval/guard 카탈로그. 웹리서치(NIST AI RMF·ISO 42001·EU AI Act GPAI·G-Eval·RAGAS·OTel GenAI·Garak) → 8항목 신설.
> 핵심: judge는 편향(순서스왑·calibration 게이트) · 에이전트는 *경로* 평가 · 거버넌스 3축(EU법+NIST방법+ISO경영) · 레드팀 배포전 게이트 · OTel GenAI 표준.
> 🏁 다음: PR 리뷰·머지 → 문서별 심화 프로그램 대부분 완료. 남은 후보(agency/ops 템플릿·메타 지침) 또는 누적 다운스트림 sync.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-078-eval-guardrail-guide-refresh` (fresh main 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-078 — 평가·가드레일 지침(guide 17, 316줄) 심화** = 기획서 지침군 프로그램 **완결(12~17)**:

- **방법**: 웹리서치 1차 소스(MT-Bench/G-Eval·RAGAS·NIST AI RMF AI 100-1+GenAI Profile AI 600-1·ISO/IEC 42001·EU AI Act GPAI Code of Practice·OpenTelemetry GenAI semconv·Garak/PyRIT). org 카탈로그(~2026-05) gap.
- **변경 (`20_guides/17_평가_및_가드레일_지침.md`)**:
  - **§3.7 LLM-judge bias & 완화** — position/verbosity/self-preference/sycophancy 표 + 순서스왑·pairwise·G-Eval·**calibration 게이트**(κ 미달 시 CI 사용금지)·judge 버전 pin·불신 조건.
  - **§3.8 에이전트/trajectory eval** — task성공·tool-call 정확성·trajectory·비용, (state,action) judge 기하평균, 3레벨.
  - **§3.9 RAG 메트릭 카탈로그**(RAGAS 4종·검색vs생성 실패 진단) — 16 feature가 참조.
  - **§3.10 eval 데이터 위생**(오염·홀드아웃·버전·합성 검토).
  - **§4.4 EU AI Act GPAI 갱신**(2025.8 적용/2026.8 집행/2027.8 레거시·CoP 3장·Art.55·Art.50).
  - **§4.5 레드팀 pre-release 게이트**(Garak/PyRIT·finding→regression CI).
  - **§4.6 거버넌스 3축 매핑**(NIST Govern/Map/Measure/Manage+600-1·ISO 42001 AIMS·EU) — 최대 gap이었음.
  - **§6 OTel GenAI semconv 정렬**(gen_ai.* 속성·dual-emission).
  - §10 환류 + README §3.4 갱신. 16(feature)↔17(org) 경계 재확인.

## 다음 사람에게 (구체적 첫 행동)

1. METH-078 PR 리뷰·머지 → **기획서 지침군 12~17 심화 완결**.
2. **문서별 심화 프로그램 현황**: 템플릿 13종(063~071)·서비스기획서 부모/자식·기획서 지침군 6종(073~078) 완료. 남은 후보 — agency/ops 템플릿(proposal-go-nogo·qa-*·operation-spec·post-launch-monitoring·profitability-sheet·execution-plan·work-request-ticket·wbs·glossary), 메타 지침(00~09·18~20). 사용자와 다음 대상 합의.
3. **누적 다운스트림 sync** — 지침 심화분(073~078) + 홀드 3곳(ai-icons·cafe24·icons-invest) clean 후 재개. gamblescan·icons는 072까지 반영됨 → 073~ 추가 필요.

## 미해결 결정사항 (Open Questions)

- 지침 심화 완결 → 다운스트림 일괄 sync(2차) 타이밍. gamblescan·icons도 073~078 반영 필요.
- 남은 심화 대상(agency/ops·메타 지침)을 계속할지 여기서 일단락할지 — 사용자 판단.

## 환경 메모

- 브랜치: `claude/meth-078-eval-guardrail-guide-refresh` (fresh main 기준). main 직접 PR. branch-first 준수.
- 변경: `20_guides/17_평가_및_가드레일_지침.md`(§3·§4·§6·§10) + `20_guides/README.md` + 라이브 4종.
- 진척: 063~071 템플릿+072 sync(#61)+073~078 지침군 6종(운영·마케팅·브랜드·PM·AI기능·평가, #62~#66+이번). **기획서 지침군 완결.**
