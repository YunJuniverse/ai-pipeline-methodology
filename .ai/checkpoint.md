# Checkpoint — 2026-07-10 (METH-103 상시 SOP 쓰기 트리거)

> ✅ **METH-103**: 반복작업 SOP의 *쓰기* 규칙 신설 — "기억해줘/반복작업이야" → `standing/SOP_*` 박제를 operating rule로. 102는 읽기만 완비했던 구멍을 닫음. Class A(7 repo).
> 🧭 base=main 단일 PR (095~102 = #84·#89·#91 머지 완료, 스택 아님).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-103-standing-write-trigger` (updated main 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
**METH-103 — 상시 SOP 쓰기 트리거 규칙.** 사용자 질문("반복작업으로 기억해줘 하면 진짜 반복작업으로 기억하나?")에서 도출:
- **진단**: 102가 standing SOP의 *읽기*(boot이 ★ 노출·착수 전 확인 규칙)만 완비했고, *쓰기* 반사신경 = "요청 시 SOP 작성"이 operating rule로 없었다. 즉 선반은 놨는데 "얹어라"가 규칙에 없어 보장 안 됨.
- **수정**: CLAUDE/AGENTS managed block(§2)에 **"반복 작업 기억 (요청 시)"** 규칙 신설 — 사용자가 "기억해줘/이건 반복(정기) 작업이야" → `00_briefs/standing/SOP_<topic>.md` 박제(`SOP_template.md` 형식), 절차 변경 감지 시 갱신 제안. **구분 명기**: 반복 *작업 절차*=repo standing SOP(팀 공유·boot 노출) / 사용자 개인 선호·사실=도구 메모리(별개). `00_briefs/_README §5`도 반영.
- 검증: managed block 동일(self-ref만 차이) · 두 파일에 규칙 1건씩.

## 다음 사람에게
1. **METH-103 PR(base=main) 머지** — 쓰기 트리거가 7 repo 전파. 이후 "반복작업 기억해줘"가 실제로 standing SOP를 만든다.
2. **ai-icons(별도 세션)**: 이제 "업무기술서 처리를 반복작업으로 기억해줘" 하면 `standing/SOP_worksheet-processing.md`가 생기고, 다음 세션 boot에서 ★로 뜬다 — 이번 사고 근본 종결. + 비대 라이브파일 트리밍(101 린트).
3. 방법론 부팅 개선 시리즈(101 boot·102 경계+상시브리프·103 쓰기트리거) 완결.

## 환경 메모
- 브랜치: `claude/meth-103-standing-write-trigger` (updated main). branch-first. #91까지 머지 완료라 스택 아님.
- 누적 상태(오픈이슈·PR 목록)는 **HANDOFF 참조** — 여기 복제 안 함(경계 규칙 dogfooding).
- 진척: …+graph(099)+v3.2(100)+부팅(101)+경계/상시브리프(102)+**쓰기트리거(103)**.
