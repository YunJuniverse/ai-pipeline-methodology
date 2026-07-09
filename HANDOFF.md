# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **METH-099 graph.json 노드 보강 + 096~098 stranded 복구**. ⚠️ **스택-PR 함정 발견**: #85/#86/#87이 main이 아닌 중간 브랜치로 머지돼 096/097/098이 main에 미반영(main엔 #84 095만). 이 브랜치를 `origin/claude/meth-097-...`(095-098 온전 보존) 기준으로 잡아 graph 작업을 얹음 → **단일 PR base=main으로 096+097+098+099 한 번에 복구**(재스택 회피). **METH-099**: methodology-graph.json 노드 29→42(guide 02·03·05·06·07·08·09·19·20·21 10개 추가[04는 미존재], 학습루프 observations/catalog/skeletons, checkpoint), 엣지 39→53(g00 parent-of 메타룰·g18→g21→g19/g20 dev트랙·observe→catalog→skeleton), stale ai-log 노드 제거(AI-LOG.md 083삭제), tier6 신설, learning kind. dashboard 렌더 검증(nodes=42)·JSON 정합(dangling/dup 0). Class A. PR 대기.
- **Current mode**: fullstack
- **Next TODO**: ① **점검·정합·구조·전파·정비 사이클 완료** — 079~099(…·다운스트림 sync·번호 remediation·skills 삭제·경로 sweep·메타/dev 지침 심화 092~094·agency/ops 템플릿 12종 095~098·**graph.json 노드 보강 099**). 남은 후보(전부 Low·선택): v3.2 backward-compat 코드 정리(별건). 다른 repo(별도 세션): ai-icons 92_LOCAL↔상류05 환류, talmo-com 실작업. ② 학습 루프 후속: friction 축적→thinktank→catalog 승급→skeleton bake. **프로세스: branch-first 준수. ⚠️ 스택-PR 지양 — main 직행 단일 PR 선호(재타깃 함정).**
- **Blockers**: none

## Active Links

- Current PR: METH-099 graph 노드+096~098 복구 (신규, base=main) · 095=#84 머지 · 096/097/098=#85/#86/#87 중간브랜치 머지(main 미반영→099로 복구) · 063~094 = #53~#83 머지 완료
- Current issue:
- Relevant ADRs:
- Relevant snapshots: `40_dev/snapshots/implementation-plan-2026-05-07.md`, `40_dev/snapshots/transfer-drill-2026-05-08.md`

## Open Decisions

| ID | Decision | Needed By | Status |
|----|----------|-----------|--------|
| - | `.claude/worktrees/` and `.codex/` are local tool metadata and should be gitignored | 2026-05-07 | Closed |

## Open Issues

