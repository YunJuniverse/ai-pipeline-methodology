# Checkpoint — 2026-07-10 (METH-101 부팅 강제 + 비대화 린트)

> ✅ **METH-101**: ai-icons 새 세션 부팅 실패 사고의 상류 진단·수정. `methodology.py boot` 명령 신설 + wrap 사이즈 린트(HANDOFF>150·checkpoint>200·Done>6) + CLAUDE/AGENTS 부팅 의무를 boot 실행으로 정본화. Class A(7 repo 전파).
> 🧭 **base=main 단일 PR** (095~100은 #84·#89로 이미 머지 완료 — 이번엔 스택 아님). py_compile·boot 실행·린트 발화 검증.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-101-boot-cmd-size-lint` (updated main 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것
**METH-101 — 부팅 강제 + 라이브 파일 비대화 방지.** ai-icons 새 세션이 부팅을 건너뛰고 기존 프로세스를 모른 채 시작(오답까지)한 사고의 **상류 원인 진단·수정**:
- **진단**: 방법론 고장 아님·기록 유실 아님(규칙·316 obs·checkpoint·TODO·git 다 있음, 규칙도 downstream managed block에 있음). 원인 2개 — ① 부팅 의무가 **강제 없는 서술 텍스트**뿐(wrap/ship은 세션 *종료*만 sha로 검증, *시작*은 무방비, boot 명령 없음) ② **라이브 파일 비대화 무통제**(wrap이 sha만 보고 *사이즈 안 봄* → ai-icons HANDOFF 81KB·checkpoint 421KB·TODO 361KB; 비대한 HANDOFF은 "기본 부팅 컨텍스트=CLAUDE+HANDOFF" 설계를 무력화 → 잘 부팅해도 포커스가 노이즈에 묻힘).
- **수정(사용자 "둘 다" 승인)**:
  - (A) **`methodology.py boot` 명령 신설**(cmd_boot) — 세션 시작 시 브리프 목록·HANDOFF 포커스·checkpoint 요지·사이즈 경고·dashboard URL을 한 번에. 부팅 계약을 실행 명령으로 격상.
  - (B) **wrap 사이즈 린트** — `live_file_size_warnings(target)` 공용 헬퍼(HANDOFF>150·checkpoint>200·TODO Done>6 경고). **실패 아님**(이미 초과된 7 repo의 ship 안 막음) + boot에서도 재사용.
  - CLAUDE/AGENTS managed block: 부팅 의무를 `boot` 실행으로 정본화 + "IR·작업 질문에 바로 뛰어들지 말 것" + wrap 규칙에 비대화 경고 명기(두 파일 동일 편집).
- 검증: py_compile · `boot` 실행(5개 섹션 출력) · 사이즈 린트 발화(300줄 HANDOFF→2.0× 경고 3건).

## 다음 사람에게
1. **METH-101 PR(base=main) 머지** — boot 명령 + 사이즈 린트가 7 repo로 전파. 이후 각 repo 세션은 `methodology boot`로 시작.
2. **ai-icons(별도 세션)**: 비대 라이브 파일(HANDOFF 81KB·checkpoint 421KB·TODO 361KB) 트리밍 — 101 린트가 지목할 것. 오래된 내용 git·snapshots로 이관하고 요지만.
3. 079~101 점검·정합·구조·전파·정비 사이클 **종료**. 다른 repo: ai-icons 92 환류·talmo-com.

## 환경 메모
- 브랜치: `claude/meth-101-boot-cmd-size-lint` (updated main 기준). branch-first. 이번엔 스택 아님(095~100 이미 머지).
- 진척: 메타/dev(092-094) + agency/ops(095-098) + graph(099) + v3.2 compat(100) + **부팅강제+비대화린트(101)**. 사이클(079~101) **종료**.
