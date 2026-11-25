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

### METH-153 · 산문 규칙 슬림화 목록 (ADR-007 D3)
- **mode**: fullstack / **change-class**: C(목록 승인 필요) / **owner**: AI + Human
- **acceptance criteria**:
  - [ ] CLAUDE.md §2 규칙을 «도구가 fail-closed 로 막는가»로 분류한 표 — 도구 강제(한 줄 포인터로 축소) / 산문 유지(최근 전수조사 위반·재발 근거 있음) / 지침 본문으로 내림
  - [ ] 표와 목표 분량을 사용자에게 제시 → 승인 후에만 CLAUDE.md·AGENTS.md 수정
- **notes**: ADR-007 은 방향만 정했다. 미적용 repo 용 얇은 판 제안 여부는 이 결과물을 보고 판단(ADR-007 Open questions).

## InProgress

## Blocked

## Done

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

### METH-151 · 전수조사 판단 7지점 반영 (ADR-006)
- **mode**: fullstack / **change-class**: C(사람 승인 ADR-006) / **owner**: AI
- **acceptance criteria**:
  - [x] ADR-006 — D1~D7 승인 박제(2026-11-09 채팅)
  - [x] D1 checkpoint 세션별 절 — CLAUDE/AGENTS 역할표·③·지침 30 v5·템플릿 · `rotate --checkpoint` 절 단위 회전 · 절 4개+ 경고
  - [x] D2 land 머지 기록 직접 커밋(`chore(land):`, TODO·HANDOFF 만, push 거부 시 작업트리 보존) · `--no-record` · CLAUDE «no direct push» 예외 명기
  - [x] D3 같은 날 관찰로그 갱신 인정 · 지침 03 v4
  - [x] D4 공유 가드 미추적 신규만(`-uall` — 새 디렉터리 접힘 결함 동시 수정)
  - [x] D5 land `required_checks`
  - [x] D6 C-004~006 승급
  - [x] 테스트 7건(tests/test_meth151_decisions.py) · 전체 127/127
  - [x] PR 머지 + maincheck → Done 전이
- **notes**: 이 PR 의 land 가 D2 를 첫 실주행한다 — 이 항목이 Done 으로 자동 이동하면 실증. 전파(D7)는 그 뒤.
- **landed**: PR #186 · main `69b956ca` · 2026-11-09 (land 자동 기록)
- **전파**(D7, 2026-11-09): 13/13 — origin 실내용 5항목 대조 ✓ · ai-icons 깨진 헤더 선복구 ai-icons#469

### METH-150 · 전수조사 판단 7지점 — 운영 규칙 변경(사람 결정 대기)
- **mode**: fullstack / **change-class**: C / **owner**: Human
- **resolved**: 2026-11-09 사용자 채팅 — 7건 모두 권고안 → **ADR-006** · 반영 METH-151
- **acceptance criteria**:
  - [x] D1 checkpoint 모델(세션별 절 prepend 공식화 vs 덮어쓰기 유지)
  - [x] D2 머지 기록 PR(land 가 머지 후 Done 전이를 main 에 기록 — 직행 예외, ADR 필요 vs 현행)
  - [x] D3 관찰로그 의무 빈도(연속 PR·재시도는 기존 로그 갱신 인정 vs 현행)
  - [x] D4 공유 체크아웃 가드 범위(미추적 신규 파일만 열거 vs 현행)
  - [x] D5 land 필수 체크 지정(`required_checks`) · 기계 증거 Class B 하위 등급
  - [x] D6 catalog 승급 P-010·P-011·P-013 → C-004~006
  - [x] D7 METH-149 다운스트림 전파 여부·시점
- **notes**: 근거 수치는 스냅샷 §1 Q2·Q3·Q7. METH-147 의 «checkpoint 세션별 분리 파일» 비채택과 D1 은 다른 안(파일 1개·절 단위).






### METH-149 · 전레포 30일 전수조사(2026-10-10~11-09) 반영
- **mode**: fullstack / **change-class**: A / **owner**: AI(조사·반영) + Human(판단 METH-150)
- **acceptance criteria**:
  - [x] 30일 활동 9개 repo 읽기 전용 조사(에이전트 9기) — 커밋 2,187·friction 260건·≈3,049분. 스냅샷 `40_dev/snapshots/2026-11-09_전레포-30일-전수조사.md`(패턴 Q1~Q14)
  - [x] 도구 결함 15건 반영(T1~T15: 사이즈 린트 글자 수·줄 길이·Recent·Done 밖 ✅ · 칸반 제목 부연·깨진 헤더 · phase 오값 거부 · repeat_of `new`→null · agent 계열 · reserve 접두어 추론·아카이브·0 채움 · land TODO change-class·스냅샷 제외·push 확인·`--match-head-commit` · `ship --land` PR 생성 · ship 대용량 신규 파일 · ADR 두 형식 · AGENTS.md 중복) — negative case 14건(옛 코드 13 실패), 전체 120/120
  - [x] 지침 8개 개정 — 03 v3·05 v6·08 v3·19 v6·23 v7·24 v6·29 v2·30 v4 · README v4.9
  - [x] pending P-010~014 · 상류 SOP `SOP_external-sheet-edit.md`(shared_paths 등록)
  - [x] PR 머지 + maincheck → Done 전이 — PR **#185** · main `86a11ed7` ✓
  - [x] 다운스트림 전파 — METH-151 결정 반영분과 함께 한 번에(methodology:ADR-006 D7)
- **notes**: 직전 조사(07-29) 대비 스택-PR 사고 0·cafe24 friction 기록 정착·크롤 페널티 0 은 개선. 남긴 도구 후보는 스냅샷 §2 말미.


