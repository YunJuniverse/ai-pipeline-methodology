# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

## Blocked

## Done

### METH-056 · Compaction 프로토콜 구현 (RFC-002 R2)
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). **로드맵의 첫 실제 구현** — 진단·문서화를 넘어 약점(런타임 compaction 규율)을 실제로 고침. `20_guides/06_컨텍스트_컴팩션_프로토콜.md` 신설(보존/폐기 규칙·checkpoint를 compaction 경계 인계로 확장·pre-compaction 체크리스트). CLAUDE/AGENTS 운영 규칙에 "컴팩션 경계 트리거" 편입(부팅 로드·준수 강제). README 06 + RFC-002 R2 ✅구현 표시. 다음: guide 06 sync, P1(R1 Reflect/Learn), P3(온보딩 다이어트).

### METH-055 · RFC-002 draft→accepted 비준
- **notes**: 2026-07-08. Class A. **PR #45 머지 완료**. #44(2026-Q3 회고) 머지 = 사람 게이트 → `70_meta/rfc/RFC-002` status=accepted + accepted_via(#44)·relates_to·비준 blockquote. 별도 ADR 미승급(RFC-001 선례). 발전 로드맵이 진화 백로그로 확정.

### METH-054 · 첫 분기 회고(2026-Q3) + MP-003
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). 백서 §9 ROI 게이트 첫 발화(~9주 초과). `70_meta/retrospectives/2026-Q3_first-methodology-review.md` — 5섹션. **정직 모드**: 지표 인프라 미달(관찰 41/100·Catalog 1/5) → README 규칙대로 다음 분기 P1=지표 인프라+thinktank 존폐(a되살림/b공식화, b권장). P2=compaction(RFC-002 R2, Class A). P3=온보딩 밴드 다이어트(무게 감사 MED). **RFC-002 draft→accepted 권장**(이 회고 머지=비준). 스택-PR 고아화 교훈을 `70_meta/catalog/_pending/MP-003_stacked-pr-orphan.md`로 캡처(N≥2 재발 시 MC 승급). 다음: P2 compaction(METH-056)부터.

### METH-053 · guide 04→05 리넘버 + 식별자 예약범위 + RFC-002 복구
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). ① 상류 산출물 채널 분리 지침 `04`→`05` 이동 — ai-icons·icons-invest가 커스텀 `04_프로젝트_문서_보관_및_분류`(doc_id guide-04) 점유 중이라 sync 시 충돌. guide 02 **§8 신설**: 지침 번호 예약(상류 00–89 / 다운스트림-커스텀 90–99), 레거시 비준수 04 마이그레이션 대상. CLAUDE/AGENTS/README 참조·guide 05 doc_id·heading 갱신, guide 02 v2. ② **RFC-002 복구** — METH-052(#42)가 스택 PR 함정(base=이미 머지된 meth-051)으로 main 미도달·고아화 → 파일 복원·재포함. 교훈: 스택 PR에서 base PR 먼저 머지 시 stacked PR은 stale 브랜치로 머지됨(retrospective·MC 후보).

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~053 (2026-05~07). METH-051 산출물채널분리(guide 05, #41)·052 SOTA평가/RFC-002·053 리넘버+RFC-002복구 포함. 상세는 git log --grep="METH-" 및 PR #5~#45, 40_dev/snapshots/ 참조. -->
