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

### METH-137 · 캡슐 트리아지 3회차 2026-08-20 — 신규 5건 전량 종결
- **mode**: fullstack / **change-class**: A / **owner**: Human(판정) + AI(반영)
- **acceptance criteria**:
  - [x] `collect --apply` — 신규 5건 적재(원장 16→21), icons 미러 6repo 동일 id dedup
  - [x] 5건 판정 사람 확정(2026-08-20) — **유효 5 · 이미 반영 0 · 만료 0**. 초안: `40_dev/snapshots/2026-08-20_캡슐-트리아지-판정초안.md`
  - [x] 유효분 반영 — 지침 05 v3(§9b 배포 문서 작성 규율 6항) · 지침 23 v3(§4b 공개 주장 릴리스 표면 매트릭스) · 훅 timeout(run_guarded 폴링 감시자·fail-closed·우회 friction 기록 안내) · `land` 오진 수정(`_pr_merge_info` 머지/로컬정리 분리·checkout rc 검사·`--no-sync`·squash SHA maincheck) · catalog P-002(소비자 표면 카피 4원칙)
  - [x] negative case 실효 증명 — land 가짜 gh 하네스 A/B/C · 훅 타임아웃 D1~D4 (지침 23 §1-3)
  - [x] `_inbox` 정리 — 5건 삭제, 원장 21건 유지
  - [x] PR #146 land 착지(**maincheck squash 0e1a6aef ✓** — 새 land 코드가 첫 실전에서 squash SHA 판정) → 전파 **11/11 repo push + origin 실내용 대조 ✓**(guide05 §9b·guide23 §4b·run_guarded — icons 계열 worktree 5곳은 icons origin 공유로 자동 커버) → 훅 3 repo(ai-icons·invest-ops·lifeManager) `--force` 재설치·run_guarded 확인
- **notes**: 캡슐 루프 3회차(1회차 METH-128·2회차 METH-131). gamblescan 2건 id 접두어 `gamblescan-p0-pr__`(워크트리명) 형식 경고 — 발신 시점 id 검증 부재, 후속 후보. land 오진 3지점(4/6 rc 일괄·5/6 checkout rc 무시·6/6 HEAD 기준)은 코드 재현 후 수정 — gamblescan#309 실사고의 근본 폐색.

### METH-116 · 지침 22 정련 — 콘텐츠·디자인 분리 (텍스트 덱 = SSOT)
- **mode**: fullstack
- **change-class**: A
- **owner**: AI + Human
- **notes**: 2026-07-25. 신설분(지침 22 + 스켈레톤 `ir-deck-build`)은 PR #112 로 이미 land — 본 항목은 그 뒤 사용자 피드백으로 이어진 **정련**. 텍스트 md 덱을 지속 SSOT 로 승격하고 콘텐츠(스토리라인→슬라이드 텍스트 구조화)를 디자인보다 먼저 닫는 모델로 §2 를 6단계 재편(P0 데이터·P1 스토리라인·P2 텍스트구조화·P3 디자인후보 탐색·P4 빌드검증·P5 파생), §3 "후보 탐색 후 고정"·§8 재작성. 스켈레톤: `contract.py` `THEMES` 후보 레지스트리+`apply_theme()`(호출시점 late-bind), `build.py --theme`/`--candidates`(테마별 대표 슬라이드 비교 렌더), `deck.template.md`(SSOT 2층). 검증: 3모드 동작·테마 색 실제 교체(A네이비·B화이트·C딥차콜)·geometry 통과. branch-first(`docs/guide-22-ir-deck-methodology`). **main 리베이스(2026-08-22)**: 그 사이 land 된 v2(METH-128)·v3(METH-129)와 병합 — 불변규율을 6개로 통합(v2 규율 4 파일=유일소스·5 안정 슬라이드 ID 승계), P3 리드백 게이트를 신 P4 행에 이관, 변경이력 v1~v3 보존 + v4 추가.

### METH-131 · 캡슐 트리아지 2026-08 — 15건 전량 종결
- **mode**: fullstack / **change-class**: A / **owner**: Human(판정) + AI(반영)
- **acceptance criteria**:
  - [x] 15건 판정 — **유효 13 · 이미 반영 1 · 만료 0**(사람 확정 2026-08-07). 초안: `40_dev/snapshots/2026-08-07_캡슐-트리아지-판정초안.md`
  - [x] 유효분 반영 — 도구 3(`land`·hook 참조전용 면제·build-guard 스코프+tsc 폴백·Done 주장 경고) · 지침 23 v2 5조항 · 지침 19 v3 §8b · 지침 07 부작용 범위 봉쇄 · 지침 24 v2 §3b
  - [x] `_inbox` 정리 — 14건 삭제, **원장 16건 유지**(재수거 방지)
  - [x] 전파 **12/12** — main 7곳 직접·비-main/dirty 4곳 worktree, 전부 origin 대조(지침 23·19·07·24 + 도구 5항목)
  - [x] 훅 재설치 — 설치된 3개 repo(ai-icons·invest-ops·lifeManager)에 `hooks install --force`, 참조전용 면제 반영 확인
