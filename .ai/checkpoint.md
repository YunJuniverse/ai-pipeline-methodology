# Checkpoint — 2026-07-09 (METH-075 브랜드기획서 지침 심화 · DBA·Share of Search·브랜드 in AI)

> ✅ METH-075: 기획서 지침군 3번째 = guide 14 브랜드기획서. 웹리서치(Dunford·Ehrenberg-Bass/Romaniuk·Binet·WCAG·소닉) → §6에 8항목 신설(§6.14~6.21).
> 핵심: **브랜드는 감성 문장이 아니라 (1)식별 자산(DBA fame×uniqueness) (2)측정(Share of Search) (3)AI 답변 속 인식 (4)기계판독 규칙(brand-as-code)**.
> 🏁 다음: PR 리뷰·머지 → 지침군 계속(PM 15·AI기능 16·평가 17) 또는 홀드 다운스트림 sync 재개.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-075-brand-plan-guide-refresh` (fresh main 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-075 — 브랜드기획서 지침(guide 14, 737줄) 심화** (기획서 지침군 프로그램 3번째):

- **방법**: 웹리서치 1차 소스(April Dunford Obviously Awesome·Play Bigger category design·Ehrenberg-Bass/Jenni Romaniuk DBA·Les Binet Share of Search·브랜드 아키텍처 4유형·W3C WCAG 2.2·소닉 브랜딩). 현행 §6(포지셔닝·페르소나·핵심가치·메시지 하우스·톤앤매너·비주얼·경험원칙·적용가이드·AI 페르소나·Style Guide as Code·AI 시각물 가드) gap.
- **변경 (`20_guides/14_브랜드기획서_작성_지침.md`)** — §6 신규 8항목:
  - **§6.14 Dunford 5요소 포지셔닝**(경쟁대안[phantom 금지]→고유속성→가치[So what]→세그먼트→카테고리) + 카테고리 창출(Play Bigger)=Class C 분기.
  - **§6.15 Distinctive Brand Assets** — fame×uniqueness 4분면 등록부·"로고 없이 성립"·contrast 설계.
  - **§6.16 브랜드 아키텍처(Branded House/House of Brands/Endorsed/Hybrid) + 버벌/네이밍**(tagline vs slogan·금칙어 lexicon).
  - **§6.17 브랜드 헬스** — 퍼널(인지→고려→선호→충성)·NPS·**Share of Search**(Binet, Google Trends 무료 선행지표).
  - **§6.18 브랜드 in AI 답변**(최우선) — AI 인식 감사(LLM이 브랜드를 어떻게 서술/인용). §6.13 생성통제와 다른 *인식 모니터링* 축.
  - **§6.19 brand-as-code 확장** — voiceProfile 4축(격식·에너지·따뜻함·복잡성)·promptLibrary·bodyOfWork.
  - **§6.20 WCAG 접근성** — 본문 4.5:1·큰텍스트/UI 3:1·상태별 승인 컬러쌍(style-as-code CI 가드).
  - **§6.21 모션·소닉** — 소닉 로고·모션 아이덴티티, DBA 등록부에 등재.
  - §8.1 목차·§16 체크리스트·§19.7 환류·README §3.2 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-075 PR 리뷰·머지.
2. **기획서 지침군 심화 계속** — PM(15)·AI기능(16)·평가(17). 같은 패턴(현행 §6/§19 고찰 → 웹리서치 → §6 신규 + §8/§16/§19/README).
3. **홀드 다운스트림 sync 재개** — ai-icons(dirty+커스텀 guide 충돌)·cafe24-renewal·icons-invest clean 후. 073~075 지침 심화분도 다음 sync에 포함.

## 미해결 결정사항 (Open Questions)

- 지침 §6 항목 증가(브랜드 13→21) — lean 위해 조건부(AI)·심화 레이어·기존절 보강으로 관리. 실사용 무게 재점검.
- 지침군 심화 누적분(073·074·075~)을 다운스트림에 sync할 타이밍.

## 환경 메모

- 브랜치: `claude/meth-075-brand-plan-guide-refresh` (fresh main 기준). main 직접 PR. branch-first 준수.
- 변경: `20_guides/14_브랜드기획서_작성_지침.md`(§6·§8·§16·§19) + `20_guides/README.md` + 라이브 4종.
- 진척: 063~071 템플릿+072 sync(#61)+073 운영(#62)+074 마케팅(#63)+**075 브랜드(이번)**. 지침군 남음: 15·16·17.
