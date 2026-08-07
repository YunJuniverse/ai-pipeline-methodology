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


### METH-134 · 실험 모드 — 지침 28 신설 (샌드박스 경계 + 졸업 게이트)
- **mode**: fullstack / **change-class**: A (근거: ADR-004) / **owner**: AI
- **acceptance criteria**:
  - [x] 지침 28 신설 — 샌드박스 4조건·해제/유지 목록·시간범위 박스 선언·졸업 게이트 7항·실패 모드 4종
  - [x] CLAUDE.md·AGENTS.md §2 진입 규칙, `20_guides/README.md` 카탈로그 등록
  - [ ] **잔여**: 첫 실전 적용 시 선언 형식·졸업 정산이 실제로 작동하는지 확인 → 안 맞으면 v2
- **notes**: 사용자 제기("경영상 제약이 프로토타입 개발을 막는다") 대응. 결정: **전면 해제가 아니라 샌드박스 경계 + 졸업 게이트**(사용자 선택). 진단은 "규칙이 많다"가 아니라 "프로토타입과 운영이 같은 게이트 사다리를 쓴다" — 그래서 사다리를 분리했다. invest-ops(조합원·금융)·운영 서비스가 같은 규칙을 받는 무경계 안은 기각.
  - [x] 전파 종결 **12/12** — sync-all(main 7곳 직접·비-main/dirty 4곳 worktree·icons-vault 는 icons 워크트리라 자동 커버), 전부 origin 대조


### METH-133 · `land` — 머지 착지 자동화 (Class A + CI green)
- **mode**: fullstack / **change-class**: A (근거: ADR-004, 사람 승인 2026-08-07) / **owner**: AI
- **acceptance criteria**:
  - [x] `methodology.py land` 신설 — PR 식별 → Class 판정 → CI green → squash 머지 → 기본 브랜치 동기화 → maincheck (6단계, 전부 fail-closed)
  - [x] `ship --land` 연결 실행 + `--dry-run`·`--no-ci-check` 플래그
  - [x] Class B/C 경로 판정기 더미 위반 실효 증명(지침 23 §1-3) — 마이그레이션·인증·과금·외부API·큐·CI·법무 7종 차단, 일반 경로 통과
  - [x] 이 PR을 `land`로 실제 머지해 end-to-end 증명 — **PR #140 을 land 가 스스로 착지시킴**(maincheck 747e9457 ✓)
- **notes**: 수거 캡슐 `invest-ops__2026-07-31_land-command-post-merge` 설계 채택(트리아지 **유효** → 반영 완료, `_inbox`에서 정리·원장 유지). **알려진 한계: Class 판정이 경로 패턴 기반이라 의미적 정책 변경을 못 잡는다** — 예컨대 이 PR(거버넌스 변경)도 경로상으론 Class A로 보인다. 그래서 land 는 "사람 판단의 대체"가 아니라 "기계로 확인 가능한 것만 자동화"다. 놓친 트리거는 friction으로 기록하되 **패턴을 넓히기 전 신규 적중분 전수 재측정**(캡슐 `measure-before-widening-a-guard`).
  - [x] 전파 종결 **12/12** — sync-all(main 7곳 직접·비-main/dirty 4곳 worktree·icons-vault 는 icons 워크트리라 자동 커버), 전부 origin 대조


### METH-132 · CI `validate` 복구 — observation lint 6건 형식 위반
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] `repeat_of` 자유서술 6건 정규화(허용형: null · session_id · kebab-슬러그 · C-NNN) — 서술은 `resolution`으로 이동
  - [x] main 머지 후 Actions `validate` green 확인 — **maincheck addfb63 ✓ · main CI conclusion=success**
- **notes**: **CI가 #136·#137·#138 세 번 연속 main에서 red였다** — 자동 머지(METH-133)의 전제가 이미 깨져 있었음. 원인은 5월 레거시 관찰로그 5건 + 07-24 1건이 나중에 도입된 `repeat_of` 스키마를 위반한 것. 내용 손실 없음(서술은 resolution에 보존). **교훈: 스키마를 좁힐 때 기존 자산 전수 재검증** — 수거 캡슐 `measure-before-widening-a-guard`(가드 확장 전 전수 재측정)의 거울상. 근본 원인(머지 후 CI 확인 단계 부재)은 METH-133 `land`의 maincheck 단계로 닫음. #139 머지.








