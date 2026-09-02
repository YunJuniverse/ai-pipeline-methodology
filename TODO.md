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

### METH-144 · METH-142 후속 2건 — 지침 30 워크트리 push 부작용 · 그래프 22~30 노드 백필
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] 지침 30 v2 — §1 에 「워크트리 `push origin HEAD:main` 은 원본 체크아웃의 로컬 main 을 따라오게 하지 않는다」 + 대응(원본이 main 이면 `pull --ff-only`, 아니면 fetch 만 하고 checkpoint 기록 — 브랜치 전환은 §1 위반). invest-ops 2차 전파 3파일 충돌 실사고를 근거로
  - [x] `methodology-graph.json` — 지침 22~30 **노드 9개 + 엣지 18개** 백필(nodes 42→51 · edges 53→71). 22 이후가 통째로 빠져 있던 것. 계층: 23·24·28·29·30 은 g00 parent-of(메타 지침 tier 3), 25 는 26·27·20·22 의 상위(guide-ai tier 5), 01 §5.11 라우팅 → 28·29·30, 29→28 선결·29→07 예산, 30→08 축 구분, 23↔19 상보, 10→22 변환 공정
  - [x] lifecycle 배치 — L2 += g22 · L5 += g24 · L6 += g19·g20·g23·g30(개발 단계에 개발 규칙이 하나도 없던 것도 함께 정정)
  - [x] **원본 포맷 보존** — 첫 시도가 `json.dumps` 재직렬화로 1055+/187- 전면 재작성이 되어 되돌리고 **행 단위 텍스트 삽입**으로 49+/4- 로 축소(지침 19 §8b.3). 치환 건수 assert
  - [x] 검증 — JSON 파싱·전 엣지 노드 존재·경로 실존 assert · graph-viz 렌더 nodes=51 · dashboard nodes=51 · 테스트 87/87
- **notes**: METH-142 종결 시 남긴 후속 2건. 그래프 version 스탬프 `v3.2-2026-07`→`v4.0-2026-09`.

### METH-143 · wrap 라이브 파일 구조 검증 — 편집 사고 기계 탐지
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] 계기 — 2026-09-02 상류 실사고: 인덱스 기반 편집으로 `# HANDOFF.md` 제목이 덮이고 Working-on 이 둘이 된 채 **PR 6개**를 지났다. boot 가 첫 매치만 읽어 출력이 정상으로 보인 탓
  - [x] `live_file_structure_issues()` — **중복(모호성)은 error · 부재·드리프트는 warn**. Working-on 중복 · HANDOFF 섹션 중복 · 칸반 섹션 중복이 error
  - [x] **착수 전 전수 실측**(지침 23 §4-3) — 12 repo 스캔: **error 0건**, warn 은 gamblescan 6·tshome 2·icons/icons-invest/lifeManager 각 1. 부재를 fail 로 잡으면 10곳이 매 push 막혀 가드가 무시당한다는 근거로 경계를 그었다
  - [x] boot 파서 계약 준수 — 비볼드 `- Working on:`(METH-114 스캐폴드 이력) 허용
  - [x] wrap 배선 — 경고는 항상 출력, error 는 `--strict` 에서 fail(탈출구 없음: 중복은 고치는 것 말고 정당한 상태가 없다)
  - [x] negative case 5테스트 — 사고 재현·부재는 경고·칸반 중복·정상 무음·비볼드 허용. 전체 87/87 green
  - [x] **전파 11/11**(2026-09-02) — main 직접 8 · 격리 워크트리 3(icons·icons-invest·insta-toon). origin 실내용 대조 11/11 ✓(`live_file_structure_issues` 블롭 grep) · 훅 3 repo 재설치. 전파 후 실측 **error 0 · warn 11**(gamblescan 6·tshome 2·icons/icons-invest/lifeManager 각 1) — 예측과 일치
- **notes**: 사이즈 린트(METH-101/122)가 「너무 큰가」라면 이것은 「파싱 가능한가」다. 지침 19 §8b.3(편집 후 구조 검증)의 기계화 — 그 조항을 쓴 당일에 내가 그 조항을 어긴 것이 계기다.

