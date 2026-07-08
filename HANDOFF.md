# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-053 **guide 04→05 리넘버 + 식별자 예약범위 + RFC-002 복구**. ① 상류 산출물 채널 분리 지침 04→**05** 이동(ai-icons·icons-invest 커스텀 04 doc_id 충돌 회피) + guide 02 §8 신설(지침 번호 예약: 상류 00–89 / 다운스트림-커스텀 90–99). ② **스택 PR 함정으로 main 미도달한 RFC-002(METH-052) 복구** — #42가 이미 머지된 base 브랜치로 들어가 고아화됨. Class A. PR 대기(main 직접, 스택 금지).
- **Current mode**: fullstack
- **Next TODO**: ① `70_meta/retrospectives` 첫 엔트리(무게 감사 HIGH + 스택-머지 고아 교훈 + guide-04 충돌 교훈). ② guide 05 다운스트림 sync(충돌 해소됨). ③ RFC-002 draft→accepted → R2 compaction.
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

- 2026-07-08: **METH-053 guide 04→05 리넘버 + 식별자 예약범위 + RFC-002 복구 (Class A)** — ① 상류 산출물 채널 분리 지침을 `04`→`05`로 이동(ai-icons·icons-invest가 커스텀 `04_프로젝트_문서_보관_및_분류` 점유 → doc_id 충돌 회피). guide 02 §8 신설: 지침 번호 예약(상류 00–89 / 다운스트림-커스텀 90–99), 레거시 비준수 04는 마이그레이션 대상. CLAUDE/AGENTS/README 참조 05로 갱신. ② **RFC-002 복구** — METH-052(#42)가 스택 PR 함정(base=이미 머지된 meth-051 브랜치)으로 main 미도달·고아화 → 파일 복원해 main 직접 PR에 재포함.
- 2026-07-08: **METH-052 SOTA 평가 + RFC-002 발전 로드맵 (Class A)** — 무게 감사(에이전트 16개, MIXED: 코어 정당·군살 국소[온보딩 밴드 중복·휴면 thinktank·~9주 초과 ROI 게이트]) + SOTA 웹 리서치(harness/context/loop engineering·ERL: 코어가 정합/선행, 약점=Reflect/Learn 자동화+compaction·budget). `70_meta/rfc/RFC-002`(draft, R1~R6). ※#42 고아화로 main 미반영 → METH-053에서 복구.
- 2026-07-08: **METH-051 산출물 채널 분리 지침 신설 (Class A, PR #41 머지)** — 다운스트림(ai-icons) 반복 피드백("작업 메타를 산출물에 넣지 마라", 06-19→07-06→07-07 + 명시승인)을 에이전트 토론(찬반→반론→심판)으로 상류 격상 판정. 결론: 백서 헌법 직행이 아닌 전-도메인 지침. `20_guides/04_산출물_채널_분리_규칙.md`(청중 축=외부 무맥락 공유 여부로 트리거, 주제 축=changelog류 예외, 메타는 삭제 아닌 라우팅) + CLAUDE/AGENTS File Roles "Output channel" 행 + README 카탈로그(02·03·04). 백서 미수정(제0·제2·§8-4·§8-5 인용만). 강제 grep 래칫은 §7 스펙만(fail-open 금지).
- 2026-06-29: **METH-050 P-002 → active `C-001` 승급 (사용자 승인)** — N≥2(gamblescan 실세계 + canonical) 근거로 자가발전 루프 1회전 완결. ① `50_resources/catalog/C-001_frontend-design-tokens.md`(active, P-002 삭제) ② 스켈레톤 `bakes-in.json`에 C-001 합류 → `skeleton build`로 lock/README 재생성(이제 새 프로젝트 자동 주입) ③ canonical 가드레일을 *전 prefix × 전 Tailwind 팔레트 family*로 broaden(교훈②, amber/blue/rose 더미 검출 확인) ④ 지침20 v2 + design-system.md + README 갱신. Class A.
- 2026-06-29: **METH-049 gamblescan 실세계 검증 — 패턴 교훈 2건 + P-002 N≥2** — canonical 스켈레톤을 gamblescan(독립 구현, hex 3,030 codemod 완료)에 교차검증. ① gamblescan 가드레일이 `text-` 회색만 검사 → `bg-/border-/from-/shadow-` 회색 **32건(13파일)**이 CI 초록불 뒤로 누출됨을 canonical(전 prefix)이 검출 → gs PR #155로 리트로핏(Silver→허용hex, 구조→토큰, 가드레일 broaden). ② **off-system은 회색만 아님** — amber/orange 251건 잔존(canonical 가드레일도 회색만 잡음 → 비-회색 팔레트 broaden 검토). P-002 status=tentative, **N≥2 충족(gamblescan 실세계 + canonical) → C-NNN 승급 후보(사람 승인 대기)**.
- 2026-06-29: **METH-049 프론트엔드 디자인 토큰 시스템 — 지침 20 + 스켈레톤 + P-002 (PR #38 머지)** — 색 하드코딩·드리프트 방지 4기둥(@theme 시맨틱 토큰·cn+프리미티브·색 가드레일·제약문서). 지침 17 §4.2를 시각 품질에 인스턴스화(19=구조, 20=시각). 다운스트림 전파 3/5(ai-icons·icons·cafe24).
- 2026-06-24: **METH-048 백서·온보딩에 코드 품질 가드레일 통합** — 지침 19(METH-047)를 standalone에서 *방법론 표준 서사*로 통합(사용자 지시). `방법론_백서_가이드.md` §5 "코드 품질 craft(Guardrails by Construction)" + §7 워크플로 day-1 가드레일·lint 게이트 / **`WHITEPAPER.md`(헌법) §8-5 신규 운영 원칙**(AI 안전+코드 품질 횡단) + 부록A + v0.3.0 / `HOW_TO_APPLY.md` §5 Fullstack 게이트. 백서 변경이라 **Class C·ADR-003 신설**(사용자 지시=승인). PR 대기.
- 2026-06-24: **METH-047 클린아키텍처·클린코드 지침 19 신설 (PR #36 머지)** — GambleScan REFACTOR-CLEAN(~50 PR) 회고 역주입. 4 코드 가드레일(레이어경계·no-explicit-any·no-console·max-lines=400)·래칫·4-레이어·god파일 분할·day-1 체크리스트. 지침 17 §4.2의 코드 품질 인스턴스화. Class A.
- 2026-06-24: **METH-046 sync mirror-delete 버그 픽스 (PR #35 머지)** — sync가 상류에 없는 다운스트림 고유 파일(ai-icons `20_guides/04`)을 조용히 삭제하던 데이터손실 차단. prune을 `--prune` opt-in으로(기본 보존+경고). Class A.
- 2026-06-24: **METH-045 방법론 백서 겸 가이드 (PR #34 머지)** — 철학+거버넌스+기획 craft+25 템플릿/6모드+워크플로 공유용 종합본. 레포 `10_foundation/방법론_백서_가이드.md`(11섹션) + Notion In-spire 하위 페이지(app.notion.com/p/3891a2ebe06a812aa1f8cd6b79e2ae20).
