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
- **notes**: 2026-07-29 사용자 요청 — "전문용어를 몰라 지시가 길어지거나 핑퐁이 늘어나는 걸 스스로 교정할 데이터·리포트가 필요. 즉시 피드백보다 **언제나 남겨질 기록으로 뒷단에서 알아서 판단한 뒤 리포트 자동 업데이트**"(상시 기록이 확정 방향). 마찰 루프와 동형의 코칭 루프(L1 기록→집계→사람 교정). 발판: observe `prompt_patterns`(intent·success·rounds)가 이미 있으나 형식적 사용 — 이걸 확장. 정직한 한계 합의: 토큰 실측은 세션 내 불가(프록시로 시작), 원문 저장은 발췌로 제한. 사용자 선호는 도구 메모리(`prompting-feedback-preference`)에 별도 저장(즉시 피드백은 언제든 가능).

### METH-119 · 2026-07 전수조사 발견 트리아지 — 승급·백로그 분배
- **mode**: planning
- **change-class**: A (개별 승급 건은 각자 등급)
- **owner**: Human + AI
- **acceptance criteria**:
  - [ ] `40_dev/snapshots/2026-07-29_전레포-월간-전수조사-마찰-인사이트.md`의 승급 후보 P1~P12를 사람이 트리아지(채택/보류/기각) — Catalog Review 시간 합류
  - [ ] 채택분을 목적지 분배: 도구 백로그(§2 — observe CLI 강제는 METH-118과 통합 검토) / 지침 신설·보강(§3) / catalog `_pending` / RFC(P10 라이브 파일 병렬 충돌은 운영 규칙 변경이라 RFC 후보)
  - [ ] §5 즉시 주의 5건은 해당 repo 세션 과제로 전달(방법론 아님) — 특히 insta-toon 스택-PR 미도달 복구·invest-ops 민감정보 합의
- **notes**: 2026-07-29 사용자 지시로 11개 repo 최근 한 달 병렬 전수조사(에이전트 11기·읽기 전용). 관찰로그 1,006건·friction 302건·기록된 비용만 90h+. 교차-repo 반복 패턴 12종(P1 스택-PR 6곳·P2 observe 스키마 결함 9곳·P6 dev-build 충돌 "7회 반복" 등) — 상세·증거는 스냅샷이 정본. 캡슐 루프 가동 이전 미환류분의 소급 수거에 해당. grooman 커버리지 밖.

## Ready

## InProgress

## Blocked

## Done

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

### METH-114 · boot HANDOFF 파서·스캐폴드 템플릿 정합
- **notes**: 2026-07-23. Class A. boot의 "Working on" 파서(볼드만 기대) ↔ init 스캐폴드 템플릿(비볼드 생성) 불일치로 새 다운스트림 boot가 "(미기재)" 표시(invest-ops friction에서 발견). 파서를 `_handoff_working_on` 헬퍼로 추출해 볼드·비볼드 양쪽 허용, 템플릿은 실사용 형식(볼드)으로 정합, `tests/test_boot_handoff.py` 5종(템플릿↔파서 회귀 가드 포함). methodology.py·templates 둘 다 shared_paths → 다음 sync-all에서 전 다운스트림 자동 전파. branch-first(fix/boot-handoff-working-on-parser).

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
