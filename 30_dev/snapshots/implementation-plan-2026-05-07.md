# 실행 가능한 헌법 구현 기획

> Snapshot. Live state is `HANDOFF.md` and `TODO.md`.
> 기준 백서: `00_foundation/WHITEPAPER.md` v0.2.0
> 작성일: 2026-05-07

## 1. 목적

이 계획은 백서의 철학을 실제 운영 가능한 시스템으로 옮기기 위한 구현 순서를 정의한다.

핵심 목표:
- 누구나 15분 안에 방법론을 이해하고 첫 작업을 시작한다.
- 어떤 AI 모델·PC에서도 저장소만 있으면 작업을 이어받는다.
- 한 번 겪은 문제는 raw 관찰 → 후보 → 활성 자산 → Skeleton 반영으로 이동한다.
- 대시보드는 현재 상태, 자주 쓰는 문서, 반복 마찰, 씽크탱크 제안을 한 화면에서 보여준다.

## 2. 구현 원칙

1. 이식성 코어가 먼저다.
2. 자동화는 어댑터에 둔다.
3. L1 raw 데이터는 많이 쌓고, L2 활성 자산은 작게 유지한다.
4. Skeleton은 `base/`와 `lock/apply result`를 분리한다.
5. 씽크탱크는 제안만 만들고, 시스템 변경은 사람 게이트를 통과한다.

## 3. 구현 단계

| 단계 | 이름 | 핵심 산출물 | 완료 기준 |
|---|---|---|---|
| P1 | Portable Boot | `.ai/context.json` 스키마, `.ai/checkpoint.md` 템플릿, adapter 초안 | 새 AI가 `context.json`과 `checkpoint.md`만 보고 다음 행동을 말할 수 있음 |
| P2 | Observation Flow | L1 관찰 로그 생성 명령, lint 규칙, 누락 감지 | 세션 종료 시 관찰 1건을 일관 포맷으로 남김 |
| P3 | Asset Pipeline | `_pending/`, Catalog active, archive 규칙, 첫 seed | 1회 해결과 N≥2 승급이 분리되어 동작 |
| P4 | Skeleton Builder | domain base, `bakes-in.json`, `skeleton.lock.json`, apply/build 명령 | 가장 자주 쓰는 도메인 1개를 새 프로젝트에 적용 |
| P5 | Thinktank v0 | L1 + Git metadata 마이닝, weekly insight snapshot | 반복 마찰 후보와 가이드 수정 제안이 생성됨 |
| P6 | Dashboard Integration | NOW/NEXT/LIBRARY/THINKTANK 패널 | 대시보드에서 상태와 자산을 30초 안에 찾음 |
| P7 | Transfer Drill | 다른 AI 또는 깨끗한 환경에서 인계 시뮬레이션 | 추가 질문 없이 임의 TODO 1건을 이어 작업 |

## 4. 첫 구현 묶음

가장 먼저 할 묶음은 P1 + P2다.

이유:
- 데이터 수집은 일찍 시작할수록 유리하다.
- 인계 가능성은 나중에 덧붙이기 어렵다.
- L2/L3/Skeleton은 L0/L1이 안정된 뒤에야 신뢰할 수 있다.

구체 산출물:
- `.ai/schema/context.schema.json`
- `.ai/context.json` v1
- `.ai/checkpoint.md` 템플릿
- `.ai/adapters/{claude,codex,gpt,generic}.md`
- `50_tools/methodology.py observe` 명령 설계
- L1 관찰 로그 lint 규칙 초안

## 5. TODO 후보

| 후보 ID | 제목 | Change Class | 의존성 | 수용 기준 |
|---|---|---|---|---|
| METH-006 | L0 이식성 코어 스키마와 체크포인트 템플릿 구현 | A | 없음 | `.ai/context.json`이 스키마 검증되고 `checkpoint.md`가 필수 섹션을 가진다 |
| METH-007 | L1 관찰 로그 생성·검증 흐름 구현 | A | METH-006 | `methodology observe`가 `40_resources/ai_observations/`에 규칙 준수 파일을 만든다 |
| METH-008 | Pending Lesson과 Catalog 승급 흐름 정리 | B | METH-007 | `_pending/`과 active Catalog가 분리되고 승급 기준이 README에 반영된다 |
| METH-009 | 첫 Skeleton domain build/apply v0 구현 | A | METH-008 | `methodology skeleton build/apply <domain>`이 최소 도메인 1개에서 동작한다 |
| METH-010 | Thinktank v0 마이닝 리포트 구현 | A | METH-007 | L1 + Git metadata에서 반복 friction 후보를 snapshot으로 출력한다 |
| METH-011 | Dashboard L0~L4 패널 통합 | A | METH-006, METH-008 | NOW/NEXT/LIBRARY/THINKTANK 패널이 실제 파일을 읽어 표시한다 |
| METH-012 | 인계 시뮬레이션과 온보딩 검증 | A | METH-006 | 신규 AI/환경이 15분 안에 첫 의미 있는 작업을 시작한다 |

## 6. 검증 기준

P1/P2 완료 후:
- 새 AI가 `AGENTS.md`, `HANDOFF.md`, `.ai/context.json`, `.ai/checkpoint.md`만 읽고 다음 행동을 제시한다.
- 관찰 로그 샘플 1건이 `10_guides/03_AI_관찰_로그_작성_규칙.md`를 통과한다.
- 절대 경로, 모델 전용 지시, 로컬 시간대 가정이 코어 파일에 들어가지 않는다.

P3/P4 완료 후:
- 1회 해결 항목은 `_pending/`에 남고 Skeleton에 반영되지 않는다.
- N≥2 또는 사람 승인 항목만 active Catalog로 승급된다.
- Skeleton lock은 동일 입력에서 동일 출력으로 재생성된다.

P5/P6/P7 완료 후:
- weekly insight snapshot이 생성된다.
- 대시보드가 TODO/HANDOFF/Catalog/Skeleton/Insights를 연결한다.
- 다른 AI 또는 깨끗한 환경에서 인계 시뮬레이션을 통과한다.

## 7. 주요 리스크

| 리스크 | 대응 |
|---|---|
| L1 기록이 귀찮아져 누락됨 | `methodology observe`를 한 명령으로 줄이고, lint로 누락을 드러낸다 |
| Catalog가 다시 위키처럼 비대해짐 | `_pending/`과 active를 분리하고 active 승급을 사람 게이트로 제한한다 |
| Skeleton이 도메인별로 갈라져 유지보수가 어려워짐 | 첫 도메인 1개만 구현하고, 두 번째 도메인은 P7 이후 결정한다 |
| 대시보드가 보여주기용으로만 흐름 | 모든 패널은 실제 파일에서 파싱한 데이터만 표시한다 |
| 특정 AI 도구 자동화에 묶임 | 자동화는 `.ai/adapters/`에만 둔다 |

## 8. 권장 다음 액션

1. `METH-006`을 Ready로 올리고 L0 이식성 코어부터 구현한다.
2. `.claude/worktrees/`, `.codex/` 정책은 `METH-002`에서 먼저 정리한다.
3. P1 완료 직후 작은 인계 시뮬레이션을 실행해 백서의 제0원칙을 검증한다.
