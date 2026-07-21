# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

### METH-113 · 기존 앱 retrofit 지원 (init non-empty 우회 자동화)
- **mode**: fullstack
- **change-class**: A
- **owner**: AI + Human
- **acceptance criteria**:
  - [ ] `init`이 비어있지 않은 디렉터리를 거부하는 현재 동작을, 기존 앱에 방법론을 얹는 공식 경로로 보완 (예: `methodology.py apply-existing <path>` 또는 `init --into-existing`)
  - [ ] 충돌 파일(CLAUDE.md·.gitignore) 자동 보존/병합 — 기존 CLAUDE.md는 `00_briefs/reference/`로 이관, .gitignore는 관리 블록 append
  - [ ] 코드 폴더 관례 감지(예: `app/` 존재 시 빈 `src/` 생성 생략)
- **notes**: grooman(11번째 다운스트림) 적용 시 임시 staging init 후 수동 복사·병합으로 우회한 마찰에서 도출. 관찰로그 `2026-07-21_grooman-methodology-bootstrap.md`(friction: init-nonempty-refusal) 참조. 기존 앱을 방법론으로 편입하는 수요가 재발하면 승급.

## Ready

## InProgress

## Blocked

## Done

### grooman 방법론 적용·11번째 다운스트림 등록
- **notes**: 2026-07-22. Class A. 기존 Next.js14+Supabase 앱에 v4.0 retrofit(별도 세션, grooman PR#1). `init` non-empty 거부 → staging init 후 복사, 구 CLAUDE.md 보존·`.gitignore` 병합. 관리 다운스트림 **10→11곳**(sync-all 자동 발견). 소스 HANDOFF/checkpoint 정합화(이 branch: chore/register-grooman-downstream). grooman 내부 작업(retro-ADR 3건·GRM-010)은 grooman 인스턴스가 정본. 마찰→METH-113 백로그. branch-first.

### cafe24 sync — 전 다운스트림 배포 종료
- **notes**: 2026-07-15. Class A. PR base=main 대기(chore/sync-cafe24). 사용자 "준비완료"(WIP landing) → clean 재확인 → METH-106 절차(main 체크아웃→sync→push→피처브랜치 복원, add -A로 루트 shared 포함). 커스텀 guide 6개 보존. **관리 10곳 전부 방법론 payload 해시 동일** 검증. 버전스탬프 차이는 라이브파일 전용 커밋(#103·#104) 탓 cosmetic. branch-first.

### sync-all 보류분 처리 (ai-icons·cafe24)
- **notes**: 2026-07-15. Class A. PR base=main 대기(chore/sync-ai-icons-residual). ai-icons: WIP(tier2_ai_text.py=프로젝트 코드) 보존한 채 방법론만 sync·push(add -A→WIP reset로 안전 스테이징). main==origin 5a2547c. cafe24: 피처브랜치+skin184 활성 WIP 91건 → 사용자 결정으로 그 세션 위임(미처리). 관리 10곳 중 9 최신·1 보류. branch-first.

### sync-all 다운스트림 전파 (88b9382)
- **notes**: 2026-07-15. Class A. PR base=main 대기(chore/sync-all-propagate). 방법론 최신(graph-viz·dagre·대시보드 통합·슬림화)을 다운스트림 일괄 전파. `sync-all --apply`(가드 skip dirty·비-main) → main-clean 4곳 처리; clean 피처브랜치 4곳(gamblescan·icons·lifeManager·tshome)은 main 체크아웃→sync→push→복원. 8/10 반영(main==origin 0/0). 보류 2: ai-icons·cafe24(dirty WIP). friction: 타깃 스테이징이 루트 shared(ONBOARDING.md) 누락→추가 커밋. branch-first.


> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
