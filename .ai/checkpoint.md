# Checkpoint — 2026-07-09 (METH-070 아키텍처 문서 심화 · arc42 + C4 + fitness functions)

> ✅ METH-070: 문서별 심화 8번(개발명세 계열 시작) = architecture. 웹리서치(arc42·C4·fitness functions·OWASP·AI 게이트웨이) → 강화.
> 핵심: **품질 속성 top3(least-worst) + fitness function(CI 강제)** · C4 다이어그램 · 신뢰경계/위협 · AI 아키텍처(조건부).
> 🏁 다음: PR 리뷰·머지 → 심화 계속(data-model 또는 기획서 지침군) 또는 누적 다운스트림 sync.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-070-architecture-refresh` (fresh main 기준, branch-first 규율 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-070 — 아키텍처 문서(architecture.md) 심화** (문서별 심화 프로그램 8번, 개발명세 계열 시작):

- **방법**: 웹리서치 1차 소스(arc42·C4/Simon Brown·Richards&Ford Fundamentals·ThoughtWorks fitness functions·OWASP STRIDE·Fairbanks·LLM 게이트웨이 2025-26). 현행 14섹션을 **arc42 12섹션에 매핑**해 gap 도출(crosscutting concepts는 이미 강함; 빠진 것 = 품질요구·런타임뷰·배포뷰·리스크).
- **변경 (`50_resources/templates/architecture.md`)** — 14→21 섹션, 각 compact:
  - **§2 품질 속성 우선순위 top3** — least-worst, 도메인 근거·측정 시나리오·트레이드오프·의도적 제외.
  - **§16 적합성 함수** — 특성→지표→검사(도구)→임계→CI 위치. 지침19 가드레일과 연결.
  - **§4 목표 아키텍처 = C4**(Context+Container, Mermaid diagrams-as-code). §6 **런타임 뷰**(핵심 시나리오 sequence).
  - **§11 신뢰경계·위협**(STRIDE-lite, 경계별; 완화는 §8 권한·§9 멱등 재사용). **§14 배포 뷰**.
  - **§15 AI 아키텍처**(조건부) — 게이트웨이/라우터·폴백·RAG·가드레일/eval 배치·비용·지연 예산 → 16/17·prd §9 링크.
  - **§20 리스크/기술부채 register** — §21 미해결 *결정*과 구분.
  - 프리앰블: risk-driven "just enough" + 이 문서+ADR+diagrams-as-code = AI 에이전트 컨텍스트.
  - _CATALOG 한줄 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-070 PR 리뷰·머지.
2. **문서별 심화 계속** — 대상 합의. 개발명세 남은 것: **`data-model`**(ERD·정규화·마이그레이션·인덱싱). 그 외: 기획서 *지침*군(운영 12·마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17), agency/ops 템플릿(proposal·qa·operation·profitability 등).
3. **누적 심화(063~070)를 다운스트림에 일괄 sync** — 여러 PR 쌓였으니 세트로(적용 프로젝트 반영).
4. METH-060 잔여(ai-icons 번호 정리 등).

## 미해결 결정사항 (Open Questions)

- 067 PRD main 직접(A) — 라이브 문구 068에서 정정 완료.
- 심화 다운스트림 sync 타이밍(세트로).
- architecture가 21섹션으로 커짐 — 각 compact(표1개/블록1개)이고 다수 조건부(AI·규제·배포)라 lean-mode에선 해당분만. 실사용에서 무거우면 arc42 "risk-driven 생략" 원칙대로 스킵 안내.

## 환경 메모

- 브랜치: `claude/meth-070-architecture-refresh` (fresh main 기준). main 직접 PR. branch-first 준수.
- 변경: `50_resources/templates/architecture.md`(재작성) + `_CATALOG.md`(한줄) + 라이브 4종.
- 문서별 심화 진척: 063#53·064#54·065#55·066#56·068#57·069#58 머지 / 067 PRD main직접(A) / 070 architecture(이번). **기획 템플릿 계열 완료 → 개발명세 계열 진입.**
