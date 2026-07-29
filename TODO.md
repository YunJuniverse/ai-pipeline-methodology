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

### METH-128 · 지침 22 보강 — 전수조사 갭 15건 (캡슐 수거분)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [ ] `meth_inbox/icons-invest__2026-07-29_guide-22-audit-gaps.md` 캡슐(트리아지 판정: **유효**)의 15건을 지침 22에 반영 — 텍스트본=유일 소스·리드백 필수·차트 글리프 가드·안정 슬라이드 ID·패널 결함 해소 루프 등
- **notes**: **캡슐 루프 첫 실전 왕복** — icons-invest 발신→push→collect 수거→원장 기록→트리아지 유효 판정. 서브에이전트 스톨 감지(⑧)는 지침 08에도 교차 반영.

## Ready

## InProgress













### METH-125 · P7 — 스크래핑 페이스 SOP 상류 승급 + 외부 소스 폴백 사다리
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] gamblescan `SOP_scraping-pace.md`(페널티 누적·IP 교체 무효·배치 분할)를 상류 standing SOP로 승급
  - [x] 리서치 flow에 폴백 사다리(WebFetch→Firecrawl→브라우저→API 우선) + "폴백 사용 시 정밀도 한계 표기" 명문화
- **notes**: 전수조사 P7(6곳). **2026-07-29 구현 완료(PR 대기)**: 상류 `00_briefs/standing/SOP_scraping-pace.md` 신설(shared_paths 등록 — 전 repo 배포: 페널티 누적·프로브≠회복·IP 교체 무효·페이스 절차·폴백 사다리·신규 소스 3축 평가·정밀도 한계 표기).

### METH-126 · P8 — CI-로컬 정합 (지침 19 보강 + 스캐폴드)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] "CI가 쓰는 패키지 매니저로 검증" 규칙 + `packageManager` 핀·락파일 단일화 스캐폴드 기본 + lockfile sync 가드(gamblescan 자산 재사용) + "런북 작성=절차 실측" 패턴
- **notes**: 전수조사 P8(3곳) — tshome 프로덕션 4일 정지가 대표 사고. **2026-07-29 구현 완료(PR 대기)**: 지침 19 §11 CI-로컬 정합 신설(v2) — CI 매니저로 검증·packageManager 핀·락파일 단일화·lockfile 가드·런북=절차 실측.

### METH-127 · P11 — 지침 05 보강: 사실 주장 출처 규칙·샘플 마킹
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] 사실 주장(수치·정책·연혁)은 출처 등급 없이 라이브 금지 + 플레이스홀더/`[샘플]` 명시 마킹 + 제거 스크립트 패턴(icons-marketing 원형 승급)
- **notes**: 전수조사 P11(4곳) — tshome AI 생성 콘텐츠 2개월 게시가 대표 사고. **2026-07-29 구현 완료(PR 대기)**: 지침 05 §9 사실 주장·샘플 데이터 규칙 신설(v2) — 출처 없는 사실 주장 라이브 금지·[샘플] 마킹+제거 체크·근거 등급 표기·기존 잔존물 강등.
## Blocked

## Done





### METH-123 · 지침 23 신설 — 검증 규범 (무음 실패·빈 상태·검증불가 등록부)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] P4: 0건 처리=실패 sanity assert · 검사 못 함≠깨끗함(대상 0개 exit 1) · 금지형 가드 negative case 주입 증명 · 빌드 통과≠산출물 정상(리드백/grep)
  - [x] P9: 비어있지 않은 데이터로·최대 표시 크기로·존재가 아닌 내용/가시성 어서션으로 검증
  - [x] P12: 검증불가 등록부(무엇을·왜·대체 검증·확인 요청 대상) + 드래그/업로드 UI 비-포인터 대안 규칙
