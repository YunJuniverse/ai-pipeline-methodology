# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: 메타/dev 지침 심화 배치 **완결**(사용자 "전부", 092·093·094). **METH-094**: guide 20에 W3C DTCG 상호운용 표준 §8 신설(`$value`/`$type`/`{alias}`·Style Dictionary·Tokens Studio·도입 트리거·4기둥↔DTCG 매핑, "필요할 때만" 프레이밍). **05·09·02·19는 검토 결과 이미 성숙 → 콘텐츠 추가 없음**(bloat 회피 — 세션 관통 원칙). 배치 총괄: 심화 필요분 03(092)·06·07·08(093)·20(094) 완료, 나머지 5개 검토·적정 확인. Class A. PR 대기.
- **Current mode**: fullstack
- **Next TODO**: ① **점검·정합·구조·전파·정비 사이클 완료** — 079~091(…·SPRINTS붕괴·다운스트림 sync 6곳·번호 remediation·skills 삭제·경로 sweep). 남은 후보(전부 Low·선택): agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs), graph.json 노드(02~09·19~21), v3.2 backward-compat 코드 정리(별건). 다른 repo(별도 세션): ai-icons 92_LOCAL↔상류05 환류, talmo-com 실작업. ② 학습 루프 후속: friction 축적→thinktank→catalog 승급→skeleton bake. **프로세스: branch-first 준수.**
- **Blockers**: none

## Active Links

- Current PR: METH-094 guide20 DTCG (신규) · METH-092/093 = #81/#82 대기 · 063~091 = #53~#80 머지 완료
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

- 2026-07-09: **METH-094 guide 20 DTCG 상호운용 + 메타 배치 완결 (Class A, PR 대기)** — 메타/dev 지침 심화 배치 3번(마무리). **guide 20**(디자인 토큰)에 실제 gap 발견 — W3C DTCG 표준·툴 미언급 → **§8 상호운용 표준 신설**: DTCG JSON(`$value`/`$type`/`{alias}` 앨리어스·composite·모드)·Style Dictionary(다타깃 빌드)·Tokens Studio(Figma)·도입 판정 트리거(멀티플랫폼/디자이너 소유/멀티repo 중 1)·4기둥↔DTCG 매핑(4기둥=DTCG 부분집합, 승격 시 연속)·"필요할 때만"(거대시스템 회피 유지)·v3 이력. **05·09·02·19는 검토 결과 이미 성숙**(내부 규칙 완결·planning-handoff 정합·최근 v3/v1) → **콘텐츠 추가 없음**(padding=이번 세션 내내 제거한 bloat). 배치 총괄: 심화 필요분(03·06·07·08·20) 완료, 나머지 5개 검토·적정.
- 2026-07-09: **METH-093 guide 06·07·08 심화 — 에이전트 메카닉 웹리서치 (Class B, PR #82 대기)** — 메타/dev 배치 2번, 리서치 3건(Anthropic context-engineering·harness·multi-agent·agent-loop·measuring-autonomy + Cognition). 얇던 3개(76/52/55줄)에 §SOTA 보강 + v2 이력: **06 컴팩션** — 두 층 모델·임계치(하네스 ~95%/proactive ~60%)·auto-survive 명시(파일 재읽기·CLAUDE.md 재주입→포인터 안전)·paths-scoped rule re-anchor·safest-first 폐기순서·post-compaction 검증·subagent isolation(공간축). **07 자율/정지** — 이중예산(runtime turns/USD + declared scope; SDK 기본 무제한 경고)·6 circuit breaker·ground-truth 진척+build/eval 분리·ask→clarify→escalate(over-asking도 실패)·비가역=Class C 정지·stop report(ResultMessage형)·재선언 전 checkpoint. **08 서브에이전트** — fan-out vs single-writer(Cognition, 언제 안 쓰나)·sizing(1/2-4/10+)·위임 계약 필드·per-subagent model/effort·concurrency 3-5 cap·completeness critic·artifact 외부메모리·Workflow 스케일 escape+결정론.
- 2026-07-09: **METH-092 guide 03(AI 관찰 로그) 심화 — CLI 정본화 + 학습루프 연결 (Class B, PR #81 대기)** — 메타/dev 지침 심화 배치의 1번(내부 정합, 리서치 불요). guide 03이 §5에서 아직 수동 `cat` 요청 방식을 안내(stale)하던 것을 **`observe` CLI 정본화**: 직접 `cat >` 금지(형식오류로 wrap fail)·헌법 §2④ 의무화 명시 + `--friction` **positional 형식**(where\|cost_minutes\|resolution\|repeat_of)·캡처 규칙(비자명·재발·막힘만, 노이즈 방지)·where=재발판정키. §6에 **학습 파이프라인**(observe→thinktank[≥2 승급후보]→pending→catalog→skeleton) + "마찰 안 남기면 루프 굶는다" + catalog/skeleton _README 교차링크. v2 변경이력 신설. METH-085(friction 규칙)·086(flow) 반영.
- 2026-07-09: **METH-091 legacy 경로 sweep — 라이브 문서 3건 수정 (Class A, PR #80 머지)** — 라이브 문서의 pre-v4 경로 참조 점검(90_archive·마이그레이션·시점기록 제외). **실제 stale 3건 발견·수정**: `10_foundation/{KICKOFF_PROMPT,DIAGRAM,HOW_TO_APPLY}.md`가 산출물 위치를 `docs/snapshots/`(구조 개편 前)로 안내 → `40_dev/snapshots/`(v4)로 교정(신규 사용자 오도 제거). 나머지 `docs/` 참조는 정당 확인: guide 19의 `gamblescan:docs/snapshots/...retrospective` = gamblescan 실제 파일 위치(자체 docs), api-contract `docs/openapi.yaml` = 프로젝트 예시. **부수 발견**: v3.2 backward-compat 코드 폴백(methodology.py·dashboard의 40_resources/60_meta/docs 폴백)은 현존 7 repo 전부 v4.0이라 dead지만 코드 backward-compat라 별건 Open Issue 등재(제거는 v3 지원 포기 결정 필요). Open Issue(docs sweep) Closed.
- 2026-07-09: **METH-090 `.claude/skills` 레거시 3종 삭제 (Class A, PR #79 머지)** — ai-planning·ai-relay·vibe-coding(2026-03 작성) 삭제. 3개 다 구모델(스프린트·기획서6종/개발명세8종·Phase1-10·`docs/planning|sprints|development/` dead 경로) 기준이라, 호출 시 v4와 반대로 안내하는 stale 중복. 기능은 이미 정본이 담당: 기획 오케→guide 01+`prompts/plan-routing`, 멀티AI 릴레이→guide 08(+checkpoint=handoff note), 구현 워크플로/4-레이어→guide 19+guide 00. 살릴 고유 콘텐츠 없음. 다운스트림 sync 대상 아님(shared_paths 밖, 로컬만). 잔여 참조는 90_archive/legacy-methodology 히스토리뿐(보존). 세션 관통 SSOT/anti-중복(AI-LOG·last_built·SPRINTS 제거와 동종).
