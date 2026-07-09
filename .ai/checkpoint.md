# Checkpoint — 2026-07-09 (agency/ops 템플릿 심화 배치 — 096 수주)

> ✅ agency/ops 템플릿(12종) 심화 배치 — 리서치 3건(QA·수주·ops) **전부 완료**(요약 하단). **095=QA 3종·096=수주 5종 완료.** 남음: 097 ops 3종·098 glossary.
> 🏁 다음 세션이 097/098을 이어서 하면 배치 완결. 리서치 요약이 하단에 있어 재리서치 불요.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-096-proposal-templates-deepen` (095 브랜치 위 스택, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것
**agency/ops 템플릿(12종) 심화 배치** — 사용자 "전부 웹리서치 기반". 클러스터별 PR: 095=QA·096=수주·097=ops·098=glossary. 템플릿=**lean 폼**(essay 금지, 필드 완성도만).
- **096(완료)**: 수주 5종. proposal-go-nogo(결정소유자+게이트일자·경쟁포지션 axis·cost-to-pursue·kill 규칙[1축 미달=포기]), research-collection(시장 3버킷 + 프로젝트셋업 4버킷[사업목표/성공KPI·BANT·컴플라이언스·기존자산]+출처열), profitability-sheet(과금모델 enum·리스크 컨틴전시[근거=과거초과율]·gross/net 분리·손익분기·변경요청), execution-plan(가정·범위제외·인수기준+승인권자·리스크레지스터·커뮤니케이션·인계 + §5 W1-W4→Phase/Milestone 재프레임), wbs(100%룰·PM/QA포함·work package 롤업·비고=WBS dictionary).
- **095(완료)**: QA 3종(RTM 폐루프).

## 다음 사람에게 (097·098 원료 = 하단 리서치 요약)
1. 095(#84)·096 PR 리뷰·머지.
2. **METH-097 — ops 3종**(operation-spec·post-launch-monitoring·work-request-ticket). SRE·ITIL4·OTel·DORA, **guide 12 정합(재설명 말고 참조)**:
   - operation-spec(runbook): ownership+온콜·SLO/SLI+error budget policy(소진 시 액션+집행자)·의존성·인시던트 SEV1-4·rollback/DR(RTO/RPO)·모니터링 refs·access/break-glass·비용/유지보수창·AI-ops row.
   - post-launch-monitoring: 골든시그널(latency/traffic/errors/saturation)+임계치·burn-rate(>14.4/1h page)·SLI 대시보드·trace_id 상관·비즈니스 지표·온콜 라우팅·리뷰 케이던스·AI 시그널.
   - work-request-ticket: 티켓유형(request/incident/change)·priority=impact×urgency(P1-P4)·done 기준·상태 워크플로·**Class A/B/C 링크**·change type(Standard/Normal/Emergency)·rollback(type=change&class≥B)·위험변경만 승인게이트.
3. **METH-098 — glossary** 경량(DDD ubiquitous language·용어→정의→예시; context-glossary 지침이 깊은 버전이라 이건 간단).
4. 다른 repo(별도 세션): ai-icons 92 환류·talmo-com.

## 리서치 요약 (1차 소스)
- **수주**: Shipley bid/no-bid(5요인)·APMP 게이트(소유자+일자)·PMBOK WBS 100%룰·SOW discovery(BANT·exclusions·acceptance)·PS margin(gross40-60%·util75-80%·PMI contingency).
- **QA**(반영됨): ISO/IEC/IEEE 29119-3·ISTQB(entry/exit·severity≠priority)·RTM thin·BDD Gherkin 옵션.
- **ops**: Google SRE(runbook·SLO·burn-rate·on-call)·ITIL4(request/incident/change·priority matrix·change type)·OTel 골든시그널·DORA·LLM observability.

## 환경 메모
- 브랜치: `claude/meth-096-proposal-templates-deepen` (095 위 스택). branch-first.
- 진척: 메타/dev 배치(092-094) 완결 + **agency/ops 배치 095(QA)·096(수주) 완료**, 097/098 남음.