### METH-142 · 캡슐 트리아지 4회차 — 수거 24건 전량 종결
- **mode**: fullstack / **change-class**: A / **owner**: Human(판정) + AI(반영)
- **acceptance criteria**:
  - [x] `collect --apply` 전 repo 순회 — 16곳 스캔, **신규 24건** 적재(원장 21→45). icons 계열 워크트리 5곳은 METH-140 수정 효과로 전부 dedup(첫 실전 검증 ✓). 착지: PR #155 squash `4c8b57f5` · maincheck origin/main 도달 ✓
  - [x] **판정 초안 작성**(AI) — `40_dev/snapshots/2026-09-02_캡슐-트리아지-판정초안.md`. 전 24건 상류 코드·지침 실측 대조. 초안 집계: **유효 19 · 이미 반영 5 · 만료 0**
  - [x] **초안 기준 16건 선반영**(2026-09-02) — 사람 판단 3지점에 걸리지 않는 전부. 도구 3(rotate 순서 검사 · build-guard 를 `dev-check` 단일 판정으로 · ship 스테이징 확인) · 지침 5(05 v4 · 19 v4 · 23 v4 · 24 v3 · 25 v2) · catalog `_pending` 3(P-003·004·005) · 하류 존치 1
  - [x] negative case 실효 증명(지침 23 §1-3) — rotate 역전 감지 5테스트(수정 전 미감지) · build-guard 실프로세스 A/B/C(같은 repo 차단 1 · 타 디렉터리 통과 0 · 자기적중 배제 0) · ship 인덱스 4테스트. 전 테스트 **80/80 green**
  - [x] `_inbox` 정리 — 21건 삭제(반영 16 + 이미 반영 5), **원장 45건 유지**(재수거 방지). 잔여 3건은 판단 대기분
  - [x] **판단 4지점 확정**(2026-09-02, 권고안 전부 채택) — ① land 콘텐츠 판정 **비채택**(근거 박제, 뒤집으려면 ADR 선행) ② 동시 세션 격리 **신설 지침 30** ③ 플랫폼 고유 지식 **하류 정본 존치를 발신 규칙으로 명문화** ④ 훅 sync 면제를 **메시지→변경 경로 기준**으로 교체
  - [x] **전 repo 전파 11/11**(2026-09-02) — main 직접 7곳 · origin/main 기반 격리 워크트리 4곳(icons·icons-invest·insta-toon·invest-ops, 진행 중 작업 보호). icons 계열 워크트리 5곳은 icons origin 공유로 자동 커버. **origin 실내용 대조 11/11 ✓**(지침 5개 + build-guard `dev-check` 블롭 grep). 훅 3 repo 재설치
  - [x] **잔여 3건 반영** — #6 비채택 종결 · #10·#11 지침 30 으로 병합 승급. `_inbox` **비움**(원장 45 유지) → **24건 전량 종결**
  - [x] 판단 ④ 실 증명 A/B/C(실 push) — 한국어 sync 메시지+관리경로만 통과 · 경로 밖 섞이면 차단 · sync 의도 없으면 차단. 테스트 82/82
  - [x] **2차 전파 11/11**(지침 30·훅 경로판정·outbox 규칙) — main 직접 8곳 · 격리 워크트리 3곳(icons·icons-invest·insta-toon). origin 실내용 대조 11/11 ✓(지침30 파일·`shared-paths`·outbox 원칙·CLAUDE 트리거 4항목). 훅 3 repo 재설치 후 **경로 판정 반영 확인**
