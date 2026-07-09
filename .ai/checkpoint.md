# Checkpoint — 2026-07-09 (메타/dev 지침 심화 배치 — 093 완료)

> ✅ 배치 진행: 092(guide 03)·**093(guide 06·07·08 웹리서치 심화)** 완료. 남음: **094 = 05·09 내부정합 + 02/19/20 경량**.
> 🏁 다음 세션이 094를 이어서 하면 배치 완결. 이후 남은 건 전부 Low·선택(graph.json·v3.2 코드) 또는 별도 repo(ai-icons 92 환류·talmo-com).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-093-agent-mechanics-deepen` (#81 위 스택, branch-first)

## 부팅 계약

1. Read `.ai/context.json`. 2. `must_read` 순서대로. 3. `last_session.checkpoint_file`(이 파일) 즉시 인계. 4. "다음 사람에게" 첫 항목부터.

## 방금 한 것 (정확히)

**메타/dev 지침(02~09·19~20) 심화 배치** — 사용자 "전부".

- **092(완료, PR #81)**: guide 03(관찰 로그). observe CLI 정본화 + friction 캡처 + 학습루프 파이프라인. v2.
- **093(완료, 이 브랜치)**: guide 06·07·08 웹리서치 심화. 각 §SOTA 보강 섹션 + v2 이력:
  - **06 컴팩션**: 두 층 모델(하네스 ~95% / API 150k)·proactive ~60%·auto-survive 명시(파일 재읽기·CLAUDE.md 재주입→포인터 안전)·⚠️paths-scoped rule/nested CLAUDE.md는 재주입 안 됨→re-anchor·safest-first 폐기(raw output 먼저)·post-compaction 검증·subagent isolation=공간축.
  - **07 자율/정지**: 이중예산(runtime turns/USD[SDK 기본 무제한 경고] + declared scope)·6 circuit breaker(①②⑤만 SDK enforced)·ground-truth 진척(self-report 금지)+build/eval 분리·ask→clarify→escalate(over-asking도 실패)·비가역=Class C 정지·stop report(ResultMessage: 사유+예산소비+검증+남은것+resume handle)·재선언 전 checkpoint.
  - **08 서브에이전트**: fan-out(read/search/verify) vs single-writer(coupled generation, Cognition)·sizing(1/2-4/10+)·위임 계약 필드(목표+출력+경계, 프롬프트가 유일 채널)·per-subagent model/effort·concurrency 3-5 cap·completeness critic rubric·artifact 외부메모리 집계·[CC] Workflow 스케일 escape+"복잡도는 이득 있을 때만".

## 다음 사람에게 (구체적 첫 행동)

1. METH-092(#81)·093 PR 리뷰·머지.
2. **METH-094 — 05·09 내부 정합 + 02/19/20 경량**(배치 마무리):
   - **05 산출물 채널 분리**(127줄): 내부 규칙, 이미 적정 — 변경이력 신설 + (필요 시) grep 시그니처·AI 답변 채널 등 경량 보강.
   - **09 기획 핸드오프 재포맷**(87줄): 내부 규칙, planning-handoff 모드와 정합 확인 + 변경이력.
   - **02/19/20**: 이미 성숙 → 변경이력 유무만 확인, 실질 보강 최소(재심화 낭비 회피).
3. 남은 것(전부 Low·선택): graph.json 노드(02~09·19~21)·v3.2 backward-compat 코드 정리. 다른 repo(별도 세션): ai-icons 92 환류·talmo-com 실작업.

## 미해결 결정사항 (Open Questions)

- 메타/dev 배치를 094까지 하면 문서별 심화 프로그램 사실상 전종 완료. 이후 방법론 정비는 일단락 지점.

## 환경 메모

- 브랜치: `claude/meth-093-agent-mechanics-deepen` (#81 위 스택). branch-first.
- 진척: …091 sweep + 092 guide03(#81) + **093 guide06/07/08(이번)**. 남은 배치: 094(05/09/02/19/20).
