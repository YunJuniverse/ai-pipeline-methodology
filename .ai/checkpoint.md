# Checkpoint — 2026-07-10 (METH-105 브리프 자동 분류·정리 체계)

> ✅ **METH-105**: 사용자가 브리프를 던지면 AI가 유형 판별해 폴더 배치. 유형 폴더(research/reference/ideas 신설 + meetings/standing) + `_README §자동 분류` 규칙표 + CLAUDE/AGENTS §2 규칙 + boot 유형별 그룹 노출. Class A(7 repo).
> 🧭 base=main 단일 PR (095~104 = #84·#89·#91·#92·#93 머지 완료, 스택 아님).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-105-brief-auto-filing` (updated main 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
**METH-105 — 브리프 자동 분류·정리 체계.** 사용자 요청("브리프 넣으면 니가 알아서 분류해 폴더 정리하는 체계 원함 — 회의→회의록, 리서치→리서치, 레퍼런스→레퍼런스"):
- **유형 폴더 정립**: 기존 meetings/·standing/ + **신설 research/·reference/·ideas/**. `current/`는 레거시(기존 repo 호환, boot이 읽음)·신규는 ideas/가 미분류 기본.
- **자동 분류 규칙**: `00_briefs/_README §자동 분류` 규칙표(회의→meetings / 조사·분석→research / 외부 원본·링크→reference / 아이디어·방향→ideas / 반복 절차→standing/SOP / 애매하면 사용자 확인). research vs reference = "내가 소화·정리"vs"외부 원본 날것". CLAUDE/AGENTS §2에 "브리프 자동 분류" operating rule(synced).
- **boot 개편**: [1]을 유형 폴더별 그룹으로 노출(standing ★ 최상단·archived 제외·template/_README 필터). 폴더 추가돼도 자동 인식(generic iterdir).
- MANIFEST init_paths에 research/reference/ideas 추가(current 제거). 검증: py_compile·boot 그룹 스캔(4폴더)·manifest·managed sync.

## 다음 사람에게
1. **METH-105 PR(base=main) 머지** — 브리프 분류 체계 7 repo 전파. 이후 브리프 던지면 AI가 유형별 폴더로 정리.
2. **ai-icons(별도 세션)**: boot으로 시작 → 회의/리서치/참고자료 던지면 자동 분류. 업무기술서 SOP는 standing/에. + 비대 라이브파일 트리밍.
3. 부팅·브리프 개선 시리즈(101 boot·102 상시브리프·103 쓰기트리거·104 인식신호·105 자동분류) **완결**.

## 환경 메모
- 브랜치: `claude/meth-105-brief-auto-filing` (updated main). branch-first. #93까지 머지 완료라 스택 아님.
- 누적 상태(오픈이슈·PR 목록)는 **HANDOFF 참조** — 여기 복제 안 함(경계 규칙 dogfooding).
- 진척: …+부팅(101)+상시브리프(102)+쓰기트리거(103)+인식신호(104)+**브리프 자동분류(105)**.