- **notes**: 초안 분배 — 지침 5갈래(05 §9b·19 §8b·23 §3/§4·24 §2/§4b·25 §5) · 도구 4건(land 주석·rotate 정렬·build-guard cwd·ship 스테이징 경고) · catalog `_pending` 3건 · 하류 존치 1건. 내역 — icons 14(도구 4·지침 4·catalog 6) · cafe24-renewal 5(플랫폼 캐시·자가치유 게이트·편집배포 안전장치) · ai-icons 1(대시 꼬리 금지) · 상류 선반영 의심 4(`land-billing-pattern`·`asset-exts`·`repo-name-from-git-common-dir`·`land-classbc-plan-viewer` = METH-138~141 로 이미 처리 → **판정 시 '이미 반영' 유력**). 형식 경고 1건: `icons-wt-hub__2026-08-31_land-class-regex-plan-viewer-false-positive` 는 id 접두어가 워크트리명(`priceless-perlman-c80820`) — METH-140 이전 발행분, 내용은 위 선반영 건과 중복.

- **종결**(2026-09-02): 수거→초안→반영→전파를 한 세션에 완주. PR **#155**(수거 24건)·**#157**(판정 초안)·**#158**(16건 반영)·**#159**(1차 전파)·**#160**(잔여 3건+판단 4지점)·**#161**(2차 전파). maincheck 전건 통과. 산출: 지침 5개 개정 + **지침 30 신설** · 도구 4건(rotate·build-guard·ship·훅 sync 판정) · catalog `_pending` 3건 · `_inbox` 비움(원장 45 유지). 테스트 82/82.

### METH-141 · Class B/C 트리거에서 표현용 자산 제외 (하류 icons#670 역주입)
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] 원인 — 트리거는 «경로 단어»로 위험을 추정하는데 이미지·영상·폰트는 그 경로에 있어도 로직을 못 바꾼다. icons 실측: 인증 트리거 적중 25건 중 **16건이 `public/gallery/auth-*.jpg`** 갤러리 스크린샷 — 재촬영 PR 마다 Class B
  - [x] `ASSET_EXTS`(이미지·영상·폰트 22종) + `_is_asset` — 확장자만 보고 경로 위치는 무관
  - [x] **문서 확장자는 의도적 제외** — `legal/terms.pdf`·`billing/pricing.json` 은 정책·약관·가격을 실제로 담으므로 Class C 판정 대상 유지. 이 경계가 무너지면 자산 제외가 곧 법무·과금 미탐
  - [x] `_excluded_assets` + land 출력 — «무엇을 안 봤는지» 밝힌다(침묵 제외 금지)
  - [x] 테스트 3건 추가(자산 인식·문서 비자산·경로 무관) — 11/11 · 상류 8파일 전체 green
  - [x] end-to-end — 임시 repo 로 `_classify_change` 실검증: `public/auth-shot.jpg` 제외 / `legal/terms.pdf` 는 Class C 유지
- **notes**: 하류 icons#670 역주입. `60_tools/methodology.py` 는 sync 대상이라 하류 로컬 패치는 다음 sync 에 덮인다 — METH-139(#667)·140(#668)과 같은 사유. 이로써 이번 경합에서 나온 하류 패치 3건이 전부 상류에 안착했다.

### METH-140 · 캡슐 `origin_repo` 워크트리 갈라짐 — `_repo_name` 을 git 공통 디렉터리 기준으로
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] 원인 — `_repo_name` 이 디렉터리명만 써서, 워크트리에서 발행한 캡슐이 워크트리명(`icons-wt-hub`·`.claude/worktrees/<임시명>`)을 `origin_repo`·id 로 갖는다. 캡슐 id 는 `_collect_plan` 의 **중복 수거 방지 키**라 같은 제안이 워크트리마다 갈라져 중복 적재
  - [x] METH-137 에서 경고만 남기고 원인 미해소였던 `gamblescan-p0-pr__...` 건의 근본 원인
  - [x] 수정 — `git rev-parse --git-common-dir` 로 주 체크아웃 이름 환원, bare(`<repo>.git`)·非git·git 부재 전부 폴백
  - [x] 테스트 2건 — 실제 worktree 생성 후 주 체크아웃 이름 반환 확인 / 非git 폴백. 상류 8파일 전체 green
  - [x] 실측 — 이 세션 워크트리 `priceless-perlman-c80820` → `icons` 반환 확인
