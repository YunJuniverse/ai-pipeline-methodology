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
- `docs/adr/`는 코드에서 역산할 수 없는 결정 이유만 기록한다.
- `docs/snapshots/`의 문서는 날짜가 찍힌 산출물이며 live source가 아니다.
- 인간 승인은 텍스트 선언이 아니라 `merged PR` 또는 링크된 `issue/ADR approval evidence`로만 성립한다.

### 기본 부트 컨텍스트

세션 시작 시 AI는 기본적으로 아래 두 파일만 읽는다.

- `CLAUDE.md`
- `HANDOFF.md`

그 뒤 필요한 경우에만 아래를 추가로 읽는다.

- 관련 `TODO.md` 항목
- 관련 코드/테스트
- 관련 `docs/adr/*.md`
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
├── CLAUDE.md
├── AGENTS.md
├── HANDOFF.md
├── TODO.md
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── adr/
│   └── snapshots/
├── src/        # fullstack만
└── tests/      # fullstack만
```

각 파일의 역할:

| File | 역할 |
|------|------|
| `CLAUDE.md` | 프로젝트 설정, 변경 등급 트리거, 코딩/리뷰 규칙 |
| `AGENTS.md` | Codex용 미러 |
| `HANDOFF.md` | 지금 무엇을 하고 있는지, 다음 무엇을 해야 하는지 |
| `TODO.md` | backlog와 acceptance criteria |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR 근거, 테스트, 승인 증거 체크 |
| `docs/adr/` | 결정 이유 |
| `docs/snapshots/` | 필요할 때만 생성하는 문서 |

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
4. 결과를 `docs/snapshots/`에 날짜가 찍힌 문서로 생성한다.
5. 인간이 PR 또는 issue에서 검토한다.
6. AI가 `HANDOFF.md`와 `TODO.md`를 갱신한다.

---

## Snapshot Rules

`docs/snapshots/`의 문서는 다음 규칙을 따른다.

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
bash "$METHODOLOGY/init-project.sh" my-project --type fullstack
```

첫 세션에서는 [KICKOFF_PROMPT.md](KICKOFF_PROMPT.md)를 사용하면 된다.
적용 절차는 [HOW_TO_APPLY.md](HOW_TO_APPLY.md)에 정리되어 있다.

---

## Repository Map

- [CLAUDE.md](CLAUDE.md)
- [AGENTS.md](AGENTS.md)
- [HOW_TO_APPLY.md](HOW_TO_APPLY.md)
- [KICKOFF_PROMPT.md](KICKOFF_PROMPT.md)
- [DIAGRAM.md](DIAGRAM.md)
- [docs/REDESIGN_PROPOSAL.md](docs/REDESIGN_PROPOSAL.md)
- [docs/templates/HANDOFF.md](docs/templates/HANDOFF.md)
- [docs/templates/ADR-template.md](docs/templates/ADR-template.md)
- [docs/on-demand-prompts/](docs/on-demand-prompts)

레거시 자료는 아래에 보존했다.

- [docs/archive/legacy-methodology/](docs/archive/legacy-methodology)
- [docs/archive/planning-guides/](docs/archive/planning-guides)

평가와 외부 비판 문서는 그대로 유지한다.

- [evaluation/](evaluation)
