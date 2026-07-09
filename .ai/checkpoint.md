# Checkpoint — 2026-07-09 (METH-077 AI기능기획서 지침 심화 · 에이전트·MCP·RAG·컨텍스트 엔지니어링)

> ✅ METH-077: 기획서 지침군 5번째 = guide 16 AI기능기획서(AI-native ~2026-05). 웹리서치(Anthropic·MCP·RAGAS·OWASP LLM Top10) → §5에 7항목 신설(2026-05 이후 발전).
> 핵심: **workflow vs agent 게이트+정지조건 · MCP 통합계약 · RAG-eval(faithfulness) · constrained decoding · 컨텍스트 엔지니어링(context rot)·모델 적응 사다리 · OWASP LLM Top10 feature 패스**.
> 🏁 다음: PR 리뷰·머지 → 지침군 마지막 1개(평가·가드레일 17, 16과 짝) 또는 홀드 다운스트림 sync 재개.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-077-ai-feature-guide-refresh` (fresh main 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-077 — AI기능기획서 지침(guide 16, 413줄) 심화** (기획서 지침군 프로그램 5번째):

- **방법**: 웹리서치 1차 소스(Anthropic Building Effective Agents·effective context engineering·MCP 스펙 2025·OpenAI structured outputs·RAGAS·OWASP LLM Top10 2025). 이 지침은 AI-native지만 ~2026-05 작성이라 그 이후 발전이 gap.
- **변경 (`20_guides/16_AI_기능_기획서_작성_지침.md`)** — §5 신규 7항목:
  - **§5.15 에이전트 아키텍처** — workflow vs agent 게이트(고정흐름=워크플로우, 동적일 때만 에이전트)·loop 패턴(ReAct/plan-execute/reflection)·**정지조건**(iter/tool/토큰 캡·no-progress·에스컬레이션)=LLM10 방어·지침07 feature판.
  - **§5.16 에이전트 메모리** — short(컨텍스트)/long(벡터·파일)·TTL·메모리 PII.
  - **§5.17 MCP 통합** — tools/resources/prompts·OAuth(RFC 8707)·스코프·tool 응답=미신뢰(LLM01).
  - **§5.18 RAG 설계+RAG-eval** — chunking/임베딩/하이브리드/rerank·grounding/citation·RAGAS(context precision/recall·faithfulness·answer relevancy)·agentic RAG.
  - **§5.19 구조화 출력 메커니즘** — JSON Schema·constrained decoding·strict function calling·실패 계약(LLM05).
  - **§5.20 컨텍스트 엔지니어링 + 모델 적응 결정트리** — prompt caching·compaction·context rot·프롬프트→RAG→FT→추론 사다리(RAG-first).
  - **§5.21 OWASP LLM Top10 2025** feature-level 위협 체크(조직 카탈로그는 17).
  - §7 목차·§15.2 환류·README §3.4 갱신. 상호 배선(정지조건↔LLM10·MCP↔LLM01·grounding↔LLM09·구조화출력↔LLM05).

## 다음 사람에게 (구체적 첫 행동)

1. METH-077 PR 리뷰·머지.
2. **기획서 지침군 심화 완료** — 마지막 = **평가·가드레일(17)**. 16(feature 인스턴스)의 org 카탈로그 짝 — eval 메트릭·LLM-as-judge·골든셋·4-카테고리 가드·EU AI Act·인간 게이트 표준. 현행 정독 후 gap(judge bias·agent trajectory eval·NIST AI RMF·EU AI Act GPAI 등) 판단.
3. **홀드 다운스트림 sync 재개** — ai-icons·cafe24-renewal·icons-invest clean 후. 073~077 지침 심화분 포함.

## 미해결 결정사항 (Open Questions)

- 17까지 완료 후 지침 심화 누적분(073~078)을 다운스트림에 sync할 타이밍.
- 지침 항목 증가 — lean 위해 조건부/기존절 보강으로 관리 중.

## 환경 메모

- 브랜치: `claude/meth-077-ai-feature-guide-refresh` (fresh main 기준). main 직접 PR. branch-first 준수.
- 변경: `20_guides/16_AI_기능_기획서_작성_지침.md`(§5·§7·§15) + `20_guides/README.md` + 라이브 4종.
- 진척: 063~071 템플릿+072 sync+073~076 지침(운영·마케팅·브랜드·PM, #62~#65)+**077 AI기능(이번)**. 지침군 남음: 17.
