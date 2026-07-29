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

### METH-118 · 프롬프팅 코칭 루프 — 상시 자동 기록 + 자동 갱신 리포트
- **mode**: fullstack
- **change-class**: A
- **owner**: AI + Human
- **acceptance criteria**:
  - [ ] **상시 기록(자동·의무)**: wrap 의무에 프롬프팅 관찰 추가 — observe 스키마 `prompting:` 블록 확장(세션 총 라운드 수 + 교환별: intent·rounds·두루뭉술 지시 *발췌*+교정안 쌍·몰라서 비용 든 용어·상황 태그 예 `webpage-design-choice`·재지시 패턴). 피드백 가치 없는 세션은 minimal(rounds만) — CLI가 형식 강제. **원문 전체 저장 금지**(발췌만 — 볼륨·sensitive 반경), sensitive 스캔 대상
  - [ ] **판단 시점 정의**: 질적 판단(교정안·용어·상황 태그)은 wrap 시 그 세션 AI가 생성(맥락이 있는 유일한 시점) — 뒷단 배치 아님을 문서에 명시. 결정적 집계는 CLI만
  - [ ] **`prompt-report` 명령 + 자동 갱신**: 살아있는 리포트 파일 재생성 — 반복 모호 패턴 통계(빈도순)·배울 용어 사전·상황별 프롬프트 플레이북·라운드 수 추이·토큰 적정성(v1 프록시=라운드·재지시 수). **wrap 파이프라인이 기록 후 자동 재생성** → 세션 종료마다 최신. boot가 리포트 헤드라인 1줄 표시
  - [ ] **토큰 실측(옵션 게이트)**: v1은 프록시. PostHog LLM Analytics(`llma-cc-setup`) 연동 시 리포트가 실측 토큰을 읽는 확장 포인트만 설계(구현은 후속)
  - [ ] **교차-repo 통합은 v1 제외 명시**: 리포트는 repo 로컬. 통합 리포트는 collect 인프라 확장 후속(사용자 단위 데이터라 통합 가치 큼 — 재논의 트리거를 notes에 기록)
- **notes**: 2026-07-29 사용자 요청 — "전문용어를 몰라 지시가 길어지거나 핑퐁이 늘어나는 걸 스스로 교정할 데이터·리포트가 필요. 즉시 피드백보다 **언제나 남겨질 기록으로 뒷단에서 알아서 판단한 뒤 리포트 자동 업데이트**"(상시 기록이 확정 방향). 마찰 루프와 동형의 코칭 루프(L1 기록→집계→사람 교정). 발판: observe `prompt_patterns`(intent·success·rounds)가 이미 있으나 형식적 사용 — 이걸 확장. 정직한 한계 합의: 토큰 실측은 세션 내 불가(프록시로 시작), 원문 저장은 발췌로 제한. 사용자 선호는 도구 메모리(`prompting-feedback-preference`)에 별도 저장(즉시 피드백은 언제든 가능). **METH-121(observe 스키마 강제)과 통합 구현 예정(METH-119 트리아지).**

### METH-122 · P3+P6 도구 — 라이브 파일 fail-closed·자동 회전 + build 가드
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [ ] wrap 사이즈 경고를 자동 아카이브 회전 또는 fail-closed로 승급(cafe24 342KB·gamblescan 761줄 재발 방지) + HANDOFF 신선도(갱신일 vs 최근 커밋) 검사 + wrap 미실행 N일 감지
  - [ ] 외부 게이트(대표·결제·자격증명) 대기 항목 = TODO Blocked 강제 이동 규칙 문서화(4개 repo에서 Blocked 미사용 실증)
  - [ ] dev 서버 감지 시 build 차단 가드 스크립트를 스캐폴드 포함(ai-icons 7회 반복 — 규칙 아닌 강제)
- **notes**: 전수조사 P3(7곳)+P6(4곳).

### METH-123 · 지침 23 신설 — 검증 규범 (무음 실패·빈 상태·검증불가 등록부)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [ ] P4: 0건 처리=실패 sanity assert · 검사 못 함≠깨끗함(대상 0개 exit 1) · 금지형 가드 negative case 주입 증명 · 빌드 통과≠산출물 정상(리드백/grep)
  - [ ] P9: 비어있지 않은 데이터로·최대 표시 크기로·존재가 아닌 내용/가시성 어서션으로 검증
  - [ ] P12: 검증불가 등록부(무엇을·왜·대체 검증·확인 요청 대상) + 드래그/업로드 UI 비-포인터 대안 규칙
- **notes**: 전수조사 P4(6곳)+P9(5곳)+P12(4곳) 통합 지침.

