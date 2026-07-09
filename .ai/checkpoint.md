# Checkpoint — 2026-07-09 (METH-099 graph 노드 보강 + 096~098 복구)

> ✅ **METH-099**: methodology-graph.json 노드 29→42(guide 10종+학습루프+checkpoint, stale ai-log 제거)·엣지 39→53·dashboard 렌더 검증. + **agency/ops 템플릿 12종(095~098) 완결.**
> ⚠️ **스택-PR 함정 복구**: #85/#86/#87이 main 아닌 중간 브랜치로 머지돼 096/097/098이 main 미반영이었음. 이 브랜치(095-098 온전) + 099를 **base=main 단일 PR**로 한 번에 복구. 교훈: 스택-PR 지양, main 직행.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-099-graph-nodes` (origin/claude/meth-097-... 기준=095-098 온전 보존, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것
**METH-099 — methodology-graph.json 노드 보강** (대시보드 관계 그래프, METH-079 Open Issue 종결):
- 노드 29→42: guide 10개(02·03·05·06·07·08·09·19·20·21; **04 미존재라 제외**) + 학습루프(ai_observations·catalog·skeletons) + checkpoint(핵심 라이브 누락분). **stale ai-log 노드 제거**(AI-LOG.md는 083서 삭제=dead).
- 엣지 39→53: g00 parent-of 메타룰 7 · g18→g21→g19/g20 dev트랙 · observe→catalog→skeleton 학습루프 · templates→checkpoint.
- tier6 "개발 트랙 규칙" 신설 · learning kind · v3.2. dashboard 재생성 렌더 검증(nodes=42) · JSON 정합(dangling/dup 0·경로 전부 존재·lifecycle g21 참조 해소).
- **부수 복구**: 스택-PR 함정으로 #85/#86/#87이 main 아닌 중간 브랜치로 머지돼 096/097/098이 main 미반영이던 것을 이 브랜치(095-098 온전)+099 = **base=main 단일 PR**로 복구.

**직전: agency/ops 템플릿 12종(095~098) 완결** — QA/수주/ops/glossary, 전부 lean 폼 + 지침 참조(SSOT). (096=go-nogo kill·SOW/BANT·PS gross/net·PMBOK WBS / 097=runbook SLO·골든시그널·ITIL 변경관리 / 098=glossary SSOT 경계)

## 다음 사람에게
1. **METH-099 PR(base=main) 머지** — 096+097+098+099 한 번에 반영. 머지 후 origin의 중간 스택 브랜치(095/096/097 deepen)는 정리(삭제) 가능.
2. 남은 후보(전부 Low·선택): v3.2 backward-compat 코드 정리(별건, dead 폴백).
3. 다른 repo(별도 세션): ai-icons 92 환류·talmo-com 실작업.
4. **교훈(반영됨)**: 스택-PR은 재타깃 취약 → 앞으로 **main 직행 단일 PR** 선호.

## 환경 메모
- 브랜치: `claude/meth-099-graph-nodes` (095-098 온전 보존 브랜치 기준). branch-first.
- 진척: 메타/dev 배치(092-094) + **agency/ops 배치(095-098) 완결** + **graph 노드 보강(099)**. 점검·정합·구조·전파·정비 사이클(079~099) 사실상 마무리.
