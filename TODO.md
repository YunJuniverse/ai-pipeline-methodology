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

### METH-130 · UI repo 방어층 설치 — axe·간격 검사·프리미티브 (repo 과제 묶음)
- **mode**: fullstack
- **change-class**: A / **owner**: AI(각 repo 세션) + Human
- **acceptance criteria**:
  - [ ] UI 보유 repo(tshome·talmo-com·lifeManager·icons-marketing·gamblescan·icons)에 각각: ① axe-core PR 차단 게이트 설치 ② 인접 요소 간격 검사 스크립트 ③ 절대색 차단을 기존 토큰 가드레일에 추가 ④ Section/Stack 프리미티브 내장 간격 확인(기본 패딩 0 구조면 교정)
  - [ ] 각 repo 완료 시 더미 위반 주입으로 게이트 실효 증명(지침 23 §1-3)
- **notes**: 2026-07-29 사용자 반복 실수 환류(다크 배경+검은 텍스트·패딩 누락 텍스트 붙음) — 지침 20 v3(§4 절대색 차단·§9.5 3층 방어)로 규칙화 완료, 이 항목은 **각 repo 실설치**. 규칙은 sync로 전파되지만 게이트 설치는 repo별 작업이라 분리. 해당 repo 세션 착수 시 이 항목 참조. **규칙 전파(07-29) 완료 11/11** — 잔여는 설치뿐.

## Ready

## InProgress

## Blocked

## Done

### METH-155 · ship `--no-test --no-build` 조합 NameError 수정
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] 패키지 매니저 판정을 `_pkg_manager()` 로 빼 test·build 단계 진입 전에 한 번 정한다 — 두 단계를 모두 건너뛰어도 `tsc --noEmit` 최소 검증이 죽지 않는다
  - [x] npm 은 `npm exec -- tsc --noEmit`(`--` 없으면 `--noEmit` 이 npm 옵션으로 먹힌다)
  - [x] 회귀 테스트 3 — 매니저 판정 · tsc 명령 · `manager` 가 조건 블록 안에서 정해지면 실패. 전체 스위트 통과
- **notes**: 다운스트림 세션이 겪고 «상류에서 고칠 일»로 넘긴 건(2026-11-26). `package.json`·`tsconfig.json` 둘 다 있는 repo 에서만 난다. 실제 Node repo 에서 ship 을 끝까지 돌려 보지는 않았다. 전파는 머지 직후 활동 repo 에 sync — 결과는 각 repo 의 `.methodology-version` 적용 커밋으로 확인한다.

### METH-153 · CLAUDE.md §2 슬림화 (ADR-007 D3)
- **mode**: fullstack / **change-class**: C(사람 승인 — 분류표 채팅 승인 2026-11-25) / **owner**: AI
- **acceptance criteria**:
  - [x] §2 규칙 20개 분류표(`40_dev/snapshots/2026-11-25_claude-md-규칙-분류표.md`) — 도구가 막음 4 · 산문 유지 4 · 지침으로 내림 6 · 원칙 6
  - [x] 지우기 전 정본 대조 — 지침에 없던 절차(마감·ship·land·스택-PR·Blocked·export)는 **지침 31 신설**, 프롬프팅 기록은 03 §5.3, SOP·캡슐 요청 절차는 각 README 로 이관
  - [x] CLAUDE.md·AGENTS.md §2 재작성 — 11.3KB → 3.8KB(−66%), 파일 전체 18.6KB → 11.1KB · 테스트 전체 통과
- **notes**: 표의 목표(2.9KB)보다 0.9KB 크다 — 키워드 트리거와 부팅 줄을 덜 줄였다. 준수율 변화는 측정하지 않았다. **전파 7/7(2026-11-25)** — 활동 repo 에 브랜치 PR → land, origin 대조(§2 3.8KB·지침 31·03 §5.3·AGENTS 동일·적용 커밋 `dc58a54`). 휴면 repo 는 미전파.

### METH-154 · ADR-007 전파 — 활동 repo 만
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] METH-152 가 main 에 도달한 뒤 `sync-all --apply`(휴면 repo 자동 skip) + 다른 루트의 활동 repo 개별 sync — 다른 세션이 도는 repo 는 격리 워크트리
  - [x] 전파된 repo 의 origin 에서 CLAUDE.md «머지 기록 커밋·PR 을 만들지 않는다» 문구와 land 기록 코드 부재 대조
- **notes**: 2026-11-25 활동 repo 7/7 — repo 마다 origin/main 격리 워크트리 → sync → 브랜치 PR → land(Class A·실패 체크 0) → origin 대조(규칙 문구·직push 예외 삭제·기록 코드 부재·적용 커밋 `d809c27`). main 직접 push 는 권한 검사에 막혀 PR 경로로 전환. 휴면 6곳은 미전파(다음 세션 boot 가 알림).

### METH-152 · land 머지 기록 폐지 · 전파 축소 (ADR-007)
- **mode**: fullstack / **change-class**: C(사람 승인 ADR-007) / **owner**: AI
- **acceptance criteria**:
  - [x] ADR-007 — D1~D3 승인 박제(2026-11-25 채팅 «전부 채택»), ADR-006 Status 에 D2 대체 표기
  - [x] D1 land 기록 커밋 제거 — `_land_record`·`_land_record_todo` 삭제, `--no-record` 무동작 유지 · CLAUDE/AGENTS: Done 전이는 작업 PR 안에, «no direct push» 예외 삭제, §6 워크플로 순서
  - [x] D2 `sync-all` 휴면 skip(최근 30일 작업 커밋 0, sync 커밋 제외, `--include-dormant`·`--active-days`) · boot 상류 버전 차이 알림
  - [x] D3 방향 박제 → 실행은 METH-153
  - [x] 테스트 — 기록 코드 부재 1 · 활동 판정 2 · 상류 알림 1, 전체 스위트 통과
- **notes**: 근거는 2026-11-25 전 repo 30일 커밋 집계(ADR-007 Context). 전파는 METH-154.