- **notes**: 전수조사 P4(6곳)+P9(5곳)+P12(4곳) 통합 지침. **2026-07-29 구현 완료(PR 대기)**: `20_guides/23_검증_규범.md` 신설 — 무음 실패 4규칙·내용 기준 검증 3기준·검증불가 등록부(4필드+우회 사다리). README §3.6·이력 v4.2. **머지(#127)·전파(07-29) 종결 11/11**(maincheck 01f11071 ✓).

### METH-124 · 지침 24 신설 — 착수 게이트 (정본·전제·해석 확인)
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] 과거 사실 기록물은 "무엇이 정본인가" 사용자 확인 선행 / 조사 스냅샷 진단은 착수 시점 코드로 재확인 / 시안·요청 해석 계약(정확 구현 vs 참고) 첫 질문 / 사용자가 그은 경계는 거절 전 원문 검증
- **notes**: 전수조사 P5(5곳) — 최고 단일 비용군(ai-icons 195분·gamblescan 90분·80분). **2026-07-29 구현 완료(PR 대기)**: `20_guides/24_착수_게이트.md` 신설 — 정본 확인·진단 재검증(반증 대조군)·해석 계약·경계 원문 검증 + 상황별 질문표. **머지(#127)·전파(07-29) 종결 11/11.**
### METH-118 · 프롬프팅 코칭 루프 — 상시 자동 기록 + 자동 갱신 리포트
- **mode**: fullstack
- **change-class**: A
- **owner**: AI + Human
- **acceptance criteria**:
  - [x] **상시 기록(자동·의무)**: wrap 의무에 프롬프팅 관찰 추가 — observe 스키마 `prompting:` 블록 확장(세션 총 라운드 수 + 교환별: intent·rounds·두루뭉술 지시 *발췌*+교정안 쌍·몰라서 비용 든 용어·상황 태그 예 `webpage-design-choice`·재지시 패턴). 피드백 가치 없는 세션은 minimal(rounds만) — CLI가 형식 강제. **원문 전체 저장 금지**(발췌만 — 볼륨·sensitive 반경), sensitive 스캔 대상
  - [x] **판단 시점 정의**: 질적 판단(교정안·용어·상황 태그)은 wrap 시 그 세션 AI가 생성(맥락이 있는 유일한 시점) — 뒷단 배치 아님을 문서에 명시. 결정적 집계는 CLI만
  - [x] **`prompt-report` 명령 + 자동 갱신**: 살아있는 리포트 파일 재생성 — 반복 모호 패턴 통계(빈도순)·배울 용어 사전·상황별 프롬프트 플레이북·라운드 수 추이·토큰 적정성(v1 프록시=라운드·재지시 수). **wrap 파이프라인이 기록 후 자동 재생성** → 세션 종료마다 최신. boot가 리포트 헤드라인 1줄 표시
  - [x] **토큰 실측(옵션 게이트)**: v1은 프록시. PostHog LLM Analytics(`llma-cc-setup`) 연동 시 리포트가 실측 토큰을 읽는 확장 포인트만 설계(구현은 후속)
  - [x] **교차-repo 통합은 v1 제외 명시**: 리포트는 repo 로컬. 통합 리포트는 collect 인프라 확장 후속(사용자 단위 데이터라 통합 가치 큼 — 재논의 트리거를 notes에 기록)
- **notes**: 2026-07-29 사용자 요청 — "전문용어를 몰라 지시가 길어지거나 핑퐁이 늘어나는 걸 스스로 교정할 데이터·리포트가 필요. 즉시 피드백보다 **언제나 남겨질 기록으로 뒷단에서 알아서 판단한 뒤 리포트 자동 업데이트**"(상시 기록이 확정 방향). 마찰 루프와 동형의 코칭 루프(L1 기록→집계→사람 교정). 발판: observe `prompt_patterns`(intent·success·rounds)가 이미 있으나 형식적 사용 — 이걸 확장. 정직한 한계 합의: 토큰 실측은 세션 내 불가(프록시로 시작), 원문 저장은 발췌로 제한. 사용자 선호는 도구 메모리(`prompting-feedback-preference`)에 별도 저장(즉시 피드백은 언제든 가능). **METH-121(observe 스키마 강제)과 통합 구현 예정(METH-119 트리아지).** **2026-07-29 구현 완료(PR 대기, METH-121 잔여분 통합)**: observe `--rounds-total`(상시 의무)·`--prompting "intent|rounds|모호발췌(≤200자 가드)|교정안|용어|상황태그"`(교환별), prompting 프론트매터 블록 렌더/파서, `prompt-report` 명령 + **wrap 자동 재생성**(`50_resources/prompting-report.md`: 요지·라운드 추이·모호→교정 목록·용어 사전·상황 플레이북·토큰 프록시+PostHog 확장 포인트) + boot 헤드라인. 판단 시점(wrap 세션 AI)·v1 스코프(교차-repo 제외) 리포트 헤더 명시. ship sensitive가 관찰로그 내용도 스캔. CLAUDE/AGENTS wrap 규칙에 상시 기록 의무 추가. tests 7종. **머지(#125)·전파(07-29) 종결 11/11** — 전 repo에서 프롬프팅 상시 기록·리포트 자동 갱신 가동. maincheck 검증(69de6d95 ✓) 후 Done. 첫 실데이터·리포트는 방법론 repo에 생성됨(`50_resources/prompting-report.md`).
> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
