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

### METH-132 · CI `validate` 복구 — observation lint 6건 형식 위반
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] `repeat_of` 자유서술 6건 정규화(허용형: null · session_id · kebab-슬러그 · C-NNN) — 서술은 `resolution`으로 이동
  - [ ] main 머지 후 Actions `validate` green 확인(maincheck + `gh run list`)
- **notes**: **CI가 #136·#137·#138 세 번 연속 main에서 red였다** — 자동 머지(METH-133)의 전제가 이미 깨져 있었음. 원인은 5월 레거시 관찰로그 5건 + 07-24 1건이 나중에 도입된 `repeat_of` 스키마를 위반한 것. 내용 손실 없음(서술은 resolution에 보존). **교훈: 스키마를 좁힐 때 기존 자산 전수 재검증** — 수거 캡슐 `measure-before-widening-a-guard`(가드 확장 전 전수 재측정)의 거울상.





















## Blocked

### METH-131 · 캡슐 트리아지 2026-08 — 15건 / 3 repo (_inbox 적재 완료)
- **mode**: fullstack
- **change-class**: A / **owner**: Human(트리아지 판정) + AI(반영)
- **대기 사유(외부 게이트)**: 캡슐 판정(유효/이미 반영/만료)은 **사람만** 내린다 — 백서 §8-2 자동 승급 금지. 판정 전 반영 착수 불가.
- **acceptance criteria**:
  - [ ] 15건 각각 판정 → 유효분만 목적지 분배(지침 보강 PR / TODO 백로그 / `catalog/_pending` / 도구 변경)
  - [ ] 판정 후 '이미 반영'·'만료'분은 `_inbox`에서 삭제(원장 유지 — 재수거 방지), 근거 한 줄을 커밋 메시지에
  - [ ] 유효분 반영 PR은 main 직행 단일 PR·maincheck로 도달 확인
- **notes**: 2026-08-07 `collect --apply` 수거(원장 1→16건). thinktank 교차 집계: **CROSS-REPO** guide-23 x4(gamblescan·lifeManager) · guide-07 x2 · guide-19 x2, **DUP-TARGET** catalog x2 — 우선 검토 신호. 도구 변경 3건(tool/ship·tool/land·tool/hooks, invest-ops)은 서로 의존하는 한 세트라 함께 판정. `tool/hooks`(pre-push가 브랜치 삭제 push 차단)는 thinktank 승급 후보 ≥2회와 동일 마찰. `catalog` 2건은 07-31 제안의 08-07 재발 캡슐(누적 5실사례)이라 중복이 아닌 승급 근거. 집계: `40_dev/snapshots/insights/2026-W32_thinktank.md`.

## Done








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

