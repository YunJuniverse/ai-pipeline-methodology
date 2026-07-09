# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: agency/ops 템플릿 심화 배치(사용자 "전부 웹리서치 기반", 12종). 리서치 3건(QA·수주·ops) 완료. **METH-097(완료)**: ops 클러스터 3종(Google SRE·ITIL4·OTel·DORA, guide 12 §6.15~6.22 정합=재설명 말고 참조) — operation-spec(§0 신뢰성 계약: SLI/SLO/error-budget 소진액션+집행자·의존성·SEV·롤백 RTO/RPO·break-glass·AI-Ops), post-launch-monitoring(A 골든시그널 4종+burn-rate>14.4/1h 페이지+trace_id 상관+AI 시그널 / B 결함추적), work-request-ticket(티켓유형 request/incident/change·우선순위=영향×긴급 P1-P4·완료기준 DoD·변경관리[변경유형 Std/Normal/Emergency + Change Class A/B/C + 롤백]·상태 워크플로). lean 유지. **남음**: 098=glossary. Class A. PR 대기.
- **Current mode**: fullstack
- **Next TODO**: ① **점검·정합·구조·전파·정비 사이클 완료** — 079~091(…·SPRINTS붕괴·다운스트림 sync 6곳·번호 remediation·skills 삭제·경로 sweep). 남은 후보(전부 Low·선택): agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs), graph.json 노드(02~09·19~21), v3.2 backward-compat 코드 정리(별건). 다른 repo(별도 세션): ai-icons 92_LOCAL↔상류05 환류, talmo-com 실작업. ② 학습 루프 후속: friction 축적→thinktank→catalog 승급→skeleton bake. **프로세스: branch-first 준수.**
- **Blockers**: none

## Active Links

