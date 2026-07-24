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

### METH-115 · ship push 반영 검증 (origin HEAD 대조)
- **notes**: 2026-07-24. Class A. ai-icons에서 push 유실 사고(ICONS-365) — 백그라운드 PR 머지로 원격이 앞서가 push가 non-fast-forward 거부됐는데 ship이 exit code만 보고 "완료" 보고, 16커밋이 로컬에만 쌓여 배포 정지. 다운스트림 패치(ICONS-366)를 업스트림에 이식: push 후 `git ls-remote origin <branch>`로 원격 HEAD를 로컬 HEAD와 대조 — 불일치/미존재면 fail(rebase 안내), 조회 불가면 "반영 미검증" 경고, 성공 시 반영 SHA 출력. methodology.py는 shared_paths → 다음 sync-all에서 전 다운스트림 전파(ai-icons는 기적용). 테스트 21/21. branch-first(fix/ship-push-verify).

### METH-114 · boot HANDOFF 파서·스캐폴드 템플릿 정합
- **notes**: 2026-07-23. Class A. boot의 "Working on" 파서(볼드만 기대) ↔ init 스캐폴드 템플릿(비볼드 생성) 불일치로 새 다운스트림 boot가 "(미기재)" 표시(invest-ops friction에서 발견). 파서를 `_handoff_working_on` 헬퍼로 추출해 볼드·비볼드 양쪽 허용, 템플릿은 실사용 형식(볼드)으로 정합, `tests/test_boot_handoff.py` 5종(템플릿↔파서 회귀 가드 포함). methodology.py·templates 둘 다 shared_paths → 다음 sync-all에서 전 다운스트림 자동 전파. branch-first(fix/boot-handoff-working-on-parser).

### invest-ops 부트스트랩·12번째 다운스트림 등록
- **notes**: 2026-07-23. Class A. 민법상 투자조합 운영 repo 신규 생성 — `init --type planning-only`, Mode: planning, private. 딜 분석 standing SOP + deal-memo 고유 템플릿 + ADR-0001(invest-trading repo 분리·투자 도메인 Class C 확장: 출자 실행/조합원 커뮤니케이션/외부 공유/실계좌 주문). INV-001~003 시드, 로컬 main 2커밋(원격은 대표 승인 대기). sync-all 발견 ✓. 마찰: 스캐폴드 HANDOFF "Working on" 볼드 형식이 boot 파서와 불일치 → Open Issue + 태스크 칩. grooman이 이 머신 스캔에 없음 → Open Issue. branch-first(chore/bootstrap-invest-ops).

### grooman 방법론 적용·11번째 다운스트림 등록
- **notes**: 2026-07-22. Class A. 기존 Next.js14+Supabase 앱에 v4.0 retrofit(별도 세션, grooman PR#1). `init` non-empty 거부 → staging init 후 복사, 구 CLAUDE.md 보존·`.gitignore` 병합. 관리 다운스트림 **10→11곳**(sync-all 자동 발견). 소스 HANDOFF/checkpoint 정합화(이 branch: chore/register-grooman-downstream). grooman 내부 작업(retro-ADR 3건·GRM-010)은 grooman 인스턴스가 정본. 마찰→METH-113 백로그. branch-first.


> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
