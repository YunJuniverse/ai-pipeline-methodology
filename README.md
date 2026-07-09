# Evidence-Driven AI Development Methodology

**1인+AI 개발에 맞춘 경량 운영 체계. 문서 연극은 줄이고, 코드·테스트·PR·결정 근거는 남긴다.**

---

## Why This Exists

이 저장소의 이전 방법론은 문서, 게이트, 보고 체계를 너무 많이 요구했다.
실전에서는 다음 문제가 반복됐다.

- AI 컨텍스트가 문서 유지보수에 잠식됨
- 텍스트 게이트가 물리적으로 강제되지 않아 무력화됨
- 보고서가 환류보다 의례가 됨
- 상태 문서가 많아질수록 실제 코드 품질 검토가 약해짐

이 버전은 그 실패를 전제로 다시 설계했다.

핵심 변화는 단순하다.

- 구현의 진실은 `code + tests + PR`
- 결정의 진실은 `ADR + 승인 증거`
- 세션 상태의 진실은 `HANDOFF.md`
- 대외 문서는 `snapshot`으로만 생성

---

## Active Model

### 운영 원칙

- `CLAUDE.md`와 `AGENTS.md`는 에이전트 운영 규칙만 담는다.
- `HANDOFF.md`는 현재 상태만 담는다. 살아 있는 운영 파일은 이 문서 하나다.
- `TODO.md`는 backlog와 acceptance criteria를 담는다.
- `40_dev/adr/`는 코드에서 역산할 수 없는 결정 이유만 기록한다.
- `40_dev/snapshots/`의 문서는 날짜가 찍힌 산출물이며 live source가 아니다.
- 인간 승인은 텍스트 선언이 아니라 `merged PR` 또는 링크된 `issue/ADR approval evidence`로만 성립한다.

### 기본 부트 컨텍스트

세션 시작 시 AI는 기본적으로 아래 두 파일만 읽는다.

- `CLAUDE.md`
- `HANDOFF.md`

그 뒤 필요한 경우에만 아래를 추가로 읽는다.

- 관련 `TODO.md` 항목
- 관련 코드/테스트
- 관련 `40_dev/adr/*.md`
- 필요한 snapshot 문서

---

## Change Classes

| Class | 의미 | 자동 트리거 | 필요한 증거 | Gate |
|------|------|-------------|-------------|------|
| `A` | 기본 구현 변경 | 트리거 없음 | 테스트/PR 설명 | PR merge |
| `B` | 영향이 큰 기술 변경 | DB migration, 새 외부 API, 인증/권한 변경, destructive data change, background job | PR에 결정 근거, 영향 범위, rollback, 리스크 | PR merge |
| `C` | 비기술 또는 대외 영향 변경 | 가격, 법무/규정, 브랜드, 공개 릴리스, 대외 약속, 인간이 명시적으로 승격한 항목 | ADR 또는 issue approval 링크 | 인간 승인 후 PR merge |

추가 규칙:

- AI는 작업을 `A`에서 `B/C`로 상향 분류할 수 있다.
- AI는 자동 트리거가 걸린 작업을 임의로 하향 분류하지 않는다.
- `Class C`는 구현 전에 인간 승인 증거가 있어야 한다.

---

## Project Files

새 프로젝트의 기본 구조는 아래와 같다.

```text
my-project/
├── CLAUDE.md, AGENTS.md          # 진입점 (AI 자동 로드)
├── HANDOFF.md, TODO.md           # 라이브 상태
├── 10_foundation/                # 백서·온보딩·다이어그램
├── 20_guides/                    # 작성 지침서 (00~18)
├── 30_planning/                  # 기획 산출물 (v0 스켈레톤 미리 위치)
│   ├── 10_사업기획서.md
│   ├── 11_서비스기획서.md
│   ├── 12_운영기획서.md
│   ├── 13_마케팅기획서.md
│   ├── 14_브랜드기획서.md
│   ├── 15_PM기획서.md
│   ├── 16_AI_기능/AI-NNN.md      # AI 기능별 1개
│   └── 17_평가_가드레일.md
├── 40_dev/                       # 개발 산출물
│   ├── MASTER_PLAN.md            # 18번 기반, 프로젝트당 1개
│   ├── adr/                      # Class B/C 결정 기록
│   └── snapshots/                # 날짜별 산출물
├── 50_resources/                 # 재사용 자원
│   ├── templates/
│   └── prompts/
├── 60_tools/                     # CLI·대시보드 빌더·그래프 데이터
│   ├── methodology.py
│   ├── generate-dashboard.py
│   └── methodology-graph.json
├── 90_archive/                   # 레거시 자료
├── src/                          # fullstack만
└── tests/                        # fullstack만
```

