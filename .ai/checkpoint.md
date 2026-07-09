# Checkpoint — 2026-07-09 (메타/dev 지침 심화 배치 — METH-092 guide 03)

> ✅ METH-092: guide 03(관찰 로그) 심화 — `observe` CLI 정본화 + friction 캡처 규칙 + 학습루프 파이프라인 명시.
> 🔄 진행 중 배치(사용자 "전부"): 06·07·08 웹리서치 **3건 전부 도착**(아래 요약) → 093으로 반영 예정. 이후 094=05·09+02/19/20 경량.
> 🏁 리서치 결과 요약은 이 파일 하단 "리서치 요약" 참조 — 다음 세션이 093을 이어서 하면 됨.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-092-guide03-observation-deepen` (main tip 기준, branch-first)

## 부팅 계약

1. Read `.ai/context.json`. 2. `must_read` 순서대로. 3. `last_session.checkpoint_file`(이 파일) 즉시 인계. 4. "다음 사람에게" 첫 항목부터.

## 방금 한 것 (정확히)

**메타/dev 지침(02~09·19~20) 심화 배치** — 사용자 "전부". 계획: 092=guide 03(완료), 093=06·07·08(리서치), 094=05·09+02/19/20 경량. (02/19/20은 이미 성숙 → 경량 확인만.)

- **METH-092(완료)**: guide 03. §5 수동 cat→`observe` CLI 정본화(cat 금지=wrap fail·헌법 §2④)+`--friction` positional(where\|cost\|resolution\|repeat_of)·캡처 규칙. §6 학습 파이프라인+catalog/skeleton 교차링크. v2 이력.

## 다음 사람에게 (구체적 첫 행동)

1. METH-092 PR 리뷰·머지.
2. **METH-093 — guide 06·07·08 심화**(웹리서치 3건 이미 수행, 요약 하단). 각 guide에 반영:
   - **06 컴팩션**: safest-first drop(raw tool output 먼저)·aggressive 위험 인용·임계치(harness ~95%/proactive ~60%)·scoped rule 재anchor·auto-survive 명시(파일 재읽기·CLAUDE.md 재주입)·post-compaction 검증·subagent isolation 교차링크(08)·API vs Claude Code 2층 모델.
   - **07 자율/정지**: 이중 예산(runtime turns/USD + declared files/PR; "SDK 기본 무제한" 경고)·6 circuit breaker·ground-truth 진척(self-report 금지)·ask→clarify→escalate 사다리(over-asking도 실패)·"confirm before irreversible"=Class C 연결·stop report=ResultMessage 형태·budget 재선언 전 checkpoint·build/eval 분리.
   - **08 서브에이전트**: fan-out(read/search/verify) vs single-writer(coupled generation, Cognition)·sizing heuristic(1/2-4/10+)·delegation 계약 필드(objective+output+boundaries)·per-subagent model/effort·concurrency 3-5 cap·LLM-judge completeness rubric·artifact/external-memory 집계·Workflow 스케일 escape+"복잡도는 이득 있을 때만".
3. **METH-094 — 05·09 내부 정합 + 02/19/20 경량**(변경이력 신설 등, 필요 시).
4. 다른 repo(별도 세션): ai-icons 92 환류·talmo-com 실작업.

## 리서치 요약 (093 원료 — 1차 소스)

- **06**: Anthropic context-engineering/harness, Claude Code compaction(~95-98% auto; API 150k trigger). 핵심: 파일 flush 먼저·smallest high-signal·JIT 포인터·context rot·safest drop=tool output·subagent isolation.
- **07**: Anthropic Building Effective Agents/agent-loop(max_turns·max_budget_usd 기본 무제한)/harness/measuring-autonomy. 핵심: 이중 예산·ground truth·ask-vs-act·irreversible gate=Class C·ResultMessage stop report.
- **08**: Anthropic multi-agent research(15× 토큰·3-5 병렬·sizing)/Building Effective Agents·Cognition single-writer. 핵심: breadth fan-out vs single-writer·context isolation·completeness critic·artifact memory·Workflow 스케일.

## 환경 메모

- 브랜치: `claude/meth-092-guide03-observation-deepen`. branch-first.
- 진척: …091 경로 sweep + **092 guide03(이번)**. 남은 배치: 093(06/07/08)·094(05/09/02/19/20).
