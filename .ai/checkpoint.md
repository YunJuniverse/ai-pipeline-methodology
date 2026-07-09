# Checkpoint — 2026-07-09 (METH-068 KPI 단위경제 트리 심화)

> ✅ METH-068: 문서별 심화 6번 = kpi-tree. 웹리서치(a16z·Bessemer·Amplitude) → 마켓플레이스 GMV 워터폴을 단위경제·리텐션·자본효율·드라이버 트리로 확장.
> 핵심: **마진 워터폴(돈이 어디로)과 드라이버 트리(어떤 레버가 결과를)는 상보 — 혼동 금지**. gross-margin LTV·gross-margin payback.
> 🏁 다음: PR 리뷰·머지 → 문서별 심화 계속(대상 선정).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-068-kpi-tree-refresh` (fresh main 기준, branch-first 규율 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-068 — KPI 단위경제 트리(kpi-tree.md) 심화** (문서별 심화 프로그램 6번):

- **방법**: 웹리서치 서브에이전트 1차 소스(a16z·Bessemer·David Skok·Reforge·Amplitude·Benchmarkit·SaaS Capital) — 현행(마켓플레이스 GMV→CM 워터폴 + 고정/변동비) gap. 지침 10 §19.11(마켓 10-패널·AAARR·LTV/CAC 벤치)은 *중복 안 하고 링크*.
- **변경 (`50_resources/templates/kpi-tree.md`)**:
  - **§1 비즈모델 top-line 토글** — 마켓(GMV×take)/구독(MRR 브리지→ARR)/거래(주문×AOV)/사용량(활성×사용×단가) → 공통 Gross→Contribution 워터폴.
  - **§2 단위경제** — CAC · **gross-margin LTV**(매출-LTV 아님) · LTV:CAC(3:1 하한·3~5 스윗·**>5 과소투자**) · **CAC payback**(GM 기준) · CM/단위.
  - **§3 리텐션** — NRR(≥100/엘리트120)·GRR(~90)·로고vs매출 churn·코호트 평탄=PMF.
  - **§4 자본효율** — Rule of 40·Burn Multiple(<1~>3 스케일)·Magic Number·Quick Ratio.
  - **§5 원가 + AI COGS** — 추론/토큰비=변동 COGS·**AI GM 50~60%**(SaaS 80%+ 복붙 금지)·CPAU·워크플로우당 CM·추론비 연 10x 하락.
  - **§6 드라이버 트리** — North Star = 입력레버 곱(선행), *마진 워터폴과 상보·혼동 금지* 명시.
  - 벤치마크 스트립(what-good 2025-26) + _CATALOG 한줄 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-068 PR 리뷰·머지.
2. **문서별 심화 계속** — 대상 합의. 기획 계열 남은 것: `context-glossary`. 다른 기획서 지침(운영 12·마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17). 개발명세(`architecture`·`data-model`).
3. 심화 산출물 실사용 시 실전 예를 지침 §19 craft로 환류.
4. **누적 심화(063~068)를 다운스트림에 일괄 sync** 검토 + METH-060 잔여(ai-icons 번호 정리 등).

## 미해결 결정사항 (Open Questions)

- 067 PRD는 main 직접 커밋(A로 수습) — 라이브 파일에 "PR 대기"로 남은 문구는 본 커밋(068)에서 정정됨.
- 문서별 심화 누적 PR을 다운스트림에 세트로 sync할 타이밍.
- kpi-tree가 §1~7로 커짐 — 각 섹션 표 1개 유지로 lean 근접. 실사용에서 무거우면 자본효율/드라이버 트리를 옵션 분리 검토.

## 환경 메모

- 브랜치: `claude/meth-068-kpi-tree-refresh` (fresh main 기준). main 직접 PR. **branch-first 규율 준수**(067 사고 후 메모리 `branch-first-discipline` 반영).
- 변경: `50_resources/templates/kpi-tree.md`(재작성) + `_CATALOG.md`(한줄) + 라이브 4종.
- 문서별 심화 진척: 063#53·064#54·065#55·066#56 머지 / 067 PRD main직접(A) / 068 kpi-tree(이번).