| ID | Issue | Severity | Next Step |
|----|-------|----------|-----------|
| - | ~~sync가 다운스트림 고유 파일 mirror-delete~~ | — | **Closed** — METH-046(PR #35)로 prune을 --prune opt-in화(기본 보존) |
| - | ~~legacy/archive docs pre-v4 경로 언급~~ | — | **Closed(METH-091)** — 라이브 문서 sweep: `10_foundation/` 3건(`docs/snapshots/`→`40_dev/snapshots/`) 수정. 나머지는 정당(정확한 인용·예시)·90_archive는 히스토리 보존 |
| - | (참고, 별건) v3.2 backward-compat 코드 폴백 — `methodology.py _wrap_obs_dirs`·dashboard obs/templates 폴백(40_resources/60_meta/docs) | Low | 현존 repo 7곳 전부 v4.0이라 dead. 제거 시 v3 지원 포기 — 필요시 별도 판단(마이그레이션 스크립트는 유지) |
| - | ~~ai-icons·icons-invest guide 번호 충돌~~ | — | **Closed(METH-089)** — 커스텀 04/05/21→90/91/92 이관·doc_id·참조 갱신, origin/main 검증. 잔여: ai-icons 92_LOCAL(구 21)은 상류 05 정본과 149줄 차이=로컬 발전분 → 각 repo 세션에서 상류 05로 환류·재조정 검토 |
| - | ~~sync 홀드 3곳(dirty)~~ | — | **Closed(METH-088)** — ai-icons·cafe24·icons-invest dirty 해소 후 086 sync 완료. **관리 다운스트림 6곳 전부 086 반영** |
| - | ~~`methodology-graph.json` 노드 불완전~~ | — | **Closed(METH-099)** — guide 10종(02·03·05·06·07·08·09·19·20·21) + 학습루프(observations·catalog·skeletons) + checkpoint 노드 추가, stale ai-log 제거. 노드 29→42·엣지 39→53. dashboard 렌더 검증(nodes=42)·JSON 정합 0 오류. (04는 미존재라 제외) |
| - | ⚠️ **스택-PR 재타깃 함정** — #85/#86/#87이 main 아닌 중간 브랜치로 머지됨(096/097/098 main 미반영) | — | **복구중(METH-099)** — 099 브랜치가 095-098 온전 보존 브랜치 기준 → base=main 단일 PR로 096+097+098+099 한 번에 복구. 교훈: 스택-PR은 순서·브랜치 삭제 타이밍 취약 → **main 직행 단일 PR 선호** |
| - | ~~`.claude/skills` 레거시 3종~~ | — | **Closed(METH-090)** — ai-planning·ai-relay·vibe-coding 삭제. 기능은 guide 01/08/19+prompts가 정본. 90_archive 히스토리는 보존 |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-09: **METH-099 methodology-graph.json 노드 보강 + 096~098 stranded 복구 (Class A, PR base=main 대기)** — 대시보드 관계 그래프가 guide 00·01·10~18만 담아 **02~21 상당수 누락**(METH-079 발견 Open Issue)을 종결. **노드 29→42**: guide 10개(02 식별자·03 관찰로그·05 채널분리·06 컴팩션·07 자율진행·08 서브에이전트·09 핸드오프재포맷·19 클린아키텍처·20 디자인토큰·21 개발명세; **04는 미존재라 제외**) + 학습루프 3종(ai_observations·catalog·skeletons) + checkpoint(핵심 라이브인데 누락). **엣지 39→53**: g00 parent-of 메타룰 7·g18→g21→g19/g20 dev트랙·observe→catalog→skeleton 학습루프·templates→checkpoint. **stale ai-log 노드 제거**(AI-LOG.md는 083서 삭제됨=dead). tier6 "개발 트랙 규칙" 신설·learning kind 추가·v3.2. dashboard 재생성 렌더 검증(nodes=42)·JSON 정합(dangling/dup 0·경로 전부 존재·lifecycle g21 참조 해소). **부수(중요)**: 스택-PR 재타깃 함정으로 #85/#86/#87이 main 아닌 중간 브랜치로 머지→096/097/098 main 미반영이던 것을 이 단일 PR(base=main)로 복구.
- 2026-07-09: **METH-098 agency/ops 템플릿 배치 4 — glossary + 배치 완결 (Class A, PR #87 대기)** — **glossary.md**(SI 단계별 용어규약집) 심화. 핵심=**SSOT 경계 명시**: glossary=계약·산출물 *표면 라벨* 통일(영업~운영 단계) / context-glossary=도메인 개념 *canon*(유비쿼터스 언어·코드까지·린트 훅) — 개념 정의는 후자에서, 여기선 링크만(중복 금지). 표준용어 표에 **예시(용례)·상태(Approved/Deprecated)** 열 추가, 관리자=용어 분쟁 해결권자 명시, 폐기어도 유사용어로 남겨 추적성. **배치 완결**: agency/ops 12종(095 QA 3·096 수주 5·097 ops 3·098 glossary 1) 전부 lean 폼 필드 보강 + 지침 참조(SSOT)로 완료 — 성숙 지침 재설명 없이 값 폼만.
- 2026-07-09: **METH-097 agency/ops 템플릿 배치 3 — ops 3종 (Class A, PR #86 대기)** — Google SRE·ITIL4·OTel·DORA. guide 12(§6.15~6.22)가 이미 성숙 → 템플릿은 **이론 재설명 없이 값만 채우는 lean 폼 + 지침 참조**(SSOT). **operation-spec(runbook)**: §0 신뢰성 계약 신설(SLI→SLO→SLA 표·**Error Budget 소진 시 액션+집행자**·의존성·SEV1-4·롤백 RTO/RPO·break-glass·유지보수창·AI-Ops row) + 서비스오너/on-call. **post-launch-monitoring**: A 시스템 건강도(**골든 시그널** latency/traffic/errors/saturation+임계치·**burn-rate>14.4/1h=페이지**·비즈니스·AI 시그널·trace_id 상관) + B 결함추적(기존)·리뷰 케이던스. **work-request-ticket**: 티켓유형(request/incident/change)·**우선순위=영향×긴급 P1-P4**(요청구분≠우선순위)·완료기준 DoD·§4 변경관리(변경유형 Std/Normal/Emergency + **Change Class A/B/C 링크** + 롤백[변경&Class≥B 필수])·위험 변경만 승인게이트·상태 워크플로. 남음: 098 glossary.
- 2026-07-09: **METH-096 agency/ops 템플릿 배치 2 — 수주 5종 (Class A, PR #85 대기)** — Shipley·APMP·PMBOK·SOW·PS-margin. lean 폼 필드 보강: **proposal-go-nogo**(결정소유자+게이트일자·경쟁포지션 axis·cost-to-pursue·kill 규칙[1축 미달=포기]·Shipley 5요인 포괄) · **research-collection**(기존 시장 3버킷 + 프로젝트셋업 4버킷[사업목표/성공KPI·예산/일정/의사결정권자 BANT·제약/컴플라이언스·기존자산/연동]+출처열) · **profitability-sheet**(과금모델 enum·리스크 컨틴전시[근거=과거초과율]·gross/net 마진 분리·손익분기·변경요청 별도) · **execution-plan**(가정·범위제외·인수기준+승인권자·리스크레지스터·커뮤니케이션 케이던스·인계/종료·필요 고객 입력물 + **§5 W1-W4→Phase/Milestone 재프레임**[스프린트 없음]) · **wbs**(100%룰·PM/QA도 산출물·work package=견적 롤업·비고=WBS dictionary). 남음: 097 ops 3종·098 glossary.
- 2026-07-09: **METH-095 agency/ops 템플릿 심화 배치 1 — QA 3종 (Class A, PR #84 대기)** — 웹리서치 3건(QA·수주·ops) 착수, 이번은 QA 클러스터(ISO/IEC/IEEE 29119-3·ISTQB). 얇던 3종에 lean 폼 필드 보강: **qa-acceptance-plan** — 진입기준(Entry, 단위/통합 통과·P1/P2 0)·검수유형(기능/UAT/회귀/NFR)·정량 종료기준(≥95% 실행·P1 100%)·심각도≠우선순위 척도+트리아지·테스트데이터·요구사항ID(RTM)·Out-of-scope. **qa-test-scenario** — 케이스 ID·요구사항 ID·사전조건·단계(시나리오형)·실제결과(결함증거)·부정/경계 태그·GWT 옵션(시나리오형만)·AI초안/사람검토 표기. **qa-acceptance-signoff** — 인수 버전/빌드 pin·종료기준 충족(계획서 대비)·개방결함(심각도별)+웨이버·조건부합격 조건+기한·증거링크·하자보수/인계. 3종 연결=RTM(요구사항 ID) 폐루프. 남음: 096 수주 5종·097 ops 3종·098 glossary.
