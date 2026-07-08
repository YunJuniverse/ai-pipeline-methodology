# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-058 **P3 온보딩 밴드 다이어트 (무게 감사 MED)**. `HOW_TO_APPLY §6` Change Class 전문(35줄, CLAUDE §3 재서술·드리프트)을 요지 3줄 + **CLAUDE §3 단일출처 포인터**(8줄)로 축약. 앵커 참조 없음 확인. shared_paths라 하류 무게도 감소. 이로써 **회고 3대 우선순위(P1·P2·P3) 모두 실제 구현 완료.** Class A. PR 대기(main 직접).
- **Current mode**: fullstack
- **Next TODO**: ① guide 05·06 다운스트림 sync(20_guides shared). ② R1(a) 관련성 top-k 자동 주입(임베딩 어댑터, Class B) 또는 R3 budget·R4 서브에이전트 자산화. ③ 2026-Q4 회고 시 지표(thinktank) 추세 확인.
- **Blockers**: none

## Active Links

- Current PR: #35 (METH-046 sync 픽스)
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
| - | Some legacy/archive docs may still mention pre-`40_dev` or pre-`60_tools` paths | Low | Sweep only if those docs become live references again |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-08: **METH-058 온보딩 밴드 다이어트 — 무게 감사 MED P3 (Class A)** — `HOW_TO_APPLY §6` Change Class 전문(트리거·요구증거·프로세스 35줄)이 `CLAUDE §3`을 재서술하며 드리프트(B/C 무단강등 금지 누락 등)한 것을 **요지 3줄 + CLAUDE §3 단일출처 포인터**(8줄)로 축약. 앵커 참조 0 확인(안전). shared_paths라 하류 무게 동시 감소. USER_GUIDE §8·WHITEPAPER §8-2·AGENTS·DIAGRAM은 load-bearing이라 미변경(감사 판정 준수). **회고 3대 우선순위 P1(#47)·P2(#46)·P3(이번) 전부 실제 구현 완료.**
- 2026-07-08: **METH-057 지표 인프라 + thinktank 재구성 — RFC-002 R1(b) (Class A, PR #47 머지)** — 회고 최우선. 휴면·"자동 루프" 과장이던 thinktank를 **정직한 지표 집계 + 승급 후보 마킹** 도구로 재구성(`60_tools/methodology.py cmd_thinktank`): 출력에 §7-근접 지표 신설(관찰 43·기간 62일·주당 4.9·task_type 분포·마찰 총계/Catalog 재적중/승급 후보 수), 도크스트링·`catalog/_README §승급`·`retrospectives/README`에 "수동 승급이 정식·자동 승급 없음" 명문화(문서-현실 부패 해소). 회고 §1 지표 소스로 연결(회고 직전 실행). 실행 검증 완료. RFC-002 R1 🟡부분구현 표시. R1(a) 관련성 자동 주입은 임베딩 어댑터 필요 → 별도 후속.
- 2026-07-08: **METH-056 Compaction 프로토콜 구현 — RFC-002 R2 첫 실제 구현 (Class A, PR #46 머지)** — 진단·로드맵을 넘어 **약점을 실제로 고친 첫 항목**. `20_guides/06_컨텍스트_컴팩션_프로토콜.md` 신설: compaction 경계 보존/폐기 규칙(보존=결정·게이트 상태·open question·경로 포인터 / 폐기=원시 툴 출력·중복·이미 파일 반영분), checkpoint를 세션 종료뿐 아니라 **compaction 경계·긴 세션 자연 경계**에서도 갱신(=세션 중간 인계), pre-compaction 체크리스트. CLAUDE/AGENTS 세션 절차에 "컴팩션 경계 트리거" 편입(로드·준수 강제). README 카탈로그 06 + RFC-002 R2 ✅구현 표시. SOTA(Anthropic context engineering)를 방법론 구조에 접합.
- 2026-07-08: **METH-055 RFC-002 draft→accepted 비준 (Class A, PR #45 머지)** — #44(2026-Q3 회고) 머지 = 사람 게이트 통과 → `70_meta/rfc/RFC-002` status=accepted, accepted_at·accepted_via(#44)·relates_to([RFC-001,2026-Q3,MP-003]) 갱신 + 비준 blockquote. 별도 단일 ADR 미승급(RFC-001 선례: accepted Class A 로드맵/도구 RFC는 ADR 미승급; 개별 R1~R6의 Class B/C 항목만 각자 ADR). 발전 로드맵이 방법론 진화 백로그로 확정 — 다음은 실제 구현(P2 compaction부터).
- 2026-07-08: **METH-054 첫 분기 회고(2026-Q3) + MP-003 (Class A, PR #44 머지)** — 백서 §9 ROI 게이트 첫 발화(~9주 초과, 무게 감사·SOTA 평가가 촉발). `70_meta/retrospectives/2026-Q3_first-methodology-review.md` — **정직 모드: 지표 인프라 미달**(관찰 41/권장 100·active Catalog 1/권장 5), README 규칙대로 "지표 인프라 1순위" 자인. 효과적=경험 루프 1회전 완주·서브에이전트 하네스 / 부패=thinktank 휴면·온보딩 중복·프로세스 사고 2건. 다음 분기 P1 지표+thinktank 존폐(a되살림/b공식화, b권장)·P2 compaction(R2)·P3 온보딩 다이어트. **RFC-002 draft→accepted 권장**(머지=비준). 스택-PR 고아화를 `70_meta/catalog/_pending/MP-003`으로 캡처(N≥2 재발 시 MC 승급).
- 2026-07-08: **METH-053 guide 04→05 리넘버 + 식별자 예약범위 + RFC-002 복구 (Class A, PR #43 머지)** — 상류 산출물 채널 분리 지침 `04`→`05`(ai-icons·icons-invest 커스텀 04 doc_id 충돌 회피) + guide 02 §8 지침 번호 예약(상류 00–89/다운스트림 90–99). 스택 PR 함정으로 고아화된 RFC-002(METH-052) 복원·재포함.