- **notes**: 하류(icons#668)에서 먼저 고쳐진 것을 상류로 역주입. `60_tools/methodology.py` 는 sync 로 내려오는 파일이라 **하류 로컬 패치만으로는 다음 sync 에 덮여 되돌아온다** — 같은 이유로 METH-138·139 도 상류에 올렸다. 하류 수정을 발견하면 상류 반영 여부를 함께 확인할 것.

### METH-139 · land `plan` 규칙 정련 — 병렬 세션 두 수정안의 합집합 채택
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] 계기 — METH-138(경계 `[./]`)과 icons 병렬 세션의 독립 수정(icons#667, 과금낱말 복합어만)이 **상보적**임을 실측으로 확인. 어느 쪽도 상대를 포함하지 않았다
  - [x] 실측 근거 — icons 2502 경로 전수: 옛 단독 `plan` **824건**(레포의 1/3) · icons#667 **2건** · METH-138 **4건** · 채택안 **2건**. 남은 2건은 전부 진짜 `checkout/`
  - [x] METH-138 의 단수 허용이 오히려 오탐이었음 확인 — `50_apps/plan-viewer/app/plan/page.js`·`50_resources/prompts/plan.md` 둘 다 기획 용법
  - [x] 채택 — 과금낱말 복합어(`plan_pricing`·`plan-tier`) **+ 복수형만**(`plans.ts`·`plans/`). 단수 `plan` 은 제외
  - [x] 복수형 추가가 이 repo 군에서 무비용임을 실측 — icons 전체에 `plans` 경로 0건
  - [x] 테스트 8케이스(신규 3) · 상류 8파일 전체 green
- **notes**: 병렬 작업이 낳은 이득 — 단독으로는 둘 다 최적이 아니었다. `test_bare_plan_would_be_catastrophic` 은 회귀 방지가 아니라 **근거의 박제**(824 숫자)로, 경계를 다시 넓히자는 제안이 오면 먼저 보게 한다. icons 로컬 패치(#667)는 이 상류 반영으로 대체된다.

### METH-138 · land Class 스캐너 `plan` 오탐 — 경계 축소 + 회귀 테스트 신설
- **mode**: fullstack / **change-class**: A / **owner**: AI
- **acceptance criteria**:
  - [x] 재현 — `CLASS_BC_PATTERNS` 과금 항의 `plan` 대안이 넓은 경계 `[./_-]` 라 `plan-viewer` 를 문다. icons 레포 `50_apps/plan-viewer/` 아래 **모든** 변경이 Class B 로 판정돼 자동 머지 영구 불가(실사고 PR #664)
  - [x] 테스트 선행 — `tests/test_land_class_patterns.py` 신설, 수정 전 3/5 fail 로 오탐 재현 확인
  - [x] 수정 — `plan` 만 분리해 경계 `[./]`(세그먼트·파일명 전체)로 축소. 나머지 6낱말은 경계 불변
  - [x] 미탐 방지 고정 — 진짜 과금 경로 8종·타 트리거 10종·평범 경로 4종 회귀 테스트 (6/6 pass)
  - [x] 감수한 대가를 테스트로 명시 — `plan_limits.json` 류 복합어는 놓친다(대조군: `billing/plan_limits.json`·`src/pricing/plan_limits.json` 은 계속 걸림)
  - [x] 실사고 재판정 — 수정된 `_classify_change` 로 PR #664 실제 diff → **Class A, 트리거 없음**
  - [x] 상류 전체 회귀 — 8파일 64테스트 전부 pass
- **notes**: fail-closed 설계(오탐 싸고 미탐 비쌈)는 유지. 다만 앱 디렉터리 하나를 통째로 오판하는 오탐은 사람을 `--no-ci-check`·수동 머지로 밀어내 **오히려 안전을 깎는다** — 늘 우는 늑대는 무시된다. `plan` 은 목록 7낱말 중 유일하게 요금제 밖에서도 흔한 수식어라 이 항만 좁혔다. 발신 캡슐: icons `50_resources/meth_outbox/2026-09-01_land-billing-pattern-path-false-positive.md`.

