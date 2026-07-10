# Checkpoint — 2026-07-10 (METH-104 SOP 트리거 "인식 신호")

> ✅ **METH-104**: SOP 템플릿 트리거에 "인식 신호"(어떤 요청/말이 이 작업을 의미하는가) 항목 추가 — 반복작업 매칭이 문자열이 아닌 LLM 의미추론이라, 이 앵커로 매칭 신뢰도↑. SOP_template + _README §standing. Class A(7 repo).
> 🧭 base=main 단일 PR (095~103 = #84·#89·#91·#92 머지 완료, 스택 아님).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-104-sop-recognition-cues` (updated main 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
**METH-104 — SOP 트리거에 "인식 신호" 항목 추가.** 사용자 질문("반복작업 다시 하려면 키워드로 추론해서 알아서 하나?")에서 도출:
- **답/진단**: 문자열 키워드 엔진이 아니라 **LLM 의미추론**이다(boot이 SOP 로드 → 요청을 의미로 매칭 → 절차 따르되 SOP의 주의점·게이트 지킴). 신뢰도의 레버 = SOP 트리거가 "어떤 요청/말이 이 작업을 의미하는가"를 명시하는 것. 기존 템플릿 트리거는 *주기/이벤트*만 담아 이 앵커가 없었다.
- **수정**: `SOP_template.md` 트리거를 **인식 신호**(요청/말 앵커, 예: "업무기술서 확인해줘") + **주기/이벤트**로 분리. `00_briefs/_README §standing`의 "무엇을 담나"에 인식 신호 명시.
- 검증: 편집 2파일, 형식 확인.

## 다음 사람에게
1. **METH-104 PR(base=main) 머지** — SOP 템플릿 개선이 7 repo 전파.
2. **ai-icons(별도 세션)**: "업무기술서 처리를 반복작업으로 기억해줘" → SOP 작성 시 **인식 신호에 "업무기술서 확인/처리·회수함" 등 실제 사용자 문구**를 넣으면 다음 세션이 정확히 매칭. + 비대 라이브파일 트리밍(101 린트).
3. 방법론 부팅 개선 시리즈(101 boot·102 경계+상시브리프·103 쓰기트리거·104 인식신호) **완결**.

## 환경 메모
- 브랜치: `claude/meth-104-sop-recognition-cues` (updated main). branch-first. #92까지 머지 완료라 스택 아님.
- 누적 상태(오픈이슈·PR 목록)는 **HANDOFF 참조** — 여기 복제 안 함(경계 규칙 dogfooding).
- 진척: …+v3.2(100)+부팅(101)+경계/상시브리프(102)+쓰기트리거(103)+**인식신호(104)**.
