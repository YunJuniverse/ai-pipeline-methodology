# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-057 **P1 지표 인프라 + thinktank 재구성 (RFC-002 R1(b))**. 회고 최우선 항목. thinktank(`methodology.py thinktank`)를 휴면·과장 서사에서 **정직한 지표 집계 + 후보 마킹 도구**로 재구성 — §7-근접 지표(관찰 43건·62일·주당 4.9·task 분포·마찰/재적중/후보) 산출, "수동 승급이 정식" 명문화(CLI 도크스트링·catalog/_README·retrospectives/README). 회고 §1 지표 소스로 연결. R1(a) 관련성 자동 주입은 임베딩 의존이라 별도 후속. Class A. PR 대기(main 직접).
- **Current mode**: fullstack
- **Next TODO**: ① P3 온보딩 밴드 다이어트(무게 감사 MED: HOW_TO_APPLY §6 → CLAUDE 링크 축약). ② guide 06 다운스트림 sync. ③ R1(a) 관련성 top-k 자동 주입(임베딩 어댑터, Class B) 또는 R3 budget.
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

- 2026-07-08: **METH-057 지표 인프라 + thinktank 재구성 — RFC-002 R1(b) (Class A)** — 회고 최우선. 휴면·"자동 루프" 과장이던 thinktank를 **정직한 지표 집계 + 승급 후보 마킹** 도구로 재구성(`60_tools/methodology.py cmd_thinktank`): 출력에 §7-근접 지표 신설(관찰 43·기간 62일·주당 4.9·task_type 분포·마찰 총계/Catalog 재적중/승급 후보 수), 도크스트링·`catalog/_README §승급`·`retrospectives/README`에 "수동 승급이 정식·자동 승급 없음" 명문화(문서-현실 부패 해소). 회고 §1 지표 소스로 연결(회고 직전 실행). 실행 검증 완료. RFC-002 R1 🟡부분구현 표시. R1(a) 관련성 자동 주입은 임베딩 어댑터 필요 → 별도 후속.
- 2026-07-08: **METH-056 Compaction 프로토콜 구현 — RFC-002 R2 첫 실제 구현 (Class A, PR #46 머지)** — 진단·로드맵을 넘어 **약점을 실제로 고친 첫 항목**. `20_guides/06_컨텍스트_컴팩션_프로토콜.md` 신설: compaction 경계 보존/폐기 규칙(보존=결정·게이트 상태·open question·경로 포인터 / 폐기=원시 툴 출력·중복·이미 파일 반영분), checkpoint를 세션 종료뿐 아니라 **compaction 경계·긴 세션 자연 경계**에서도 갱신(=세션 중간 인계), pre-compaction 체크리스트. CLAUDE/AGENTS 세션 절차에 "컴팩션 경계 트리거" 편입(로드·준수 강제). README 카탈로그 06 + RFC-002 R2 ✅구현 표시. SOTA(Anthropic context engineering)를 방법론 구조에 접합.
- 2026-07-08: **METH-055 RFC-002 draft→accepted 비준 (Class A, PR #45 머지)** — #44(2026-Q3 회고) 머지 = 사람 게이트 통과 → `70_meta/rfc/RFC-002` status=accepted, accepted_at·accepted_via(#44)·relates_to([RFC-001,2026-Q3,MP-003]) 갱신 + 비준 blockquote. 별도 단일 ADR 미승급(RFC-001 선례: accepted Class A 로드맵/도구 RFC는 ADR 미승급; 개별 R1~R6의 Class B/C 항목만 각자 ADR). 발전 로드맵이 방법론 진화 백로그로 확정 — 다음은 실제 구현(P2 compaction부터).
- 2026-07-08: **METH-054 첫 분기 회고(2026-Q3) + MP-003 (Class A, PR #44 머지)** — 백서 §9 ROI 게이트 첫 발화(~9주 초과, 무게 감사·SOTA 평가가 촉발). `70_meta/retrospectives/2026-Q3_first-methodology-review.md` — **정직 모드: 지표 인프라 미달**(관찰 41/권장 100·active Catalog 1/권장 5), README 규칙대로 "지표 인프라 1순위" 자인. 효과적=경험 루프 1회전 완주·서브에이전트 하네스 / 부패=thinktank 휴면·온보딩 중복·프로세스 사고 2건. 다음 분기 P1 지표+thinktank 존폐(a되살림/b공식화, b권장)·P2 compaction(R2)·P3 온보딩 다이어트. **RFC-002 draft→accepted 권장**(머지=비준). 스택-PR 고아화를 `70_meta/catalog/_pending/MP-003`으로 캡처(N≥2 재발 시 MC 승급).
- 2026-07-08: **METH-053 guide 04→05 리넘버 + 식별자 예약범위 + RFC-002 복구 (Class A, PR #43 머지)** — ① 상류 산출물 채널 분리 지침을 `04`→`05`로 이동(ai-icons·icons-invest가 커스텀 `04_프로젝트_문서_보관_및_분류` 점유 → doc_id 충돌 회피). guide 02 §8 신설: 지침 번호 예약(상류 00–89 / 다운스트림-커스텀 90–99), 레거시 비준수 04는 마이그레이션 대상. CLAUDE/AGENTS/README 참조 05로 갱신. ② **RFC-002 복구** — METH-052(#42)가 스택 PR 함정(base=이미 머지된 meth-051 브랜치)으로 main 미도달·고아화 → 파일 복원해 main 직접 PR에 재포함.
- 2026-07-08: **METH-052 SOTA 평가 + RFC-002 발전 로드맵 (Class A)** — 무게 감사(에이전트 16개, MIXED: 코어 정당·군살 국소[온보딩 밴드 중복·휴면 thinktank·~9주 초과 ROI 게이트]) + SOTA 웹 리서치(harness/context/loop engineering·ERL: 코어가 정합/선행, 약점=Reflect/Learn 자동화+compaction·budget). `70_meta/rfc/RFC-002`(draft, R1~R6). ※#42 고아화로 main 미반영 → METH-053에서 복구.
- 2026-07-08: **METH-051 산출물 채널 분리 지침 신설 (Class A, PR #41 머지)** — 다운스트림(ai-icons) 반복 피드백("작업 메타를 산출물에 넣지 마라", 06-19→07-06→07-07 + 명시승인)을 에이전트 토론(찬반→반론→심판)으로 상류 격상 판정. 결론: 백서 헌법 직행이 아닌 전-도메인 지침. `20_guides/04_산출물_채널_분리_규칙.md`(청중 축=외부 무맥락 공유 여부로 트리거, 주제 축=changelog류 예외, 메타는 삭제 아닌 라우팅) + CLAUDE/AGENTS File Roles "Output channel" 행 + README 카탈로그(02·03·04). 백서 미수정(제0·제2·§8-4·§8-5 인용만). 강제 grep 래칫은 §7 스펙만(fail-open 금지).
- 2026-06-29: **METH-049 gamblescan 실세계 검증 — 패턴 교훈 2건 + P-002 N≥2** — canonical 스켈레톤을 gamblescan(독립 구현, hex 3,030 codemod 완료)에 교차검증. ① gamblescan 가드레일이 `text-` 회색만 검사 → `bg-/border-/from-/shadow-` 회색 **32건(13파일)**이 CI 초록불 뒤로 누출됨을 canonical(전 prefix)이 검출 → gs PR #155로 리트로핏(Silver→허용hex, 구조→토큰, 가드레일 broaden). ② **off-system은 회색만 아님** — amber/orange 251건 잔존(canonical 가드레일도 회색만 잡음 → 비-회색 팔레트 broaden 검토). P-002 status=tentative, **N≥2 충족(gamblescan 실세계 + canonical) → C-NNN 승급 후보(사람 승인 대기)**.
- 2026-06-24: **METH-048 백서·온보딩에 코드 품질 가드레일 통합** — 지침 19(METH-047)를 standalone에서 *방법론 표준 서사*로 통합(사용자 지시). `방법론_백서_가이드.md` §5 "코드 품질 craft(Guardrails by Construction)" + §7 워크플로 day-1 가드레일·lint 게이트 / **`WHITEPAPER.md`(헌법) §8-5 신규 운영 원칙**(AI 안전+코드 품질 횡단) + 부록A + v0.3.0 / `HOW_TO_APPLY.md` §5 Fullstack 게이트. 백서 변경이라 **Class C·ADR-003 신설**(사용자 지시=승인). PR 대기.
- 2026-06-24: **METH-047 클린아키텍처·클린코드 지침 19 신설 (PR #36 머지)** — GambleScan REFACTOR-CLEAN(~50 PR) 회고 역주입. 4 코드 가드레일(레이어경계·no-explicit-any·no-console·max-lines=400)·래칫·4-레이어·god파일 분할·day-1 체크리스트. 지침 17 §4.2의 코드 품질 인스턴스화. Class A.
- 2026-06-24: **METH-046 sync mirror-delete 버그 픽스 (PR #35 머지)** — sync가 상류에 없는 다운스트림 고유 파일(ai-icons `20_guides/04`)을 조용히 삭제하던 데이터손실 차단. prune을 `--prune` opt-in으로(기본 보존+경고). Class A.
- 2026-06-24: **METH-045 방법론 백서 겸 가이드 (PR #34 머지)** — 철학+거버넌스+기획 craft+25 템플릿/6모드+워크플로 공유용 종합본. 레포 `10_foundation/방법론_백서_가이드.md`(11섹션) + Notion In-spire 하위 페이지(app.notion.com/p/3891a2ebe06a812aa1f8cd6b79e2ae20).
