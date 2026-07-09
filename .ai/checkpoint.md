# Checkpoint — 2026-07-09 (METH-069 도메인 용어집 심화 · 유비쿼터스 언어 + SKOS)

> ✅ METH-069: 문서별 심화 7번(기획 템플릿 계열 마지막) = context-glossary. 웹리서치(DDD·SKOS·AI 그라운딩) → 유비쿼터스 언어 계약으로 재정의.
> 핵심: 표준어가 **코드·UI에 그대로 흐름**(사전 아님) · 같은 단어 맥락별 다른 뜻은 **바운디드 컨텍스트로 분리**(false unification 금지).
> 🏁 다음: PR 리뷰·머지 → 심화 계속(개발명세 또는 기획서 지침군) 또는 누적 다운스트림 sync.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-069-context-glossary-refresh` (fresh main 기준, branch-first 규율 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-069 — 도메인 용어집(context-glossary.md) 심화** (문서별 심화 프로그램 7번, 기획 *템플릿* 계열 마지막):

- **방법**: 웹리서치 1차 소스(Evans DDD Reference·Fowler·Agile Alliance·W3C SKOS·DataHub/Atlan glossary 표준·2026 AI 그라운딩 arXiv 2편). 현행(표준어+정의+`_Avoid_`+혼동쌍+예시대화) gap.
- **위상 재정의**: 사전이 아니라 **유비쿼터스 언어(DDD) 계약** — 표준어가 대화·문서·UI·테스트·**코드에 그대로**. SKOS 매핑(표준어=prefLabel·동의어=altLabel·`_Avoid_`=hiddenLabel).
- **변경 (`50_resources/templates/context-glossary.md`)** — 전부 *용어당 선택*(소규모 최소형 유지):
  - **바운디드 컨텍스트** 섹션 — 같은 단어 맥락별 다른 뜻(Fowler meter/Customer/Order), false unification 금지, 컨텍스트 태그로 중복 등재 허용.
  - **상태(Draft/Approved/Deprecated)/Owner** 메타, **See also**(skos:related, 혼동쌍과 구분).
  - **Code/UI 식별자 매핑**(`OrderLine`/"주문 항목") — 유비쿼터스 언어의 핵심 + 린트 타깃.
  - **약어** 표 — 다의어 약어의 AI 오해석 위험 → 고정.
  - **AI 스티어링 훅**(CLAUDE/AGENTS/llms.txt 링크 = 그라운딩) + **린트 훅**(`_Avoid_` = Vale/CI 가드레일).
  - _CATALOG 한줄 갱신.

## 다음 사람에게 (구체적 첫 행동)

1. METH-069 PR 리뷰·머지.
2. **문서별 심화 계속** — 대상 합의. 기획 *템플릿* 계열은 069로 일단락(prd·requirements·user-story·service-policy·ia·user-flow·functional·wireframe·api·microcopy·kpi·context-glossary 모두 최신화). 남은 축: **개발명세**(`architecture`·`data-model`), **기획서 지침군**(운영 12·마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17), **agency/ops 템플릿**(proposal·qa·operation 등).
3. **누적 심화(063~069)를 다운스트림에 일괄 sync** — 여러 PR 쌓였으니 세트로.
4. METH-060 잔여(ai-icons 번호 정리 등).

## 미해결 결정사항 (Open Questions)

- 067 PRD main 직접 커밋(A) — 라이브 "PR 대기" 문구는 068에서 정정 완료.
- 심화 다운스트림 sync 타이밍(세트로 한 번).
- 심화 템플릿군 lean 유지 — context-glossary는 추가분 전부 용어당 선택이라 최소형 보존됨. 지속 점검.

## 환경 메모

- 브랜치: `claude/meth-069-context-glossary-refresh` (fresh main 기준). main 직접 PR. branch-first 규율 준수.
- 변경: `50_resources/templates/context-glossary.md`(재작성) + `_CATALOG.md`(한줄) + 라이브 4종.
- 문서별 심화 진척: 063#53·064#54·065#55·066#56 머지 / 067 PRD main직접(A) / 068 kpi-tree #57 머지 / 069 context-glossary(이번).