### METH-124 · 지침 24 신설 — 착수 게이트 (정본·전제·해석 확인)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [ ] 과거 사실 기록물은 "무엇이 정본인가" 사용자 확인 선행 / 조사 스냅샷 진단은 착수 시점 코드로 재확인 / 시안·요청 해석 계약(정확 구현 vs 참고) 첫 질문 / 사용자가 그은 경계는 거절 전 원문 검증
- **notes**: 전수조사 P5(5곳) — 최고 단일 비용군(ai-icons 195분·gamblescan 90분·80분).

### METH-125 · P7 — 스크래핑 페이스 SOP 상류 승급 + 외부 소스 폴백 사다리
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [ ] gamblescan `SOP_scraping-pace.md`(페널티 누적·IP 교체 무효·배치 분할)를 상류 standing SOP로 승급
  - [ ] 리서치 flow에 폴백 사다리(WebFetch→Firecrawl→브라우저→API 우선) + "폴백 사용 시 정밀도 한계 표기" 명문화
- **notes**: 전수조사 P7(6곳).

### METH-126 · P8 — CI-로컬 정합 (지침 19 보강 + 스캐폴드)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [ ] "CI가 쓰는 패키지 매니저로 검증" 규칙 + `packageManager` 핀·락파일 단일화 스캐폴드 기본 + lockfile sync 가드(gamblescan 자산 재사용) + "런북 작성=절차 실측" 패턴
- **notes**: 전수조사 P8(3곳) — tshome 프로덕션 4일 정지가 대표 사고.

### METH-127 · P11 — 지침 05 보강: 사실 주장 출처 규칙·샘플 마킹
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [ ] 사실 주장(수치·정책·연혁)은 출처 등급 없이 라이브 금지 + 플레이스홀더/`[샘플]` 명시 마킹 + 제거 스크립트 패턴(icons-marketing 원형 승급)
- **notes**: 전수조사 P11(4곳) — tshome AI 생성 콘텐츠 2개월 게시가 대표 사고.

### METH-128 · 지침 22 보강 — 전수조사 갭 15건 (캡슐 수거분)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [ ] `meth_inbox/icons-invest__2026-07-29_guide-22-audit-gaps.md` 캡슐(트리아지 판정: **유효**)의 15건을 지침 22에 반영 — 텍스트본=유일 소스·리드백 필수·차트 글리프 가드·안정 슬라이드 ID·패널 결함 해소 루프 등
- **notes**: **캡슐 루프 첫 실전 왕복** — icons-invest 발신→push→collect 수거→원장 기록→트리아지 유효 판정. 서브에이전트 스톨 감지(⑧)는 지침 08에도 교차 반영.

## Ready

## InProgress


### METH-120 · P1 도구 — main 도달 검증 + 스택-PR 금지 명문화
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] Done 전이·배포 게이트용 main 도달 검사(`git merge-base --is-ancestor <sha> origin/main`)를 CLI로 제공(wrap 또는 신규 명령), TODO Done 처리 규칙에 연결
  - [x] "스택-PR 금지 — 앞 PR 머지 후 main에서 새로 분기" 를 CLAUDE/AGENTS §2에 명문화(개인 메모리→전 repo 규칙 승급)
- **notes**: 전수조사 P1 — 6개 repo 사고. insta-toon 복구는 그 repo PR #7(머지 완료). **2026-07-29 구현 완료(PR 대기)**: `maincheck` 명령(fetch→origin main/master 대조·다건 sha·미도달 exit 1+안내), CLAUDE/AGENTS §2 스택-PR 금지·Done 검증 불릿.

### METH-121 · P2 도구 — observe CLI 스키마 강제 (METH-118 통합)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] 메타 자동 채움: host_os 상시 실측, agent/tool 환경 추정, domain은 컨텍스트/인자 강제(기본값 "meta" 금지)
  - [x] `repeat_of` enum 강제(null | 관찰 session_id) — "repeat_of:" 접두 오염·자연어 거부, validate 반영
  - [x] 다건 friction 실사용 가능 확인(현행 F-001 캡 원인 규명) + 기본값 그대로면 validate가 "미기입" 경고
  - [x] prompt_patterns 상용구 제거 — METH-118 prompting 블록과 통합 설계
- **notes**: 전수조사 P2 — 전 repo 900+건 메타 상수·repeat_of 포맷 붕괴. **2026-07-29 구현 완료(PR 대기)**: `normalize_repeat_of`(접두 오염 정규화+enum 강제, 위반 시 생성·validate 거부), 메타 자동 채움(ctx unknown 무시·env 추정·host_os 실측), domain 기본값 meta 제거(미지정 시 exit 2), prompt_patterns 상용구 제거(기본 []), `observation_quality_warnings`(unknown·meta·상용구 경고). prompting 실측 블록은 METH-118 잔여. tests 11종.
## Blocked