각 영역의 역할:

| 영역 | 폴더 | 역할 |
|------|------|------|
| 메타 / 진입점 | (root) | CLAUDE/AGENTS/HANDOFF/TODO — AI 부트 컨텍스트 |
| 헌법 / 온보딩 | `10_foundation/` | 백서(WHITEPAPER)·HOW_TO_APPLY·KICKOFF·DIAGRAM |
| 지침서 | `20_guides/` | *어떻게* 문서를 작성하는가의 표준 (11종) |
| 기획 산출물 | `30_planning/` | *무엇을 만드는가* — 지침에 따라 채워지는 v0 스켈레톤 |
| 개발 산출물 | `40_dev/` | *어떤 순서로 어떻게 빌드하는가* — MASTER_PLAN/ADR/snapshots |
| 재사용 자원 | `50_resources/` | 템플릿·프롬프트 |
| 도구 | `60_tools/` | `methodology.py` CLI · `generate-dashboard.py` · `methodology-graph.json` |
| 아카이브 | `90_archive/` | 레거시 자료 |

**폴더 번호 컨벤션**: 십의 자리 = 워크플로 단계(00 헌법 → 10 지침 → 20 산출물 → 30 빌드 → 40 자원 → 50 도구 → 90 아카이브). `20_guides/`와 `30_planning/`은 **끝번호로 페어링**(`20_guides/11_서비스기획서_작성_지침.md` ↔ `30_planning/11_서비스기획서.md`). 자세한 정의는 [10_foundation/WHITEPAPER.md](10_foundation/WHITEPAPER.md) 부록 참조.

---

## Workflows

### Fullstack

1. 인간이 `TODO.md`에 작업과 acceptance criteria를 적는다.
2. AI가 `CLAUDE.md`와 `HANDOFF.md`를 읽고 시작한다.
3. AI가 관련 TODO와 코드만 추가로 로드한다.
4. AI가 Change Class를 판별한다.
5. `Class A`는 바로 구현한다.
6. `Class B`는 PR에 영향과 근거를 남기고 구현한다.
7. `Class C`는 ADR 또는 issue approval evidence를 확보한 뒤 구현한다.
8. 비즈니스 로직 변경에는 테스트를 추가하고 PR을 연다.
9. 인간이 리뷰하고 merge한다.
10. AI가 `HANDOFF.md`와 `TODO.md`를 갱신한다.

### Planning-Only

1. 인간이 `TODO.md`에 리서치/기획 항목과 acceptance criteria를 적는다.
2. AI가 `CLAUDE.md`와 `HANDOFF.md`를 읽고 시작한다.
3. 필요한 외부 자료를 조사한다.
4. 결과를 `40_dev/snapshots/`에 날짜가 찍힌 문서로 생성한다.
5. 인간이 PR 또는 issue에서 검토한다.
6. AI가 `HANDOFF.md`와 `TODO.md`를 갱신한다.

---

## Snapshot Rules

`40_dev/snapshots/`의 문서는 다음 규칙을 따른다.

- 파일명에 날짜를 포함한다.
- 문서 상단에 snapshot 경고를 넣는다.
- 코드에서 역산할 수 없는 사실은 외부 근거 링크를 요구한다.
- 근거가 없으면 추정으로 포장하지 말고 `Evidence Needed` 섹션에 남긴다.
- snapshot은 후속 세션의 live operating doc로 사용하지 않는다.

---

## What Changed

현재 활성 방법론에서 제거된 것:

- Phase 0~10 선형 파이프라인
- 기획서 6종 + 개발명세서 8종 상시 유지
- 스프린트 완료/피드백/계획 보고서 3종 의무화
- approval log 같은 텍스트 게이트 중심 운영
- 프로젝트마다 대형 템플릿 세트 복사

남긴 것:

- 테스트 중심 완료 기준
- 인간 승인 원칙
- ADR
- 휴먼리더블 코드 규칙
- 기획 문서 생성 능력 자체

---

## Getting Started

