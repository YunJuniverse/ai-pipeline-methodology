# Checkpoint — 2026-07-09 (METH-079 오케스트레이션 지침 라우팅 갱신)

> ✅ METH-079: 라우터(guide 01)에 12~17 심화(073~078) 신규 영역 반영. 내부 정합성 작업(리서치 없음).
> 핵심: §5.9 신규 영역 라우팅 표 + **AI 주제 경계 disambiguation**(brand in AI[14]/GEO[13]/AI기능[16], 에이전트 기능[16]/작업관리[15]/장애[12], feature[16]/org[17]) · §5.10 모드·템플릿 라우팅.
> 🏁 다음: PR 리뷰·머지 → 남은 후보(agency/ops 템플릿·메타 지침) 또는 **누적 다운스트림 sync(073~079)**.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-079-orchestration-guide-refresh` (fresh main 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-079 — 오케스트레이션 지침(guide 01) 라우팅 갱신** (사용자 지적: 라우터가 심화된 12~17을 아직 모름):

- **성격**: *내부 정합성* — 웹리서치 없음. 12~17 심화(073~078)·신규 템플릿(api-contract)·신규 모드(planning-handoff)를 라우터에 반영.
- **변경 (`20_guides/01_AI_기획_오케스트레이션_지침서.md`)**:
  - **§5.9 2025-26 신규 영역 라우팅 표** — SLO/인시던트/AI운영→운영12 · GEO/AEO/MMM/growth loop→마케팅13 · DBA/Share of Search/brand in AI→브랜드14 · 딜리버리/DORA/OKR/에이전트 거버넌스→PM15 · MCP/RAG/구조화출력→AI기능16 · NIST/ISO/레드팀→평가17.
  - **AI 주제 경계 disambiguation**(핵심): brand in AI 답변[14] vs GEO/AEO[13] vs AI기능 설계[16] / 에이전트 *기능설계*[16] vs 에이전트 *작업관리*[15] vs *장애·가드위반 대응*[12] / feature eval·guard 인스턴스[16] vs 조직 카탈로그[17].
  - **§5.10 모드·템플릿 라우팅** — 01은 기획서 라우팅이 본령, 모드(planning-handoff 등)·템플릿(api-contract 등)은 _CATALOG(§1)·지침21이 정본.
  - §5.7 키워드(MCP·구조화출력·컨텍스트 엔지니어링) · §18.1 빠른 분류 체크리스트 포인터.
  - graph.json 노드 누락(guide 02~09·19~21) 발견 → Open Issue(별건, 대시보드 렌더 영향 확인 후).

## 다음 사람에게 (구체적 첫 행동)

1. METH-079 PR 리뷰·머지.
2. **문서별 심화 프로그램 현황**: 템플릿 13종(063~071)·서비스기획서 부모/자식·기획서 지침군 6종(073~078)·오케스트레이션(079) 완료. 남은 후보 — agency/ops 템플릿(proposal-go-nogo·qa-*·operation-spec·post-launch-monitoring·profitability-sheet·execution-plan·work-request-ticket·wbs·glossary), 메타/dev 지침(00·02~09·18~20). 사용자와 합의.
3. **누적 다운스트림 sync(2차)** — gamblescan·icons는 072까지 반영 → **073~079 지침 심화분 추가 필요**. 홀드 3곳(ai-icons·cafe24·icons-invest)은 clean 후. (지침·가이드·_CATALOG가 shared_paths라 sync로 전파됨.)
4. **graph.json 노드 완성**(별건) — guide 02~09·19~21 추가, 대시보드 렌더 확인.

## 미해결 결정사항 (Open Questions)

- 심화 프로그램을 여기서 일단락할지(핵심 문서군 완료) vs agency/ops·메타 지침까지 이어갈지 — 사용자 판단.
- 2차 다운스트림 sync 타이밍(073~079 누적).

## 환경 메모

- 브랜치: `claude/meth-079-orchestration-guide-refresh` (fresh main 기준). main 직접 PR. branch-first 준수.
- 변경: `20_guides/01_AI_기획_오케스트레이션_지침서.md`(§5.7·§5.9·§5.10·§18.1) + 라이브 4종. (graph.json 미변경 — 별건.)
- 진척: 063~071 템플릿+072 sync(#61)+073~078 지침군(#62~#67)+**079 오케스트레이션(이번)**.