## Done

### METH-119 · 2026-07 전수조사 발견 트리아지
- **notes**: 2026-07-29. Class A, planning. 사용자와 트리아지 완료 — **P1~P9·P11·지침22 갭 전부 채택**, P10(라이브 파일 병렬 충돌)은 **RFC-003 초안**으로(`70_meta/rfc/RFC-003_live-file-parallel-conflict.md`, 결정 대기), 즉시 주의 5건 중 insta-toon 스택-PR 미도달은 즉시 복구(insta-toon PR #7 — 머지 무충돌·테스트 64/64). 분배: METH-120(P1)·121(P2, METH-118 통합)·122(P3+P6)·123(지침23)·124(지침24)·125(P7)·126(P8)·127(P11)·128(지침22 갭). 구현 착수 순서: 120·121 먼저(Ready). 지침 22 갭은 icons-invest 캡슐 발신→collect 수거로 **캡슐 루프 첫 실전 왕복 검증**. 잔여 repo 과제 4건(invest-ops 민감정보·tshome I-006·icons-marketing 원장·icons 배포 루틴)은 각 repo 세션 몫. 근거 스냅샷: `40_dev/snapshots/2026-07-29_전레포-월간-전수조사-마찰-인사이트.md`.

### METH-117 · 역방향 루프 — 캡슐 outbox + 수동 일괄 수거
- **mode**: fullstack
- **change-class**: A
- **owner**: AI + Human
- **acceptance criteria**:
  - [x] **캡슐 스키마·outbox 신설**: 다운스트림에 상류행 제안 전용 디렉터리(예: `50_resources/meth_outbox/`) — **1 제안 = 1 캡슐 = 1 파일**(통합·혼합 금지, catalog "1문제 1엔트리"와 동일 granularity). frontmatter: `id`(origin repo+session_id 기반 — 수거 중복 방지 키)·`type`(guide-update | friction-escalation | pattern | tool-change)·`target`(예: guide-22, catalog, skeleton/<도메인>)·`refs`(커밋 SHA·PR URL·repo 상대경로)·작성일. 본문: 제안 요지+근거 발췌. **포인터+요약 원칙 — 원문 덤프 금지**(원문 정본은 그 repo)
  - [x] **작성 트리거 규칙 문서화**: 사용자 명시 요청("방법론에 반영해줘")=의무, AI 자발=근거 있을 때만 권장(노이즈·트리아지 병목 방지). friction과 역할 구분 — friction=막힌 *사실*, 캡슐=변경 *제안*, 마찰 파생 캡슐은 friction id를 ref
  - [x] **`collect` 명령**(상류, 수동 트리거): 로컬 스캔+origin fetch 병행 일괄 수거 → 상류 `_inbox/` 적재. 수거 상태는 **상류 원장**으로만 관리(다운스트림 무변경 — 캡슐에 도장 안 찍음). 원격 미생성·push 안 된 repo는 리포트에 "커버리지 밖" 명시
  - [x] **수거 잊음 방지(가시성)**: `boot`·`sync-all`이 다운스트림 outbox 잔량 카운트 표시("미수거 캡슐 N건") — 수거는 수동 유지, 잊을 수만 없게
  - [x] **안전**: outbox를 ship sensitive 스캔 대상에 포함 · outbox/_inbox는 sync-all mirror/prune 제외 경로 명시(METH-046 prune 사고 계보) · 민감 도메인 repo(예: invest-ops Class C)는 캡슐 발신 제한 규칙
  - [x] **트리아지·게이트**: _inbox 첫 판정 정형화(유효/이미 반영/만료 — stale 대응), 주기는 기존 Catalog Review 시간에 합류(병목 방지). thinktank가 _inbox 캡슐 target별 집계로 교차-repo 중복 제안 탐지(마킹만). **자동 승급 없음 유지(백서 §8-2)** — 자동화는 적재·집계·마킹까지, 분배·PR 머지는 사람
- **notes**: 2026-07-28 역방향 학습 루프 갭 분석에서 도출(순방향 sync-all만 자동, `observation_files()` 로컬 한정, 실사례 지침 05·22 모두 사람이 수동 환류). **2026-07-29 설계 확정(사용자)**: 초안(상류 pull 스캔) → **캡슐 outbox 안**으로 교체 — 다운스트림은 상류 위치 몰라도 되고(제0원칙), 캡슐이 git push와 함께 이동해 타 호스트 repo도 origin 경유 수거 가능(조건부), 명시 요청 트랙의 그릇 확보, 채널 분리(지침 05) 정합, 사람 게이트 3중. 리스크 6종 검토 — 5종 완화책 AC 반영, 결과 피드백(채택/기각 통지)은 v1 제외. **같은 날 구현(#116)**: capsule·collect 명령, boot [4b]·sync-all outbox 컬럼, ship sensitive 캡슐 내용 스캔, MANIFEST(outbox _README shared·본체 init 격리), outbox/_inbox _README, catalog §3 캡슐 트랙, CLAUDE/AGENTS §2 트리거 규칙, tests 13종+E2E 스모크. **머지(#116)·전파(07-29) 종결 11/11**: sync-all — main 6곳 직접·비-main 5곳 임시 worktree, 전 다운스트림 origin 반영·ls-remote 대조. ai-icons·invest-ops pre-push 훅 차단 → --no-verify(3회째 재발, friction repeat_of). 전 repo가 capsule 명령 보유 — 역방향 루프 가동.

### METH-116 · IR·사업기획 덱 제작 지침 신설 (지침 22 + 스켈레톤)
- **mode**: fullstack
- **change-class**: A
- **owner**: AI + Human
- **notes**: 2026-07-25. `icons-invest` IR 덱 v1→v4 제작 회고를 방법론으로 환류. 원료: 리서치 3종(AI-PPT-방법론·PPT-시각디자인·2025~26 트렌드)·python-pptx 43장 빌드 시스템(디자인 토큰 상단 고정+헬퍼+차트 xlsx→PNG)·멀티에이전트 실사 패널(4렌즈 토론결과)·100여 관찰/마찰 로그. 산출: `20_guides/22_IR_사업기획_덱_제작_지침.md` — Deck-as-Code 5단계(P0 정본화·P1 아웃라인 게이트·P2 디자인 계약·P3 코드 주입·P4 렌더검증) + 디자인 계약(색3·타입6·강조예산제) + 검증 게이트 4종+실사 패널 + 정직성 규율(헤드라인 정직·내부 메타 어휘 차단·GMV/인식매출) + 함정 체크리스트. 스켈레톤 `50_resources/skeletons/ir-deck-build/`(contract.py·build.py·textbook.template.md·panel-prompt.md), 스크래치 실행 검증(2장 빌드·geometry check 통과). README §3.6 산출물 craft 카테고리 신설. 지침 20(디자인 토큰)의 덱 레이어 자매. 사용자 선택(AskUserQuestion): 정식 가이드+실행 플레이북. branch-first(docs/guide-22-ir-deck-methodology). **전파(07-29) 종결 11/11**: #112 머지 후 sync-all — main+clean 6곳 직접, 비-main 5곳 임시 worktree로 origin/main만 조작, 전부 타깃 스테이징 커밋·push·ls-remote 대조. ai-icons·invest-ops는 pre-push wrap 훅 차단 → established 절차 --no-verify(재발 마찰, friction 기록). gamblescan은 밀린 지침 07·CLAUDE/AGENTS도 동반 따라잡음. 스켈레톤 ir-deck-build는 설계상 init 경로라 sync 비전파(정상 — shared는 _README만). grooman(타 호스트)만 커버리지 밖.

### METH-115 · ship push 반영 검증 (origin HEAD 대조)
- **notes**: 2026-07-24. Class A. ai-icons에서 push 유실 사고(ICONS-365) — 백그라운드 PR 머지로 원격이 앞서가 push가 non-fast-forward 거부됐는데 ship이 exit code만 보고 "완료" 보고, 16커밋이 로컬에만 쌓여 배포 정지. 다운스트림 패치(ICONS-366)를 업스트림에 이식: push 후 `git ls-remote origin <branch>`로 원격 HEAD를 로컬 HEAD와 대조 — 불일치/미존재면 fail(rebase 안내), 조회 불가면 "반영 미검증" 경고, 성공 시 반영 SHA 출력. 테스트 21/21. branch-first(fix/ship-push-verify). **전파(07-24) 종결 11/11**: #109 머지 후 sync-all — 전 다운스트림 반영·origin 검증(ai-icons는 상류판으로 수렴), 비-main 4곳 METH-106 절차. 잔여 icons(활성 세션→임시 worktree로 main만 조작, 도중 origin 전진 non-FF를 새 검증이 포착→rebase 재push)·invest-ops(원격 생성 확인 후 정상 sync)도 반영. grooman(타 호스트)만 커버리지 밖.

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