```bash
METHODOLOGY="/Users/hayden/Library/Mobile Documents/iCloud~md~obsidian/Documents/methodology"
cd ~/Projects
python3 "$METHODOLOGY/60_tools/methodology.py" init my-project --type fullstack
```

**처음 부팅하는 AI/사람**: [ONBOARDING.md](ONBOARDING.md) (15분 부팅 가이드 — 단일 진입점).
**철학·원칙·목표**: [10_foundation/WHITEPAPER.md](10_foundation/WHITEPAPER.md) (헌법 — 모든 하위 문서가 이것에 종속).
**첫 세션 프롬프트**: [10_foundation/KICKOFF_PROMPT.md](10_foundation/KICKOFF_PROMPT.md).
**적용 절차**: [10_foundation/HOW_TO_APPLY.md](10_foundation/HOW_TO_APPLY.md).

---

## Updating Methodology in Existing Projects

방법론 자체가 갱신되었을 때 (예: v3.0 → v3.1), 이미 적용한 프로젝트는 다음으로 업데이트:

```bash
cd my-project
python3 "$METHODOLOGY/60_tools/methodology.py" status        # 현재 vs 업스트림 비교
python3 "$METHODOLOGY/60_tools/methodology.py" sync          # 변경 미리보기 (dry-run)
python3 "$METHODOLOGY/60_tools/methodology.py" sync --apply  # 실제 적용
```

CLI는 파일을 4가지로 분류해 안전하게 갱신한다:

| 클래스 | 예시 | 정책 |
|--------|------|------|
| **shared** | `20_guides/`, `50_resources/`, `60_tools/` | sync가 항상 덮어씀 |
| **managed** | `CLAUDE.md`, `AGENTS.md` | `<!-- methodology:managed:* -->` 마커 사이만 머지 |
| **init scaffolds** | `30_planning/`, `40_dev/` | init이 1회 생성, sync 무시 |
| **project-local** | `HANDOFF.md`, `TODO.md`, `40_dev/MASTER_PLAN.md`, ADR/snapshots | 절대 안 건드림 |

**버전 마이그레이션**: `migrations/v<a>_to_<b>.py`가 자동 실행된다 (예: 폴더 구조 변경, 파일 이동).
프로젝트의 `.methodology-version`이 현재 적용된 버전을 추적한다.

```bash
python3 60_tools/methodology.py diff CLAUDE.md   # 단일 파일 변경 미리보기
python3 60_tools/methodology.py version          # 메소돌로지 자체 버전 확인
```

---

## Repository Map

- [CLAUDE.md](CLAUDE.md)
- [AGENTS.md](AGENTS.md)
- [10_foundation/WHITEPAPER.md](10_foundation/WHITEPAPER.md) — **헌법** (철학·원칙·목표)
- [10_foundation/HOW_TO_APPLY.md](10_foundation/HOW_TO_APPLY.md)
- [10_foundation/KICKOFF_PROMPT.md](10_foundation/KICKOFF_PROMPT.md)
- [10_foundation/DIAGRAM.md](10_foundation/DIAGRAM.md)
- [20_guides/](20_guides/) — 작성 지침서 카탈로그
- [30_planning/](30_planning/) — 기획 산출물 v0
- [40_dev/](40_dev/) — MASTER_PLAN / ADR / snapshots
- [50_resources/templates/](50_resources/templates/) — HANDOFF/TODO/ADR/MASTER_PLAN
- [50_resources/prompts/](50_resources/prompts/) — AI 실행 프롬프트 (기획서 생성 + 개발 전환 + 코드 기반 스냅샷; 인덱스 `_README.md`)
- [60_tools/methodology.py](60_tools/methodology.py) — 배포·갱신 CLI (init / sync / status / diff / version)
- [60_tools/generate-dashboard.py](60_tools/generate-dashboard.py) — 4탭 대시보드
- [60_tools/methodology-graph.json](60_tools/methodology-graph.json) — 폴더·문서 관계 그래프
- [migrations/](migrations/) — 버전 간 자동 마이그레이션 스크립트

레거시 및 보관 자료:

- [90_archive/decisions/](90_archive/decisions/)
- [90_archive/legacy-methodology/](90_archive/legacy-methodology/)
- [90_archive/harness/](90_archive/harness/)

평가와 외부 비판 문서는 그대로 유지한다.

- [evaluation/](evaluation)
