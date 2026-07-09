# Checkpoint — 2026-07-09 (agency/ops 템플릿 심화 배치 — 완결)

> ✅ **agency/ops 템플릿(12종) 심화 배치 완결** — 095 QA 3 · 096 수주 5 · 097 ops 3 · 098 glossary 1. 전부 lean 폼 필드 보강 + 지침 참조(SSOT).
> 🏁 남은 것은 PR 4건(#84·#85·#86·098) 순차 머지뿐. 이후 이 배치 종료.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-098-glossary-template` (097 브랜치 위 스택, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것
**agency/ops 템플릿(12종) 심화 배치 — 완결.** 사용자 "전부 웹리서치 기반". 클러스터별 PR: 095=QA·096=수주·097=ops·098=glossary. 템플릿=**lean 폼**(essay 금지, 필드 완성도만) + 성숙 지침 재설명 없이 참조(SSOT).
- **098(완료)**: glossary.md(SI 단계별 용어규약집). **SSOT 경계 명시**(glossary=계약·산출물 표면 라벨 통일 / context-glossary=도메인 개념 canon·코드까지, 중복 금지·링크만) + 표준용어 표에 예시(용례)·상태(Approved/Deprecated) 열 + 관리자=분쟁 해결권자 + 폐기어 추적성.
- **097(완료)**: ops 3종. operation-spec(runbook §0 신뢰성 계약)·post-launch-monitoring(골든시그널+burn-rate)·work-request-ticket(티켓유형·P1-4·변경관리+Change Class).
- **096(완료)**: 수주 5종(go-nogo kill·SOW/BANT·PS gross/net·PMBOK WBS·Phase/Milestone).
- **095(완료)**: QA 3종(RTM 폐루프).

## 다음 사람에게 (배치 종료 — PR 머지만)
1. **PR 4건 순차 머지**: #84(095 QA) → #85(096 수주) → #86(097 ops) → 098 glossary. 스택이라 순서대로. 머지 후 이 배치 종료.
2. 남은 후보(전부 Low·선택): graph.json 노드(02~09·19~21) 보강, v3.2 backward-compat 코드 정리(별건).
3. 다른 repo(별도 세션): ai-icons 92 환류·talmo-com 실작업.

## 리서치 요약 (1차 소스)
- **수주**: Shipley bid/no-bid(5요인)·APMP 게이트(소유자+일자)·PMBOK WBS 100%룰·SOW discovery(BANT·exclusions·acceptance)·PS margin(gross40-60%·util75-80%·PMI contingency).
- **QA**(반영됨): ISO/IEC/IEEE 29119-3·ISTQB(entry/exit·severity≠priority)·RTM thin·BDD Gherkin 옵션.
- **ops**: Google SRE(runbook·SLO·burn-rate·on-call)·ITIL4(request/incident/change·priority matrix·change type)·OTel 골든시그널·DORA·LLM observability.

## 환경 메모
- 브랜치: `claude/meth-098-glossary-template` (097 위 스택). branch-first.
- 진척: 메타/dev 배치(092-094) 완결 + **agency/ops 배치(095-098) 완결 — 12종 전부**. PR 4건 순차 머지만 남음.