### METH-129 · AI 디자인 방법론 제정 — 리서치 완료, 구성안 확정 대기
- **mode**: planning → fullstack
- **change-class**: A (지침 신설·보강)
- **owner**: Human(구성안 확정) + AI(작성)
- **acceptance criteria**:
  - [x] 구성안 확정(사람 — 2026-07-29 "5개 전부 진행"): 스냅샷 §6 — 지침 25(AI 디자인 공통 규범)·26(이미지·캐릭터 에셋)·27(영상) 신설 + 지침 20 v2·22 v3 보강 + 스켈레톤 `ai-asset-pipeline` — 채택/조정
  - [x] 확정분 작성 완료(PR 대기) — 전파는 머지 후
- **notes**: 2026-07-29 사용자 지시로 4개 도메인(영상·이미지·PPT·웹디자인) 병렬 웹리서치(에이전트 4기·1차 출처 확인). 정본: `40_dev/snapshots/2026-07-29_AI디자인-방법론-리서치.md` — 교차 공통 원칙 9종(§0)·도메인 요지·기존 자산 접속 지도(§5)·구성안(§6). 핵심 발견: 벤더 소멸 3건(Sora·Tome·Galileo — 모델 추상화 필수), Deck-as-Code 학계 검증(AutoPresent·Design-First), AI기본법 표시 의무(2026-01 시행), Midjourney 소송 리스크, LoRA 승급 사다리, DTCG 안정판+shadcn registry(12 repo 단일 배포 가능). 지형 변화 빠름 — 분기 재검증 권장. **2026-07-29 작성 완료**: 지침 25(공통 규범 9원칙)·26(이미지·캐릭터)·27(영상) 신설, 지침 20 v2(§9 AI 웹디자인: DESIGN.md 의무·금지 기본값·3안 픽·AI 티 테스트·axe/시각회귀)·22 v3(§7b: 레이아웃 린트 4종·패널 taxonomy·Vega-Lite·리플렉션 루프·HTML 경유 금지), README v4.3. 스켈레톤 ai-asset-pipeline은 후속 후보(미착수). **머지(#134)·전파(07-29) 종결 11/11**(maincheck 79b60c3f ✓) — 12개 repo 전부 AI 디자인 규범 적용.
### METH-128 · 지침 22 보강 — 전수조사 갭 15건 (캡슐 수거분)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] `meth_inbox/icons-invest__2026-07-29_guide-22-audit-gaps.md` 캡슐(트리아지 판정: **유효**)의 15건을 지침 22에 반영 — 텍스트본=유일 소스·리드백 필수·차트 글리프 가드·안정 슬라이드 ID·패널 결함 해소 루프 등
- **notes**: **캡슐 루프 첫 실전 왕복** — icons-invest 발신→push→collect 수거→원장 기록→트리아지 유효 판정. 서브에이전트 스톨 감지(⑧)는 지침 08에도 교차 반영. **2026-07-29 구현 완료(PR 대기)**: 지침 22 v2 — 불변규율 4(텍스트본 파일=유일 소스)·5(안정 슬라이드 ID), P0 흡수 대상 전수 확정, P3 리드백 필수, §4.2 패널 결함 해소 루프(TODO 승격+다음 패널 판정), §7 함정 8종 추가. 지침 08 §7 스톨 감지 교차 신설. 반영 완료 캡슐은 _inbox에서 정리(원장 유지 — 재수거 방지). **머지(#131)·전파(07-29) 종결 11/11**(maincheck 0bdc3830 ✓) — 트리아지 12/12 전량 종결.
### METH-125 · P7 — 스크래핑 페이스 SOP 상류 승급 + 외부 소스 폴백 사다리
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] gamblescan `SOP_scraping-pace.md`(페널티 누적·IP 교체 무효·배치 분할)를 상류 standing SOP로 승급
  - [x] 리서치 flow에 폴백 사다리(WebFetch→Firecrawl→브라우저→API 우선) + "폴백 사용 시 정밀도 한계 표기" 명문화
- **notes**: 전수조사 P7(6곳). **2026-07-29 구현·전파 종결**: 상류 `00_briefs/standing/SOP_scraping-pace.md` 신설(shared_paths 등록 — 전 repo 배포: 페널티 누적·프로브≠회복·IP 교체 무효·페이스 절차·폴백 사다리·신규 소스 3축 평가·정밀도 한계 표기).

### METH-126 · P8 — CI-로컬 정합 (지침 19 보강 + 스캐폴드)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] "CI가 쓰는 패키지 매니저로 검증" 규칙 + `packageManager` 핀·락파일 단일화 스캐폴드 기본 + lockfile sync 가드(gamblescan 자산 재사용) + "런북 작성=절차 실측" 패턴
- **notes**: 전수조사 P8(3곳) — tshome 프로덕션 4일 정지가 대표 사고. **2026-07-29 구현·전파 종결**: 지침 19 §11 CI-로컬 정합 신설(v2) — CI 매니저로 검증·packageManager 핀·락파일 단일화·lockfile 가드·런북=절차 실측.

