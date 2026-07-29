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

### METH-127 · P11 — 지침 05 보강: 사실 주장 출처 규칙·샘플 마킹
- **mode**: fullstack / **change-class**: A / **owner**: AI + Human
- **acceptance criteria**:
  - [x] 사실 주장(수치·정책·연혁)은 출처 등급 없이 라이브 금지 + 플레이스홀더/`[샘플]` 명시 마킹 + 제거 스크립트 패턴(icons-marketing 원형 승급)
- **notes**: 전수조사 P11(4곳) — tshome AI 생성 콘텐츠 2개월 게시가 대표 사고. **2026-07-29 구현·전파 종결**: 지침 05 §9 사실 주장·샘플 데이터 규칙 신설(v2) — 출처 없는 사실 주장 라이브 금지·[샘플] 마킹+제거 체크·근거 등급 표기·기존 잔존물 강등.

> METH-125~127 공통: 머지(#129)·전파(07-29) 11/11, maincheck(b6fbf034 ✓).
