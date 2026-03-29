# How To Apply

> 이 방법론을 새 프로젝트에 붙이는 실무 절차.

---

## 1. Choose A Mode

| Mode | 언제 쓰는가 | 생성되는 코드 폴더 |
|------|-------------|-------------------|
| `fullstack` | 구현까지 갈 프로젝트 | `src/`, `tests/` 생성 |
| `planning-only` | 리서치/기획만 필요한 프로젝트 | 없음 |

핵심 차이는 코드 유무다. 승인 방식은 둘 다 PR 또는 issue evidence를 남기는 쪽으로 가져간다.

---

## 2. Initialize A Project

```bash
METHODOLOGY="/Users/hayden/Library/Mobile Documents/iCloud~md~obsidian/Documents/methodology"
cd ~/Projects
bash "$METHODOLOGY/init-project.sh" my-project --type fullstack
```

생성 결과:

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

---

## 3. Fill Project Settings

처음 세션에서 아래 값만 채우면 된다.

- project name
- objective
- mode
- stack
- primary approver
- release policy

이 값들은 `CLAUDE.md`와 `AGENTS.md` 상단에 들어간다.

---

## 4. Start The First Session

프로젝트 폴더로 이동한 뒤 AI 세션을 연다.

```bash
cd ~/Projects/my-project
```

첫 메시지는 [KICKOFF_PROMPT.md](KICKOFF_PROMPT.md)를 기준으로 보낸다.

첫 세션의 목표는 보통 아래 네 가지다.

1. Project Settings 채우기
2. `TODO.md`를 첫 backlog로 만들기
3. `HANDOFF.md`를 현재 상태 기준으로 초기화하기
4. 첫 작업의 Change Class를 판별하기

---

## 5. Session Rhythm

### Fullstack

1. 인간이 TODO와 acceptance criteria를 적는다.
2. AI는 `CLAUDE.md`와 `HANDOFF.md`를 읽는다.
3. 필요한 코드, 테스트, ADR만 추가 로드한다.
4. Change Class를 판별한다.
5. 구현하고 PR을 연다.
6. 인간이 리뷰하고 merge한다.
7. AI가 `HANDOFF.md`와 `TODO.md`를 갱신한다.

### Planning-Only

1. 인간이 TODO를 적는다.
2. AI가 필요한 외부 자료를 조사한다.
3. 결과를 `docs/snapshots/`에 생성한다.
4. 인간이 PR 또는 issue에서 검토한다.
5. AI가 `HANDOFF.md`와 `TODO.md`를 갱신한다.

---

## 6. Change Class Rules

### Class A

- 기본값
- Gate는 PR merge

### Class B

자동 트리거:

- DB migration
- 새 외부 API 연동
- 인증/권한 변경
- destructive data change
- background job/queue

PR에 반드시 남길 것:

- why
- impact scope
- rollback plan
- risk note

### Class C

자동 후보:

- 가격/과금
- 법무/규정
- 브랜드/공개 메시지
- 공개 릴리스
- 외부 약속된 범위

이 경우 구현 전에 issue 또는 ADR approval evidence가 필요하다.

---

## 7. Keep HANDOFF Short

`HANDOFF.md`는 현재 상태만 담는 파일이다.
길어지기 시작하면 분리하지 말고 먼저 지운다.

정리 기준:

- 완료된 항목은 삭제
- 장기 결정은 ADR로 이동
- 열린 이슈는 상위 몇 개만 유지
- snapshot은 링크만 남기고 본문 요약은 지움

권장 한도는 150줄 이하다.

---

## 8. Snapshot Discipline

Snapshot 문서는 필요할 때만 만든다.

- 날짜를 파일명에 포함
- 문서 상단에 snapshot 경고 삽입
- 외부 사실은 링크로 증명
- 증거 없는 내용은 `Evidence Needed`로 명시

on-demand prompt 예시는 [docs/on-demand-prompts/](docs/on-demand-prompts)에 있다.

---

## 9. Review Checklist

세션 종료 전에 아래만 확인하면 된다.

- `TODO.md`가 현재 backlog를 반영하는가
- `HANDOFF.md`가 다음 세션 시작점이 되는가
- 필요한 ADR이 빠지지 않았는가
- PR 또는 issue에 승인 증거가 남아 있는가
