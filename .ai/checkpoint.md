# Checkpoint — 2026-07-09 (agency/ops 템플릿 심화 배치 — 097 ops)

> ✅ agency/ops 템플릿(12종) 심화 배치 — 리서치 3건(QA·수주·ops) **전부 완료**(요약 하단). **095=QA 3종·096=수주 5종·097=ops 3종 완료.** 남음: 098 glossary(경량, 마지막).
> 🏁 다음 세션이 098만 하면 배치 완결.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-097-ops-templates-deepen` (096 브랜치 위 스택, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것
**agency/ops 템플릿(12종) 심화 배치** — 사용자 "전부 웹리서치 기반". 클러스터별 PR: 095=QA·096=수주·097=ops·098=glossary. 템플릿=**lean 폼**(essay 금지, 필드 완성도만).
- **097(완료)**: ops 3종. guide 12(§6.15~6.22)가 이미 성숙 → 이론 재설명 없이 값만 채우는 lean 폼 + 지침 참조(SSOT). operation-spec(runbook: §0 신뢰성 계약 SLI/SLO/SLA·error-budget 소진액션+집행자·의존성·SEV1-4·롤백 RTO/RPO·break-glass·유지보수창·AI-Ops + 서비스오너/on-call), post-launch-monitoring(A 골든시그널 4종+burn-rate>14.4/1h 페이지+trace_id 상관+AI 시그널 / B 결함추적 / 리뷰 케이던스), work-request-ticket(티켓유형 request/incident/change·우선순위=영향×긴급 P1-P4·완료기준 DoD·변경관리[Std/Normal/Emergency+Change Class A/B/C+롤백]·위험변경만 승인게이트·상태 워크플로).
- **096(완료)**: 수주 5종(go-nogo kill·SOW/BANT·PS gross/net·PMBOK WBS·Phase/Milestone).
- **095(완료)**: QA 3종(RTM 폐루프).

## 다음 사람에게 (098 = 마지막)
1. 095(#84)·096(#85)·097 PR 리뷰·머지.
2. **METH-098 — glossary** 경량. 대상 파일 확인(50_resources/templates/ 에 glossary/용어집류 있으면 그것, 없으면 신규). DDD ubiquitous language(용어→정의→예시·동의어·소유자), context-glossary 지침이 깊은 버전이라 이건 lean 1장. 이걸로 agency/ops 배치 완결.
3. 다른 repo(별도 세션): ai-icons 92 환류·talmo-com.

## 리서치 요약 (1차 소스)
- **수주**: Shipley bid/no-bid(5요인)·APMP 게이트(소유자+일자)·PMBOK WBS 100%룰·SOW discovery(BANT·exclusions·acceptance)·PS margin(gross40-60%·util75-80%·PMI contingency).
- **QA**(반영됨): ISO/IEC/IEEE 29119-3·ISTQB(entry/exit·severity≠priority)·RTM thin·BDD Gherkin 옵션.
- **ops**: Google SRE(runbook·SLO·burn-rate·on-call)·ITIL4(request/incident/change·priority matrix·change type)·OTel 골든시그널·DORA·LLM observability.

## 환경 메모
- 브랜치: `claude/meth-097-ops-templates-deepen` (096 위 스택). branch-first.
- 진척: 메타/dev 배치(092-094) 완결 + **agency/ops 배치 095(QA)·096(수주)·097(ops) 완료**, 098(glossary)만 남음.