- **notes**: 캡슐 루프 2회차(1회차는 METH-128). **판정 중 근거 정정 1건**: 초안에 `tool/hooks` 를 "이 세션 22회 우회로 실증"이라 적었으나 실측 결과 훅 설치 repo 는 11개 중 3개뿐이고 그 3개 전부 이미 sync 면제를 갖고 있었다 — 내 우회는 측정 없는 예방적 우회였다. 판정(유효)은 코드 판독 근거로 유지: delete/tag push 는 여전히 `wrap --strict` 를 통과해야 한다. **승급 2건**: `perf-ab-sampling`·`no-kill-foreign-process` 를 이번 세션에 지침 29·28(모드 전용)에 넣었던 것이 잘못 — 캡슐이 지목한 23·07 로 옮기고 모드 지침은 참조만 남겼다.


### METH-136 · 운영 모드 키워드 트리거 — 지침 28·29 로딩 경로 연결
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] 지침 01 §5.11 신설 — 운영 모드 라우팅 표(키워드 → 지침 28/29/07/land) + 경계 disambiguation 3항
  - [x] CLAUDE.md·AGENTS.md §2 를 *서술*에서 **동작 지시**로 전환 — "키워드가 나오면 지침 본문을 먼저 로드한 뒤 착수, 요약만 보고 시작 금지"
  - [x] 전파 **12/12** — main 6곳 직접·비-main/dirty 5곳 worktree, 전부 origin 대조(CLAUDE.md 트리거 + 지침 01 §5.11)
- **notes**: 사용자 질문("자율주행·실험모드를 키워드로 쓰면 그 모드 규칙을 찾아 시행하는가")에서 도출된 실제 갭. **기존 상태는 절반만 작동** — CLAUDE.md 요약은 매 세션 자동 로드되지만 지침 28/29 *본문* 로드는 AI 판단에 의존했고, 지침 01 라우팅 표(§5.9 기획서·§5.10 작업 모드)에는 **운영 모드 축이 아예 없었다**. 요약(3~4줄)만으로 8시간 루프를 돌리면 조건·정지 규칙이 빠진다. 핵심 안전장치: "제약 없이 빨리"라는 속도 요구만으로 실험 모드가 켜지지 않게 — **4조건 확인이 선행**이고 어긋나면 일반 모드로 진행하며 사용자에게 알린다.


### METH-135 · 자율주행 모드 — 지침 29 신설 (장시간 자율 턴)
- **mode**: fullstack / **change-class**: A (근거: ADR-004) / **owner**: AI
- **acceptance criteria**:
  - [x] 지침 29 신설 — 기계강제/운영계약 구분·사전 요구 4종·P0 기획 환산·4단계 루프·정지 조건 7종·stop report
  - [x] CLAUDE.md·AGENTS.md §2 진입 규칙, `20_guides/README.md` 카탈로그 등록
  - [ ] **첫 실주행으로 검증** — 사이클 45~90분 환산치가 실제와 맞는지, 정지 조건이 실제로 발동하는지 실측 → 지침 29 v2에 환류
  - [ ] 무인 실행용 권한 사전 allowlist 정리(settings.json) — 없으면 첫 권한 프롬프트에서 정지
- **notes**: 8시간 자율주행 요청. **가능하되 조건부** — 지침 07 §5.2대로 wall-clock은 런타임 미강제(반복수·비용·권한범위 3개만 강제)라 시간은 *사이클 환산 단위 + 사람이 돌아올 약속*으로만 쓴다. 이게 "시간 다 채울 필요 없음" 요구와 정확히 일치. **METH-134가 선결 조건** — 샌드박스 밖 자율주행은 Class B/C에서 반복 정지한다. 실질 blocker 3종: 권한 프롬프트(최대)·컴팩션·Class 게이트.
  - [x] 전파 종결 **12/12** — sync-all(main 7곳 직접·비-main/dirty 4곳 worktree·icons-vault 는 icons 워크트리라 자동 커버), 전부 origin 대조