- Current PR: METH-097 ops 3종 (신규) · 095 QA=#84 · 096 수주=#85 대기 · 063~094 = #53~#83 머지 완료
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
| - | `methodology-graph.json` 노드 불완전 — guide 02~09·19~21 누락(00·01·10~18만) | Low | 대시보드 시각화 그래프. METH-079에서 발견. 노드/엣지 보강은 별건(대시보드 렌더 영향 확인 후) |
| - | ~~`.claude/skills` 레거시 3종~~ | — | **Closed(METH-090)** — ai-planning·ai-relay·vibe-coding 삭제. 기능은 guide 01/08/19+prompts가 정본. 90_archive 히스토리는 보존 |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-09: **METH-097 agency/ops 템플릿 배치 3 — ops 3종 (Class A, PR 대기)** — Google SRE·ITIL4·OTel·DORA. guide 12(§6.15~6.22)가 이미 성숙 → 템플릿은 **이론 재설명 없이 값만 채우는 lean 폼 + 지침 참조**(SSOT). **operation-spec(runbook)**: §0 신뢰성 계약 신설(SLI→SLO→SLA 표·**Error Budget 소진 시 액션+집행자**·의존성·SEV1-4·롤백 RTO/RPO·break-glass·유지보수창·AI-Ops row) + 서비스오너/on-call. **post-launch-monitoring**: A 시스템 건강도(**골든 시그널** latency/traffic/errors/saturation+임계치·**burn-rate>14.4/1h=페이지**·비즈니스·AI 시그널·trace_id 상관) + B 결함추적(기존)·리뷰 케이던스. **work-request-ticket**: 티켓유형(request/incident/change)·**우선순위=영향×긴급 P1-P4**(요청구분≠우선순위)·완료기준 DoD·§4 변경관리(변경유형 Std/Normal/Emergency + **Change Class A/B/C 링크** + 롤백[변경&Class≥B 필수])·위험 변경만 승인게이트·상태 워크플로. 남음: 098 glossary.
- 2026-07-09: **METH-096 agency/ops 템플릿 배치 2 — 수주 5종 (Class A, PR #85 대기)** — Shipley·APMP·PMBOK·SOW·PS-margin. lean 폼 필드 보강: **proposal-go-nogo**(결정소유자+게이트일자·경쟁포지션 axis·cost-to-pursue·kill 규칙[1축 미달=포기]·Shipley 5요인 포괄) · **research-collection**(기존 시장 3버킷 + 프로젝트셋업 4버킷[사업목표/성공KPI·예산/일정/의사결정권자 BANT·제약/컴플라이언스·기존자산/연동]+출처열) · **profitability-sheet**(과금모델 enum·리스크 컨틴전시[근거=과거초과율]·gross/net 마진 분리·손익분기·변경요청 별도) · **execution-plan**(가정·범위제외·인수기준+승인권자·리스크레지스터·커뮤니케이션 케이던스·인계/종료·필요 고객 입력물 + **§5 W1-W4→Phase/Milestone 재프레임**[스프린트 없음]) · **wbs**(100%룰·PM/QA도 산출물·work package=견적 롤업·비고=WBS dictionary). 남음: 097 ops 3종·098 glossary.
- 2026-07-09: **METH-095 agency/ops 템플릿 심화 배치 1 — QA 3종 (Class A, PR #84 대기)** — 웹리서치 3건(QA·수주·ops) 착수, 이번은 QA 클러스터(ISO/IEC/IEEE 29119-3·ISTQB). 얇던 3종에 lean 폼 필드 보강: **qa-acceptance-plan** — 진입기준(Entry, 단위/통합 통과·P1/P2 0)·검수유형(기능/UAT/회귀/NFR)·정량 종료기준(≥95% 실행·P1 100%)·심각도≠우선순위 척도+트리아지·테스트데이터·요구사항ID(RTM)·Out-of-scope. **qa-test-scenario** — 케이스 ID·요구사항 ID·사전조건·단계(시나리오형)·실제결과(결함증거)·부정/경계 태그·GWT 옵션(시나리오형만)·AI초안/사람검토 표기. **qa-acceptance-signoff** — 인수 버전/빌드 pin·종료기준 충족(계획서 대비)·개방결함(심각도별)+웨이버·조건부합격 조건+기한·증거링크·하자보수/인계. 3종 연결=RTM(요구사항 ID) 폐루프. 남음: 096 수주 5종·097 ops 3종·098 glossary.
- 2026-07-09: **METH-094 guide 20 DTCG 상호운용 + 메타 배치 완결 (Class A, PR #83 머지)** — 메타/dev 지침 심화 배치 3번(마무리). **guide 20**(디자인 토큰)에 실제 gap 발견 — W3C DTCG 표준·툴 미언급 → **§8 상호운용 표준 신설**: DTCG JSON(`$value`/`$type`/`{alias}` 앨리어스·composite·모드)·Style Dictionary(다타깃 빌드)·Tokens Studio(Figma)·도입 판정 트리거(멀티플랫폼/디자이너 소유/멀티repo 중 1)·4기둥↔DTCG 매핑(4기둥=DTCG 부분집합, 승격 시 연속)·"필요할 때만"(거대시스템 회피 유지)·v3 이력. **05·09·02·19는 검토 결과 이미 성숙**(내부 규칙 완결·planning-handoff 정합·최근 v3/v1) → **콘텐츠 추가 없음**(padding=이번 세션 내내 제거한 bloat). 배치 총괄: 심화 필요분(03·06·07·08·20) 완료, 나머지 5개 검토·적정.
- 2026-07-09: **METH-093 guide 06·07·08 심화 — 에이전트 메카닉 웹리서치 (Class B, PR #82 대기)** — 메타/dev 배치 2번, 리서치 3건(Anthropic context-engineering·harness·multi-agent·agent-loop·measuring-autonomy + Cognition). 얇던 3개(76/52/55줄)에 §SOTA 보강 + v2 이력: **06 컴팩션** — 두 층 모델·임계치(하네스 ~95%/proactive ~60%)·auto-survive 명시(파일 재읽기·CLAUDE.md 재주입→포인터 안전)·paths-scoped rule re-anchor·safest-first 폐기순서·post-compaction 검증·subagent isolation(공간축). **07 자율/정지** — 이중예산(runtime turns/USD + declared scope; SDK 기본 무제한 경고)·6 circuit breaker·ground-truth 진척+build/eval 분리·ask→clarify→escalate(over-asking도 실패)·비가역=Class C 정지·stop report(ResultMessage형)·재선언 전 checkpoint. **08 서브에이전트** — fan-out vs single-writer(Cognition, 언제 안 쓰나)·sizing(1/2-4/10+)·위임 계약 필드·per-subagent model/effort·concurrency 3-5 cap·completeness critic·artifact 외부메모리·Workflow 스케일 escape+결정론.
