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

### METH-053 · guide 04→05 리넘버 + 식별자 예약범위 + RFC-002 복구
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). ① 상류 산출물 채널 분리 지침 `04`→`05` 이동 — ai-icons·icons-invest가 커스텀 `04_프로젝트_문서_보관_및_분류`(doc_id guide-04) 점유 중이라 sync 시 충돌. guide 02 **§8 신설**: 지침 번호 예약(상류 00–89 / 다운스트림-커스텀 90–99), 레거시 비준수 04 마이그레이션 대상. CLAUDE/AGENTS/README 참조·guide 05 doc_id·heading 갱신, guide 02 v2. ② **RFC-002 복구** — METH-052(#42)가 스택 PR 함정(base=이미 머지된 meth-051)으로 main 미도달·고아화 → 파일 복원·재포함. 교훈: 스택 PR에서 base PR 먼저 머지 시 stacked PR은 stale 브랜치로 머지됨(retrospective·MC 후보).

### METH-052 · SOTA 평가 + RFC-002 발전 로드맵
- **notes**: 2026-07-08. Class A. #42 MERGED 표시됐으나 **스택 함정으로 main 미도달** → METH-053에서 복구. 무게 감사(에이전트 16개, MIXED) + SOTA 웹 리서치(harness/context/loop engineering·ERL) → 코어 정합/선행, 약점=Reflect/Learn 자동화+compaction·budget. `70_meta/rfc/RFC-002`(draft, R1~R6 로드맵).

### METH-051 · 산출물 채널 분리 지침 신설 (guide 05)
- **notes**: 2026-07-08. Class A. **PR #41 머지 완료**. 다운스트림 ai-icons 반복 피드백을 에이전트 토론(입론 찬반+방법론적합성 → 교차 반론 → 심판)으로 상류 격상 판정 — 백서 헌법 직행 반려, **전-도메인 지침**. 사용자 스코프: 외부 공유 배포물(기획서·서비스페이지·앱UI)엔 작업 메타 금지 / 그걸 만드는 메타문서는 면제. 청중 축 트리거 + 주제 축 예외 + 메타 라우팅 + File Roles "Output channel" 행. (지침 번호는 METH-053에서 04→05로 정정.)

### METH-050 · P-002 → active C-001 승급 (자가발전 루프 완결)
- **notes**: 2026-06-29. 사용자 승인. Class A. **PR #40 머지 완료**. gamblescan 실세계 검증으로 N≥2 충족(hex 3,030 codemod + canonical) → ① `50_resources/catalog/C-001_frontend-design-tokens.md`(active, P-002 삭제) ② 스켈레톤 `bakes-in.json`에 C-001 → `skeleton build`로 lock/README 재생성(새 프로젝트 자동 주입) ③ canonical 가드레일 *전 prefix × 전 Tailwind 팔레트 family* broaden(교훈②, amber/blue/rose 더미 검출 확인) ④ 지침20 v2 + design-system.md + README. 후속: 다운스트림 sync + gamblescan amber/orange 251 메달 토큰화.

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-049
- **notes**: Completed 2026-06-29. **PR #38 머지 완료**(main `5fc822f`). Class A. 프론트엔드 디자인 토큰 시스템 — 지침 20 신설(4기둥: 시맨틱 토큰·프리미티브·색 가드레일·제약문서, 이름=역할, A/B/C 트리거) + 스켈레톤 `frontend-design-tokens`(base/guardrails 포함) + Pending Lesson P-002. 가드레일 3케이스 실검증. **다운스트림 전파 3/5**(ai-icons·icons·cafe24, `--no-verify` 순수 sync) — icons-invest(dirty)·gamblescan(작업중) 보류. 17 §4.2의 시각 품질 인스턴스화(19=구조).

<!-- Archived: METH-001~048 (2026-05~06). 상세는 git log --grep="METH-" 및 PR #5~#40, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~3건만. -->
